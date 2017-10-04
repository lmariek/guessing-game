import random

def sillygame(low,high):
    """A number-guessing game."""
    secret_number = random.randint(low,high)

    guesses = 0
    guessed = False
    too_low = low
    too_high = high

    print "Shh... the secret number is %d" % secret_number

    print "The starting boundary is between %d and %d." % (low,high)

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

def score_conversion(x, y, z):
    #score, possiblities (number of ints in range)
    #weighted score = score / possibilites
    result = ((x/(z-y))*()
    #return the conerted score


name = raw_input("Hello, what's your name?")
print "Hello %s!" % name
best_score = None
while True:
    playwithme = raw_input("Do you want to play a silly guessing game? Y or N ").upper()
    if playwithme == "Y":
        ask_bounds = raw_input("Do you want to set the bounds? Y or N").upper()
        if ask_bounds == "N":
            score = sillygame(0,100)
        else:
            low_n = int(raw_input("What is the lowest number? "))
            high_n = int(raw_input("What is the highest number? "))
            score = sillygame(low_n,high_n) #pass low and high
        if score == None:
            print "Try again."
        elif best_score is None:
            best_score = score
            print "Good job! You got the best score: %d" % best_score
        elif score_conversion(score, low_n, high_n) < best_score:
            #analyze score in new func
            
            #print you win!
            print "Try again! The best score is still: %d" % best_score
    else:
        print "Peace out, homes."
        break
