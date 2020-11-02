#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 11:32
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : auto_driver.py
@Project : AutoTestPlatform
"""
from auto_driver import *
from function.exception_action import ExceptionAction


class Driver(object):
    def __init__(self, platform_name):
        """
        初始化驱动调用程序
        :param platform_name: 平台类型：iOS,Android
        """
        self.platform_name = platform_name

    def driver(self):
        """
        驱动调用
        :return:
        """
        try:
            if "iOS" in self.platform_name or "Android" in self.platform_name:
                self.app_driver = AppDriver(self.platform_name).mobile_driver
                return self.app_driver
            elif "pc" in self.platform_name:
                pass
            elif "web" in self.platform_name:
                self.web_driver = WebChromeDriver().chrome_browser
                return self.web_driver
            elif "api" in self.platform_name:
                pass
            elif "shell" in self.platform_name:
                pass
            elif "sip" in self.platform_name:
                pass
        except Exception as e:
            ExceptionAction().log().error(e)
            raise Exception(e)
