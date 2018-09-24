import random
import mysql.connector

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
        return EASY_TOP_LIMIT,"Easy"
    elif choice == 2:
        return NORMAL_TOP_LIMIT,"Normal"
    elif choice == 3:
        return HARD_TOP_LIMIT,"Hard"
    elif choice == 4:
        return EXTREME_TOP_LIMIT,"Extreme"
    else:
        print("Invalid choice!")
        exit()


# F2:Random number genrator corresponding to difficulty level
def random_number_generator(toplimit):
    t = random.randint(1, toplimit)
    return t

def save_score(score,playerName,level):
    # print(type(score),type(playerName),type(level))
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root"
    )
    mycursor = mydb.cursor()
    try:
        mycursor.execute("CREATE DATABASE HOTNCOLD")
    except:
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database = "HOTNCOLD"
        )
        mycursor = mydb.cursor(buffered=True)
        # print("HEllo")
        sql="CREATE TABLE GAME(ID INT AUTO_INCREMENT PRIMARY KEY, NAME VARCHAR(20), SCORE INT, LEVEL VARCHAR(20))"
        try:
            mycursor.execute(sql)
        except:
            insert = "INSERT INTO GAME (NAME, SCORE, LEVEL) VALUES(%s,%s,%s)"
            val = (playerName,score,level)
            mycursor.execute(insert,val)
            mydb.commit()
            # print("Success!")
    finally:
        # query = "SELECT* FROM GAME GROUP BY LEVEL ORDER BY SCORE WHERE LEVEL = %s"
        # where = level
        #mycursor.execute(query,where)

        # mycursor.execute("SELECT* FROM GAME GROUP BY LEVEL ORDER BY SCORE WHERE LEVEL = %s",(level))

        query = "SELECT* FROM GAME GROUP BY LEVEL HAVING LEVEL = %s ORDER BY SCORE"
        # query1="SELECT* FROM GAME"
        # query2="SELECT LEVEL, COUNT(LEVEL) FROM GAME GROUP BY LEVEL"
        query3 = "SELECT NAME, SCORE FROM GAME WHERE LEVEL = %s ORDER BY SCORE DESC;"
        value = (level,)
        # mycursor.execute(query,value)
        mycursor.execute(query3,value)

        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

        mycursor.close()
        mydb.close()


# F3:Prints th summary of the game, end point of the game
def match_won(score, playerName,level):
    print("Congratulation! " + playerName + " You guessed it correct!\nYour final score is " + str(score))
    save_score(score,playerName,level)
    print("Your score is saved!")
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
def try_again(oldGuess, value, name, score, top,level):
    while score>=0:
        # print(score)
        newGuess = int(input())
        if newGuess == value:
            match_won(score, name,level)
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
def check_match(guessedNumber, trueNumber, name, score, top,level):
    if guessedNumber == trueNumber:
        match_won(score, name,level)
    else:
        penalty =penalty_evaluator(top)
        score -= penalty
        print("Try again! I know " + name + " can do better!")
        try_again(guessedNumber, trueNumber, name, score, top, level)


# F0:Start point, collects player name
def main():
    print("Enter player name : ", end='')
    name = input()
    top,level = choose_game_level()
    score = top
    value = random_number_generator(top)
    print("LET'S BEGIN!\nSo,what's your 1st guess?")
    guessed = int(input())
    check_match(guessed, value, name, score, top,level)


# script starts here
main()
