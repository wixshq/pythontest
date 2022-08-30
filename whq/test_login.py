"""
=============
Author: whq
Time: 2022-08-25 20:52


"""
import os.path
import unittest

import ddt
from login import login_check

datas = [
    {"username":"whq","password":"123456","check":{"errcode":0,"errmsg":"登录成功"}},
    {"username":"whq1","password":"123456","check":{"errcode":1,"errmsg":"账号或密码错误"}},
    {"username":"123","password":"123456","check":{"errcode": 1, "errmsg": "账号或密码不能为空"}},
]

@ddt.ddt
class TestLogin(unittest.TestCase):

    # def setUp(self):
    #     print("开始")
    #
    # def tearDown(self):
    #     print("结束")


    @ddt.data(*datas)
    def test_login_true(self,case):
        res = login_check(case["username"],case["password"])
        self.assertEqual(res,case["check"])



