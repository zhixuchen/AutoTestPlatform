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
        self.platform_name = platform_name
        self.element = MobileAction().element(platform_name)
        self.start(account, pwd)

    def start(self, account, pwd):
        ExceptionAction().log().info("======执行" + self.__class__.__name__ + "；参数为：" + locals())
        try:
            if "Android" == self.platform_name:
                self.element.click(B.hwmconf_welcome_login_btn, "登录/注册")
                self.element.click(B.login_choice_title, "密码登录")
                self.element.input(B.hwmconf_login_account_input, account, "登录账户")
                self.element.input(B.hwmconf_login_password_input, pwd, "登录密码")
                self.element.click(B.hwmconf_login_login_btn, "登录")
                if self.element.is_display(B.privacy_dialog_title, "隐私协议"):
                    self.element.click(B.hwmconf_dialog_button_right, "确定")
                if self.element.is_display(B.base_dialog_title, "来电提醒设置"):
                    self.element.click(B.hwmconf_dialog_button_left, "跳过")
            elif "iOS" == self.platform_name:
                self.element.click(I.hwmconf_welcome_login_btn, "登录/注册")
                self.element.click(I.login_choice_title, "密码登录")
                self.element.input(I.hwmconf_login_account_input, account, "登录账户")
                self.element.input(I.hwmconf_login_password_input, pwd, "登录密码")
                self.element.click(I.hwmconf_login_login_btn, "登录")
                if self.element.is_display(I.privacy_dialog_title, "隐私协议"):
                    self.element.click(I.hwmconf_dialog_button_right, "确定")
                if self.element.is_display(I.base_dialog_title, "来电提醒设置"):
                    self.element.click(I.hwmconf_dialog_button_left, "跳过")
            ExceptionAction().log().info("======执行" + self.__class__.__name__ + "结束")
        except Exception as e:
            ExceptionAction().log().error(e)
            ExceptionAction().app_catch_image(self.driver)
            raise Exception(e)


def get_plugin_class():
    return LoginAction


