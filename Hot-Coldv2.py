import random

# Constant upper limit of the range corresponding to different to difficulty level
EASY_TOP_LIMIT = 20
EASY_PENALTY = 2
NORMAL_TOP_LIMIT = 50
NORMAL_PENALTY = 3
HARD_TOP_LIMIT = 100
HARD_PENALTY = 10
EXTREME_TOP_LIMIT = 1000
EXTREME_PENALTY = 15


# F1:Asks the level of difficulty
def choose_game_level():
    print(" ******************* Hot or Cold *********************** ")
    print("Choose difficulty:\n1. Easy (1-20)\n2. Normal (1-50)\n3. Hard (1-100)\n4. Extreme (1-1000)")
    choice = int(input())
    if choice == 1:
        return EASY_TOP_LIMIT
    elif choice == 2:
        return NORMAL_TOP_LIMIT
    elif choice == 3:
        return HARD_TOP_LIMIT
    elif choice == 4:
        return EXTREME_TOP_LIMIT
    else:
        print("Invalid choice!")
        exit()


# F2:Random number genrator corresponding to difficulty level
def random_number_generator(toplimit):
    t = random.randint(1, toplimit)
    return t


# F3:Prints th summary of the game, end point of the game
def match_won(score, playerName):
    print("Congratulation! " + playerName + " You guessed it correct!\nYour final score is " + str(score))
    print("Press 'y' to play again 'q' to quit")
    playChoice = input()
    if playChoice == 'y':
        main()
    elif playChoice == 'q':
        exit()
    else:
        print("Invalid choice, closing the game")
        exit()


# F4: Returns penalty corresponding to the difficulty level
def penalty_evaluator(top):
    if top == EASY_TOP_LIMIT:
        return EASY_PENALTY
    elif top == NORMAL_TOP_LIMIT:
        return NORMAL_PENALTY
    elif top == HARD_TOP_LIMIT:
        return HARD_PENALTY
    else:
        return EXTREME_PENALTY


# F5:Indicates whether the series of guesses are relatively warm or cold
def try_again(oldGuess, value, name, score, top):
    while True:
        newGuess = int(input())
        if newGuess == value:
            match_won(score, name)
        elif oldGuess < value:
            if oldGuess < newGuess < value:
                print("It's getting warmer!")
            elif oldGuess < value < newGuess:
                print("Oops! You overshot the number!")
            elif newGuess < oldGuess < value:
                print("It's pretty cold!")
        else:
            if value < newGuess < oldGuess:
                print("Warmer! Warmer!")
            elif value < oldGuess < newGuess:
                print("Colder! Colder!")
            elif newGuess < value < oldGuess:
                print("Overshoot! Overshoot!")
        oldGuess = newGuess
        penalty = penalty_evaluator(top)
        score -= penalty


# F5:Checks the first guess
def check_match(guessedNumber, trueNumber, name, score, top):
    if guessedNumber == trueNumber:
        match_won(score, name)
    else:
        score -= 1
        print("Try again! I know " + name + " can do better!")
        try_again(guessedNumber, trueNumber, name, score, top)


# F0:Start point, collects player name
def main():
    print("Enter player name : ", end='')
    name = input()
    top = choose_game_level()
    score = top
    value = random_number_generator(top)
    print("LET'S BEGIN!\nSo,what's your 1st guess?")
    guessed = int(input())
    check_match(guessed, value, name, score, top)


# script starts here
main()
