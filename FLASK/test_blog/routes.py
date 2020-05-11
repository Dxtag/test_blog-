from flask import render_template, url_for, flash, redirect, request
from test_blog.forms import Register, Login, Post_form
from test_blog import app , db, bcrypt
from test_blog.data_forms import Profile, Post



@app.route("/")
def index():
    add_post = Post_form()
    return render_template('index.html', add_post = add_post)

@app.route("/login", methods = ["POST", "GET"])
def login():
    form = Login(request.form)
    if form.validate_on_submit():
        email = form.email.data
        password_database = ""
        password_input = form.password.data

        #if bcrypt.check_password_hash(password_database, password_input):
            #log in 
        #else:
            #flash("invalid e-maill or password","danger")

    return render_template('login.html', title = "login",form = form)

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
      
    return render_template('register.html', title = "register",form = form)

@app.route("/rules")
def rules():
    return render_template('rules.html', title = "rules")

@app.route("/account/")
def account():
    return render_template('account.html')
