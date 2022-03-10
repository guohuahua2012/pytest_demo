#! /usr/bin/evn python
# -*- coding:utf-8 -*-
# @Time : 2022/3/7 09:16
# @Author : 郭春华
# @File : api_key.py
# @Software : PyCharm

'''

关键字驱动：
1.接口中，模拟各个请求的方法: post/get/put/delete/header/...
2.设置入参为默认值时，设置的参数必须放在最后
'''
import json

import jsonpath
import requests


class ApiKey:
    # get请求的封装 ，可能存在无参数的情况，默认设置为None
    def get(self, url, params=None, **kwargs):
        return requests.get(url=url, params=params, **kwargs)

    # post请求的封装，同样存在无参数的情况，默认设置为None
    def post(self, url, data=None, **kwargs):
        return requests.post(url=url, data=data, **kwargs)

    # jsonpath 通过关键字key获取json值的封装
    def get_jsonpath_key_data(self, txt, key):
        """
        通过jsonpath获取对应关键字的值
        :param txt: 数据源，json格式的数据
        :param key: 关键字
        :return: value
        """
        try:
            # 加载数据
            txt = json.loads(txt)
            # 通过jsonpath表达式获取值，获取成功则返回list,否则，返回False
            value = jsonpath.jsonpath(txt, f'$..{key}')
            if value: # 返回数据不为False
                if len(value) > 1:
                    return value[0]
                return value
        except Exception as e:
            return e
        return value

if __name__ == '__main__':
    ak = ApiKey()
    data = {
        "username": "admin",
        "password": "123456"
    }
    res = ak.post(url='http://39.98.138.157:5000/api/login', json=data, timeout=0.1)
    print(res.text)

