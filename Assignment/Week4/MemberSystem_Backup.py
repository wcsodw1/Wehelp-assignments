
# Python MemberSystem.py
# Flask Quickstart Tutorials(https://flask.palletsprojects.com/en/2.0.x/quickstart/#sessions)

from flask import Flask, render_template, request, redirect
from flask import session

# 初始化資料連線 :
import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://root:root123@mycluster.gpvb7.mongodb.net/myFirstDatabase?ssl=true&ssl_cert_reqs=CERT_NONE")
db = client.test
collection = db.users  # 選擇要操作資料庫裏面的集合
# collection.insert_one({
#     "name": "David",
#     "gender": "男",
#     "email": "wcsodw1@gmail.com",
#     "password": "wehelp123",
# })
print("資料庫建立成功")


# 建立 Application 物件, 設定靜態檔案的路徑處理
# 靜態檔案路徑 static
app = Flask(__name__, static_folder="static",
            static_url_path="/")

# 密秘鑰匙 :
app.secret_key = "Any string but secret"  # 設定 Session 的秘鑰


# 1.首頁
# Default : 使用get方法取得路徑

@app.route("/")
def mainlyused():
    return render_template("front_page.html")


# 2.建立一個成功頁面網址的會員頁面
@app.route("/member")
def member():
    if "name" in session:
        return render_template("member.html")
    # else狀況 : 若會員資料未符合, 就算設定/member路由, 仍會導回首頁
    else:
        return redirect("/")

    # 3. /error?msg=錯誤訊息
    # Default : 使用POST方法取得路徑


@app.route("/error")
def error():
    message = request.args.get("msg", "帳號 、或密碼輸入錯誤")
    return render_template("error.html", message=message)
    # (!!) 網址error後面加上(?msg=)後typing可自由加入更改輸入在頁面的文字內容


@app.route("/signin", methods=["POST"])
def signin():
    # 藉由前端取得使用者輸入
    email = request.form["email"]
    password = request.form["password"]
    # 與資料庫互動
    collection = db.users

    # 檢查信箱密碼是否正確
    result = collection.find_one({
        "$and": [
            {"email": email},
            {"password": password}
        ]
    })
    # 若找不到對應資料,則登入失敗,並導向錯誤頁面

    if result == None:
        return redirect("/error?msg=帳號密碼輸入錯誤")

    # task3-1 : 登入驗證成功後藉由Session記錄使用者狀態為"已登入"
    # session["condition"] = "已登入"  # 把資料(ex:name)存放到["變數名稱"]中
    # condition = session["condition"]
    # 登入成功, 導向會員頁面
    session["name"] = result["name"]
    # session["condition"] = "已登入"  # 把資料(ex:name)存放到["變數名稱"]中
    return redirect("/member")  # /memeber = 成功頁面


# signout : 登出功能網址
@app.route("/signout")
def signout():
    # 移除session中的會員資訊
    del session["name"]
    return redirect("/")


# @app.route("/signup", methods=["POST"])
# def signup():
#     # 藉由前端取得使用者輸入
#     nickname = request.form["nickname"]
#     email = request.form["email"]
#     password = request.form["password"]
#     # 與資料庫互動
#     collection = db.users

#     # 檢查信箱密碼是否正確
#     result = collection.find_one({
#         "$and": [
#             {"email": email},
#             {"password": password}
#         ]
#     })
#     # 若找不到對應資料,則登入失敗,並導向錯誤頁面

#     if result != None:
#         return redirect("/error?msg=信箱已被註冊")
#     collection.insert_one({
#         "nickname": nickname,
#         "email": email,
#         "password": password
#     })
#     # 登入成功, 導向會員頁面
#     return redirect("/")

'''
@Session.route("/member")
def Website_Study():
    return render_template("member_log_success.html")


# Class11.使用GET方法處理路徑 /hello?name=使用者的名字
@Session.route("/hello")
def hello():
    name = request.args.get("name", "")
    session["username"] = name  # 把資料(ex:name)存放到["變數名稱"]中
    return "Hello, " + name

# Class11.使用GET方法處理路徑 / talk


@Session.route("/talk")
def talk():
    name = session["username"]
    return name + ", so so nice to see u !"


# 繼承之前所學的Program
# 路由2 : 常用網站(藉由主畫面點擊進入)


@Session.route("/frequentlyUsed")  # 網頁主畫面後面加增("/frequentlyUsed") 則進入HTML介面
def page():
    return render_template("frequentlyUsed.html")

# 路由3 : NBA


@Session.route("/NBAStats")
def nbaStat():
    return render_template("nbaStats.html")


# 2.表單相關
# class9 表單-測試表單路由


@Session.route("/PaySheet")
def PaySheet():
    return render_template("PaySheet.html")

'''
# 啟動伺服器 Port-3000
app.run(port=3000)
