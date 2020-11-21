from math import log
import sys
import math

setup = sys.argv
organized_dict = {}
c = 0
calculations = ['principal', 'payment', 'periods']

def config():
    organized_dict[setup[1].split("=")[0].lstrip('--')] = setup[1].split("=")[1]
    for i in range(2, len(setup)):
        if float(setup[i].split("=")[1]) < 0:
            print('Incorrect parameters')
            exit()
        else:
            organized_dict[setup[i].split("=")[0].lstrip('--')] = float(setup[i].split("=")[1])
    if 'type' not in organized_dict.keys() or len(setup) != 5 or 'interest' not in organized_dict.keys():
        print('Incorrect parameters')
        exit()
    elif 'diff' not in organized_dict.values() and 'annuity' not in organized_dict.values():
        print('Incorrect parameters')
        exit()
    for i in calculations:
        if i not in  organized_dict.keys():
            return i
what_calculate = config()


def calculation():
    if organized_dict['type'] == 'annuity':
        if what_calculate == 'principal':
            monthly_payment = organized_dict['payment']
            number_of_months = organized_dict['periods']
            loan_interest = organized_dict['interest']
            i = loan_interest / (12 * 100)
            loan_principal = math.floor(monthly_payment / ( (i * ((1 + i) ** number_of_months)) / ( ((1 + i) ** number_of_months) - 1 )))
            print('Your loan principal = {}!'.format(loan_principal))
            print('Overpayment = {}'.format(int((monthly_payment * number_of_months) - loan_principal)))
        elif what_calculate == 'periods':
            loan_principal = organized_dict['principal']
            monthly_payment = organized_dict['payment']
            loan_interest = organized_dict['interest']
            i = loan_interest / (12 * 100)
            number_of_months = math.ceil(log(monthly_payment / (monthly_payment - i * loan_principal), (1 + i)))
            if number_of_months >= 24 and number_of_months % 12 == 0:
                print('It will take {} years to repay this loan!'.format(int(number_of_months/12)))
            elif number_of_months == 12:
                print('It will take 1 year to repay this loan!')
            elif number_of_months > 24 and number_of_months % 12 > 1:
                print('It will take {} years and {} months to repay this loan!'.format(math.floor(number_of_months / 12 ), number_of_months % 12))
            elif number_of_months < 24 and number_of_months > 12 and number_of_months % 12 > 1:
                print('It will take 1 year and {} months to repay this loan!'.format(number_of_months % 12))
            elif number_of_months < 12 and number_of_months > 1:
                print('It will take {} months'.format(number_of_months))
            elif number_of_months == 13:
                print('It will take 1 year and 1 month to repay this loan!')
            elif number_of_months > 24 and number_of_months % 12 == 1:
                print('It will take {} years and 1 month to repay this loan!'.format(math.floor(number_of_months / 12)))
            print('Overpayment = {}'.format(int((monthly_payment * number_of_months) - loan_principal)))
        elif what_calculate == 'payment':
            loan_principal = organized_dict['principal']
            number_of_months = organized_dict['periods']
            loan_interest = organized_dict['interest']
            i = loan_interest / (12 * 100)
            monthly_payment = math.ceil(loan_principal * ((i * ((1 + i) ** number_of_months)) / (((1 + i) ** number_of_months) - 1)))
            print('Your monthly payment = {}!'.format(monthly_payment))
            print('Overpayment = {}'.format(int((monthly_payment * number_of_months) - loan_principal)))
    elif organized_dict['type'] == 'diff':
        loan_principal = organized_dict['principal']
        number_of_months = organized_dict['periods']
        loan_interest = organized_dict['interest']
        i = loan_interest / (12 * 100)
        total = 0
        for a in range(1, int(number_of_months)+1):
            diff_payment = int(math.ceil(loan_principal / number_of_months + (i * (loan_principal - ( (loan_principal * (a - 1)) / number_of_months )))))
            print('Month {}: payment is {}'.format(a, diff_payment))
            total += diff_payment
        print('\nOverpayment = {}'.format(int(total - loan_principal)))

calculation()
