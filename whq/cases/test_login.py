"""
=============
Author: whq
Time: 2022-08-25 20:52


"""
import os.path
import unittest
import ddt


from whq.cases.login import login_check
from whq.common.handle_excel import HandleExcel
from whq.common.my_logger import mylogger




# 获取目录下的测试数据路径
file_fir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "login_cases.xlsx")
print(file_fir)
ex = HandleExcel(file_fir,'login')
datas = ex.read_all_datas()
ex.excel_close()


# datas = [
#     {'username': 'whq', 'password': '123456', 'check': '{"errcode":0,"errmsg":"登录成功"}'},
#     {'username': 'whq1', 'password': '123456', 'check': '{"errcode":1,"errmsg":"账号或密码错误"}'},
#     {'username': None, 'password': '123456', 'check': '{"errcode": 1, "errmsg": "账号或密码不能为空"}'}]

@ddt.ddt
class TestLogin(unittest.TestCase):

    # def setUp(self):
    #     print("开始")
    #
    # def tearDown(self):
    #     print("结束")


    @ddt.data(*datas)
    def test_login_true(self,case):
        mylogger.info("************测试用例开始执行************")
        mylogger.info("测试数据为：{}".format(case))
        res = login_check(case["username"],case["password"])
        mylogger.info("实际运行结果为：{}".format(res))
        try:
            self.assertEqual(res,eval(case["check"]))
        except AssertionError:
            mylogger.exception("断言失败，用例失败！")
            raise
        else:
            mylogger.info("断言成功，用例通过！")
        mylogger.info("************测试用例执行结束************")



