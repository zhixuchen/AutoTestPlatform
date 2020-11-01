#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 15:38
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : __init__.py.py
@Project : AutoTestPlatform
"""
from test_action.moblie.mobile_action import MobileAction


class MobileCase:
    def __init__(self):
        self.mobile_action = MobileAction()
