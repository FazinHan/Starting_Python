import random
to_be_guessed = random.randint(0, 10)
guess = 0
while guess != to_be_guessed:
    guess = input("New number('q' to give up): ")
    if guess > 0:
        if guess > to_be_guessed:
            print("Number too large")
        elif guess == to_be_guessed:
			print("Congratulations, you did it!")
		else:
            print("Number too small")
    elif guess == 'q':
        print("Sorry that you're giving up!")
    else:
		print("Invalid input")
###
input('Press enter to quit')