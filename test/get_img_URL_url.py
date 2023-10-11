# _*_coding:utf-8 _*_
# @Time　　 :2021/2/9   18:23
# @Author　 :
# @File　　 :get_img_URL_url.py
# @Theme    :PyCharm

from lxml import etree
import requests,os,time

def get_URL(program_name):
    url="https://app.mi.com/search?keywords={}".format(program_name)
    res=requests.get(url)
    html=etree.HTML(res.text)
    result=html.xpath(r"//html/body/div[@class='main']/div[@class='container cf']/div[@class='main-con']/div[@class='applist-wrap'][1]/div[2]/strong/text()")[0]
    return img_name,img_url,img_URL_url

if __name__ == '__main__':
    with open(os.path.join(os.getcwd(),'img_url.txt'),'r',encoding='utf-8') as f:
        for line in f.readlines():
            result=get_URL(line.strip())
            time.sleep(1)
            print(result)
