import mysql.connector
import datetime

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "crudpython"
)

cursor = connection.cursor();

sql = "INSERT INTO users(name,email) VALUES (%s,%s)"

data = (
    "Primeiro Usuário",
    "primeirousuario@gmail.com"
)

cursor.execute(sql, data)

connection.commit()

userId = cursor.lastrowid

cursor.close()
connection.close()

print("Foi cadastrado o novo usuário de ID = ", userId)