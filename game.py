# Put your code here
# greet player
# get player name
# choose random number between 1 and 100
# while True:
#     get guess
#    if guess is incorrect:
#        give hint
#        increase number of guesses
#    else:
#        congratulate player

from random import randint

name = raw_input("Welcome! What is your name? ")
print "%s, I'm thinking of a number between 1 and 100." % name
our_number = randint(1, 100)
num_guesses = 1
while True:
    guess = int(raw_input("What is your guess? "))
    if guess != our_number:
        if guess < our_number:
            print "Your guess is too low. Try again."
            num_guesses += 1
        else:
            print "Your guess is too high. Try again."
            num_guesses += 1
    else:
        print "Congratulations, %s! You found it in %s tries." % (name, num_guesses)
        break
