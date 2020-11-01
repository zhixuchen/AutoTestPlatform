#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 11:17
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : suite.py
@Project : AutoTestPlatform
"""
# from test_case.web import login_case
from test_case.moblie import login_case
from function.report_html import *
from function.send_email import SendEmail
import unittest


class Suite(object):
    def __init__(self):
        self.suite = unittest.TestSuite()

    def mobile_suite(self):
        self.suite.addTest(login_case.LoginCase('login_case'))
        # self.suite.addTest(login_case.LoginCase('login_out'))
        return self.suite


if __name__ == '__main__':
    suite_tests = Suite()
    mobile_suite = suite_tests.mobile_suite()
    report_name = "测试报告"
    description = "登录验证"
    report_html = ReportHtml()
    html_file_path = report_html.build_report(mobile_suite, report_name, description)

    # sent_email = SendEmail()
    # sent_email.sent_email(html_file_path)
