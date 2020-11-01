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
import logging
from global_variable import *


def get(title, string):
    try:
        config = configparser.ConfigParser()
        config.read(CONFIG_PATH)
        result = config.get(title, string)
        return result
    except Exception as e:
        logging.error("获取配置报错：" + e)
