from flask import request, Response
from main import create_app
from .controller.register_user import register_user
from .controller.login_user import login_user
from .controller.convert_to_text import convert_to_text
from .controller.convert_to_speech import convert_to_speech

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

@app.route('/convert/text', methods=['POST'])
def convert_image_to_text():
    image = request.files['file']
    language = request.form.get('language')
    return convert_to_text(image, language=language)

@app.route('/convert/speech', methods=['POST'])
def convert_image_to_speech():
    image = request.files['file']
    language = request.form.get('language')
    return convert_to_speech(image, language=language)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)
