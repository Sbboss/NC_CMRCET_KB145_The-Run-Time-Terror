import cv2
import matplotlib.pyplot as plt
from PIL import Image
from pytesseract import Output
import pytesseract
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
import nltk

def cv(a):
    img = cv2.imread(a,)
    #if img == None:
      #  img = plt.imread(a)
    d = pytesseract.image_to_data(img, config='-l eng --psm 11', output_type=Output.DICT)
    # print(d['text'])
    overlay = img.copy()
    n_boxes = len(d['text'])

    text = 'the'
    text = word_tokenize(text)
    n_boxes = len(d['text'])
    print(text)
    ic=1
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:
           # print(d['text'][i])
            if (d['text'][i]) in text:
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                cv2.rectangle(overlay, (x, y), (x + w, y + h), (255, 0, 0), -1)
                alpha = 0.4
                img_new = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)
                width = 600
                height = 650
                dim = (width, height)
                resized = cv2.resize(img_new, dim, interpolation = cv2.INTER_AREA)
                fn = "page_"+str(ic)+".jpg"
                plt.imsave(fn,resized)
                ic=ic+1