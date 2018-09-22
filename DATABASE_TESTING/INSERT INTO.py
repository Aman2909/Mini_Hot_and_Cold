import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user ="root",
    passwd = "root",
    database = "test1"
)

mycursor= mydb.cursor()
sql = "INSERT INTO customers (name,address) VALUES(%s,%s)"
# value = ("John1", "Highway 211")
# mycursor.execute(sql,value)



value = [
    ("Aman","Manushree"),
    ("XYZ","hjk"),
    ("Aman","Manushree"),
    ("XYZ","hjk"),
    ("Aman","Manushree"),
    ("XYZ","hjk")
]

mycursor.executemany(sql,value)

mydb.commit()
print(mycursor.rowcount, "record inserted.")


mycursor.execute("SELECT* FROM customers")
myresult=mycursor.fetchall()

for x in myresult:
    print(x)


mycursor.execute("SELECT* FROM customers")
myresult=mycursor.fetchall()

for x in myresult:
    print(x)