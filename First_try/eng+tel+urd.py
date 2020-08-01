from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img=Image.open(r"D:\sampleurdtel.jpeg")

c=r"-l urd+eng+tel"
text=pytesseract.image_to_string(img, config=c)
print(text)
