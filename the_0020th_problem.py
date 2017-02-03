# -*- coding:utf-8 -*-

import xlrd
import glob
import re

class count_all_time():
    #统计每个月的通话时间
    def count_time(self, file):
        excel = xlrd.open_workbook(file)
        table = excel.sheet_by_index(0)
        pattern1 = re.compile(r"(\d+)分")
        pattern2 = re.compile(r"(\d+)秒")
        count = 0
        for row in range(1, table.nrows):
            cell_val =  table.row(row)[3].value
            pattern1 = re.compile(r"(\d+)分")
            pattern2 = re.compile(r"(\d+)秒")
            m1 = re.search(pattern1, cell_val)
            m2 = re.search(pattern2, cell_val)
            if m1:
                min = int(m1.group(1))
                count += 60 * min
            second = int(m2.group(1))
            count += second
        return count



    #遍历所有文件
    def traverse(self):
        files = glob.iglob(r"C:\Users\asus\Desktop\通话记录\*.xls")
        count = 0
        for file in files:
            count += self.count_time(file)
        return str(count)+"秒"

if __name__ == "__main__":
    test = count_all_time()
    print(test.traverse())