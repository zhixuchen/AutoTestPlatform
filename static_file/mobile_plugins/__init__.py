#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/2 0:28
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : __init__.py.py
@Project : AutoTestPlatform
"""
from WebforAutoTestPlatform.static_file.mobile_cases import MobileCase


class MobilePlugin(object):
    def __init__(self,suite_id):
        self.mobile_plugin = MobileCase(suite_id).mobile_action.action_plugins

    def mobile_plugins(self, plugin_name,  **kwargs):
        self.mobile_plugin[plugin_name](**kwargs)
