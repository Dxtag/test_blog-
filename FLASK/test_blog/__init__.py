from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "]xf7x9fxabxcfx87{xadjxd3exea4RYA"
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqllite:///site.db"
#db = SQLAlchemy(app)
#bcrypt = Bcrypt(app)

from test_blog import routes



