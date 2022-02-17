
# Python MemberSystem.py
# python Flask Quickstart 教學(https://flask.palletsprojects.com/en/2.0.x/quickstart/#sessions)
# 讀取所有會員資料的方法
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
email_test = "test"
password_test = 'test'

# 2.路由設定 :
#   2.1 首頁


@app.route("/")
def front_page():
    return render_template("front_page.html")


#   2.2 登入路由(無頁面, 藉邏輯導向成功或失敗頁面 -> a.成功頁面 b.失敗頁面) :
# 設定網路權限取得管轄 methods = ["POST"], default為["GET"]
@app.route("/signin", methods=["POST"])
def signin():
    # 先藉由前端取得使用者輸入(信箱與密碼)
    email = request.form["email"]
    print("email : ", email)
    password = request.form["password"]
    print("password : ", password)

    # A.成功登入 : 信箱/密碼驗證成功, 儲存驗證的Data(Email. Password)放入Session中
    if email == email_test and password == password_test:
        print("Enter")
        session["varify_email"] = email
        session["varify_password"] = password
        return redirect("/member/")

    # # B.失敗登入1 : 若帳號或密碼未輸入, 則登入失敗, 並導向錯誤頁面
    elif email == '' or password == '':
        print("Email or Password is None")
        return redirect("/error?message=請輸入帳號密碼")

    # # C.失敗登入2 : 若帳號密碼有誤, 則登入失敗, 並導向錯誤頁面
    else:
        print("Fail")
        return redirect("/error?message=帳號密碼錯誤")


# 2.3 會員路由 :
@app.route("/member/")
def member():
    # A.若信箱(帳號)及密碼存在資料中(驗證成功的意思), 導向會員頁面
    if session["varify_email"] == email_test and session["varify_password"] == password_test:
        return render_template("member.html")

    # B.若會員資料未符合, 就算設定/member路由, 仍強制導回首頁
    else:
        return redirect("/")


# 2.4 失敗登入的介面 :  # (!!) 網址(error)後面加上 "?msg="" 後typing可自由加入更改輸入在頁面的文字內容
@app.route("/error")
def error():
    # 與前端互動, 抓取後端signin判斷式的值放入前端error.html("")中
    msg = request.args.get("message", "")
    return render_template("error.html", message=msg)


# 2.5 signout(登出)功能網址 :
@app.route("/signout")
def signout():
    # 移除session中的會員資訊 = 可以使得member介面再次回到未輸入帳號密的狀態
    del session["varify_email"]
    del session["varify_password"]
    return redirect("/")  # 導回首頁(front_page.html)
# ========================================================================= #


# 3.啟動伺服器 Port-3000
if __name__ == '__main__':
    app.run(port=3000, debug=True)
