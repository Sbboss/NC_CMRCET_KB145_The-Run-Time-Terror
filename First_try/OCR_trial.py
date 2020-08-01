from PIL import Image
import pytesseract


#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img=Image.open(r"C:\Users\Shiv\Desktop\OCR\io.jpg")

lang_in = input("Enter language: ")


langs = '-l ' + lang_in.lower()[:3]

text=pytesseract.image_to_string(img,config=langs)
print(text)
