#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 11:17
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : mobile_action.py
@Project : AutoTestPlatform
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