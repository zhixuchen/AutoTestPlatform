#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version:
author:c30002875
@time: 2020/04/30
@file: __init__.py.py
@function:
@modify:
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
