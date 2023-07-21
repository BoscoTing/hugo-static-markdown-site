import pymysql
db_password = "BoscoTing122333"
db = pymysql.connect(
    host='localhost',
    user='root',
    password=db_password,
    database="assignment"
)
cursor = db.cursor()