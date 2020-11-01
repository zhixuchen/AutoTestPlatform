#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 11:17
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : get_config.py
@Project : AutoTestPlatform
"""
import configparser
from global_variable import *
from function.exception_action import ExceptionAction


def get(title, string):
    try:
        config = configparser.ConfigParser()
        config.read(CONFIG_PATH)
        result = config.get(title, string)
        return result
    except Exception as e:
        ExceptionAction().log().error("获取配置报错：" + title+"下的"+string+"获取失败")
        raise Exception(e)
