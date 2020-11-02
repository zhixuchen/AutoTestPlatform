#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 11:17
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : qppium_driver.py
@Project : AutoTestPlatform
"""
from appium import webdriver
from function.exception_action import ExceptionAction


class AppIumDriver(object):
    def __init__(self, platform_name, remote_ip, remote_port, device_name, platform_version, app_package,
                 automation_name, app_activity=None, xcode_org_id=None, xcode_signing_id=None, ud_id=None):
        """
        初始化移动端驱动
        :param platform_name: 平台类型：iOS、Android 必填
        :param remote_ip: appium远程IP 必填
        :param remote_port: appium远程端口 必填
        :param device_name: 设备名称
        :param platform_version: 设备平台版本
        :param app_package: 应用包名
        :param automation_name:自动化使用的框架：Android：uiautomator2 ；iOS：XCUITest
        :param app_activity: 应用首页
        :param xcode_org_id:苹果开发者组织ID
        :param xcode_signing_id:苹果开发者ID
        :param ud_id:苹果设备ID
        """
        if "Android" == platform_name:
            self.desired_caps = {
                'platformName': "Android",
                'deviceName': device_name,
                'appPackage': app_package,
                'appActivity': app_activity,
                'platformVersion': platform_version,
                'noSign': True,
                'adbPort': 9999,
                'automationName': automation_name,
                'dontStopAppOnReset': True,
                'noReset': True,
                'newCommandTimeout': 72000,
                'defaultCommandTimeout': 600,
                'resetKeyboard': True,
                'unicodeKeyboard': True,
                'avdArgs': '-session-override -no-reset'
            }
        elif "iOS" == platform_name:
            self.desired_caps = {
                'platformName': "iOS",
                'deviceName': device_name,
                'bundleId': app_package,
                'platformVersion': platform_version,
                'automationName': automation_name,
                'xcodeOrgId': xcode_org_id,
                'xcodeSigningId': xcode_signing_id,
                'udid': ud_id,
                'startIWDP': True,
                'noReset': False,
            }
        ExceptionAction().log().info("获取appDriver的参数：" + str(self.desired_caps))
        self.driver = webdriver.Remote('http://' + remote_ip + ':' + remote_port + '/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()
