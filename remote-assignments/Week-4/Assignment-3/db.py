import mysql.connector

password = "BoscoTing122333"

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password=password,
    database="assignment"
)
my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE assignment")
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)

# my_cursor.execute("CREATE TABLE user (id INTEGER AUTO_INCREMENT PRIMARY KEY, email VARCHAR(255), password VARCHAR(30))")
# my_cursor.execute("SHOW TABLES")
# for table in my_cursor:
#     print(table[0])