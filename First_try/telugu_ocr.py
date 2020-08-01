from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img=Image.open(r"D:\telugu_image.jpeg")


text=pytesseract.image_to_string(img,lang='tel')
print(text)
