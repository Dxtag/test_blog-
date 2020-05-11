from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, Form
from wtforms.validators import DataRequired, Length, EqualTo, Email


class Register(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up!")
    rules = BooleanField(validators=[DataRequired()])


class Login(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
    remember_me = BooleanField("Remember me")


class Post_form(FlaskForm):
    topic =  StringField("Topic", validators=[DataRequired(),Length(min=2,max=100)])
    content = TextAreaField("Content", render_kw={"rows":5},validators=[Length(min=2)] )
    submit = SubmitField("Send")
                                             

