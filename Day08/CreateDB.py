import mysql.connector
from mysql.connector import Error

try:
    myDB = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = ""
    )

    myCursor = myDB.cursor()

    myCursor.execute("CREATE DATABASE SchoolDB")
    print ("Database 'SchoolDB' has successfully created")

except Error as e:
    print (f"Error: {e}")
