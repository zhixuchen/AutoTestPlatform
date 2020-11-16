#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 22:29
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : Login.py
@Project : AutoTestPlatform
"""
from WebforAutoTestPlatform.function.exception_action import ExceptionAction
from WebforAutoTestPlatform.test_action.moblie.android import B
from WebforAutoTestPlatform.test_action.moblie.ios import I
from WebforAutoTestPlatform.test_action.moblie.mobile_action import MobileAction
from Test_Platform.models import Config


class Login(object):
    def __init__(self, **kwargs):
        self.platform = str(Config.objects.get(conf_key="platform"))
        self.driver= MobileAction(suite_id).driver()
        self.element = MobileAction(suite_id).element(self.driver)
        self.start(**kwargs)

    def start(self, **kwargs):
        ExceptionAction().log().info("======执行" + self.__class__.__name__ + "；参数为：" + str(locals()))
        try:
            account = kwargs.get("account")
            pwd = kwargs.get("pwd")
            if "Android" == self.platform:
                self.element.click(B.hwmconf_welcome_login_btn, "登录/注册")
                self.element.click(B.login_choice_title, "密码登录")
                self.element.input(B.hwmconf_login_account_input, account, "登录账户")
                self.element.input(B.hwmconf_login_password_input, pwd, "登录密码")
                self.element.click(B.hwmconf_login_login_btn, "登录")
                if self.element.is_display(B.privacy_dialog_title, "隐私协议"):
                    self.element.click(B.hwmconf_dialog_button_right, "确定")
                if self.element.is_display(B.base_dialog_title, "来电提醒设置"):
                    self.element.click(B.hwmconf_dialog_button_left, "跳过")
            elif "iOS" == self.platform:
                self.element.click(I.login_btn, "登录/注册")
                self.element.click(I.password_login, "密码登录")
                if self.element.is_display(I.account_clean, "清空按钮"):
                    self.element.click(I.account_clean, "清空")
                self.element.input(I.account_input, account, "登录账户")
                if self.element.is_display(I.password_clean, "清空按钮"):
                    self.element.click(I.password_clean, "清空")
                self.element.input(I.password_input, pwd, "登录密码")
                self.element.click(I.login_btn, "登录")
                if self.element.is_display(I.privacy_dialog_title, "隐私协议"):
                    self.element.click(I.hwmconf_dialog_button_right, "确定")
                if self.element.is_display(I.base_dialog_title, "来电提醒设置"):
                    self.element.click(I.hwmconf_dialog_button_left, "跳过")
            ExceptionAction().log().info("======执行" + self.__class__.__name__ + "结束")
        except Exception as e:
            ExceptionAction().log().error(e)
            ExceptionAction().app_catch_image(self.driver,suite_id)
            raise Exception(e)


def get_plugin_class(suite):
    global suite_id
    suite_id=suite
    return Login
