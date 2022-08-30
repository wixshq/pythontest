"""
=============
Author: whq
Time: 2022-08-25 20:52


"""
import os.path
import unittest
import ddt


from login import login_check
from handle_excel import HandleExcel


# 获取目录下的测试数据路径
file_fir = os.path.join(os.path.dirname(os.path.abspath(__file__)),"login_cases.xlsx")
print(file_fir)
ex = HandleExcel(file_fir,'login')
datas = ex.read_all_datas()
ex.excel_close()

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
        self.assertEqual(res,eval(case["check"]))



