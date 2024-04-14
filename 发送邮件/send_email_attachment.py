# _*_coding:utf-8 _*_
# @Time　　 :2021/6/22/022   16:30
# @Author　 : Antipa
# @File　　 :send_email_attachment.py
# @Theme    :PyCharm

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

from_addr = '1569873132@qq.com'  # 邮件发送账号
qqCode = 'zioyuypxubqvhcbb'  # 授权码（这个要填自己获取到的）
to_addrs = '2511633760@qq.com'  # 接收邮件账号
smtp_server = 'smtp.qq.com'  # 固定写死
smtp_port = 465  # 固定端口

# 配置服务器
stmp = smtplib.SMTP_SSL(smtp_server, smtp_port)
stmp.login(from_addr, qqCode)

# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = "aaaa 1569873132@qq.com"  # 发件人
message['To'] = Header("bbbb", 'utf-8')  # 收件人
mail_title = '主题：这是带附件的邮件'
message['Subject'] = Header(mail_title, 'utf-8')  # 邮件标题

# 邮件正文内容
message.attach(MIMEText('这是邮件的正文', 'plain', 'utf-8'))

# # 构造附件1（附件为TXT格式的文本）
# att1 = MIMEText(open('text1.txt', 'rb').read(), 'base64', 'utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# att1["Content-Disposition"] = 'attachment; filename="text1.txt"'
# message.attach(att1)
#
# # 构造附件2（附件为JPG格式的图片）
# att2 = MIMEText(open('123.jpg', 'rb').read(), 'base64', 'utf-8')
# att2["Content-Type"] = 'application/octet-stream'
# att2["Content-Disposition"] = 'attachment; filename="123.jpg"'
# message.attach(att2)
#
# # 构造附件3（附件为HTML格式的网页）
# att3 = MIMEText(open('report_test.html', 'rb').read(), 'base64', 'utf-8')
# att3["Content-Type"] = 'application/octet-stream'
# att3["Content-Disposition"] = 'attachment; filename="report_test.html"'
# message.attach(att3)

# 构造超链接4（附件为HTML格式的网页）
typelink_message = '''
<table border=1>
<tr><th>水果</th><th>蔬菜</th></tr>
<tr><td>苹果</td><td>西红柿</td></tr>
<tr><td>香蕉</td><td>黄瓜</td></tr>
</table>
<p><a href="https://www.baidu.com">进入异世界百度搜索</a></p>
<img src="...">
'''
att4 = MIMEText(typelink_message, 'html', 'utf-8')
message.attach(att4)

smtpObj = smtplib.SMTP_SSL(smtp_server, smtp_port)  # 注意：如果遇到发送失败的情况（提示远程主机拒接连接），这里要使用SMTP_SSL方法
smtpObj.login(from_addr, qqCode)
# smtpObj.sendmail(from_addr, to_addrs, message.as_string())
print("邮件发送成功！！！")
smtpObj.quit()
