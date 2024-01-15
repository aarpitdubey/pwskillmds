
```python
import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="<USERNAME>",
  password="<PASSWORD>"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)
```

```SQL
SHOW DATABASES
```
![Alt text](image.png)

```python

import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="<USERNAME>",
  password="<PASSWORD>"
)
print(mydb)
mycursor = mydb.cursor()
INSERT_QUERY = 'INSERT INTO test.test_table VALUES(123, "ARPIT", 99.99, 007, "DUBEY")'
mycursor.execute(INSERT_QUERY)
mydb.commit()
mycursor.close()

```

```SQL
INSERT INTO test.test_table VALUES(123, "ARPIT", 99.99, 007, "DUBEY");
```

![Alt text](image-1.png)