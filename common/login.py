#! /usr/bin/evn python
# -*- coding:utf-8 -*-
# @Time : 2022/3/9 09:40
# @Author : 郭春华
# @File : login.py
# @Software : PyCharm
import requests

from configs.config import HOST


class Login:

    def login(self, inData, mode=True):  # 登录方法
        path = "/ucas/user/app/login"
        url = HOST + path
        payload = inData
        resp = requests.request("POST", url=url, json=payload, verify=False)
        if mode:
            return resp.json()['data']['token'] # 获取用户token
        return resp.json() # 返回响应信息


if __name__ == '__main__':
    result = Login().login({"telNum": "18198247429", "password": ""}, mode=False)
    print(result)
