from ..models.users import User
import re
from .. import bcrypt


def register_user(request):
    body = request.get_json()
    email_re = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    email = body["email"]
    name = body["name"]
    password = body["password"]
    confirmPassword = body["confirmPassword"]

    if (email == ''  or name == '' or password == '' or confirmPassword == ''):
        return {"msg":"Please enter all the fields"}, 400

    if not(re.search(email_re,email)):
        return {"msg":"Please enter a valid email id"}, 400

    if (password != confirmPassword):
        return {"msg":"Passwords do not match"}, 400
    
    try:
        existing_user = User.objects.get(email= body["email"])
    except:
        existing_user = None
        
    if (existing_user):
        return {"msg": "This email id is already registered"}, 400

    password_hash = bcrypt.generate_password_hash(password).decode('UTF-8')

    user_data = {"email":email,"name":name,"password":password_hash}
    user = User(**user_data).save()
    id = user.id
    return {"id":str(id)},201
