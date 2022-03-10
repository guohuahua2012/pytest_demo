#! /usr/bin/evn python
# -*- coding:utf-8 -*-
# @Time : 2022/3/7 10:21
# @Author : 郭春华
# @File : json_path_test.py
# @Software : PyCharm

import jsonpath, json

data = {
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
            },
            {
                "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
            },
            {
                "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99
            },
            {
                "category": "fiction",
                "author": "J. R. R. Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
            }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    },
    "expensive": 10
}

bicycle = jsonpath.jsonpath(data, '$.store.bicycle')
print(bicycle)

book = jsonpath.jsonpath(data, '$.store.book')
print(book)

# 获取store节点下所有的price节点的值
price = jsonpath.jsonpath(data, '$.store..price')
print(price)

# 获取指定book下的price节点的值
book_price = jsonpath.jsonpath(data, '$.store.book[0:4].price')
print(book_price)

# 获取price大于10的所有book节点
book_price_10 = jsonpath.jsonpath(data, '$..book[?(@.price>10)]')
print(book_price_10)

