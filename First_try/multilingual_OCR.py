import pytesseract
pytesseract.pytesseract.tesseract_cmd =r"C:\Program Files\Tesseract-OCR\tesseract.exe"

number=input("Enter no.of languages:")
if number=='1':
    language_input = input("Enter language: ")
    language= '-l ' + language_input.lower()[:3]
    text = pytesseract.image_to_string("d.jpeg",config=language)
    
elif number=='2':
    language_input1 = input("Enter 1st language: ")
    language_input2= input("Enter 2nd language: ")
    language = language_input1.lower()[:3]+'+'+language_input2.lower()[:3]
    text = pytesseract.image_to_string("d.jpeg",lang=language)
else:

    text = pytesseract.image_to_string("d.jpeg","eng+urd+tel")
    
print(text)
