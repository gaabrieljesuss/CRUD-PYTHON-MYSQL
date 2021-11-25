import mysql.connector
import datetime

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "crudpython"
)

cursor = connection.cursor()

sql = "UPDATE users SET name = %s, email = %s WHERE id = %s"

data = (
    "Gabriel",
    "bielzinho@gmail.com",
    1
)

cursor.execute(sql,data)
connection.commit()

recordsaffected = cursor.rowcount


cursor.close()
connection.close()

print(recordsaffected, " registros alterados")