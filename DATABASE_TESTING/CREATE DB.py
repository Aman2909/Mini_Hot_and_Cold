import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"
)
print(mydb)
mycursor = mydb.cursor()

# CREATING DATABASE
# mycursor.execute("CREATE DATABASE TEST1")

# CHECK IF DATABASE IS CREATED
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
