# _*_coding:utf-8 _*_
# @Time　　 :2021/1/19/019   9:05
# @Author　 : Antipa
# @File　　 :get_img_soure_url.py
# @Theme    :PyCharm
import os,requests,time
from lxml import etree
from fake_useragent import UserAgent
import numpy as np
ua=UserAgent()
with open(os.path.join(os.getcwd(),'back_url.txt'),encoding='utf-8') as f:
    back_url_list=[line.strip() for line in f.readlines()]

# def get_source_url(img_url):
#     headers={
#         'User-Agent':np.random.choice(ua)
#     }
#     res=requests.get(img_url,headers=headers)
#     html=etree.HTML(res.text)
#     img_name=html.xpath("//h1[@class='viewer-title' and @data-text='image-title']/text()")[0]
#     img_source_url=html.xpath("//input[@id='embed-code-5']/@value")[0]
#     return  img_url,img_name,img_source_url


if __name__ == '__main__':
    with open(os.path.join(os.getcwd(), 'back_url.txt'), encoding='utf-8') as f:
        back_url_list = [line.strip() for line in f.readlines()]
    for back_url in back_url_list:
        time.sleep(1)
        tmp_ua=np.random.choice(ua)
        print(tmp_ua)
        headers = {
            'User-Agent': tmp_ua
        }
        res = requests.get(back_url, headers=headers)
        if res.status_code==200:
            html = etree.HTML(res.text)
            img_name = html.xpath("//h1[@class='viewer-title' and @data-text='image-title']/text()")[0]
            img_source_url = html.xpath("//input[@id='embed-code-5']/@value")[0]
            print(back_url, img_name, img_source_url)
        else:
            print(back_url,res.status_code)


