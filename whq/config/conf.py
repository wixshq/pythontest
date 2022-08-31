"""
=============
Author: whq
Time: 2022-08-31 15:29


"""

import os
from configparser import ConfigParser


class HandleConfig(ConfigParser):
    def __init__(self, file_path):
        super().__init__()
        self.read(file_path, encoding="utf-8")


file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
conf = HandleConfig(file_path)

if __name__ == '__main__':
    conf = HandleConfig("setting.ini")
    value = conf.get("log", "a")
    print(value)
