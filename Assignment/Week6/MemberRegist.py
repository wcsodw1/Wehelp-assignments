
# python MemberRegist.py


# 1.Preprocess :
#   1.1 Import Library
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

    # C.確認註冊帳號是否已被註冊
    sql = "SELECT * FROM memeber_data"
    cursor.execute(sql)
    results = cursor.fetchall()
    username_ = []
    #   C1.寫迴圈確認是否account已存在, 若已存在導入error路由
    for row in results:
        account = row[1]
        print("已存在之帳號名稱 :", account)

        # 打印结果
        print("account=%s" % (account))
        if Email == account:
            username_.append(Email)
            print("Account already exist!")
            message = request.args.get("msg", "信箱已被註冊")
            return render_template("error.html", message=message)

    # D.若帳號無被註冊, 註冊新帳號 :
    #   D1.連接資料庫裏面的Table(ex : MEMEBER_DATA), 及裡面有的資料參數
    sql = "INSERT INTO MEMEBER_DATA (NAME, ACCOUNT, PASSWORD) VALUES (%s,%s, %s)"
    # E.讀取A中的註冊資料, 放入
    val = (Name, Email, Password)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "筆資料被記錄.")

    return redirect("/")
    # 根據接收到的資料, 與資料庫互動


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

    # C.搜尋資料庫, 若帳號密碼吻合登入
    sql = "SELECT * FROM memeber_data"
    cursor.execute(sql)
    results = cursor.fetchall()
    name_list = []
    username_list = []
    password_list = []

    for row in results:
        Name_ = row[0]
        account_ = row[1]
        password_ = row[2]

        print("account=%s" % (account_))
        if email == account_ and password == password_:
            name_list.append(Name_)
            print("name_list :", name_list)
            username_list.append(account_)
            password_list.append(password_)
            # A.儲存mail至session, 供後續登出系統(/signout)刪除使用
            session["sess_email"] = email
            # B.Query String : 擷取會員名稱放入, member.html中顯示(xxx，歡迎登入系統)
            message = request.args.get("msg",  name_list)
            return render_template("member.html", Name_args=message)

    # D.若帳號密碼錯誤, 導入錯誤路由
    return redirect("/error")


# 3.2 會員路由 :
@app.route("/member/")
def member():
    # A.若帳號(email)資料存在session, 進入會員頁面
    if "sess_email" in session:  # and "varify_password" in session:
        print("sess_email yes")
        return render_template("member.html")

    # B.若會員資料未符合, 就算設定/member路由, 仍強制導回首頁
    else:
        return redirect("/")


# 3.3 失敗登入的介面 :
@app.route("/error")
def error():
    message = request.args.get("msg", "帳號 、或密碼輸入錯誤")
    return render_template("error.html", msg=message)


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
