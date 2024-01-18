import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ineuron"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS test_database")
mydb.close()

