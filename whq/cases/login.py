"""
=============
Author: whq
Time: 2022-08-30 15:43


"""
import os

def login_check(username=None,password=None):
    if username !=None and password != None:
        if username=="whq" and password=="123456a":
            return {"errcode":0,"errmsg":"登录成功"}
        else:
            return {"errcode":1,"errmsg":"账号或密码错误"}
    else:
        return {"errcode": 1, "errmsg": "账号或密码不能为空"}


if __name__ == '__main__':
    print(os.getcwd()+'\login.py')
    print(os.path.join(os.path.dirname(os.path.abspath(__file__))),'\login.py')