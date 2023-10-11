# _*_coding:utf-8 _*_
# @Time　　 :2021/5/7/007   10:08
# @Author　 : Antipa
# @File　　 :main_single_threading_7881.py
# @Theme    :PyCharm
import numpy as np
import requests,time,json,re

def get_comany_id():
    return id

def get_company_info_by_id(id):
    pass

company_name='海口成发'
url='https://www.baidu.com/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

res=requests.get(url,headers=headers,proxies={'http':'http://111111111:57114'})
print(res.status_code)
