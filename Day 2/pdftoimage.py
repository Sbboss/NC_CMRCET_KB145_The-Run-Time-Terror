from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

pdf_file =  r"C:\Users\sonal priya\PycharmProjects\tesser\venv\d.pdf"
page= convert_from_path(pdf_file,poppler_path=r'C:\Users\sonal priya\Desktop\poppler-0.68.0_x86\poppler-0.68.0\bin')
image_counter=1
for pages in page:
    filename= "page_"+str(image_counter)+".jpg"
    pages.save(filename,'JPEG')
    image_counter = image_counter+1
    for i in range(1,image_counter):
        filename= "page_"+str(i)+".jpg"
        text=str(((pytesseract.image_to_string(Image.open(filename)))))
print(text)








