#!/usr/bin/env python3
#coding: utf-8
import uuid
import redis

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

def save_in_redis():
    HOST = 'localhost'
    PORT = 6379
    r = redis.Redis(HOST, PORT)
    randon_code = get_random_code(200)
    for i in randon_code:
        r.sadd('code', i)
    r.save()

if __name__ == '__main__':
    save_in_redis()