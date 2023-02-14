from app import db
from sqlalchemy_serializer import SerializerMixin

class BlogEntry(db.Model, SerializerMixin):
    __tablename__ = "blogentry"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    message = db.Column(db.String(280))

    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message


    def update(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message


