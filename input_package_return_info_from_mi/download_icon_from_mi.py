# _*_coding:utf-8 _*_
# @Time　　 :2021/2/9   13:25
# @Author　 :
# @File　　 :download_icon_from_mi.py
# @Theme    :参考小米应用市场，通过包名搜索应用信息并下载应用图标

import requests,os,time,csv
from lxml import etree


def get_package_info(package_name):
    """
    :param package_name: 包名
    :return:返回包名搜索的返回的应用信息
    """
    url="https://app.mi.com/details?id={}&ref=search".format(package_name)
    res=requests.get(url)
    html=etree.HTML(res.text)
    program_name=html.xpath(r"/html/body/div[@class='main']/div[@class='container cf']/div[@class='app-intro cf']/div[@class='app-info']/div[@class='intro-titles']/h3/text()")[0]
    size=html.xpath(r"/html/body/div[@class='main']/div[@class='container cf']/div[3]/div[@class='float-left']/div[2]/text()")[0]
    version=html.xpath(r"/html/body/div[@class='main']/div[@class='container cf']/div[4]/div[@class='float-left']/div[2]/text()")[0]
    update_time=html.xpath(r"/html/body/div[@class='main']/div[@class='container cf']/div[5]/div[@class='float-left']/div[2]/text()")[0]
    package_name=html.xpath(r"/html/body/div[@class='main']/div[@class='container cf']/div[6]/div[@class='float-left']/div[2]/text()")[0]
    developer=html.xpath(r"/html/body/div[@class='main']/div[@class='container cf']/div[4]/div[@class='float-right']/div[2]/text()")[0]
    icon_url=html.xpath(r"/html/body/div[@class='main']/div[@class='container cf']/div[@class='app-intro cf']/div[@class='app-info']/img/@src")[0]
    result=program_name,package_name,size,version,update_time,developer,icon_url
    return result

def write_into_csv(item_list,method):
    """
    :param item_list:写入到行列表
    :param method:写入方式
    :return:
    """
    with open(os.path.join(os.getcwd(),'app_info_result.csv'),method) as f:
        csv_writer=csv.writer(f)
        csv_writer.writerow(item_list)

def download_icon(program_name,icon_url):
    """
    :param program_name: 应用名称
    :param icon_url:应用图标
    :return:下载图标
    """
    try:
        res=requests.get(icon_url)
    except Exception as e:
        print('图标下载异常:',program_name,icon_url,e)
    else:
        with open(os.path.join(os.getcwd(),'icon',program_name + '.png'),'wb') as f:
            f.write(res.content)

if __name__ == '__main__':
    with open(os.path.join(os.getcwd(),'program_package_info.txt'),'r',encoding='utf-8') as f:
        app_info_list=f.readlines()[1:]
        app_info_list=[line.strip() for line in app_info_list]
    colums_list=['program_name','package_name','size','version','update_time','developer','icon_url']
    write_into_csv(colums_list,'w')
    for line in app_info_list:
        program_name,package_name=line.split(',')
        try:
            result=get_package_info(package_name)
            icon_url=result[-1]
        except Exception as e:
            print(program_name,package_name,e)
        else:
            write_into_csv(result,'a+')
            download_icon(program_name,icon_url)
        time.sleep(0.5)
