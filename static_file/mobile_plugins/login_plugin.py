#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 22:29
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : login_plugin.py
@Project : AutoTestPlatform
"""
from function.exception_action import ExceptionAction
from test_action.moblie.android import B
from test_action.moblie.ios import I
from test_action.moblie.mobile_action import MobileAction


class LoginAction(object):
    def __init__(self, platform_name, account, pwd):
        self.element = MobileAction().element(platform_name)
        self.start(account, pwd)

    def start(self, account, pwd):
        ExceptionAction().log().info("======执行" + self.__class__.__name__ + "；参数为：" + locals())
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
            ExceptionAction().log().info("======执行" + self.__class__.__name__ + "结束")
        except Exception as e:
            ExceptionAction().log().error(e)
            ExceptionAction().app_catch_image(self.driver)
            raise Exception(e)


def get_plugin_class():
    return LoginAction


# def get_plugin_class_name():
#     return self.__class__.__name__