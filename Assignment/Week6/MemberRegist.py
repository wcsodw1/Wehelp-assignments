
# python MemberRegist.py
# 讀取單一(效能較佳)會員資料的方法


# 1.Preprocess :
#   1.1 Import Library
from tkinter import INSERT
import pymysql
from flask import Flask, render_template, request, redirect, session

#   1.2 設定靜態路由及初始路由:
app = Flask(__name__, static_folder="static", static_url_path="/")
#   1.3 設定session密鑰 : 密秘鑰匙
app.secret_key = "Any string but secret"  # 設定 Session 的秘鑰
# ================================================================== #


''' PartA : Sign Up '''


# 2.路由設定 :
#   2.1 首頁
@app.route("/")
def front_page():
    return render_template("front_page.html")


#   2.1 Signup :
@app.route("/signup", methods=["POST"])
def signup():
    # A.串接前後端, 接收前端會員註冊的資料至後端
    #   A1.request.form  : 取得來自前端註冊的資料
    Name = request.form["name"]
    Email = request.form["email"]
    Password = request.form["password"]

    print("")
    print("===========")
    print("Test Member Regist data : ", Name, Email, Password)

    # B.連接MySQL資料庫
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         database='website')
    cursor = db.cursor()

    # C.確認註冊帳號是否已被註冊 :
    #   sql = "SELECT * FROM memeber_data" # 抓取table所有資料(不建議使用, 資料量大時運送效能會非常差)
    #   cursor.execute(sql)

    # (!!關鍵SQL指令)用WHERE方法, 只單純取出符合條件的值(就不會一次要取出整個資料庫TABLE的資料)
    cursor.execute("SELECT * FROM memeber_data WHERE ACCOUNT = %s", (Email,))

    #   C1.這邊的result代表已取出與使用者輸入相對應的帳號(email)值(名稱)
    results = cursor.fetchone()  # cursor.fetchall()
    print("results :", results)
    print("results type :", type(results))
    print("results=%s" % (results))

    if results != None:
        print("Account already exist!")

        # C2.用Query String的方法處理要新增至前端html中的字串, message(變數名稱)
        return redirect("/error?message=信箱已被註冊")

    # D.若帳號無被註冊, 註冊新帳號 :
    #   D1.連接資料庫裏面的Table(ex : MEMEBER_DATA), 及Insert裡面有的資料參數
    sql = "INSERT INTO MEMEBER_DATA (NAME, ACCOUNT, PASSWORD) VALUES (%s,%s, %s)"
    # E.讀取A中的註冊資料, 放入
    val = (Name, Email, Password)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "筆資料被記錄.")

    return redirect("/")


'''================  PartB : Log In(Sign In)  ==============='''


# 3.1 登入路由 :
# 設定網路權限取得管轄 methods = ["POST"], default為["GET"]
@app.route("/signin", methods=["POST"])
def signin():
    # A.藉由前端取得使用者輸入(帳號與密碼)
    email = request.form["email"]
    print("email : ", email)
    password = request.form["password"]
    print("password : ", password)

    # B.連接MySQL資料庫
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         database='website')
    cursor = db.cursor()

    # C.搜尋資料庫, 若帳號密碼吻合登入 :
    # sql = "INSERT INTO MEMEBER_DATA (ACCOUNT, PASSWORD) VALUES (%s,%s)"
    # val = (email, password)
    # cursor.execute(sql, val)

    # 一樣用WHERE方法(指讀取一筆資料)確認帳號密碼若吻合, 取出資料
    cursor.execute(
        "SELECT * FROM memeber_data WHERE account = %s and password= %s ", (email, password,))

    results = cursor.fetchone()
    print("results :", results)
    print("results type :", type(results))  # tuple

    # D.判斷式
    #   D1.若沒找到重複帳號密碼, 新增會員資料
    if results != None:
        # 1.儲存mail至session, 供後續登出系統(/signout)刪除使用
        session["sess_email"] = email
        # 2.Query String : 擷取會員名稱放入, member.html中顯示(xxx，歡迎登入系統)
        session["sess_Name"] = results[0]
        print("session[sess_Name] :", session["sess_Name"])

        return redirect("/member")

    #   D2.若帳號密碼有任一個空值, 藉由query string輸出"請輸入帳號密碼"
    elif email == "" or password == "":
        return redirect("/error?message=請輸入帳號密碼")  # 就是一個路由(網址)

    #   D3.若帳號密碼錯誤, 藉由query string輸出"帳號密碼錯誤"
    else:
        return redirect("/error?message=帳號密碼錯誤")


# 3.2 會員路由 :
@app.route("/member/")
def member():
    # A.若帳號(email)資料存在session, 進入會員頁面
    if "sess_email" in session:  # and "varify_password" in session:
        msg = session["sess_Name"]
        return render_template("member.html", Name_args=msg)

    # B.若會員資料未符合, 就算設定/member路由, 仍強制導回首頁
    else:
        return redirect("/")


# 3.3 失敗登入的介面 :
@app.route("/error")
def error():
    # Query String與前端互動, 抓取後端signin判斷式的值放入前端error.html("")中
    msg = request.args.get("message", "")
    return render_template("error.html", message=msg)


# 3.4 signout(登出)功能網址 :
@app.route("/signout")
def signout():
    # (!)移除session中的會員資訊 = 可以使得member介面再次回到未輸入帳號的狀態
    del session["sess_email"]
    return redirect("/")  # 導回首頁(front_page.html)
# ========================================================================= #


# 4.啟動伺服器 Port-3000
if __name__ == '__main__':
    app.run(port=3000, debug=True)
