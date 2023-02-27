from flask_login import UserMixin

from app import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import DateTime
from datetime import datetime

class BlogEntry(db.Model, SerializerMixin):
    __tablename__ = "blogentry"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    message = db.Column(db.String(280))
    date_created = db.Column(DateTime,default = datetime.utcnow)
    date_updated = db.Column(DateTime,default = datetime.utcnow, onupdate= datetime.utcnow)
    avatar_url = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, name, email, message, avatar_url,password):
        self.name = name
        self.email = email
        self.message = message
        self.avatar_url = avatar_url
        self.password = password

    def update(self, name, email, message, avatar_url,password):
        self.name = name
        self.email = email
        self.message = message
        self.avatar_url = avatar_url
        self.password = password
        
class PrivateBlogEntry(BlogEntry, UserMixin, SerializerMixin):
    owner_id = db.Column(db.Integer, db.ForeignKey('blogentry.id'))

    def __init__(self, name, emil, message,password,avatar_url, owner_id):
        super().__init__(name, email, message,password,avatar_url)
        self.owner_id = owner_id


