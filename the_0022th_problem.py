# -*- coding:utf-8 -*-

from PIL import Image
import glob

class change_image():
    def __init__(self, phone_type = 'iPhone5'):
        self.phone_type = phone_type
        self.phone_config = {
            'iPhone5': (1136, 640),
            'iPhone6': (1334, 750),
            'iPhone6Plus': (2208, 1242)
        }

    #变成对应型号的尺寸
    def change(self):
        for file in glob.iglob("C:\\Users\\asus\\Pictures\\Saved Pictures\\test\\*.jpg"):
            size = self.phone_config[self.phone_type]
            img = Image.open(file)
            newim = img.resize(size)
            newim.save(file)

if __name__ == "__main__":
    test = change_image('iPhone6')
    test.change()
