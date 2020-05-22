#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version:
author:c30002875
@time: 2020/04/30
@file: login_case.py
@function:
@modify:
"""
from element_handling.web.find_elements import *
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
