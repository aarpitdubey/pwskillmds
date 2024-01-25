import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ineuron"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT Name, CGPA, College FROM test_database.test_table");

for record in mycursor.fetchall():
    print(record)

mydb.close()