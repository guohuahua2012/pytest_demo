#! /usr/bin/evn python
# -*- coding:utf-8 -*-
# @Time : 2022/3/2 09:43
# @Author : 郭春华
# @File : test_login.py.py
# @Software : PyCharm
import pytest

@pytest.fixture(scope='module', autouse=True) # fixture 装饰器，前后置
def my_fixture():
    print('前置处理')
    yield
    print('后置处理')

class TestLogin:

    def test_login_01(self): # 该用例使用前后置
        print('\n登录测试1')

    def test_login_02(self):
        print('\n登录测试2')

class TestLogout:

    def test_logout_01(self): # 该用例使用前后置
        print('\n登出测试1')

    def test_logout_02(self):
        print('\n登出测试2')


if __name__ == '__main__':
    pytest.main(['-vrs', './testcase/test_login.py'])