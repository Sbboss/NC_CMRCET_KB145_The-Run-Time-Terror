import pytesseract
pytesseract.pytesseract.tesseract_cmd =r"C:\Program Files\Tesseract-OCR\tesseract.exe"
text = pytesseract.image_to_string("d.jpeg",config="-l eng+urd+tel")
print(text)
