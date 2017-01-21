#!/usr/bin/env python
#coding: utf-8
import uuid

def get_random_code(num):
	assert True == isinstance(num,int)
	assert num > 0
	the_random_code = []
	while True:
		tmp = str(uuid.uuid1())
		if tmp not in the_random_code:
			the_random_code.append(tmp)
		num -= 1
		if num == 0:
			break
	return the_random_code

if __name__ == "__main__":
	print get_random_code(200)