#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 11:17
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : request.py
@Project : AutoTestPlatform
"""
import requests
import json

class PyRequest:
    @staticmethod
    def py_post(url, payload, json_data, headers,querystring):
        response = requests.post(url, data=payload, json=json_data, headers=headers, params=querystring)
        json_result=json.loads(response.text)
        return json_result

    @staticmethod
    def py_get(url, querystring, headers):
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.text
