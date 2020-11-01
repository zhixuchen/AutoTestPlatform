#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 11:17
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : mobile_action.py
@Project : AutoTestPlatform
"""
from auto_driver.auto_driver import Driver
from element.elements import Element
from test_action.moblie.android import B
from test_action.moblie.ios import I
from function.exception_action import ExceptionAction
from function.check import CheckAssert
import sys


class MobileAction(object):
    def __init__(self, platform_name):
        """
        初始化mobile_actin
        :param platform_name: 平台类型：iOS,Android
        """
        self.platform_name = platform_name
        self.driver = Driver(self.platform_name).mobile_driver
        self.element = Element(self.driver)
        self.check = CheckAssert()

    def login(self, account, pwd):
        """
        登录action
        :param account: 账户
        :param pwd: 密码
        :return:
        """
        ExceptionAction().log().info("======执行" + sys._getframe().f_code.co_name + "；参数为：" + locals())
        try:
            if "Android" == self.platform_name:
                self.element.click(B.Bid_test, "登录")
                self.element.input(B.Bid_test, account, "账号")
                self.element.input(B.Bid_test, pwd, "密码")
                self.element.click(B.Bid_test, "登录")
            elif "iOS" == self.platform_name:
                self.element.click(I.Bid_test, "登录")
                self.element.input(I.Bid_test, account, "账号")
                self.element.input(I.Bid_test, pwd, "密码")
                self.element.click(I.Bid_test, "登录")
            ExceptionAction().log().info("======执行" + sys._getframe().f_code.co_name + "结束")
        except Exception as e:
            ExceptionAction().log().error(e)
            ExceptionAction().app_catch_image(self.driver)
            raise Exception(e)

    def login_out(self):
        ExceptionAction().log().info("======执行" + sys._getframe().f_code.co_name + "；参数为：" + locals())
        ExceptionAction().log().info("======执行" + sys._getframe().f_code.co_name + "结束")
        pass

    def check_login(self):
        self.check.app_check_equal("1", "1", "相等", self.driver)

    def teardown(self):
        """
        关闭
        :return:
        """
        self.driver.teardown()
