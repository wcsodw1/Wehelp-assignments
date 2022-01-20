
# Python MyMemberSystem.py
# python Flask Quickstart 教學(https://flask.palletsprojects.com/en/2.0.x/quickstart/#sessions)
# ========================================================================= #


# 1.Preprocessing :
# 1.1 Import Module :
from flask import Flask, render_template, request, redirect, session
import pymongo

#   1.2 建立物件, 設定靜態路徑(ex:static)
# 靜態default路徑已("/")為出發點, ex:static_url_path="/"
# 靜態檔案放 static, 路徑設定時可以省略(static),直接從裡面取得檔案(比如說這裡連動到html設定css路徑的案例)
app = Flask(__name__, static_folder="static", static_url_path="/")
# ========================================================================= #


# 2.Connect with MongoDB's database :
mongoDB_Connect = pymongo.MongoClient(
    "mongodb+srv://root:root123@mycluster.gpvb7.mongodb.net/myFirstDatabase?ssl=true&ssl_cert_reqs=CERT_NONE")

#   2.1 創建(新增) or 搜尋資料庫裡面的"資料庫"名稱(可以有很多資料庫) ex:資料庫名稱MemberData
database = mongoDB_Connect.MemberData
data = database.wehelp  # 創建(新增) or 搜尋資料庫裡面的"集合"名稱  ex:集合名稱 wehelp

#   2.2 新增資料至資料庫 :
# data.insert_one({
#     "name": "David",
#     "email": "wcsodw1@gmail.com",
#     "password": "wehelp123"
# })
print("< ============== 連線至資料庫(修改)data成功 ============== >")

#   2.3 設定session密鑰 : 密秘鑰匙
app.secret_key = "Any string but secret"  # 設定 Session 的秘鑰
# ========================================================================= #


# 3.路由設定 :
#   3.1 首頁
@app.route("/")
def front_page():
    return render_template("front_page.html")


# 3.2 登入路由(無頁面, 藉邏輯導向成功或失敗頁面 -> a.成功頁面 b.失敗頁面) :
# 設定網路權限取得管轄 methods = ["POST"], default為["GET"]
@app.route("/signin", methods=["POST"])
def signin():
    # A.藉由前端取得使用者輸入(信箱與密碼)
    email = request.form["email"]
    password = request.form["password"]

    # B.與資料庫互動-取資料庫資料
    data = database.wehelp

    # C.檢查信箱密碼是否正確 : 邏輯是, 若帳號密碼這兩者同時可以找到, 那麼代表這個帳戶存在
    result = data.find_one({
        "$and": [
            {"email": email},
            {"password": password}
        ]
    })

    # D.若找不到相對應資料,則登入失敗, 並導向錯誤頁面
    if result == None:
        return redirect("/error?msg=帳號密碼輸入錯誤")

    # E.若登入成功, 導向會員頁面
    session["name"] = result["name"]  # 將使用者名稱存到session中(讓電腦記得這個使用者)
    return redirect("/member")  # /memeber = 成功頁面


#   3.3 成功登入會員介面的頁面 :
@app.route("/member")
def member():
    if "name" in session:
        return render_template("member.html")
    # else狀況 : 若會員資料未符合, 就算設定/member路由, 仍會導回首頁
    else:
        return redirect("/")


#   3.4 失敗登入的介面 :
#   /error?msg=錯誤訊息
@app.route("/error")
def error():
    message = request.args.get("msg", "帳號 、或密碼輸入錯誤")
    return render_template("error.html", message=message)
    # (!!) 網址error後面加上(?msg=)後typing可自由加入更改輸入在頁面的文字內容


# 3.5 signout(登出)功能網址 :
@app.route("/signout")
def signout():
    # 移除session中的會員資訊 = 可以使得member介面再次回到
    del session["name"]
    return redirect("/")  # 導回首頁(front_page.html)
# ========================================================================= #


# 4.啟動伺服器 Port-3000
app.run(port=3000)
