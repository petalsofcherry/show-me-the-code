# -*- coding: utf-8 -*-
'''
这个题看起来简单，遇到的坑挺多的，比如记录到最多的词是冠词之类的。
还有从时间复杂度上考虑，其实应该首选哈希表，次选快速排序的。
不过Python自己有轮子，我就不自己造了。
'''
import glob
from collections import Counter
import re

class get_the_most_important_word(object):
    #记录下每一篇日记最多的词及出现次数
    def getword(self, file):
        stop_word = ['the', 'in', 'of', 'and', 'to', 'has', 'that', 'this','s', 'is', 'are', 'a', 'with', 'as', 'an']
        f = open(file,'r')
        content = f.read().lower()

        pattern = re.compile(r'\w+')
        words = re.findall(pattern, content)
        wordlist = Counter(words)
        for i in wordlist:
            if i in stop_word:
                wordlist[i] = 0
        f.close()
        return wordlist.most_common()[0]

    #遍历目录下所有文件
    def traverse(self):
        files = glob.iglob(r"C:\Users\asus\Desktop\diary\*.txt")
        most_important_word = []
        for file in files:
            most_important_word.append(self.getword(file))
        return most_important_word

get_all_word = get_the_most_important_word()
print(get_all_word.traverse())