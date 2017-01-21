# -*- coding: utf-8 -*-

from PIL import Image
import glob

def changeImage():
    count = 0
    for files in glob.glob("C:\\Users\\asus\\Pictures\\Saved Pictures\\creative design\\*.jpg"):
        count += 1
        im = Image.open(files)
        newim = im.resize((1136,640))
        newim.save("C:\\Users\\asus\\Pictures\\Saved Pictures\\test\\" + str(count) + ".jpg")
changeImage()