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


class AppIumDriver(object):
    def __init__(self, platform_name, remote_ip, remote_port, device_name, platform_version, app_package, app_activity):
        if "Android" == platform_name:
            self.desired_caps = {
                'platformName': platform_name,  # 'Android'# 设备平台
                'deviceName': device_name,  # 'mi' #设备名称
                'platformVersion': platform_version,  # x系统版本
                'appPackage': app_package,  # 包名
                'appActivity': app_activity,  # 第一个activity启动页的名称
                'unicodeKeyboard': True,  # 此两行是为了解决字符输入不正确的问题
                'resetKeyboard': True  # 运行完成后重置软键盘的状态
            }
        elif "iOS" == platform_name:
            self.desired_caps = {
                'platformName': platform_name,  # 'Android'# 设备平台
                'deviceName': device_name,  # 'mi' #设备名称
                'platformVersion': platform_version,  # x系统版本
                'appPackage': app_package,  # 包名
                'appActivity': app_activity,  # 第一个activity启动页的名称
                'unicodeKeyboard': True,  # 此两行是为了解决字符输入不正确的问题
                'resetKeyboard': True  # 运行完成后重置软键盘的状态
            }
        self.driver = webdriver.Remote('http://' + remote_ip + ':' + remote_port + '/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()
