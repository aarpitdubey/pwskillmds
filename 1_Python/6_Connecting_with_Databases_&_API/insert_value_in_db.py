import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ineuron"
)

mycursor = mydb.cursor()
mycursor.execute("INSERT INTO \
    test_database.test_table(Id, Name,\
        mobile_number, CGPA, College)\
    VALUES(1, 'Arpit Dubey', 82519, 9.2,\
        'Gyan Ganga Institute of Technology')");

mydb.commit()

mydb.close()