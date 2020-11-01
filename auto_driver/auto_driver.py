#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 11:32
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : auto_driver.py
@Project : AutoTestPlatform
"""
from auto_driver.mobile.appium_driver import AppIumDriver
from function.get_config import get
from function.exception_action import ExceptionAction


class Driver(object):
    def __init__(self, platform_name):
        try:
            if "iOS" == platform_name or "Android" == platform_name:
                self.platform_name = platform_name
                self.remote_ip = get("app", "remote_ip")
                self.remote_port = get("app", "remote_port")
                self.device_name = get(platform_name, "device_name")
                self.platform_version = get(platform_name, "platform_version")
                self.app_package = get(platform_name, "app_package")
                self.app_activity = get(platform_name, "app_activity")
                self.mobile_driver = AppIumDriver(platform_name=self.platform_name,
                                                  remote_ip=self.remote_ip,
                                                  remote_port=self.remote_port,
                                                  device_name=self.device_name,
                                                  platform_version=self.platform_version,
                                                  app_package=self.app_package,
                                                  app_activity=self.app_activity).driver
            elif "pc" == platform_name:
                pass
            elif "web" == platform_name:
                pass
            elif "api" == platform_name:
                pass
            elif "shell" == platform_name:
                pass
            elif "sip" == platform_name:
                pass
        except Exception as e:
            ExceptionAction().log().error(e)
            raise Exception(e)
