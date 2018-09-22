import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user ="root",
    passwd = "root",
    database = "test1"
)

mycursor= mydb.cursor()
# mycursor.execute("CREATE TABLE STUDENT(ROLLNO INT PRIMARY KEY , NAME VARCHAR(20))")

# sql ="DROP TABLE STUDENT"
# mycursor.execute(sql)

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")