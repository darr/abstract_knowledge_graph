#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : main.py
# Create date : 2019-08-20 13:52
# Modified date : 2019-08-20 14:20
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function


from search_concept import ConceptNet

def test_search():
    handler = ConceptNet()
    handler.search_hiearchy()

def search_text():
    handler = ConceptNet()
    all_dict = handler.build_all_concepts()
    print("1. 名词抽象路径")

    wd = "爱情"
    query_text(all_dict, wd)
    wd = "女朋友"
    query_text(all_dict, wd)
    wd = "儿子"
    query_text(all_dict, wd)
    wd = "老板"
    query_text(all_dict, wd)
    wd = "狗"
    query_text(all_dict, wd)
    wd = "苹果"
    query_text(all_dict, wd)
    wd = "梨"
    query_text(all_dict, wd)

    print("2. 状态词抽象路径")
    wd = "亢奋"
    query_text(all_dict, wd)
    wd = "悲伤"
    query_text(all_dict, wd)
    wd = "开心"
    query_text(all_dict, wd)

    print("3. 动作抽象路径")
    wd = "吹牛"
    query_text(all_dict, wd)
    wd = "吃饭"
    query_text(all_dict, wd)
    wd = "睡觉"
    query_text(all_dict, wd)
    wd = "打牌"
    query_text(all_dict, wd)
    wd = "斗殴"
    query_text(all_dict, wd)
    wd = "杀人"
    query_text(all_dict, wd)
    wd = "诬陷"
    query_text(all_dict, wd)
    wd = "打击"
    query_text(all_dict, wd)
    wd = "制裁"
    query_text(all_dict, wd)

    print("4. 其他")
    wd = "离"
    query_text(all_dict, wd)
    wd = "乎"
    query_text(all_dict, wd)

def query_text(all_dict, wd):
    paths = all_dict.get(wd, '')
    if paths:
        for path in paths:
            print(wd, '抽象路径为：', '->'.join(path))
    print("\n")

def run():
    search_text()
    test_search()

run()
