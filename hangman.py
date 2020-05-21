#imports and definitions
import random as rnd
import time
def new_word(filename="sowpods.txt"):
    f = open(filename,'r')
    line = f.readlines()
    f.close()
    return rnd.choice(line).strip()
def dots(turns, _attempts_, attempts):
    dots = _attempts_ - attempts    #number of dots
    _dots = ''                      #string of dots
    for i in range(dots):           #dots are built here
        _dots += '.'
    return _dots
def guesses_made(guessed):
    _guesses = ""
    for i in range(len(guessed)):
        _guesses += "'"
        _guesses += str(guessed[i]).upper()
        _guesses += "'"
        _guesses += " "
    return _guesses

#variables
resume = 1
turns = 20                      #number of free attempts
_attempts_ = 6                  #number of allowed wrong guesses

#main game
resume = 1
print('---------------Hangmannnn-------------------')
time.sleep(0.5)
name = input('\nPlease enter your name>>>')
name = name.capitalize()
print('\nWelcome to the game', name + '!')
time.sleep(1)
print('\nPlease hold on while I set things up...')
time.sleep(2)
print('When prompted with ">>>", guess a letter')
time.sleep(2)

while resume == 1:
    print('\nOkay',name+', get ready to guess!')
    time.sleep(2)
    word = new_word().lower()       #the word to be guessed. had to be here because loop
    so_far = []                     #list of guessed parts of word, empty is _, to be converted to string
    attempts = 0                    #number of completed wrong guesses
    guessed = []                    #guessed letters in a list
    print('GO!')
    time.sleep(1)
    for item in word:
        so_far += ['_']                 #initalising the guessed part of word, will be changed after each guess
    for i in range(turns):
        so_far_s = ''
        guess = input('\n>>>')
        if guess in guessed:
            print('You already tried that silly')
            for item in so_far:
                so_far_s += item         #guesses are made a string
            print(so_far_s)
            continue
        guessed += [guess]
        if guess in word:
            print('Good guess')
            for i in range(len(word)):
                if word[i] == guess:
                    so_far[i] = guess    #guesses so far in a list
            so_far_s = ''
            for item in so_far:
                so_far_s += item         #guesses are made a string
            print(so_far_s)
        else:
            print('That\'s not a part of the word :(')   #wrong guess
            so_far_s = ''
            for item in so_far:
                so_far_s += item         #guesses are made a string
            print(so_far_s)
            attempts += 1                #add wroong guess
        if so_far_s == word:
            print('CONGRATULATIONS!!! You got it!!!')
            print('The word was', word)
            break
        if attempts == _attempts_:
            print('You died due to hanging (and me due to laughing ahahahaha)')  #end of game
            print('The word was', word.upper())
            break
        print('Your guesses:', guesses_made(guessed))
        print('Your remaining lives:', dots(turns, _attempts_, attempts))
    a = input('\nPress enter to quit, or type restart>>>')
    if a != 'restart':
        resume = 0