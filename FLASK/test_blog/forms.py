from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, Form
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from test_blog.data_forms import Profile
from flask_login import current_user


class Register(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up!")
    rules = BooleanField()

    def validate_username(self, username):
        user = Profile.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username already exist")

    def validate_email(self, email):
        user = Profile.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email taken")
    def validate_rules(self, rules):
            rule = (rules.data == False)
            if rule:
                raise ValidationError("Click checkbox bruh")
        

class Login(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
    remember_me = BooleanField("Remember me")

    def validate_email(self, email):
        user = Profile.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError("The account with this e-mail does not exist")


class Post_form(FlaskForm):
    topic =  StringField("Topic", validators=[DataRequired(),Length(min=2,max=100)])
    content = TextAreaField("Content", render_kw={"rows":5},validators=[Length(min=2)] )
    submit = SubmitField("Send")

                                             
class Change_form(FlaskForm):
    username = StringField("Username", validators=[Length(min=2, max=20)])
    email = StringField("E-mail", validators=[Email()])
    submit = SubmitField("Update")

    def validate_username(self, username):
        if current_user != username.data:
            user = Profile.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("Username already exist")

    def validate_email(self, email):
        if current_user != email.data:
            user = Profile.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("Email taken")
    
