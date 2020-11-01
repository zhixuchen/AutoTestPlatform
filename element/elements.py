#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 11:59
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : elements.py
@Project : AutoTestPlatform
"""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from function.exception_action import ExceptionAction


def ele_click(ele, des=None):
    ele.click()
    ExceptionAction().log().info("点击{0}".format(str(des)))


def ele_get_ele(ele, b, des=None):
    ele = ele.find_element(b)
    ExceptionAction().log().info("获取{0}".format(str(des)))
    return ele


def ele_get_eles(ele, b, des=None):
    eles = ele.find_elements(b)
    ExceptionAction().log().info("获取{0}".format(str(des)))
    return eles


class Element(object):

    def __init__(self, driver):
        self.driver = driver

    def click(self, b, des=None):
        ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(b))
        ExceptionAction().log().info("根据{0}对{1}点击，".format(str(b[0]) + str(b[1]), str(des)))
        ele.click()

    def input(self, b, value, des=None):
        ele = Element(self).get_ele(b, des)
        ExceptionAction().log().info("对{0}输入{1}，".format(str(des), str(value)))
        ele.clear()
        ele.send_keys(value)

    def wait_ele(self, b, des=None):
        try:
            Element(self).get_ele(b, des)
            ExceptionAction().log().info("等待{0}展示".format(str(des)))
            return True
        except Exception as e:
            ExceptionAction().log().error(e)
            return False

    def get_text(self, b, des=None):
        text = Element(self).get_ele(b, des).text
        ExceptionAction().log().info("获取{0}的Text".format(str(des)))
        return text

    def get_ele(self, b, des=None):
        ele = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(b))
        ExceptionAction().log().info("根据{0}获取{1}".format(str(b[0]) + str(b[1]), str(des)))
        return ele

    def get_eles(self, b, des=None):
        eles = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(b))
        ExceptionAction().log().info("根据{0}获取{1}".format(str(b[0]) + str(b[1]), str(des)))
        return eles

    def click_script(self, ele, des=None):
        self.driver.execute_script("arguments[0].click()", ele)
        ExceptionAction().log().info("点击{0}".format(str(des)))

    def get_attr(self,b,type,des=None):
        Element(self).get_ele(b,des).get
