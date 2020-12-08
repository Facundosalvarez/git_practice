import math
import random
import sqlite3

#Credit card generator.
option = None
loggedacc = None
database = {}
balance = 0
current_acc = 0
conn = sqlite3.connect("card.s3db")
cur = conn.cursor()
try:
    cur.execute('SELECT * FROM card;')
    data = cur.fetchall()
  #  print(data)
except sqlite3.OperationalError:
    cur.execute("CREATE TABLE card(id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0 NOT NULL);")
    conn.commit()

try:
    cur.execute("SELECT id FROM card ORDER BY id DESC LIMIT 1;")
    numberacc = cur.fetchone()[0]
    number_of_acc = numberacc + 1
  #  print((number_of_acc))
except TypeError:
    number_of_acc = 1



def starting():
    print('''1. Create an account
2. Log into account
0. Exit''')

    option = int(input())
    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 0:
        print('\nBye!')
        exit()
    else:
        starting()

def check_lun(cardnmchk):
    sum = 0
    for i in cardnmchk[:-1:2]:
        if int(i) * 2 > 9:
            sum += (int(i) * 2) - 9
        else:
            sum += int(i) * 2
    for i in cardnmchk[1:-1:2]:
        sum += int(i)
    sum += int(cardnmchk[-1])
    if sum % 10 != 0:
        return False
    else:
        return True


def option1():
    global number_of_acc
    card_n = 0
    pin = 0
    balance = 0
    card_n = int(str(400000) + "%0.9d" % random.randint(0,999999999))
    pin_n = "%0.4d" % random.randint(0, 9999)
    suma = 0
    checksum = 0
    for i in range(0, len(str(card_n)), 2):
        if int(str(card_n)[i]) * 2 > 9:
            suma += (int(str(card_n)[i]) * 2) - 9
        else:
            suma += int(str(card_n)[i]) * 2
    for i in range(1, len(str(card_n)), 2):
        suma += int(str(card_n)[i])
    if suma % 10 != 0:
        checksum = int(str((int(str(suma)[0])) + 1) + str(0)) - suma

    card_n = (str(card_n) + str(checksum))
    print('\nYour card has been created\nYour card number:\n{}\nYour card PIN:\n{}\n'.format(card_n, pin_n))
    database[number_of_acc] = [card_n, pin_n]
    cur.execute('INSERT INTO card (id, number, pin, balance) VALUES(?, ?, ?, ?);',(number_of_acc, str(card_n), pin_n, balance))
    conn.commit()
    cur.execute("SELECT id FROM card ORDER BY id DESC LIMIT 1;")
    numberacc = cur.fetchone()[0]
    number_of_acc = numberacc + 1
    starting()

def loggedin():
    global loggedacc
    print('''1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit''')
    cur.execute('SELECT balance FROM card WHERE id = {};'.format(loggedacc))
    balance = cur.fetchone()[0]
    cur.execute('SELECT number FROM card WHERE id = {};'.format(loggedacc))
    loggedcard = cur.fetchone()[0]
    login = int(input())
    if login == 5:
        print('')
        starting()
    elif login == 1:
        print('\nBalance: {}\n'.format(balance))
        loggedin()
    elif login == 2:
        money = int(input("\nEnter income:\n"))
        cur.execute('UPDATE card SET balance = {} WHERE id = {};'.format((money + balance), loggedacc))
        conn.commit()
        print("Income was added!\n")
        loggedin()
    elif login == 3:
        transfercard = input("\nTransfer\nEnter card number:\n")
        cur.execute('SELECT * FROM card;')
        data1 = cur.fetchall()
        if check_lun(transfercard) == False:
            print("Probably you made a mistake in the card number. Please try again!\n")
            loggedin()


        elif transfercard == loggedcard:
            print("You can't transfer money to the same account!\n")
            loggedin()
        else:
            isit = False
            for key in data1:
                if transfercard[:-1] == key[1][:-1] and transfercard != key[1]:
                    print("Probably you made a mistake in the card number. Please try again!\n")

                    loggedin()

                elif transfercard == key[1]:
                    isit = True
                    moneyt = int(input("Enter how much money you want to transfer:\n"))
                    if balance < moneyt:
                        print("Not enough money!\n")
                        loggedin()
                    else:
                        new_balance = balance - moneyt
                        cur.execute('UPDATE card SET balance = {} WHERE id = {};'.format(new_balance, loggedacc))
                        conn.commit()
                        cur.execute('SELECT balance FROM card WHERE number = "{}";'.format(transfercard))
                        transferbalance = cur.fetchone()[0]
                        transferadded = moneyt + transferbalance
                        cur.execute('UPDATE card SET balance = ? WHERE number = ?;', (transferadded, transfercard,))
                        conn.commit()
                        print("Success!\n")
                        loggedin()

            if isit == False:
                print("Such a card does not exist.\n")
                loggedin()
    elif login == 4:
        cur.execute('DELETE FROM card WHERE id = ?', (loggedacc, ))
        conn.commit()
        print("\nThe account has been closed!\n")
        starting()
    elif login == 0:
        print('\nBye!')
        exit()
    else:
        loggedin()

def option2():
    global loggedacc
    card_info = input('\nEnter your card number:\n')
    pin_info = input('Enter your PIN:\n')
    cur.execute("SELECT id FROM card ORDER BY id DESC LIMIT 1;")
    numberacc = cur.fetchone()[0]
    cur.execute('SELECT * FROM card;')
    data1 = cur.fetchall()
    isit = None
    for key in data1:
        if card_info == key[1] and pin_info == key[2]:
            isit = True
            loggedacc = key[0]
        #elif card_info[:-1] == key[1][:-1] and card_info != key[1]:
         #   print("Probably you made a mistake in the card number. Please try again!\n")
          #  starting()
    if isit == None:
        print('\nWrong card number or PIN!\n')
        starting()
    elif isit == True:
        print('\nYou have successfully logged in!\n')
        loggedin()

starting()