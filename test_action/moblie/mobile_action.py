#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 11:17
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : mobile_action.py
@Project : AutoTestPlatform
"""
from auto_driver.auto_driver import Driver
from element.elements import Element
from global_variable import *
from function.check import CheckAssert

import os


class MobileAction(object):
    def __init__(self):
        """
        初始化
        """
        self.check = CheckAssert()
        self.action_plugins = {}
        self.load_actions()

    def load_actions(self):
        """
        加载action的插件
        :return: 返回acton插件的类
        """
        for filename in os.listdir(MOBILE_ACTION_PLUGIN_PATH):
            if not filename.endswith(".py") or filename.startswith("_"):
                continue
            action_name = os.path.splitext(filename)[0]
            action = __import__("static_file.mobile_plugins." + action_name, fromlist=[action_name])
            action_class = action.get_plugin_class()
            action_class_name = action_class.__name__
            self.action_plugins[action_class_name] = action_class

    def driver(self, platform_name):
        """
        获取驱动
        :param platform_name: 平台类型
        :return: 驱动
        """
        self.driver = Driver(platform_name).driver()
        return self.driver

    def element(self, driver):
        """
        获取元素处理方法类
        :param driver: 驱动
        :return:
        """
        self.element = Element(driver)
        return self.element
