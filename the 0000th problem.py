# -*- coding:utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

def draw_num(img,number):
    draw = ImageDraw.Draw(img)
    fontsize = int(min(img.size) / 5)
    numFont = ImageFont.truetype(font = "C:\\Windows\\Fonts\\arial.ttf", size = fontsize)
    draw.text((img.size[0] - fontsize, 0), number, fill = (255,0,0), font = numFont)
    img.show()
    img.save("C:\\Users\\asus\\Pictures\\Saved Pictures\\logo\mytest.png")

if __name__ == '__main__':
    image = Image.open("C:\\Users\\asus\\Pictures\\Saved Pictures\\logo\\personal-monogram_1x.png")
    draw_num(image, "99")
