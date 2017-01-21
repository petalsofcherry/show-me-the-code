# -*- coding:utf-8 -*-
import re

class tocount(object):
    def countword(self, text):
        pattern = re.compile(r'\W')
        the_list = re.split(pattern, text)
        return len(the_list)

