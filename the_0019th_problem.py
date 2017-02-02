# -*- coding:utf-8 -*-

import json
import xml.dom.minidom as minidom
import xlrd
import html.parser

class xls_to_xml():
    def __init__(self, path):
        self.path = path
        self.xmlpath = path.replace("xls", "xml")
        self.comment = '''
            <!--
                数字信息
            -->
        '''

    #读取xls
    def get_xls(self):
        excel = xlrd.open_workbook(self.path)
        sheet = excel.sheet_by_name("Sheet1")
        the_list = []
        for i in range(sheet.nrows):
            values = sheet.row_values(i)
            the_list.append(values)
        return the_list

    #生成xml
    def generate_xml(self):
        dom = minidom.getDOMImplementation().createDocument(None, 'root', None)
        root = dom.documentElement
        numbers = dom.createElement("numbers")
        root.appendChild(numbers)

        comment = dom.createTextNode(self.comment)

        dictory = json.dumps(self.get_xls(), ensure_ascii=False)
        information = dom.createTextNode(dictory)

        numbers.appendChild(comment)
        numbers.appendChild(information)

        with open(self.xmlpath, 'w') as file:
            html_parser = html.parser.HTMLParser()
            tranform = html_parser.unescape(dom.toxml())
            file.write(tranform)


if __name__ == "__main__":
    path = r"C:\Users\asus\Desktop\numbers.xls"
    test = xls_to_xml(path)
    test.generate_xml()