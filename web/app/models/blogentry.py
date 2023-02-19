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

    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message
        # self.date_created = datetime.datetime.now()
        # self.date_updated = datetime.datetime.now()

    def update(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message
        # self.date_created = date_created
        # self.date_updated = datetime.datetime.now()

