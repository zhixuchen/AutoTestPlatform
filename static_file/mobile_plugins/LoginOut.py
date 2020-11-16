#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/2
@Author : c30002875
@Email : 1195733026@qq.com
@File : LoginOut
@Project : test
"""
from WebforAutoTestPlatform.function.exception_action import ExceptionAction
from WebforAutoTestPlatform.test_action.moblie.android import B
from WebforAutoTestPlatform.test_action.moblie.ios import I
from WebforAutoTestPlatform.test_action.moblie.mobile_action import MobileAction
from WebforAutoTestPlatform.element.elements import Element
from Test_Platform.models import Config


class LoginOut(object):
    def __init__(self, **kwargs):
        self.platform = str(Config.objects.get(conf_key="platform"))
        self.driver = MobileAction(suite_id).driver()
        self.element = MobileAction(suite_id).element(self.driver)
        self.start(**kwargs)

    def start(self, **kwargs):
        ExceptionAction().log().info("======执行" + self.__class__.__name__ + "；参数为：" + str(locals()))
        try:

            if "Android" in self.platform:
                """
               代码编写区域
               
               """
                self.element.click(B.hwmconf_mine_mine_tab, "我的")
                self.element.click(B.hwmconf_mine_settings, "设置")
                if self.element.is_display(B.hwmconf_minesetting_call_setting, "通话设置"):
                    self.element.ele_swipe("up")
                self.element.click(B.hwmconf_minesetting_log_out, "退出登录")
                self.element.click(B.hwmconf_dialog_button_right, "退出登录")

            elif "iOS" in self.platform:
                """
               代码编写区域
               """
                self.element.click(I.mine_tab, "我的")
                self.element.click(I.mine_settings, "设置")
                if self.element.is_display(I.call_setting, "通话设置"):
                    self.element.ele_swipe("up")
                self.element.click(I.log_out, "退出登录")

            ExceptionAction().log().info("======执行" + self.__class__.__name__ + "结束")
        except Exception as e:
            ExceptionAction().log().error(e)
            ExceptionAction().app_catch_image(self.driver, suite_id)
            raise Exception(e)


def get_plugin_class(suite):
    global suite_id
    suite_id = suite
    return LoginOut
