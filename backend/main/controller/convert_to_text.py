from PIL import Image
import pytesseract
from googletrans import Translator

def convert_to_text(image, language):
    img = Image.open(image)
    pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
    text = pytesseract.image_to_string(img)
    t = Translator()
    converted_text = t.translate(text, dest=language)
    
    return {"text":converted_text.text},200
