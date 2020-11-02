#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/2 23:11
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : PluginTemplate.py
@Project : AutoTestPlatform
"""

from function.exception_action import ExceptionAction
from test_action.moblie.android import B
from test_action.moblie.ios import I
from test_action.moblie.mobile_action import MobileAction


class PluginTemplate(object):
    def __init__(self, *args, **kwargs):
        self.platform_name = args[0]
        self.driver = MobileAction().driver(self.platform_name)
        self.element = MobileAction().element(self.driver)
        self.start(**kwargs)

    def start(self, **kwargs):
        ExceptionAction().log().info("======执行" + self.__class__.__name__ + "；参数为：" + str(locals()))
        try:
            account = kwargs.get("account")
            pwd = kwargs.get("pwd")
            if "Android" == self.platform_name:
                """
                写代码的区域
                """
            elif "iOS" == self.platform_name:
                """
                写代码的区域
                """
            ExceptionAction().log().info("======执行" + self.__class__.__name__ + "结束")
        except Exception as e:
            ExceptionAction().log().error(e)
            ExceptionAction().app_catch_image(self.driver)
            raise Exception(e)


def get_plugin_class():
    return PluginTemplate
