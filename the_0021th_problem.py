# -*- coding:utf-8 -*-
import os
from hashlib import sha256
from hmac import HMAC

#加密密码，保证盐值类型是bytes
def encrypt_passwd(passwd, salt = None):
    if None == salt:
        salt = os.urandom(8)

    assert len(salt) == 8
    assert isinstance(salt, bytes)

    if isinstance(passwd, str):
        passwd = passwd.encode()
    assert isinstance(passwd, bytes)

    result = passwd
    for i in range(10):
        result = HMAC(result, salt, sha256).digest()

    return salt + result

#验证密码
def check_paaswd(hashed, passwd):
    salt = hashed[:8]
    return hashed == encrypt_passwd(passwd, salt)

passwd = input("输入你的密码：")
hashed = encrypt_passwd(passwd)
new_passwd = input("输入你的密码:")
if check_paaswd(hashed, new_passwd):
    print("密码正确")
else:
    print("密码错误")