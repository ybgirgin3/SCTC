# Import required packages
import cv2
import sys
import pytesseract
from PIL import Image
  
# Mention the installed location of Tesseract-OCR in your system
def ittMain(fn,tess_path):
    pytesseract.pytesseract.tesseract_cmd = tess_path
    text = pytesseract.image_to_string(Image.open(fn), lang="eng")
    print(text)

 
