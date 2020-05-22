#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version:
author:c30002875
@time: 2020/04/30
@file: login_case.py
@function:
@modify:
"""

from auto_driver.api.request import *
from custom_function.check_assert_equal import *


class LoginCase(unittest.TestCase):
    def login_case(self):
        self.check_assert = CheckAssert()
        url = "https://login.welink.digitalworkplace.cn/sso/v1/pclogintenant"
        payload = {
            "userName": 15158114445,
            "password": "Abc123456!",
            "redirect_url": "redirect_uri=https%3A%2F%2Fwelink.digitalworkplace.cn%2Fadmintenant%2F%23%2FHomepage",
            "vertifyInput": "",
            "errorCode": ""
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest"
        }
        result = PyRequest.py_post(url, payload, None, headers, None)
        print(result["result"])
        self.check_assert.check_equal(1,result["result"])


