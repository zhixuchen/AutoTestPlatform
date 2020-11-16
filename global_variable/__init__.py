#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 11:17
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : __init__.py
@Project : AutoTestPlatform
"""
import os

global GLOBAL_VARIABLE_PATH
global STATIC_FILE_PATH
global CHROME_DRIVER_PATH
global EXCEPTION_IMAGE_PATH
global REPORT_HTML_PATH
global CONFIG_PATH
global EXCEPTION_LOG_PATH
global MOBILE_ACTION_PLUGIN_PATH
global DRIVER
global SUITE_PARAMS
GLOBAL_VARIABLE_PATH = os.path.realpath(os.path.dirname(__file__))
STATIC_FILE_PATH = os.path.join(os.path.dirname(GLOBAL_VARIABLE_PATH), 'static_file')
EXCEPTION_IMAGE_PATH = os.path.join(os.path.realpath(GLOBAL_VARIABLE_PATH), '..\\..\\templates\\report\\image\\')
EXCEPTION_LOG_PATH = os.path.join(os.path.realpath(GLOBAL_VARIABLE_PATH), '..\\..\\templates\\report\\log\\')
REPORT_HTML_PATH = os.path.join(os.path.realpath(GLOBAL_VARIABLE_PATH), '..\\..\\templates\\report\\html\\')
CONFIG_PATH = os.path.join(os.path.realpath(GLOBAL_VARIABLE_PATH), '..\\..\\templates\\config\\config.ini')
CHROME_DRIVER_PATH = os.path.join(os.path.realpath(STATIC_FILE_PATH), 'driver\\chromedriver.exe')
MOBILE_ACTION_PLUGIN_PATH = os.path.join(os.path.realpath(STATIC_FILE_PATH), 'mobile_plugins')
MOBILE_CASE_PLUGIN_PATH = os.path.join(os.path.realpath(STATIC_FILE_PATH), 'mobile_cases')
DRIVER = None
SUITE_PARAMS=None
if __name__ == '__main__':
    print(MOBILE_CASE_PLUGIN_PATH)
