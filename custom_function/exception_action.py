#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version:
author:c30002875
@time: 2020/04/30
@file: exception_action.py
@function:
@modify:
"""
import time
from global_variable import *


class ExceptionAction(object):
    def __init__(self):
        self.image_name = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        self.directory_name = time.strftime("%Y-%m-%d", time.localtime(time.time()))

    def catch_image(self, browser):
        try:
            image_path = EXCEPTION_IMAGE_PATH + self.directory_name + '\\'
            if not os.path.exists(image_path):
                os.makedirs(image_path)
        except BaseException as msg:
            print("新建目录失败：%s" % msg)

        try:
            browser.save_screenshot(
                image_path + self.image_name + '.png')
        except BaseException as pic_msg:
            print("截图失败：%s" % pic_msg)
