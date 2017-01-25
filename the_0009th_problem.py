# -*- coding: utf-8 -*-

import requests
import re

def get_the_link(url):
    #定义头部，获取html
    headers = {
        'content-type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
    }
    content = requests.post(url, headers = headers)
    html = content.text

    #找到链接
    pattern = re.compile(r'<a href="(.*?)".*?</a>')
    link = re.findall(pattern, html)

    return link

if __name__ == "__main__":
    print(get_the_link(r"https://www.baidu.com/s?ie=UTF-8&wd=requests%20python"))