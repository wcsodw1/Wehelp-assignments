
# python Search MySQL.py
'''
import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='root',
                     database='website')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# cursor.execute(sql)
# SQL 查询语句
# SQL 查询语句
sql = "SELECT * FROM member_"
# try:
# 执行SQL语句
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()
print("====================")


# 关闭数据库连接
# db.close()

# ===========================================================================================

# python SearchMySQL.py

db = pymysql.connect(host='localhost',
                     user='root',
                     password='root',
                     database='website')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = "SELECT * FROM memeber_data"
# try:
# 执行SQL语句
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()
print("====================")
try:
    for row in results:
        name = row[0]
        account = row[1]
        password = row[2]

        # 打印结果
        print("name=%s, account=%s, password=%s" %
              (name, account, password))
except:
    print("Error: unable to fetch data")


# 关闭数据库连接
db.close()

'''
# ===========================================================================================

# python SearchMySQL.py
import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='root',
                     database='website')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = "SELECT * FROM memeber_data"
# try:
# 执行SQL语句
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()
print("====================")

username = []
x = "Highway"
for row in results:
    account = row[1]

    # 打印结果
    print("account=%s" % (account))
    if x == account:
        username.append(x)
        print("Account already exist!")
print("username :", username)

# 关闭数据库连接
db.close()
