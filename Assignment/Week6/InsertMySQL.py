# python InsertMySQL.py

import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='root',
                     database='website')

cursor = db.cursor()

x = "david"
sql = "INSERT INTO MEMEBER_DATA (NAME, ACCOUNT, PASSWORD) VALUES (%s,%s, %s)"
val = (x, "wcsodw1@gmail.com", "n1b2a3")

# sql = "INSERT INTO MEMEBER_DATA (NAME, ACCOUNT, PASSWORD) VALUES (%s,%s, %s, %s)"
# values = (item['title'],item['author'],item['comment'],item['time'])
cursor.execute(sql, val)
db.commit()
print(cursor.rowcount, "record inserted.")
