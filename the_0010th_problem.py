# -*- coding: utf-8 -*-

from PIL import Image,ImageDraw,ImageFont
import string
import random

class generate_the_check_code(object):
    #生成随机的四个数
    def generate_random_number(self):
        return ''.join(random.choice(string.ascii_letters) for x in range(4))

    #生成图片
    def generate_the_image(self):
        img = Image.new(imgMode="RGB", imgSize=(640,480), color="White")
        draw = ImageDraw.Draw(img)
        fontsize = int(min(img.size) / 5)
        font = ImageFont.truetype(font = r"C:\Windows\Fonts\arial.ttf", size = fontsize)
        number = self.generate_the_chack_code()
        draw.text((img.size[0] - 4*fontsize, img.size[1] / 2), number, fill=(255, 0, 0), font=font)
        img.save(r"C:\Users\asus\Pictures\Saved Pictures\test1.png")
        img.show()

if __name__ == "__main__":
    test = generate_the_check_code()
    test.generate_the_image()