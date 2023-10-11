# _*_coding:utf-8 _*_
# @Time     :2020/10/23 0023   下午 11:28
# @Author   : Antipa
# @File     :fs.py
# @Theme    :PyCharm
import requests
from lxml import etree
keyword='同城公约'
# 查找关键词
url='https://s.9fs.com/?f=1&k={}&cid=sjrj'.format(keyword)
res=requests.get(url)
html=etree.HTML(res.text)
app_url_list=html.xpath(r"//dl[@id='result']/dt/a/@href")
# APP链接
app_url=app_url_list[0]
print(app_url)
# APP详情
app_res=requests.get(app_url)
app_res.encoding='gb2312'
app_html=etree.HTML(app_res.text)
# APP下载地址
download_url=app_html.xpath(r"//ul[@class='m-down-ul info']/li/a/@href")[0]
print('download_url:',download_url)

base_info_list=app_html.xpath(r"//div[@class='f-fl m-sjconter']/div/ul/li")
type=base_info_list[0]
size=base_info_list[1]
language=base_info_list[2]
version=base_info_list[3]
time=base_info_list[4]
star=base_info_list[5]
developer=base_info_list[6]
property=base_info_list[7]
plat=base_info_list[8]

jieshao=app_html.xpath(r"//div[@class='m-center']/child::*")
intro=''
for j in jieshao:
    tmp=j.xpath('string(.)').strip()
    intro=intro+str(tmp)
