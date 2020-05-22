#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version:
author:c30002875
@time: 2020/04/30
@file: send_email.py
@function:
@modify:
"""
import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from custom_function.get_config import *
import time


class SendEmail(object):
    def __init__(self):
        self.send_email = get("email", "send_email")
        self.send_pwd = get("email", "send_pwd")
        self.to_email = get("email", "to_email")
        self.to_name = get("email", "to_name")
        self.from_name = get("email", "from_name")
        self.my_sender = self.send_email  # 发件人邮箱账号
        self.my_pass = self.send_pwd  # 发件人邮箱密码
        self.my_user = self.to_email  # 收件人邮箱账号，我这边发送给自己
        self.my_user = self.my_user.split(',')
        self.directory_name = time.strftime("%Y-%m-%d", time.localtime(time.time()))

    def sent_email(self, html_file_path):
        ret = True
        try:
            message = MIMEMultipart()
            message['From'] = Header(self.from_name, 'utf-8')
            message['To'] = Header(self.to_name, 'utf-8')
            message['Subject'] = Header('自动化测试报告', 'utf-8')
            filename = html_file_path.split(self.directory_name + "\\")[1]
            html = SendEmail.add_attach(html_file_path, filename=filename)  # 自动化测试报告附件
            message.attach(html)
            server = smtplib.SMTP_SSL("smtp.mxhichina.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(self.my_sender, self.my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.my_sender, self.my_user, message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
            print("邮件发送成功")
        except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            print(e)
            ret = False
            print("邮件发送失败")
        return ret

    @staticmethod
    def add_attach(html_file_path, filename):
        with open(html_file_path, 'rb') as fp:
            attach = MIMEBase('application', 'octet-stream')
            attach.set_payload(fp.read())
            attach.add_header('Content-Disposition', 'attachment', filename=filename)
            encoders.encode_base64(attach)
            fp.close()
            return attach
