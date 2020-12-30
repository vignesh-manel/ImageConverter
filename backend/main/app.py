from flask import request, Response
from main import create_app
from .controller.register_user import register_user
from .controller.login_user import login_user

app = create_app()

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/users/register', methods=['POST'])
def register():
    return register_user(request)

@app.route('/users/login', methods=['POST'])
def login():
    return login_user(request)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)
