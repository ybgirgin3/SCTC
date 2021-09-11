# Import required packages

from PIL import Image
import pytesseract
import pyperclip as pc
import cv2
import sys

  
# Mention the installed location of Tesseract-OCR in your system
def ittMain(fn,tess_path):
    pytesseract.pytesseract.tesseract_cmd = tess_path
    text = pytesseract.image_to_string(Image.open(fn), lang="eng").strip()
    #print(text)
    #print(type(text))
    pc.copy(text)
    return text
    #print(pc.paste())


 
