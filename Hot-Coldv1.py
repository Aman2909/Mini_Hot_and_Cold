import random

EASY_TOP_LIMIT = 20
NORMAL_TOP_LIMIT = 50
HARD_TOP_LIMIT = 100
EXTREME_TOP_LIMIT = 1000


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


def random_number_generator(toplimit):
    t = random.randint(1, toplimit)
    return t


def match_won(score, playerName):
    print("Congratulation! " + playerName + " You guessed it correct!\nYour final score is " + str(score))
    print("Press 'y' to play again 'q' to quit")
    playChoice = input()
    if playChoice == 'y':
        main()
    else:
        exit()


def try_again(guessedNumber, trueNumber, name, score, top):
    ch = 'y'
    while ch == 'y' or guess != None:
        guess = int(input())
        diff1 = guessedNumber - trueNumber
        diff2 = guess - trueNumber
        if guess == trueNumber:
            match_won(score, name)
        else:
            if trueNumber > guess and trueNumber > guessedNumber:
                if diff2 > diff1:
                    print("Getting warmer!")
                else:
                    print("Getting colder")

            elif trueNumber < guessedNumber and trueNumber < guess:
                if diff1 > diff2:
                    print("Its all cold here!")
                else:
                    print("Its getting warm!")

            elif diff1 * diff2 < 0:
                print("You overshoot the number :(")
            score -= 1


def check_match(guessedNumber, trueNumber, name, score, top):
    if guessedNumber == trueNumber:
        match_won(score, name)
    else:
        score -= 1
        print("Try again! I know " + name + " can do better!")
        try_again(guessedNumber, trueNumber, name, score, top)


def main():
    print("Enter player name : ")
    name = input()
    top = choose_game_level()
    score = top
    value = random_number_generator(top)
    # print(value)
    print("LET'S BEGIN!\nSo,what's your 1st guess?")
    guessed = int(input())
    check_match(guessed, value, name, score, top)


main()
