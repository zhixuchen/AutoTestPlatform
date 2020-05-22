#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version:
author:c30002875
@time: 2020/04/30
@file: find_elements.py
@function:
@modify:
"""

# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2018/10/16 10:50
# software: PyCharm

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

'''根据element查找elements'''


def find_elements_by_element(element, by, string):
    web_elements = element.find_elements(by, string)
    return web_elements


'''根据element查找element'''


def find_element_by_element(element, by, string):
    web_element = element.find_element(by, string)
    return web_element


'''根据element设置KEY'''


def element_send_key(element, key):
    element.clear()
    element.send_keys(key)


'''根据element触发点击'''


def element_click(element):
    time.sleep(0.5)
    while (not element.is_enabled()):
        print("不可点击")
        if (element.is_enabled()):
            element.click()
            print("发现元素，并已经点击")
            break
    element.click()


'''根据element用js进行点击'''


def element_click_script(browser, element):
    browser.execute_script("arguments[0].click()", element)


'''根据文本text查找element'''


def find_element_by_text(browser, by, string, text):
    elements = find_elements(browser, by, string)
    for element in elements:
        if text == element.text:
            return element


'''
根据文本text查找element
通过element查找
'''


def find_element_by_text_element(element, by, string, text):
    elements = find_elements_by_element(element, by, string)
    for element in elements:
        if text == element.text:
            return element


'''重写查找element,隐性等待10秒'''


def find_element(browser, by, string):
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((by, string)))
    element = browser.find_element(by, string)
    return element


'''重写查找elements,隐性等待10秒'''


def find_elements(browser, by, string):
    time.sleep(0.5)
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((by, string)))
    element = browser.find_elements(by, string)
    return element


'''知道当前element，查找同级别的input'''


def find_next_input_by_element(element):
    select_element = find_next_element(element)
    select_input = find_element_by_element(select_element, By.TAG_NAME, "input")
    return select_input


'''知道当前element，查找同级别的inputs'''


def find_next_inputs_by_element(element):
    select_element = find_next_element(element)
    select_inputs = find_elements_by_element(select_element, By.TAG_NAME, "input")
    return select_inputs


'''知道当前element查找下一个同级的element'''


def find_next_element(element):
    next_element = find_element_by_element(element, By.XPATH, "./following::*")
    return next_element
