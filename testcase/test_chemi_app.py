#! /usr/bin/evn python
# -*- coding:utf-8 -*-
# @Time : 2022/3/9 09:36
# @Author : 郭春华
# @File : test_chemi_app.py
# @Software : PyCharm

from tools.yamlControl import get_yaml_data
from common.login import Login

# 执行用例
# 1 获取用例数据
dataInfo = get_yaml_data('../data/loginCase.yaml')[1]
print(dataInfo)
# 2 调用接口方法
res = Login().login(dataInfo['data'], mode=False)
print(res)
# 3 断言
if res['retMsg'] == dataInfo['resp']['retMsg']:
    print('----登录成功----')


