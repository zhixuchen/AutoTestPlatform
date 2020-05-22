#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version:
author:c30002875
@time: 2020/04/30
@file: web_chrome_driver.py
@function:
@modify:
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
