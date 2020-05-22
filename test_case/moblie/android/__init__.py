#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version:
author:c30002875
@time: 2020/05/07
@file: __init__.py.py
@function:
@modify:
"""
from auto_driver.mobile.appium_driver import *


class AndroidCase:
    def __init__(self):
        self.app_driver = AppIumDriver(platform_name=1, device_name=2, platform_version=6, app_package=5,
                                       app_activity=8)

    def teardown(self):
        self.app_driver.teardown()
