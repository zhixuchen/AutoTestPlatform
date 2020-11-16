#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 11:17
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : suite.py
@Project : AutoTestPlatform
"""

from WebforAutoTestPlatform.function.report_html import *
import unittest

import json
class Suite(object):
    def __init__(self):
        self.suite = unittest.TestSuite()

    def add_test_case(self, cases_name):
        for case_name in cases_name:
            case = __import__("WebforAutoTestPlatform.static_file.mobile_cases." + case_name,
                              fromlist=[case_name])
            case_class = case.get_case_class(SUITE_ID,SUITE_PARAMS)
            self.suite.addTest(case_class(case_name))
        return self.suite


def suite_test(cases_name, suite_id,suite_param):
    global SUITE_PARAMS,SUITE_ID
    SUITE_ID=suite_id
    SUITE_PARAMS= json.loads(suite_param)
    mobile_suite = Suite().add_test_case(cases_name)
    report_name = "TestReport"
    description = "登录验证"
    report_html = ReportHtml()
    html_file_path = report_html.build_report(mobile_suite, report_name,suite_id, description)
    return html_file_path


if __name__ == '__main__':
    case_name = ["LoginCase", "LoginOutCase"]
    account = ""
    # suite_test(case_name,**kwargs)
