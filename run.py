#! /usr/bin/evn python
# -*- coding:utf-8 -*-
# @Time : 2022/3/2 09:45
# @Author : 郭春华
# @File : run.py.py
# @Software : PyCharm
import os

import pytest

# @pytest.mark.parametrize()

if __name__ == '__main__':
    pytest.main(['-vs', './testcase/test_fixture.py'])
    os.system('allure generate ./temp -o ./report --clean')