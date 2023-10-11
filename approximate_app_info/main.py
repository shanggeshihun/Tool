# _*_coding:utf-8 _*_
# @Time　　 : 2020/1/13   1:38
# @Author　 : zimo
# @File　   :2鼠标事件.py
# @Software :PyCharm
# @Theme    :
import requests,json,re
import os,time
from lxml import etree
import numpy as np
from fake_useragent import UserAgent
# from valid_proxy import get_valid_proxy_lst
# proxy_list=get_valid_proxy_lst()
ua_list=UserAgent()


def get_app_url(keyword):
    """
    :param keyword:
    :return:关键词对应的APP信息
    """
    main_url='https://s.pc6.com/?k={}'.format(keyword)
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': np.random.choice(ua_list)
    }
    res=requests.get(main_url, headers=headers)
    res.encoding='utf-8'
    html=etree.HTML(res.text)
    sub_url=html.xpath(r'//dl[@id="result"]/dt/a/@href')[0]

    sub_res = requests.get(sub_url, headers=headers)
    sub_res.encoding = 'gb2312'
    sub_html = etree.HTML(sub_res.text)
    app_name=sub_html.xpath(r'//dd[@id="dinfo"]/h1/text()')[0]
    x=sub_html.xpath(r'//div[@class="intro-txt"]/child::*')
    info='\n'.join([xx.xpath('string(.)').strip() for xx in x])
    return {keyword:{'app_name':app_name,'info':info}}

if __name__ == '__main__':
    app_info=get_app_url('养鱼')
    print(app_info)