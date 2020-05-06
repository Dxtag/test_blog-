from flask import Flask, render_template, url_for, request, flash, redirect, session
from flask_sqlalchemy import SQLAlchemy
from forms import Login,Register

app = Flask(__name__)
app.secret_key = "]xf7x9fxabxcfx87{xadjxd3exea4RYA"


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods = ["POST", "GET"])
def login():
    pass

@app.route("/register", methods=["POST", "GET"])
def register():
    pass

@app.route("/rules")
def rules():
    pass

        
if __name__ == '__main__':
    app.run(debug=True)
