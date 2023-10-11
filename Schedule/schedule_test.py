# _*_coding:utf-8 _*_

# @Time      : 2022/5/17  16:15
# @Author    : An
# @File      : schedule_test.py
# @Software  : PyCharm

import schedule
from WarningEmail import warning_email

import schedule
import time, platform, sys,datetime

def job_test():
    now = (datetime.datetime.now() - datetime.timedelta(days=0)).strftime('%Y-%m-%d %H:%M:%S')
    email_content = 'test schedule {}'.format(now)
    warning_email(email_content)
    print('执行完成时间：{}'.format(now))

schedule.every(1).minutes.do(job_test)
# schedule.clear()
while True:
    schedule.run_pending()
    time.sleep(1)
