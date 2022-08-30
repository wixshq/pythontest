"""
=============
Author: whq
Time: 2022-08-29 16:42


"""

import unittest
from HTMLTestRunner import HTMLTestRunner
from BeautifulReport import BeautifulReport

s = unittest.TestLoader().discover(r"C:\Users\Administrator\Desktop\pythontest\whq")

# runner = unittest.TextTestRunner()
# runner.run(s)

# with open("report.html","wb") as fs:
#     HTMLTestRunner(fs).run(s)

br = BeautifulReport(s)
br.report("测试报告")