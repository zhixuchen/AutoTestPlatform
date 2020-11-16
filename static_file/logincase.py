#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 11:17
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : mobile_action.py
@Project : AutoTestPlatform
"""
import unittest
from WebforAutoTestPlatform.static_file.mobile_plugins import MobilePlugin


class LoginCase(unittest.TestCase):

    @staticmethod
    def LoginCase():
        account = SUITE_PARAMS.get("account")
        pwd = SUITE_PARAMS.get("pwd")
        MobilePlugin(SUITE_ID).mobile_plugins("Login", account=account, pwd=pwd)


def get_case_class(suite_id,suite_params):
    global SUITE_PARAMS
    SUITE_PARAMS = suite_params
    global SUITE_ID
    SUITE_ID=suite_id
    return LoginCase
