import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
try:
    connection = mysql.connector.connect(
        host='localhost',
        database='test1',
        user='root',
        password='root'
    )
    mycursor = connection.cursor(prepared=True)
    name=('Aman',)
    sql="SELECT* FROM customers WHERE NAME = %s"
    mycursor.execute(sql,name)
    myresult = mycursor.fetchmany()
    for x in myresult:
        print (x)
except mysql.connector.Error as error :
    print("Failed to update record to database: {}".format(error))
    connection.rollback()
finally:
    #closing database connection.
    if(connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")


