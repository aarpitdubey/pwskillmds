import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ineuron"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS \
    test_database.test_table(Id INT, Name VARCHAR(50), \
        mobile_number INT, CGPA FLOAT, College VARCHAR(70))");

mydb.close()