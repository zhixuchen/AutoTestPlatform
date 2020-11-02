#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 11:17
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : __init__.py
@Project : AutoTestPlatform
"""
from selenium import webdriver
from global_variable import *
from auto_driver.mobile.appium_driver import AppIumDriver
from function.get_config import get


class AppDriver(object):
    def __init__(self, platform_name):
        """
        初始化移动端appium驱动
        :param platform_name: 平台类型：iOS ,Android
        """
        self.platform_name = platform_name
        self.remote_ip = get("app", "remote_ip")
        self.remote_port = get("app", "remote_port")
        self.device_name = get(platform_name, "device_name")
        self.platform_version = get(platform_name, "platform_version")
        self.app_package = get(platform_name, "app_package")
        self.automation_name = get(platform_name, "app_package")
        self.app_activity = get(platform_name, "app_activity")
        self.xcode_org_id = get(platform_name, "xcode_org_id")
        self.xcode_signing_id = get(platform_name, "xcode_signing_id")
        self.ud_id = get(platform_name, "ud_id")
        self.mobile_driver = AppIumDriver(platform_name=self.platform_name,
                                          remote_ip=self.remote_ip,
                                          remote_port=self.remote_port,
                                          device_name=self.device_name,
                                          platform_version=self.platform_version,
                                          app_package=self.app_package,
                                          automation_name=self.automation_name,
                                          app_activity=self.app_activity,
                                          xcode_org_id=self.xcode_org_id,
                                          xcode_signing_id=self.xcode_signing_id,
                                          ud_id=self.ud_id
                                          ).driver

    def teardown(self):
        self.mobile_driver.teardown()


class WebChromeDriver:
    def __init__(self):
        self.chrome_browser = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.chrome_browser.maximize_window()
        self.chrome_browser.implicitly_wait(30)

    def teardown(self):
        self.chrome_browser.quit()


class PcDriver:
    def __init__(self):
        self.platform_name = get("app", "ios_platform_name")
        self.app_package = get("app", "app_package")
        self.app_activity = get("app", "app_activity")
        self.driver = AppIumDriver(platform_name=self.platform_name, app_package=self.app_package,
                                   app_activity=self.app_activity).driver

    def teardown(self):
        self.driver.teardown()
