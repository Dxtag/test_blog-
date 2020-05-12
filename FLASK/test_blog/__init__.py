import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

folder = os.path.dirname(os.path.abspath(__file__))
database = os.path.join(folder, "site.db")

app = Flask(__name__)
app.secret_key = "]xf7x9fxabxcfx87{xadjxd3exea4RYA"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{ database }"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
from test_blog import routes



