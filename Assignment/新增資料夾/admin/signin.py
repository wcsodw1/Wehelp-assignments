from flask import *
import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling
from mysql.connector import connect

import connection.dbconfig as t

admin_signin = Blueprint(
    "admin_signin",
    __name__,
    template_folder="templates/admin"
)

dbconfig = {
    "host": "localhost",
    "port": "3306",
    "user": "root",
    "password": "root1234",
    "database": "L1_W6"
}


def create_connection_pool():
    cnxpool = mysql.connector.pooling.MySQLConnectionPool(
        pool_name="mysqlpool2",
        pool_size=20,
        pool_reset_session=True,
        autocommit=True,
        **dbconfig
    )

    return cnxpool


# /member ( 登入成功 )
@admin_signin.route("/member", methods=["GET"])
def member():
    if "username" in session:
        return render_template("member.html", name=session["name"])
    else:
        return redirect("/")
# /error ( 登入失敗 )


@admin_signin.route("/error")
def error():
    errorMessage = request.args.get("errorMessage", "")
    return render_template("error.html", errorMessage=errorMessage)

# /signin ( 處理中 )


@admin_signin.route('/signin', methods=["POST"])
def signin():
    # cnx = create_connection_pool()
    connection = t.cnxpool.get_connection()
    cursor = connection.cursor()

    username = request.form["username"]
    password = request.form["password"]

    # 查詢會員資料
    query_member = ("SELECT * FROM `member` "
                    "WHERE `username` = %s and `password` = %s")
    query_data = (username, password, )
    cursor.execute(query_member, query_data)

    # 資料回傳是 list 包 tuple
    records = cursor.fetchall()

    if len(records) > 0:
        # 建立 session 保存資料
        session["username"] = username
        session["name"] = records[0][1]

        cursor.close()
        connection.close()

        return redirect(url_for("admin_signin.member"))

    elif len(records) == 0:  # 帳號或密碼輸入錯誤

        cursor.close()
        connection.close()

        return redirect("/error?errorMessage=帳號或密碼輸入錯誤")
