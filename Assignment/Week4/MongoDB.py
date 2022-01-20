
# python MongoDB.py(資料庫連線測試)

# 登入pymongo :
import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://root:root12345@wehelp.fcyex.mongodb.net/myFirstDatabase?ssl=true&ssl_cert_reqs=CERT_NONE")
db = client.test
collection = db.users  # 選擇要操作資料庫裏面的集合

mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
collection.insert_one(mydict)
print("資料庫建立成功")
