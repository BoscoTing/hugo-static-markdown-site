import pymysql
from decouple import config
db_password = config('dbpassword')
# 信箱是否符合格式
def validate_email(user_email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", user_email):
        return False    
    else:
        return True

# 註冊
def sign_up(user_email, user_password):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password=db_password,
                                 database="assignment")
    # 將帳密寫進sql
    with connection:
        with connection.cursor() as cursor:
            try:
                sql = "INSERT INTO `user` (`email`, `password`) VALUES (%s, %s)"
                cursor.execute(sql, 
                               (user_email, user_password))
                connection.commit()
            # 已註冊過的email
            except pymysql.err.IntegrityError:
                raise ValueError
        # print出已寫入sql的帳密
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `user`"
            cursor.execute(sql)
            result = cursor.fetchall()[-1]
            print(result)

# (登入)email是否已註冊
def select_email(user_email):
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password=db_password,
                                database="assignment")
    with connection:
        with connection.cursor() as cursor:
            sql = f"SELECT email FROM user WHERE email = '{user_email}'"
            try:
                cursor.execute(sql)
                print(cursor.fetchone()[0])
                return True
            except TypeError:
                return False
# (登入)密碼是否打對
def select_password(user_email):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password=db_password,
                                 database="assignment")
    with connection:
        with connection.cursor() as cursor:
            sql = f"SELECT `password` FROM `user` WHERE `email` = '{user_email}'"
            cursor.execute(sql)
            result_password = cursor.fetchone()[0]
            return result_password
