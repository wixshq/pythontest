"""
=============
Author: whq
Time: 2022-08-29 16:42


"""
import unittest
import os
from BeautifulReport import BeautifulReport

# 获取测试用例路径
cases_dir = os.path.dirname(os.path.abspath(__file__))

s = unittest.TestLoader().discover(cases_dir)

br = BeautifulReport(s)
br.report("测试报告123")

