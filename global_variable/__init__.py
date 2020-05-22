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
import os

global GLOBAL_VARIABLE_PATH
global STATIC_FILE_PATH
global CHROME_DRIVER_PATH
global EXCEPTION_IMAGE_PATH
global REPORT_HTML_PATH
global CONFIG_PATH

GLOBAL_VARIABLE_PATH = os.path.abspath(os.path.dirname(__file__))
STATIC_FILE_PATH = os.path.join(os.path.dirname(GLOBAL_VARIABLE_PATH), 'static_file')
EXCEPTION_IMAGE_PATH = os.path.join(os.path.abspath(STATIC_FILE_PATH), 'report\\exception_image\\')
REPORT_HTML_PATH = os.path.join(os.path.abspath(STATIC_FILE_PATH), 'report\\html\\')
CONFIG_PATH = os.path.join(os.path.abspath(STATIC_FILE_PATH), 'config\\config.ini')
CHROME_DRIVER_PATH = os.path.join(os.path.abspath(STATIC_FILE_PATH), 'driver\\chromedriver.exe')
