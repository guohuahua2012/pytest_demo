#! /usr/bin/evn python
# -*- coding:utf-8 -*-
# @Time : 2022/3/9 23:52
# @Author : 郭春华
# @File : conftest.py
# @Software : PyCharm

import pytest
import sys
sys.dont_write_bytecode = True

@pytest.fixture()
def action():
    print("测试用例开始".center(30, '*'))
    yield
    print("测试用例结束".center(30, '*'))