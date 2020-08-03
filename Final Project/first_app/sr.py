import cv2
from PIL import Image
from pytesseract import Output
import pytesseract
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
import re
import sys

fp = sys.argv[1]
a = sys.argv[2]
text = sys.argv[3]
fn = sys.argv[4]
langs = sys.argv[5]


def cv(fp, text, fn, langs):
    global count
    count = 0
    img = cv2.imread(fp)
    # resized = Image.open(fp)
    d = pytesseract.image_to_data(img, config=langs, output_type=Output.DICT)
    overlay = img.copy()

    text = word_tokenize(text)
    n_boxes = len(d['text'])
    for i in range(n_boxes  ):
        if int(d['conf'][i]) > 60:
            for j in text:
                if re.search(j, d['text'][i], flags=re.UNICODE):
                    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                    cv2.rectangle(overlay, (x, y), (x + w, y + h), (0,255,240), -1)
                    alpha = 0.4
                    img_new = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)
                    count += 1
    try:
       resized = Image.fromarray(img_new)
       fp = fp.replace('page', 'page_')
       resized.save(fp)
       path = '/media/page_' + str(fn) + '.jpg'
       print(path)
       print(count)
    except:
        img = Image.fromarray(img)
        fp = fp.replace('page', 'page_')
        img.save(fp)
        path = '/media/page_' + str(fn) + '.jpg'
        print(path)
        print(count)


cv(fp, text, fn, langs)