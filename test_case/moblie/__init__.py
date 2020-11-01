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


class MobileCase(object):

    def __init__(self, platform_name):
        self.mobile_action = MobileAction(platform_name)
        self.driver = self.mobile_action.driver

    def teardown(self):
        self.driver.teardown()
