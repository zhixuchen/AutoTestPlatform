#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 11:17
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : check.py
@Project : AutoTestPlatform
"""
import unittest
from function.exception_action import ExceptionAction


class CheckAssert(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.exception = ExceptionAction()

    def web_check_equal(self, first, second, msg=None, browser=None):
        try:
            self.assertEqual(first, second, msg)
        except Exception as e:
            if browser is not None:
                self.exception.web_catch_image(browser)
            self.exception.log().error(e)
            raise Exception(e)

    def app_check_equal(self, first, second, msg=None, driver=None):
        try:
            self.assertEqual(first, second, msg)
        except Exception as e:
            if driver is not None:
                self.exception.app_catch_image(driver)
            self.exception.log().error(e)
            raise Exception(e)
