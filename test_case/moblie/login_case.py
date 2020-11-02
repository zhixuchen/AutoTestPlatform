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
from test_case.moblie import MobileCase


class LoginCase(unittest.TestCase):
    @staticmethod
    def login_case():
        account = "chenzhixurtca"
        pwd = "1qaz@WSX"
        MobileCase().mobile_action.action_plugins["Login"]("Android", account=account, pwd=pwd)

    @staticmethod
    def login_out():
        MobileCase().mobile_action.action_plugins["LoginOut"]("Android")
