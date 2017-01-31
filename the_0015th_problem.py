# -*- coding: utf-8 -*-

import xlwt
import json

def toxls():
    path = r"C:\Users\asus\Desktop\city.txt"
    with open(path, "r",  encoding="utf-8") as file:
        content = file.read()
    dictory = json.loads(content)
    workbook = xlwt.Workbook()
    table = workbook.add_sheet("Sheet1")

    #枚举写入内容
    for row, id in enumerate(dictory):
        table.write(row, 0, id)
        table.write(row, 1, dictory[id])

    pathExcel = path.replace("txt", "xls")
    workbook.save(pathExcel)

if __name__ == "__main__":
    toxls()