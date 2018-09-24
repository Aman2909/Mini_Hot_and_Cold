import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user ="root",
    passwd = "root",
    database = "test1"
)

mycursor= mydb.cursor()
sql = "DELETE FROM customers"
mycursor.execute(sql)

mycursor.execute("SELECT* FROM customers")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

mydb.commit()