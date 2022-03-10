#! /usr/bin/evn python
# -*- coding:utf-8 -*-
# @Time : 2022/3/7 14:29
# @Author : 郭春华
# @File : test_case_api.py
# @Software : PyCharm
import pytest
from api_keyword.api_key import ApiKey


class TestLogin:

    # @pytest.fixture(scope='class')
    @classmethod
    def setup_class(cls):
        cls.ak = ApiKey()

    def test_login(self):
        url = "http://39.98.138.157:5000/api/login"
        body = {
            "username": "admin",
            "password": "123456"
        }
        res = self.ak.post(url=url, json=body)
        print(res.text)
        # 获取响应中的结果，用于断言
        msg1 = self.ak.get_jsonpath_key_data(res.text, 'msg')
        print(msg1)
        assert msg1[0] == 'success'


if __name__ == '__main__':
    pytest.main(['-s', '../testcase/test_case_api.py'])
