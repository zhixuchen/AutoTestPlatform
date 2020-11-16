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
from WebforAutoTestPlatform.global_variable import *
from WebforAutoTestPlatform.auto_driver.mobile.appium_driver import AppIumDriver
from Test_Platform.models import Config


class AppDriver(object):
    def __init__(self):
        """
        初始化移动端appium驱动
        :param platform_name: 平台类型：iOS ,Android
        """
        self.platform_name =str(Config.objects.get(conf_name="app", conf_key="platform"))
        self.remote_ip = str(Config.objects.get(conf_name="app", conf_key="remote_ip"))
        self.remote_port = str(Config.objects.get(conf_name="app", conf_key="remote_port"))
        self.device_name = str(Config.objects.get(conf_name=self.platform_name, conf_key="device_name"))
        self.platform_version = str(Config.objects.get(conf_name=self.platform_name, conf_key="platform_version"))
        self.app_package =str( Config.objects.get(conf_name=self.platform_name, conf_key="app_package"))
        self.automation_name =str( Config.objects.get(conf_name=self.platform_name, conf_key="automation_name"))
        self.app_activity = str(Config.objects.get(conf_name="Android", conf_key="app_activity"))
        self.xcode_org_id = str(Config.objects.get(conf_name="iOS", conf_key="xcode_org_id"))
        self.xcode_signing_id =str( Config.objects.get(conf_name="iOS", conf_key="xcode_signing_id"))
        self.ud_id = str(Config.objects.get(conf_name="iOS", conf_key="ud_id"))
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
        pass

    def teardown(self):
        pass
