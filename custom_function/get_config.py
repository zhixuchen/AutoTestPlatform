#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version:
author:c30002875
@time: 2020/04/30
@file: get_config.py
@function:
@modify:
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
