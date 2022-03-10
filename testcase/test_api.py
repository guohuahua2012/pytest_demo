#! /usr/bin/evn python
# -*- coding:utf-8 -*-
# @Time : 2022/3/2 09:39
# @Author : 郭春华
# @File : test_api.py
# @Software : PyCharm
import pytest


@pytest.mark.skipif(1 == 2, reason='跳过TestApi类，会跳过类中所有的方法')
class TestApi:

    # @pytest.mark.smoke
    def test_01(self):
        print('第1条测试用例')
        assert 1 == 1

    # @pytest.mark.run(order=1)
    def test_02(self):
        print('第2条测试用例')
        assert 1 == 2


if __name__ == '__main__':
    pytest.main(['-rs', './testcase/test_api.py'])
