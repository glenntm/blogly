from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

#creates user table
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    image_url = db.Column(db.String(400))

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    content = db.Column(db.String(500), unique=False, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Tag(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    testName = db.Column(db.String(80), unique=False, nullable=True)
    #make sure that the name is not blank
    __table_args__ = (
        CheckConstraint('name != '''),
    )

#joint table between post and tags
class PostTag(db.Model):
    __tablename__ = "post_tags"
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)


#    def __repr__(self):
#        return f'<User {self.username}>'