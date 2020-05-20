#variables
resume = 1
turns = 20                      #number of free attempts
_attempts_ = 6                  #number of allowed wrong guesses

import random as rnd
import time
def new_word(filename="sowpods.txt"):
    f = open(filename,'r')
    line = f.readlines()
    f.close()
    return rnd.choice(line).strip()

print('---------------Hangmannnn-------------------')
time.sleep(0.5)
name = input('\nPlease enter your name>>>')
print('\nWelcome to the game', name + '!')
time.sleep(1)
print('\nPlease hold on while I set things up...')
time.sleep(2)
print('When prompted with ">>>", guess a letter')
time.sleep(2)

while resume == 1:
    word = new_word()
    word = word.lower()
    print('\nOkay',name+', get ready to guess!')
    time.sleep(2)
    so_far = []
    attempts = 0
    print('GO!')
    time.sleep(1)
    for item in word:
        so_far += ['_']                 #initalising the guesses list, will be changed after each guess
    for i in range(turns):
        so_far_s = ''
        guess = input('\n>>>')
        if attempts == _attempts_:
            print('You died due to hanging (and me due to laughing ahahahaha)')  #end of game
            print('The word was', word.upper())
            break
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
        for i in range(turns):
            dots = _attempts_ - attempts    #number of dots
        _dots = ''                      #string of dots
        for i in range(dots):           #dots are built here
            _dots += '.'
        print('Your remaining lives:', _dots)
    a = input('\nPress enter to quit, or type restart>>>')
    if a != 'restart':
        resume = 0