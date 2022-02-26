# python app.py
from flask import *

# 功能
from admin.signin import admin_signin
from admin.signup import admin_signup
from admin.signout import admin_signout
from admin.api import admin_api

app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)

app.secret_key = "any string but secret"

# 註冊 Flask Blueprints
app.register_blueprint(admin_signin)
app.register_blueprint(admin_signup)
app.register_blueprint(admin_signout)
app.register_blueprint(admin_api, url_prefix="/api")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=3000, debug=True)
