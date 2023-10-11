# _*_coding:utf-8 _*_
# @Time　　 :2021/2/9   13:25
# @Author　 :
# @File　　 :download_icon_from_mi.py
# @Theme    :参考小米应用市场，通过包名搜索包名的应用图标

import requests,os,time,re,json,csv
from lxml import etree


def get_package_info(region_program_name):
    url="https://sj.qq.com/myapp/searchAjax.htm?kw={}".format(region_program_name)
    print(url)
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        'cookie': 'session_uuid=4ea66a8f-2fa9-46cb-abc4-c4b6b95be804; pgv_pvid=2158348554; eas_sid=V1w6l0R9A0k7M2R2i4Y7k3w5D3; RK=grLVXYFLfZ; ptcz=2ff5b9d222a253be29e7656786c93b1f1d689535a24ef8978f92dfd1a85eb5b6; pac_uid=0_646d5cfe03dee; iip=0; sd_userid=45411609943207584; sd_cookie_crttime=1609943207584; tvfe_boss_uuid=626da46a8f7f28a9; ts_uid=1272719475; JSESSIONID=aaa_J5hnVqZeq6x5KiEEx; pgv_info=ssid=s756195440'
    }
    res=requests.get(url,headers=headers)
    res_to_json=json.loads(res.text)
    items=res_to_json['obj']['items'][0]
    package_name=items['pkgName']

    app_details=res_to_json['obj']['appDetails']
    app_details_first=app_details[0]

    apk_md5=app_details_first['apkMd5']
    program_name=app_details_first['appName']
    developers=app_details_first['authorName']
    icon_url=app_details_first['iconUrl']
    result=region_program_name,package_name,apk_md5,program_name,developers,icon_url
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
    try:
        res=requests.get(icon_url)
    except Exception as e:
        print(program_name,icon_url,e)
    else:
        with open(os.path.join(os.getcwd(),'icon',program_name + '.png'),'wb') as f:
            f.write(res.content)

if __name__ == '__main__':
    with open(os.path.join(os.getcwd(),'program_info.txt'),'r',encoding='utf-8') as f:
        app_info_list=f.readlines()[1:]
        app_info_list=[line.strip() for line in app_info_list]
    column_list=['region_program_name','package_name','apk_md5','program_name','developers','icon_url']
    write_into_csv(column_list,'w')

    for line in app_info_list:
        program_name=line.strip()
        try:
            result=get_package_info(program_name)
            icon_url=result[-1]
        except Exception as e:
            print('应用下载搜索失败',program_name,program_name,e)
        else:
            download_icon(program_name,icon_url)
            write_into_csv(result,'a+')
        time.sleep(1)