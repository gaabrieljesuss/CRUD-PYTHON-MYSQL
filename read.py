import mysql.connector
import datetime

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "crudpython"
)

cursor = connection.cursor()

sql = "SELECT * FROM users"

cursor.execute(sql)
results = cursor.fetchall()

cursor.close()
connection.close()

for result in results:
    print(result)



