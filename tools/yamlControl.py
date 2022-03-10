#! /usr/bin/evn python
# -*- coding:utf-8 -*-
# @Time : 2022/3/9 10:29
# @Author : 郭春华
# @File : yamlControl.py
# @Software : PyCharm

import yaml


def get_yaml_data(filePath):
    # 读取文件 从磁盘文件中读取文件到内存
    case_data = []
    with open(filePath, 'r', encoding="utf-8") as fo:  # fileObject 文件对象
        # 使用yaml方法获取数据
        result = yaml.load(fo, Loader=yaml.FullLoader)
        # 过滤yaml文件中第1组数据，仅取用例数据集
        result = result[1:]
        # 封装用例数据，组合成[(请求数据1，预期结果1),(请求数据2，预期结果2)]
        for i in result:
            case_data.append((i['data'], i['validate']))
        return case_data


if __name__ == '__main__':
    res = get_yaml_data('../data/loginCase.yaml')
    for i in res:
        print(i)
