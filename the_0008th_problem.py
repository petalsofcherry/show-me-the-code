# -*- coding: utf-8 -

from bs4 import BeautifulSoup
import urllib.request

def get_the_content(url):
    #定义头部
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}

    #获取网页内容
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    file = response.read().decode('utf-8')

    #soup提取
    content_list = []
    soup = BeautifulSoup(file, 'lxml')
    for string in soup.body.stripped_strings:
        content_list.append(string)
    content  = "\n".join(content_list)

    return content


if __name__ == '__main__':
    content = get_the_content('http://www.qiushibaike.com/hot/page/1')
    print(content)