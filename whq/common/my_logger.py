"""
=============
Author: whq
Time: 2022-08-31 12:31


"""

import logging

class MyLogger(logging.Logger):

    def __init__(self,name,level=logging.INFO,file=None):
        super().__init__(name,level)

        # 设置渠道的日志格式
        fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d line :%(message)s'
        formatter = logging.Formatter(fmt)

        # 控制台输出渠道
        handle1 = logging.StreamHandler()
        # # 可以给渠道设置单独的日志级别
        # handle1.setLevel(logging.ERROR)
        # 将日志格式绑定到渠道中
        handle1.setFormatter(formatter)
        # 将渠道添加到日志收集器
        self.addHandler(handle1)


        # 文件输出渠道
        if file:
            handle2 = logging.FileHandler(file, encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)



mylogger = MyLogger("whq日志", file=r"../whq/log/my2.log")


if __name__ == '__main__':
    pass