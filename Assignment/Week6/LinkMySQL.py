
# python LinkMySQL.py

import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='root',
                     database='website')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
sql = """CREATE TABLE MEMEBER_DATA (
         NAME  CHAR(20) NOT NULL,
         ACCOUNT  CHAR(20),
         PASSWORD CHAR(20)
        )"""

cursor.execute(sql)

# 关闭数据库连接
db.close()

# config = {
#     'host': '127.0.0.1',
#     'port': 3306,
#     'user': 'root',
#     'password': 'root',
#     'db': 'website',
#     'charset': 'utf8mb4',
#     'cursorclass': pymysql.cursors.DictCursor,
# }
# with connection.cursor() as cursor:
#     # 執行sql語句，進行查詢
#     sql = 'SHOW DATABASES'
#     cursor.execute(sql)
# result = cursor.fetchall()
# print(result)


# db = pymysql.connect(host='127.0.0.1', port=3306, user='root',
#                      passwd='root', charset='utf8mb4')
# cursor = db.cursor()
# sql = 'SELECT VERSION()'
# cursor.execute(sql)
# data = cursor.fetchone()
# print("Database version : %s " % data)

# # sql2 = "SHOW DATABASES"
# sql2 = "SELECT * FROM member_"
# cursor.execute(sql2)
# restul = cursor.fetchall()
# print(restul)
# cursor.close()


# import mysql.connector
# from mysql.connector import Error
# maxdb = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password="password",
#     database="website",
#     auth_plugin='root'
# )
# cursor = maxdb.cursor()
