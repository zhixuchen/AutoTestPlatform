#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version:
author:c30002875
@time: 2020/05/06
@file: login_case.py
@function:
@modify:
"""

from auto_driver.pc_w.pc_driver import *
from custom_function.check_assert_equal import *
from custom_function.get_config import *

class LoginCase(unittest.TestCase):
    @staticmethod
    def login_case():
        soft_path = get("pc","soft_path")
        app = PcDriver()
        app.start(soft_path)
        app.connect(class_name="Chrome_WidgetWin_1", title="WeLink")
        win = app.window(title="WeLink")
        win.print_control_identifiers()