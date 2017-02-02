# -*- coding:utf-8 -*-

'''
果然在windows下就会遇见一大堆的编码问题，真是累。
话说我会用vim的其实……主要是VB太卡不想用。
'''

import json
import xml.dom.minidom as minidom
from collections import OrderedDict
import xlrd
import html.parser

class xls_to_xml():
    def __init__(self, path):
        self.path = path
        self.xmlpath = path.replace("xls", "xml")
        self.comment = '''
            <!--
                学生信息表
                "id" : [名字, 数学, 语文, 英文]
            -->
        '''

    #读取xls
    def get_xls(self):
        excel = xlrd.open_workbook(self.path)
        sheet = excel.sheet_by_name("Sheet1")
        dictory = OrderedDict()
        for i in range(sheet.nrows):
            values = sheet.row_values(i)
            dictory[values[0]] = values[1:]
        return dictory

    #生成xml
    def generate_xml(self):
        dom = minidom.getDOMImplementation().createDocument(None, 'root', None)
        root = dom.documentElement
        students = dom.createElement("students")
        root.appendChild(students)

        comment = dom.createTextNode(self.comment)

        dictory = json.dumps(self.get_xls(), ensure_ascii=False)
        information = dom.createTextNode(dictory)

        students.appendChild(comment)
        students.appendChild(information)

        with open(self.xmlpath, 'w') as file:
            html_parser = html.parser.HTMLParser()
            tranform = html_parser.unescape(dom.toxml())
            file.write(tranform)


if __name__ == "__main__":
    path = r"C:\Users\asus\Desktop\student.xls"
    test = xls_to_xml(path)
    test.generate_xml()
