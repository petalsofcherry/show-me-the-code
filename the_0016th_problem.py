# -*- coding:utf-8 -*-

import xlwt
import json

def toxls():
    #打开文件，进行转换
    path = r"C:\Users\asus\Desktop\numbers.txt"
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    the_lists = json.loads(content)
    workbook = xlwt.Workbook()
    table = workbook.add_sheet("Sheet1")

    #写入excel
    for row, the_list in enumerate(the_lists):
        for col, number in enumerate(the_list):
            table.write(row, col, number)

    #保存
    pathExcel = path.replace("txt", "xls")
    workbook.save(pathExcel)

if __name__ == "__main__":
    toxls()