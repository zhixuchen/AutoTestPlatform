#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 11:17
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : __init__.py
@Project : AutoTestPlatform
"""
from WebforAutoTestPlatform.test_action.moblie.mobile_action import MobileAction


class MobileCase(object):
    def __init__(self,suite_id):
        self.mobile_action = MobileAction(suite_id)
