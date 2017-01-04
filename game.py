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
    guess = raw_input("What is your guess? ")
    try:
        val = int(guess)
    except ValueError:
        print("That's not a number!")
        break
    guess = int(guess)
    if guess != our_number:
        if 100 < guess or guess < 1:
            print "What about a number between 1 and 100? Try harder!"
            num_guesses += 1
        elif guess < our_number:
            print "Your guess is too low. Try again."
            num_guesses += 1
        else:
            print "Your guess is too high. Try again."
            num_guesses += 1
    else:
        print "Congratulations, %s! You found it in %s tries." % (name, num_guesses)
        break

# if 0 < guess < our_number:
#             print "Your guess is too low. Try again."
#             num_guesses += 1
#         else if our_number < guess < 101:
#             print "Your guess is too high. Try again."
#             num_guesses += 1
#        else if 100 < guess or guess < 1:
#            print "What about a number between 1 and 100? Try harder!"

#        replay = raw_input("Would you like to play again?")
