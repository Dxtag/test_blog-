from flask import render_template, url_for, flash, redirect
from test_blog.forms import Register, Login
from test_blog import app
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods = ["POST", "GET"])
def login():
    login = Login()
    return render_template('login.html', title = "login",login = login)

@app.route("/register", methods=["POST", "GET"])
def register():
    register = Register()
    return render_template('register.html', title = "register",register = register)

@app.route("/rules")
def rules():
    return render_template('rules.html', title = "rules")
