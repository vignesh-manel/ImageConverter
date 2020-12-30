from ..models.users import User
import re
from .. import bcrypt
from bson.json_util import dumps, loads
import jwt
from flask import current_app

def login_user(request):
    body = request.get_json()
    email_re = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    email = body["email"]
    password = body["password"]

    if (email == ''  or password == ''):
        return {"msg":"Please enter all the fields"}, 400

    if not(re.search(email_re,email)):
        return {"msg":"Please enter a valid email id"}, 400

    try:
        existing_user = User.objects.get(email= body["email"])
    except:
        existing_user = None

    if not (existing_user):
        return {"msg": "No user registered with this email id"}, 400

    isMatch = bcrypt.check_password_hash(existing_user["password"], password)

    if not isMatch:
        return {"msg": "Invalid Credentials"}, 400

    token = jwt.encode({"id": dumps(existing_user["id"])}, current_app.config.get('SECRET_KEY'),algorithm='HS256')

    return {"token":token,"email":existing_user["email"],"name":existing_user["name"]}, 200
