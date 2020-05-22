#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version:
author:c30002875
@time: 2020/04/30
@file: login_suite.py
@function:
@modify:
"""
from test_case.pc_w import login_case
import unittest
def suite():
    suite = unittest.TestSuite()
    suite.addTest(login_case.LoginCase('login_case'))
    # suite.addTest(Login_Case('test_loginfail'))
    # suite.addTest(Login_Case('test_loginusernamefail'))
    # suite.addTest(Login_Case('test_nulluser'))
    # suite.addTest(Login_Case('test_nullpwd'))
    return suite


from custom_function.report_html import *
if __name__ == '__main__':
    suite_tests=suite()
    report_name="测试报告"
    description="登录验证"
    report_html=ReportHtml()
    html_file_path=report_html.build_report(suite_tests,report_name,description)

    # sent_email = SendEmail()
    # sent_email.sent_email(html_file_path)
