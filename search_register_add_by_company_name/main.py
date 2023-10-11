# _*_coding:utf-8 _*_
# @Time　　 :2021/4/13/013   12:42
# @Author　 : Antipa
# @File　　 :main_single_threading_7881.py
# @Theme    :PyCharm

import requests
from lxml import etree

company_name='深圳市爱聊科技有限公司'
url='https://aiqicha.baidu.com/person/relevantPersonalAjax?q={}&page=1&size=10'.format(company_name)
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}
res=requests.get(url,headers=headers)
print(res.text)
# res_html=etree.HTML(res.text)
# company_info_list=res_html.xpath(r"//div[@class='company-list']/div/div/div[@class='info']/div[@class='items']")
# for company in company_info_list:
#     title=company.xpath(r"./h3/a/@title")[0]
#     href=company.xpath(r"./h3/a/@href")[0]
#     status=company.xpath(r"./h3/span/text()")[0]
#     print(company)
