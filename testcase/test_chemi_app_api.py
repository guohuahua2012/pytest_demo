#! /usr/bin/evn python
# -*- coding:utf-8 -*-
# @Time : 2022/3/9 13:56
# @Author : 郭春华
# @File : test_chemi_app_api.py
# @Software : PyCharm

import pytest
from common.login import Login
from tools.yamlControl import get_yaml_data


# 登录接口-测试类封装
class TestLogin:
    # 测试方法
    @pytest.mark.parametrize('inBody,expData', get_yaml_data('../data/loginCase.yaml'))
    def test_login(self, inBody, expData):
        # 调用业务层代码
        res = Login().login(inBody, False)
        # 断言
        assert res['retMsg'] == expData['retMsg']


if __name__ == '__main__':
    pytest.main(["./testcase/test_chemi_app_api.py", "-vs", "--allure", "../report/temp/"])
