#! /usr/bin/evn python
# -*- coding:utf-8 -*-
# @Time : 2022/3/9 22:58
# @Author : 郭春华
# @File : test_one.py
# @Software : PyCharm

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

