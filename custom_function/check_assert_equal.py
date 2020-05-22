#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version:
author:c30002875
@time: 2020/04/30
@file: check_assert_equal.py
@function:
@modify:
"""
import unittest
from custom_function.exception_action import *


class CheckAssert(unittest.TestCase):
    def __init__(self):
        self.exception = ExceptionAction()

    def check_equal(self, first, second, msg=None, browser=None):
        try:
            self.assertEqual(first, second, msg)
        except Exception as e:
            if browser is not None:
                self.exception.catch_image(browser)
            self.assertEqual(first, second, msg)
            print(e)
