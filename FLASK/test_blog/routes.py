from flask import render_template, url_for, flash, redirect, request, session
from test_blog.forms import Register, Login, Post_form
from test_blog import app , db, bcrypt, login_manager
from test_blog.data_forms import Profile, Post
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/index")
@app.route("/home")
@app.route("/")
def index():
    posts =  Post.query.all()
    return render_template("index.html", posts=posts)

@app.route("/login", methods = ["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = Login(request.form)
    if form.validate_on_submit():
        user = Profile.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash("Sucess!","info")
            next_page = request.args.get("next")
            return  redirect(url_for("account")) if next_page else  redirect(url_for("index"))
        else:
            flash("Something wrong","danger")
    return render_template("login.html", title = "login",form = form)

@app.route("/register", methods=["POST", "GET"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = Register(request.form)
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        profile = Profile(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(profile)
        db.session.commit()
        flash("Account created!", "info")
        return redirect(url_for("login"))
    return render_template("register.html", title = "register",form = form)

@app.route("/rules")
def rules():
    return render_template("rules.html", title = "rules")

@app.route("/account", methods=["POST", "GET"])
@login_required
def account():
    form = Post_form()
    if form.validate_on_submit():
        post = Post(topic=form.topic.data, content=form.content.data, profile_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash("Post added!", "info")
    posts = Post.query.filter_by(profile_id=current_user.id).all()
    return render_template("account.html", title=current_user.username, form=form, posts=posts)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/delete_post/<post_id>")
@login_required
def delete_post(post_id):
    Post.query.filter(Post.id == post_id).delete()
    db.session.commit()
    return redirect(url_for("account"))
