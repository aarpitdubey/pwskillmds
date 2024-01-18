import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ineuron"
)
print(mydb)
mycursor = mydb.cursor()
# SHOW_DATABASE="SHOW DATABASES"
# query = "CREATE TABLE IF NOT EXISTS test.test_table(c1 INT, c2 VARCHAR(50), c3 FLOAT, c4 INT, c5 VARCHAR(30))"
INSERT_QUERY = 'INSERT INTO test.test_table VALUES(123, "ARPIT", 99.99, 007, "DUBEY")'
mycursor.execute(INSERT_QUERY)
mydb.commit()
mycursor.close()

# for x in mycursor:
#   print(x)