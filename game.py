"""A number-guessing game."""
import random
secret_number = random.randint(1,100)
name = raw_input("Hello, what's your name?")
print "Hello %s!" % name

guesses = 0
guessed = False
too_low = 1
too_high = 100

print "Shh... the secret number is %d" % secret_number

print "The starting boundary is between 1 and 100."

while guessed == False:
    number = raw_input("Guess a number:")
    try:
        int(number)
        number = int(number)
        if number not in range(too_low, too_high + 1)
            print "You idiot. That wasn't the instruction. Please try again."
        else:
            guesses += 1
            if number != secret_number:
                print "Too High = %d, Too Low = %d, Guess = %d" % (too_high, too_low, number)
                if number > secret_number:
                    too_high = number
                    print "Your number is too high."
                if number < secret_number:
                    too_low = number
                    print "Your number is too low."
                print "Your new boundary is %d and %d" % (too_low, too_high)
            else:
                print "You're a superstar!\nAnd it only took you %d guesses." % guesses
                guessed = True
    except:
        print "You idiot. That wasn't the instruction. I said a NUMBER."
