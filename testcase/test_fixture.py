#! /usr/bin/evn python
# -*- coding:utf-8 -*-
# @Time : 2022/3/3 11:51
# @Author : 郭春华
# @File : test_fixture.py
# @Software : PyCharm
import os

import pytest

data = ['成龙', '李连杰', '吴京', '甄子丹']


@pytest.fixture(params=data, ids=['param1', 'param2', 'param3', 'param4'], name="aaa")
def get_data(request):
    # print(request.param)
    print('前置处理')
    yield request.param
    print('后置处理')


class TestFixture:
    def test_user_login(self, aaa):
        print(f'获取的数据值为：{aaa}')


if __name__ == '__main__':
    pytest.main(['-vs', './testcase/test_fixture.py', 'allure generate ./temp -o ./report --clean'])
    # os.system('allure generate ./temp -o ./report --clean')
