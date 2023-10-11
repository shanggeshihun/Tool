# _*_coding:utf-8 _*_
# @Time　　 :2021/2/9   13:25
# @Author　 :
# @File　　 :download_icon_from_mi.py
# @Theme    :参考小米应用市场，通过包名搜索包名的应用图标

import requests,os,time,csv
from lxml import etree


def get_package_info(region_program_name):
    url="https://app.mi.com/search?keywords={}".format(region_program_name)
    print(url)
    res=requests.get(url)
    html=etree.HTML(res.text)
    first_html_xpath=html.xpath(r"//ul[@class='applist']")[0]
    first_app=first_html_xpath.xpath(r"./li")[0]

    print(first_app.xpath(r"./a/@href")[0])
    first_app_href='https://app.mi.com'+ first_app.xpath(r"./a/@href")[0]
    print(first_app_href)
    app_res=requests.get(first_app_href)
    app_html=etree.HTML(app_res.text)
    program_name=app_html.xpath(r"//div[@class='app-info']/div/h3/text()")[0]
    icon_url=app_html.xpath(r"//div[@class='app-info']/img/@src")[0]
    type=app_html.xpath(r"//div[@class='app-info']/div/p/text()")[0]
    support=app_html.xpath(r"//div[@class='app-info']/div/p/text()")[1]
    size=app_html.xpath(r"//div[@class='float-left']/div[@style='float:right;']/text()")[0]

    version=app_html.xpath(r"//div[@class='float-left']/div[@style='float:right;']/text()")[1]
    update_date=app_html.xpath(r"//div[@class='float-left']/div[@style='float:right;']/text()")[2]
    package_name=app_html.xpath(r"//div[@class='float-left']/div[@style='float:right;']/text()")[3]
    appid=app_html.xpath(r"//div[@class='float-right']/div[@style='float:right;']/text()")[0]
    developer=app_html.xpath(r"//div[@class='float-right']/div[@style='float:right;']/text()")[1]
    private_policy=app_html.xpath(r"//div[@class='float-right']/div[@style='float:right;']/text()")[2]
    permission=app_html.xpath(r"//div[@class='float-right']/div[@style='float:right;']/text()")[3]

    result=region_program_name,program_name,type,support,size,version,update_date,package_name,appid,developer,private_policy,permission,icon_url
    return result


def write_into_csv(item_list,method):
    """
    :param item_list:写入到行列表
    :param method:写入方式
    :return:
    """
    with open(os.path.join(os.getcwd(),'app_info_result.csv'),method,encoding='utf-8') as f:
        csv_writer=csv.writer(f)
        csv_writer.writerow(item_list)


def download_icon(region_program_name,icon_url):
    """
    :param region_program_name: 应用名称
    :param icon_url:应用图标
    :return:下载图标
    """
    try:
        res=requests.get(icon_url)
    except Exception as e:
        print('图标下载异常',region_program_name,icon_url,e)
    else:
        with open(os.path.join(os.getcwd(),'icon',region_program_name + '.png'),'wb') as f:
            f.write(res.content)

if __name__ == '__main__':
    with open(os.path.join(os.getcwd(),'program_info.txt'),'r',encoding='utf-8') as f:
        app_info_list=f.readlines()[1:]
        app_info_list=[line.strip() for line in app_info_list]
    column_list=['region_program_name','program_name','type','support','size','version','update_date','package_name','appid','developer','private_policy','permission','icon_url']
    write_into_csv(column_list,'w')

    for line in app_info_list:
        program_name=line
        try:
            result=get_package_info(program_name)
            icon_url=result[-1]
        except Exception as e:
            print('应用下载搜索失败',program_name,e)
        else:
            download_icon(program_name,icon_url)
            write_into_csv(result,'a+')
        time.sleep(1)