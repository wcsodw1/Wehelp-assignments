from flask import *
import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling
from mysql.connector import connect

import connection.dbconfig as t

admin_signup = Blueprint(
    "admin_signup",
    __name__,
    template_folder="/templates/admin"
)

dbconfig = {
    "host": "localhost",
    "port": "3306",
    "user": "root",
    "password": "root1234",
    "database": "website"
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

# /error ( 註冊失敗 )


@admin_signup.route("/error", methods=["GET"])
def error():
    errorMessage = request.args.get("errorMessage", "")
    return render_template("error.html", errorMessage=errorMessage)

# /signup ( 處理中 )


@admin_signup.route('/signup', methods=["POST"])
def signup():
    # cnx = create_connection_pool()

    connection = t.cnxpool.get_connection()

    cursor = connection.cursor()

    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]

    query_member = ("SELECT * FROM `member` "
                    "WHERE `username` = %s")

    query_data = (username, )

    cursor.execute(query_member, query_data)
    # 資料回傳是 list 包 tuple
    records = cursor.fetchall()

    # /signup/error
    if len(records) > 0:

        cursor.close()
        connection.close()

        return redirect("/error?errorMessage=帳號已經被註冊")
    # / : 註冊成功，導回首頁網址
    elif (len(name) > 0) and (len(username) > 0) and (len(password) > 0):  # 首次註冊，且資料填寫正確
        session["username"] = username
        add_member = (
            "INSERT INTO `member` (`name`, `username`, `password`) VALUES (%s, %s, %s)")
        data_member = (name, username, password)
        cursor.execute(add_member, data_member)
        connection.commit()

        cursor.close()
        connection.close()

        return redirect("/")
