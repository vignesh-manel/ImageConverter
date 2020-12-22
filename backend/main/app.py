from flask import Flask, request, Response
from db_config import initialize_db
from models.users import User
import os
from dotenv import load_dotenv
load_dotenv('.flaskenv')

app = Flask(__name__)

DB_URI = os.environ.get("MONGODB_URL")

app.config['MONGODB_HOST'] = DB_URI

initialize_db(app)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/users/register', methods=['POST'])
def register():
    body = request.get_json()
    user = User(**body).save()
    id = user.id
    return {"id":str(id)},201

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)
