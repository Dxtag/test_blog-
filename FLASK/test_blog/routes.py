from flask import render_template, url_for, flash, redirect, request
from test_blog.forms import Register, Login, Post
from test_blog import app #, db, bcrypt
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods = ["POST", "GET"])
def login():
    form = Login(request.form)

    if form.validate_on_submit():
        flash("Jak to nie zadziała to dupa", "success") # kod wyświetlający tą wiadomośc jest w base.html nie index.html
        return redirect(url_for("index"))

    return render_template('login.html', title = "login",form = form)

@app.route("/register", methods=["POST", "GET"])
def register():
    form = Register(request.form)
    return render_template('register.html', title = "register",form = form)

@app.route("/rules")
def rules():
    return render_template('rules.html', title = "rules")

@app.route("/account/")
def account():
    add_post = Post()
    return render_template('account.html', add_post = add_post)
