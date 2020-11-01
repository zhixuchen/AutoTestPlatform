#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 11:17
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : __init__.py
@Project : AutoTestPlatform
"""

import unittest
from auto_driver.web.web_chrome_driver import *
from custom_function.exception_action import *


class WebCase(unittest.TestCase):
    def __init__(self):
        self.web_driver = WebChromeDriver()
        self.browser = self.web_driver.chrome_browser

    def get_url(self, url):
        try:
            self.browser.get(url)
        except Exception as e:
            print(e)
            except_action = ExceptionAction()
            except_action.catch_image(self.browser)

    def tearDown(self):
        print("登录测试结束")
        self.web_driver.teardown()
