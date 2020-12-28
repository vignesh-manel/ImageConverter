from .. import db

class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    name = db.StringField(required=True)
    password = db.StringField(required=True)
