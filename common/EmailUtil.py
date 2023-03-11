# -- coding: utf-8 --
import importlib
import sys
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
importlib.reload(sys)
import os
import smtplib


class Email:

    def send_email(self, file_path):
        ISOTIMEFORMAT = '%Y%m%d'
        caodate = str(time.strftime(ISOTIMEFORMAT, time.localtime()))
        # param file_path  report.html 路径
        smtpserver = 'smtp.163.com'
        # 设置登录邮箱的账号和授权密码
        user = 'zjsession@163.com'
        password = 'IWZMKLNJKIPOBLTK'  # 此处是授权码，不是邮箱密码
        sender = 'zjsession@163.com'
        # 可添加多个收件人的邮箱
        receives = ['1150531814@qq.com', 'zjsession@163.com']
        # 构造邮件对象
        msg = MIMEMultipart('mixed')
        # 定义邮件的标题
        subject = '自动化测试报告'
        # HTML邮件正文，定义成字典
        msg['Subject'] = Header(subject, "utf-8")
        msg['From'] = sender
        msg['To'] = ','.join(receives)  # 这里注意，直接用receivers是不行的会报错
        # 构造文字内容
        text_plain = MIMEText(caodate+"附件是最新自动化测试报告，请查看！", 'html', 'utf-8')
        msg.attach(text_plain)

        # 构造附件
        f = open(file_path, 'rb')
        mail_body = f.read()
        f.close()
        text_attr = MIMEText(mail_body, 'base64', 'utf-8')
        text_attr["Content-type"] = 'application/octet-stream'
        text_attr['Content-Disposition'] = 'attachment; filename = "index.html"'
        msg.attach(text_attr)
        with open(os.path.join(
                r"D:\tool\python\pycharm\pythonProject\autoTest\report\html", "index.html"),
                'rb') as f:
            mail_body = f.read()  # 读取测试报告的内容
        # 将测试报告的内容放在邮件的正文当中
        html = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        # 将html附加在msg里
        msg.attach(html)
        print(html)

        # 邮箱设置时勾选了SSL加密连接，进行防垃圾邮件，SSL协议端口号要使用465
        smtp = smtplib.SMTP_SSL(smtpserver, 465)
        # 向服务器标识用户身份
        smtp.helo(smtpserver)
        # 向服务器返回确认结果
        smtp.ehlo(smtpserver)
        # 登录邮箱的账号和授权密码
        smtp.login(user, password)

        print("开始发送邮件...")
        # 开始进行邮件的发送，msg表示已定义的字典
        smtp.sendmail(sender, receives, msg.as_string())
        smtp.quit()
        print("已发送邮件")


if __name__ == '__main__':
    e = Email()
    report = "../autoTest/report/html/index.html"
    e.send_email(report)
