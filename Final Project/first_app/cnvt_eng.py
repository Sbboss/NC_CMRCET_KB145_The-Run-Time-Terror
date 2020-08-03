from textblob import TextBlob
import cv2
import matplotlib.pyplot as plt
import os
def text_to_eng(text):
    d = ''
    c = ''
    b = TextBlob(text)
    try:
        c = b.translate(from_lang='ur', to='en')
    except:
        c = str(b)
    c = TextBlob(str(c))
    try:
        d = c.translate(from_lang='te', to='en')
    except:
        d = str(c)
    if isinstance(d, str):
        return TextBlob(d).correct()
    return d.correct()

