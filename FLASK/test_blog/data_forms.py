from datetime import datetime
from test_blog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(profile_id):
    return Profile.query.get(int(profile_id))

class Profile(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey("profile.id"), nullable=False)

    def __repr__(self):
        return f"Post('{self.topic}', '{self.date_posted}')"
