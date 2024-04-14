# _*_coding:utf-8 _*_
# @Time　　 :2021/6/22/022   17:12
# @Author　 : Antipa
# @File　　 :WarningEmail.py
# @Theme    :PyCharm


import smtplib
from email.mime.text import MIMEText
from email.header import Header

import base64

def From_RFC_encode(no_ascii_str):

    # 定义中文昵称和邮箱地址
    no_ascii_str = "你好呀我是"
    email_address = "example@qq.com"

    # 对中文昵称进行base64编码
    encoded = base64.b64encode(no_ascii_str.encode('utf-8')).decode('utf-8')

    return '=?UTF-8?B?{}?='.format(encoded)


from_addr = '1569873132@qq.com'  # 邮件发送账号
qqCode = 'hyhnhdbfwveibacd'  # 授权码（这个要填自己获取到的）
to_addrs = 'getfunc@163.com'  # 接收邮件账号
smtp_server = 'smtp.qq.com'  # 固定写死
smtp_port = 465  # 固定端口

# 配置服务器
stmp = smtplib.SMTP_SSL(smtp_server, smtp_port)
stmp.login(from_addr, qqCode)

# 组装发送内容
message = MIMEText('我是发送的内容', 'plain', 'utf-8')  # 发送的内容
message['From'] = "{0} <{1}>".format(From_RFC_encode('发件人'), from_addr)  # 发件人 构建符合RFC规范的"From"字段
message['To'] = "{0} <{1}>".format(From_RFC_encode('收件人'), to_addrs)  # 发件人 构建符合RFC规范的"From"字段
subject = '【预警提醒】'
message['Subject'] = Header(subject, 'utf-8')  # 邮件标题

try:
    stmp.sendmail(from_addr, to_addrs, message.as_string())
except Exception as e:
    print('邮件发送失败--' + str(e))
print('爬虫失败')
