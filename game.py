import random

def sillygame():
    """A number-guessing game."""
    secret_number = random.randint(1,100)

    guesses = 0
    guessed = False
    too_low = 1
    too_high = 100

    print "Shh... the secret number is %d" % secret_number

    print "The starting boundary is between 1 and 100."

    while guessed is False:
        number = raw_input("Guess a number:")
        try:
            number = int(number)
        except:
            print "You idiot. That wasn't the instruction. I said a NUMBER."
            continue
        if number not in range(too_low, (too_high + 1)):
            print "You idiot. That wasn't the instruction. Please try again."
            continue
        guesses += 1
        if guesses == 7:
            print "Too many tries!"
            break
        print "Too High = %d, Too Low = %d, Guess = %d" % (too_high, too_low, number)
        if number > secret_number:
            too_high = number
            print "Your number is too high."
        elif number < secret_number:
            too_low = number
            print "Your number is too low."
        else:
            guessed = True
            print "You're a superstar!\nAnd it only took you %d guesses." % guesses
            return guesses
        print "Your new boundary is %d and %d" % (too_low, too_high)


name = raw_input("Hello, what's your name?")
print "Hello %s!" % name
best_score = None
while True:
    playwithme = raw_input("Do you want to play a silly guessing game? Y or N ").upper()
    if playwithme == "Y":
        score = sillygame()
        if score == None:
            print "Try again."
        elif score < best_score or best_score is None:
            best_score = score
            print "Good job! You got the best score: %d" % best_score
        else:
            print "Try again! The best score is still: %d" % best_score
    else:
        print "Peace out, homes."
        break
