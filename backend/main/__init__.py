import os
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
load_dotenv('.flaskenv')

db = MongoEngine()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)

    DB_URI = os.environ.get("MONGODB_URL")
    app.config['MONGODB_HOST'] = DB_URI

    db.init_app(app)
    
    bcrypt.init_app(app)

    return app

