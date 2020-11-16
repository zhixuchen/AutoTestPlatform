#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 11:32
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : auto_driver.py
@Project : AutoTestPlatform
"""
from WebforAutoTestPlatform.auto_driver import *
from WebforAutoTestPlatform.function.exception_action import ExceptionAction


class Driver(object):
    def __init__(self):
        """
        初始化驱动调用程序
        :param platform_name: 平台类型：iOS,Android
        """

        self.platform = str(Config.objects.get(conf_key="platform"))

    def driver(self):
        """
        驱动调用
        :return:
        """
        try:

            if "iOS" in self.platform or "Android" in self.platform:

                self.app_driver = AppDriver().mobile_driver
                print("打印Driver的内容：", self.app_driver)
                return self.app_driver
            elif "pc" in self.platform:
                pass
            elif "web" in self.platform:
                self.web_driver = WebChromeDriver().chrome_browser
                return self.web_driver
            elif "api" in self.platform:
                pass
            elif "shell" in self.platform:
                pass
            elif "sip" in self.platform:
                pass
        except Exception as e:
            ExceptionAction().log().error(e)
            raise Exception(e)
