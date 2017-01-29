# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import urllib.request

def getImage():
    #获取html
    headers = {
        'content-type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
    }
    url = r"http://tieba.baidu.com/p/2166231880"
    content = requests.get(url = url, headers=headers)
    html = content.text

    #获取图片
    soup = BeautifulSoup(html, "lxml")
    divs = soup.find_all("div", class_="d_post_content j_d_post_content clearfix")
    count = 0
    for div in divs:
        images = div.find_all("img")
        for image in images:
            image = image.get("src")
            urllib.request.urlretrieve(image, "C:\\Users\\asus\\Desktop\\image\\" + str(count) + ".jpg")
            count += 1


if __name__ == "__main__":
        getImage()