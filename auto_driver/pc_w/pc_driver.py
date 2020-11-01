#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 11:17
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : pc_driver.py
@Project : AutoTestPlatform
"""
from pywinauto.application import Application


class PcDriver(object):
    def __init__(self):
        self.app = Application(backend="uia")

    def start(self, path):
        self.app.start(path)

    def connect(self,title):
        self.app.connect(title=title)

    def close(self, window_name):
        """
        关闭应用程序
        """
        self.app[window_name].Close()
    def max_window(self, window_name):
        """
        最大化窗口
        """
        self.app[window_name].Maximize()

    def menu_click(self, window_name, menulist):
        """
        菜单点击
        """
        self.app[window_name].MenuSelect(menulist)


    def input(self, window_name, controller, content):
        """
        输入内容
        """
        self.app[window_name][controller].TypeKeys(content)


    def click(self, window_name, controller):
        """
        鼠标左键点击
        example:
        下面两个功能相同,下面支持正则表达式
        app[u'关于“记事本”'][u'确定'].Click()
        app.window_(title_re = u'关于“记事本”').window_(title_re = u'确定').Click()
        """
        self.app[window_name][controller].Click()


    def double_click(self, window_name, controller, x = 0,y = 0):
        """
        鼠标左键点击(双击)
        """
        self.app[window_name][controller].DoubleClick(button = "left", pressed = "",  coords = (x, y))