from flask import *
import mysql.connector

import connection.dbconfig as t

admin_api = Blueprint(
    "admin_api",
    __name__,
    template_folder="/templates/admin"
)


dbconfig = {
    "host": "localhost",
    "port": "3306",
    "user": "root",
    "password": "root",
    "database": "mywebsite"
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


@admin_api.route("/members", methods=["GET"])
def queryMember():
    username = request.args.get("username", "")

    # cnx = create_connection_pool()
    connection = t.cnxpool.get_connection()
    cursor = connection.cursor()

    # 查詢會員資料
    query_member = ("SELECT * FROM `member` "
                    "WHERE `name` = %s")
    query_data = (username, )
    cursor.execute(query_member, query_data)

    # 資料回傳是 list 包 tuple
    records = cursor.fetchall()

    cursor.close()
    connection.close()

    if len(records) > 0:
        output = {
            "id": records[0][0],
            "name": records[0][1],
            "username": records[0][2]
        }
        # return {"data": output}
        return jsonify({"data": output})
    else:
        return jsonify({"data": None})


@admin_api.route("/member", methods=["POST"])
def updateMember():
    if "username" in session:
        username = request.get_json()

        # cnx = create_connection_pool()
        connection = t.cnxpool.get_connection()
        cursor = connection.cursor()

        # 查詢會員資料
        update_member = ("UPDATE `member` "
                         "SET `name` = %s "
                         "WHERE `username` = %s")
        update_data = (username["name"], session["username"])
        cursor.execute(update_member, update_data)

        connection.commit()

        cursor.close()
        connection.close()
        # 成功
        return jsonify({"ok": True})
    else:
        # 失敗
        return jsonify({"error": True})
