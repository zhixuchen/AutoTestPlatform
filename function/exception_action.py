#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 11:17
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : exception_action.py
@Project : AutoTestPlatform
"""
import time
from global_variable import *
import logging


class ExceptionAction(object):
    def __init__(self):
        self.name = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        self.directory_name = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        self.image_name = self.name + ".png"
        self.image_path = EXCEPTION_IMAGE_PATH + self.directory_name + '\\'
        self.file_image = self.image_path + self.image_name
        self.log_name = self.name + ".log"
        self.log_path = EXCEPTION_LOG_PATH + self.directory_name + '\\'
        self.file_log = self.log_path + self.log_name

    def web_catch_image(self, browser):
        try:
            if not os.path.exists(self.image_path):
                os.makedirs(self.image_path)
        except BaseException as msg:
            print("新建目录失败：%s" % msg)

        try:
            browser.save_screenshot(
                self.file_image)
        except BaseException as pic_msg:
            print("截图失败：%s" % pic_msg)

    def app_catch_image(self, driver):
        try:
            if not os.path.exists(self.image_path):
                os.makedirs(self.image_path)
        except BaseException as msg:
            print("新建目录失败：%s" % msg)

        try:
            driver.get_screenshot_as_file(
                self.file_image)
        except BaseException as pic_msg:
            print("截图失败：%s" % pic_msg)

    def log(self):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=self.file_log,
                            filemode='w')
