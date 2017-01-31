# -*- coding: utf-8 -*-

import xlwt
import re

def toxls():
    path = r"C:\Users\asus\Desktop\student.txt"
    file = open(path, "r", encoding="utf-8")
    contents = file.readlines()
    workbook = xlwt.Workbook()
    # 增加一个sheet页'Sheet1'
    worksheet1 = workbook.add_sheet('Sheet1')

    #用正则匹配相应的内容
    pattern0 = re.compile(r'"(\d+)"')
    pattern1 = re.compile(r'\["(.*?)"')
    pattern2 = re.compile(r',(\d+)')

    row = 0
    col = 0
    for content in contents[1:-1]:
        #用正则取出相应的内容
        id = re.findall(pattern0, content)[0]
        name = re.findall(pattern1, content)[0]
        score_list = re.findall(pattern2, content)

        #写入相应的内容
        worksheet1.write(row, col, id)
        worksheet1.write(row, col + 1, name)
        worksheet1.write(row, col + 2, score_list[0])
        worksheet1.write(row, col + 3, score_list[1])
        worksheet1.write(row, col + 4, score_list[2])
        row += 1

    file.close()
    pathExcel = path.replace("txt", "xls")
    workbook.save(pathExcel)

if __name__ == "__main__":
    toxls()