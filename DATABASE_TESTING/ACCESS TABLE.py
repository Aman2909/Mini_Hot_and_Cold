import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="test1"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")

for x in mycursor:
    # if x=="student":
    #     print("YES!")
    print(x)