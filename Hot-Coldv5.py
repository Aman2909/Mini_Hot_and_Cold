import random
import os
import mysql.connector

# Constant upper limit of the range corresponding to different to difficulty level
EASY_TOP_LIMIT = 20
EASY_PENALTY = 4
NORMAL_TOP_LIMIT = 50
NORMAL_PENALTY = 10
HARD_TOP_LIMIT = 100
HARD_PENALTY = 25
EXTREME_TOP_LIMIT = 1000
EXTREME_PENALTY = 40


# Asks the level of difficulty
def choose_game_level():
    print(" ******************* Hot or Cold *********************** ")
    print("Choose difficulty:\n1. Easy (1-20)\n2. Normal (1-50)\n3. Hard (1-100)\n4. Extreme (1-1000)")
    choice = int(input())
    if choice == 1:
        return EASY_TOP_LIMIT, "Easy"
    elif choice == 2:
        return NORMAL_TOP_LIMIT, "Normal"
    elif choice == 3:
        return HARD_TOP_LIMIT, "Hard"
    elif choice == 4:
        return EXTREME_TOP_LIMIT, "Extreme"
    else:
        print("Invalid choice!")
        exit()


# Random number genrator corresponding to difficulty level
def random_number_generator(toplimit):
    t = random.randint(1, toplimit)
    return t


# Saves score in the database:
def save_score(score, playerName, level):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root"
    )
    mycursor = mydb.cursor()
    try:
        mycursor.execute("CREATE DATABASE HOTNCOLD")
    except:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="HOTNCOLD"
        )
        mycursor = mydb.cursor(buffered=True)
        sql = "CREATE TABLE GAME(ID INT AUTO_INCREMENT PRIMARY KEY, NAME VARCHAR(20), SCORE INT, LEVEL VARCHAR(20))"

        try:
            mycursor.execute(sql)
        except:
            insert = "INSERT INTO GAME (NAME, SCORE, LEVEL) VALUES(%s,%s,%s)"
            val = (playerName, score, level)
            mycursor.execute(insert, val)
            mydb.commit()

    finally:
        query = "SELECT NAME, SCORE FROM GAME WHERE LEVEL = %s ORDER BY SCORE DESC;"
        value = (level,)

        mycursor.execute(query, value)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

        mycursor.close()
        mydb.close()


# Asks whether game should be played again:
def play_again():
    print("Press 'y' to play again 'q' to quit")
    playChoice = input()
    if playChoice == 'y':
        main()
    elif playChoice == 'q':
        exit()
    else:
        print("Invalid choice, closing the game")
        exit()


# Prints the summary of the game, end point of the game
def match_won(score, playerName, level):
    print("Congratulation! " + playerName + " You guessed it correct!\nYour final score is " + str(score))
    save_score(score, playerName, level)
    print("Your score is saved!")
    play_again()


# Returns penalty corresponding to the difficulty level
def penalty_evaluator(top):
    if top == EASY_TOP_LIMIT:
        return EASY_PENALTY
    elif top == NORMAL_TOP_LIMIT:
        return NORMAL_PENALTY
    elif top == HARD_TOP_LIMIT:
        return HARD_PENALTY
    else:
        return EXTREME_PENALTY


# Indicates whether the series of guesses are relatively warm or cold
def try_again(oldGuess, value, name, score, top, level):
    while score >= 0:
        newGuess = int(input())
        if newGuess == value:
            match_won(score, name, level)
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
        print("Score : "+str(score))
    print("You are out of turns. Exiting the game")
    play_again()


# Checks the first guess
def check_match(guessedNumber, trueNumber, name, score, top, level):
    if guessedNumber == trueNumber:
        match_won(score, name, level)
    else:
        penalty = penalty_evaluator(top)
        score -= penalty
        print("Try again! I know " + name + " can do better!\nScore : "+str(score))
        try_again(guessedNumber, trueNumber, name, score, top, level)


# Displays all the saved  score
def highscores(level):
    try:
        mydb = mysql.connector.connect(
            host='localhost',
            database='HOTNCOLD',
            user='root',
            password='root'
        )
        mycursor = mydb.cursor(prepared=True)

        query3 = "SELECT NAME, SCORE FROM GAME WHERE LEVEL = %s ORDER BY SCORE DESC;"
        value = (level,)
        mycursor.execute(query3, value)

        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

        print("Clear all scores? (y/n)")
        if input() == 'y':
            delquery = "DELETE FROM GAME"
            mycursor.execute(delquery)
            mydb.commit()
            print("Delete complete!")
        else:
            print("Scores are safe!")
        main()

    except mysql.connector.Error as error:
        print(error)
    finally:
        if (mydb.is_connected()):
            mycursor.close()
            mydb.close()


# Collects player name and initiates game
def game():
    print("Enter player name : ", end='')
    name = input()
    top, level = choose_game_level()
    score = top
    value = random_number_generator(top)
    print("LET'S BEGIN!\nSo,what's your 1st guess?")
    guessed = int(input())
    check_match(guessed, value, name, score, top, level)


def main():
    print("1. Let's Play\n2. View Highscores")
    choice = int(input())
    os.system("CLS")
    if choice == 1:
        game()
    elif choice == 2:
        print("Select difficulty:\n1.Easy\t2.Normal\t3.Hard\t4.Extreme")
        t = int(input())
        if t == 1:
            choice1 = "Easy"
        elif t == 2:
            choice1 = "Normal"
        elif t == 3:
            choice1 = "Hard"
        elif t == 4:
            choice1 = "Extreme"
        highscores(choice1)


# script starts here
main()
