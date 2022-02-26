
# python app.py
from flask import Flask, jsonify, url_for, json, request, render_template, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
# from flask_restful import Resource, Api

app = Flask(
    __name__,
    static_folder="static",  # 靜態檔案的資料夾名稱
    static_url_path="/"  # 靜態檔案對應的網址路徑
)

app.secret_key = "any string but secret"  # 設定 session 的密鑰


def db_connection():
    mydb = None
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            database="website",
            password="root",
            charset="utf8"
        )
    except mysql.connector.Error as e:
        print(e)
    return mydb


@app.route("/")
def index():
    return render_template("home.html")


@app.route('/api/members', methods=['GET'])
def find_member():
    username = request.args.get('username')
    mydb = db_connection()
    mycursor = mydb.cursor()
    sql = """
        SELECT id, name, username FROM member_ WHERE username = %s;
    """
    val = (username, )
    mycursor.execute(sql, val)
    num = mycursor.fetchone()
    if num:
        return {'data': {
            'id': num[0],
            'name': num[1],
            'username': num[2]
        }
        }
    else:
        return {'data': None}


@app.route('/api/member', methods=['GET', 'POST'])
def update_member():
    if "username" in session:
        new_name = request.get_json(request.data)
        username = session['username']
        sql = """
            UPDATE member_ SET name = %s WHERE username = %s
        """
        val = (new_name['name'], username, )
        mydb = db_connection()
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        return {"ok": "true"}
    else:
        return {"error": "true"}


# 可以抓到全部的資料

@app.route("/api/members/", methods=["GET"])
def api_member():
    mydb = db_connection()
    mycursor = mydb.cursor()
    sql = """
            SELECT * FROM member;
        """
    mycursor.execute(sql)
    num = mycursor.fetchall()
    return jsonify(num)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        # A.串接前後端, 接收前端會員註冊的資料至後端
        #   A1.request.form  : 取得來自前端註冊的資料
        userDetails = request.form
        Name = userDetails['name_new']
        Email = userDetails['username_new']
        Password = userDetails['password_new']

        print("")
        print("===========")
        print("Test Member Regist data : ", Name, Email, Password)

        # B.連接MySQL資料庫
        db = db_connection()
        cursor = db.cursor()
        # C.確認註冊帳號是否已被註冊 :
        #   sql = "SELECT * FROM memeber_data" # 抓取table所有資料(不建議使用, 資料量大時運送效能會非常差)
        #   cursor.execute(sql)

        # (!!關鍵SQL指令)用WHERE方法, 只單純取出符合條件的值(就不會一次要取出整個資料庫TABLE的資料)
        cursor.execute(
            "SELECT * FROM member_ WHERE username = %s", (Email,))

        #   C1.這邊的result代表已取出與使用者輸入相對應的帳號(email)值(名稱)
        results = cursor.fetchone()  # cursor.fetchall()
        print("results :", results)
        print("results type :", type(results))
        # print("results=%s" % (results))

        if results != None:
            print("Account already exist!")

            # C2.用Query String的方法處理要新增至前端html中的字串, message(變數名稱)
            return redirect("/error?message=信箱已被註冊")

        # D.若帳號無被註冊, 註冊新帳號 :
        #   D1.連接資料庫裏面的Table(ex : MEMEBER_DATA), 及Insert裡面有的資料參數
        sql = "INSERT INTO member_ (name, username, password, follower_count) VALUES (%s,%s, %s,0)"
        # E.讀取A中的註冊資料, 放入
        val = (Name, Email, Password)
        cursor.execute(sql, val)
        db.commit()
        print(cursor.rowcount, "筆資料被記錄.")
        return redirect("/")


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]

        sql = """
            SELECT * FROM member_ WHERE username = %s and password = %s;
        """
        val = (username, password)
        mydb = db_connection()
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        num = mycursor.fetchone()
        if num:
            session["name"] = num[1]
            session["username"] = username
            # session["password"] = password
            return redirect('/member')
        elif (username == '' and password == '') or (username == '' and password != '') or (username != '' and password == ''):
            result = "請輸入帳號、密碼"
            return redirect(url_for('error', message=result))
        else:
            result = "帳號或密碼輸入錯誤"
            return redirect(url_for('error', message=result))


@app.route("/member/")
def member():
    if "username" in session:
        name = session['name']
        return render_template("member.html", name=name)
    else:
        return redirect("/")


@app.route("/error")
def error():
    error = request.args.get("message")
    return render_template("error.html", message=error)


@app.route("/signout")
def signout():
    session.pop('username', None)
    return redirect('/')


app.run(port=3000, debug=True)
