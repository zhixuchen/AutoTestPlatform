#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 11:17
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : suite.py
@Project : AutoTestPlatform
"""
from global_variable import *
from selenium import webdriver


class WebChromeDriver:
    def __init__(self):
        self.chrome_browser = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.chrome_browser.maximize_window()
        self.chrome_browser.implicitly_wait(30)

    def teardown(self):
        self.chrome_browser.quit()
