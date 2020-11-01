#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 11:17
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : mobile_action.py
@Project : AutoTestPlatform
"""
from element.web.find_elements import *
from custom_function.get_config import *

from test_case.web import *


class LoginCase(unittest.TestCase):
    @staticmethod
    def login_case():
        url = get("url", "web_url")
        driver = WebCase()
        driver.get_url(url)
        login_tab = find_element_by_text(driver.browser, By.TAG_NAME, "span", "账号登录")
        element_click(login_tab)
