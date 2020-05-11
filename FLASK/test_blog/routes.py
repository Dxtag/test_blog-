from flask import render_template, url_for, flash, redirect, request, session
from test_blog.forms import Register, Login, Post_form
from test_blog import app , db, bcrypt, login_manager
from test_blog.data_forms import Profile, Post
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
def index():
    add_post = Post_form()
    return render_template("index.html", add_post = add_post)

@app.route("/login", methods = ["POST", "GET"])
def login():
    form = Login(request.form)
    if form.validate_on_submit():
        user = Profile.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash("Sucess!","success")
            return redirect(url_for("account", username=user.username))
        else:
            flash("Something wrong","danger")
    return render_template("login.html", title = "login",form = form)

@app.route("/register", methods=["POST", "GET"])
def register():
    form = Register(request.form)
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        profile = Profile(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(profile)
        db.session.commit()
        flash("Account created!", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title = "register",form = form)

@app.route("/rules")
def rules():
    return render_template("rules.html", title = "rules")


@app.route("/account")
@login_required
def account():
    return render_template("account.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))
