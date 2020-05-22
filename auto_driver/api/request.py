#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version:
author:c30002875
@time: 2020/04/30
@file: request.py
@function:
@modify:
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
