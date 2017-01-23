# -*- coding: utf-8 -*-

import re
import glob

class count_the_code_lines(object):
    #对每个文件里的代码行数，注释行数，以及空行数进行分别计数
    def count_func(self, file, the_dict):
        f = open(file, 'r', encoding='utf-8')
        content = f.read()

        pattern1 = re.compile(r'\s(?<!#)(.*?)\n')
        pattern2 = re.compile(r'\n(\n)')
        pattern3 = re.compile(r'#')

        the_dict['code_lines'] += len(re.findall(pattern1, content))
        the_dict['empty_lines'] += len(re.findall(pattern2, content))
        the_dict['comment_lines'] += len(re.findall(pattern3, content))

    #对文件夹进行遍历，分别打开每个文件
    def traverse(self):
        the_dict = {'code_lines': 0, 'empty_lines': 0, 'comment_lines': 0}
        files = glob.iglob(r"C:\Users\asus\Desktop\我的代码\python\*.py")
        for file in files:
            self.count_func(file, the_dict)
        return the_dict

if __name__ == '__main__':
    test = count_the_code_lines()
    print(test.traverse())