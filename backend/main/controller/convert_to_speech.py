from PIL import Image
import pytesseract
from gtts import gTTS
from flask import send_file
from googletrans import Translator

def convert_to_speech(image, language):
    img = Image.open(image)
    pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
    text = pytesseract.image_to_string(img)
    t = Translator()
    converted_text = t.translate(text, dest=language)
    speech = gTTS(text=converted_text.text, lang = language, slow=False)
    speech.save('output.mp3')

    return send_file('../output.mp3',as_attachment=True,attachment_filename='output.mp3'),200
             
    
