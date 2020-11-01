#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 11:17
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : report_html.py
@Project : AutoTestPlatform
"""

from BeautifulReport import BeautifulReport  # 导入BeautifulReport

from global_variable import *
import time


class ReportHtml(object):
    def __init__(self):
        self.directory_name = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        self.html_name = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

    def build_report(self, suite_tests, report_name, description):
        report_name = report_name + self.html_name
        try:
            html_file_path = REPORT_HTML_PATH + self.directory_name + '\\'
            if not os.path.exists(html_file_path):
                os.makedirs(html_file_path)
        except BaseException as msg:
            print("新建目录失败：%s" % msg)
        try:
            BeautifulReport(suite_tests).report(filename=report_name, description=description,
                                                report_dir=html_file_path)
            return html_file_path + report_name + '.html'

        except BaseException as pic_msg:
            print("生成报告失败：%s" % pic_msg)


if __name__ == '__main__':
    ReportHtml.sent_email("C:\\Users\\Administrator\\Desktop\\new_file.html")
