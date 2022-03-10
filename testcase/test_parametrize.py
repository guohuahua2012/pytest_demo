#! /usr/bin/evn python
# -*- coding:utf-8 -*-
# @Time : 2022/3/3 20:39
# @Author : 郭春华
# @File : test_parametrize.py
# @Software : PyCharm
import pytest


class TestApi:
    @pytest.mark.parametrize('name, age', [('chunhua', 18), ('xueqin', 19)])
    def test_case_01(self, name, age):
        print(name, age)


if __name__ == '__main__':
    pytest.main()
