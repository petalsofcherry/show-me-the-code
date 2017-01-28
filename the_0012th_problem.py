# -*- coding: utf-8 -*-

class check_input(object):
    def __init__(self, the_input):
        with open(r"C:\Users\asus\Desktop\我的代码\filtered_words.txt", "r", encoding='utf-8') as file:
            self.lines = file.readlines()
        self.input = the_input

    def check_input_whether_sensitive(self):
        for line in self.lines:
            line = line.strip('\n')
            if line in self.input:
                change = self.input.replace(line, "*" * len(line))
                print(change)
                return
        print(self.input)
        return

if __name__ == "__main__":
    the_input = input("输入你的文本：")
    check = check_input(the_input)
    check.check_input_whether_sensitive()