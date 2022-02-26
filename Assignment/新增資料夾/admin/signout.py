
from flask import *
import mysql.connector

admin_signout = Blueprint(
    "admin_signout",
    __name__,
    template_folder="/templates/admin"
)
# signout


@admin_signout.route("/signout")
def signout():
    # 移除 Session
    del session["username"]
    del session["name"]
    return redirect("/")
