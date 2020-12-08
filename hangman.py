# Write your code here
import random

wordss = ('python', 'java', 'kotlin', 'javascript')
selected = random.choice(wordss)
selecs = set(selected)
tries = 1
uncover = ['-' for x in range(len(selected))]
print("H A N G M A N")
letss = set()

def game():
    global selected
    global uncover
    global selecs
    global tries
    global letss
    print("\n"+"".join(uncover))
    guessed_letter = input('Input a letter: ')
    if len(guessed_letter) != 1:
        print('You should input a single letter')
        game()
    elif guessed_letter != guessed_letter.lower() or guessed_letter.isalpha() == False:
        print("Please enter a lowercase English letter")
        game()
    elif "-" not in uncover and tries < 8:
        print("You guessed the word {}!\nYou survived!".format(selected))
        exit()

    elif guessed_letter in selecs and tries < 8 and guessed_letter not in letss:
        for i in range(len(selected)):
            if guessed_letter == selected[i]:
                uncover[i] = guessed_letter
        selecs.remove(guessed_letter)
        letss.add(guessed_letter)
        game()
    elif guessed_letter in letss:
        print('You\'ve already guessed this letter')
        game()
    elif guessed_letter in uncover and tries < 8:
        print('You\'ve already guessed this letter')
        game()
    elif tries < 8 and guessed_letter not in letss and guessed_letter not in selected:
        tries += 1
        print("That letter doesn't appear in the word")
        letss.add(guessed_letter)
        game()

    elif guessed_letter in uncover and tries < 8:
        print('You\'ve already guessed this letter')
        game()
    # and len(selecs) > 0  elif len(selecs) == 0:


    elif tries == 8:
        print("That letter doesn't appear in the word")
        print("You lost!")
        exit()

def playe():
    in2 = input('Type "play" to play the game, "exit" to quit: ')

    if in2 == "play":
        game()
    elif in2 == "exit":
        exit()
    else:
        playe()
playe()
