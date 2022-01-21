
# Python UpdateMemberSystem.py
# python Flask Quickstart 教學(https://flask.palletsprojects.com/en/2.0.x/quickstart/#sessions)
# ========================================================================= #


# 1.Preprocessing :
#   1.1 Import Module :
from flask import Flask, render_template, request, redirect, session

#   1.2 建立物件, 設定靜態路徑(ex:static)
# 靜態default路徑已("/")為出發點, ex:static_url_path="/"
# 靜態檔案放 static, 路徑設定時可以省略(static),直接從裡面取得檔案(比如說這裡連動到html設定css路徑的案例)
app = Flask(__name__, static_folder="static", static_url_path="/")

#  1.3 設定session密鑰 : 密秘鑰匙
app.secret_key = "Any string but secret"  # 設定 Session 的秘鑰
# ========================================================================= #


# 2.路由設定 :
#   2.1 首頁
@app.route("/")
def front_page():
    return render_template("front_page.html")


#   2.2 登入路由(無頁面, 藉邏輯導向成功或失敗頁面 -> a.成功頁面 b.失敗頁面) :
# 設定網路權限取得管轄 methods = ["POST"], default為["GET"]
@app.route("/signin", methods=["POST"])
def signin():

    # A.先藉由前端取得使用者輸入(信箱與密碼)
    email = request.form["email"]
    password = request.form["password"]

    # B.失敗登入的介面 : 若找不到相對應資料,則登入失敗, 並導向錯誤頁面
    if email and password != "test":
        message = request.args.get("msg", "帳號 、或密碼輸入錯誤")
        return render_template("error.html", message=message)  # error = 失敗頁面

    # C.成功登入的話, 儲存驗證的Data(Email. Password)放入session中
    session["varify_email"] = email
    session["varify_password"] = password
    return redirect("/member/")  # memeber = 成功頁面


# 2.3 會員路由 :
@app.route("/member/")
def member():
    # A.若信箱(帳號)及密碼存在資料中(驗證成功的意思), 導向會員頁面
    if "varify_email" and "varify_password" in session:
        return render_template("member.html")

    # B.若會員資料未符合, 就算設定/member路由, 仍強制導回首頁
    else:
        return redirect("/")


# 2.4 失敗登入的介面 :  # (!!) 網址(error)後面加上 "?msg="" 後typing可自由加入更改輸入在頁面的文字內容
@app.route("/error")
def error():
    # 這邊操作要在html中新增的文字, 並回傳至html
    message = request.args.get("msg", "帳號 、或密碼輸入錯誤")
    return render_template("error.html", message=message)


# 2.5 signout(登出)功能網址 :
@app.route("/signout")
def signout():
    # 移除session中的會員資訊 = 可以使得member介面再次回到未輸入帳號密的狀態
    del session["varify_email"]
    del session["varify_password"]
    return redirect("/")  # 導回首頁(front_page.html)
# ========================================================================= #


# 3.啟動伺服器 Port-3000
app.run(port=3000)
