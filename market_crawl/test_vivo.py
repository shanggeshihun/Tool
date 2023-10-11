# _*_coding:utf-8 _*_
# @Time　　 :2021/6/4/004   15:16
# @Author　 : Antipa
# @File　　 :test_vivo.py
# @Theme    :PyCharm

import requests
program,page,app_id='微信','10','9'
search_url = u'https://search.appstore.vivo.com.cn/port/packages/?screensize=1080_1808&plateformVersion=0&apps_per_page=5&app_version=1704&nt=WIFI&plateformVersionName=null&abtest=0&pictype=webp&model=MHA-AL00&platApkVer=0&key={0}&density=3.0&session_id=1547948539292&elapsedtime=751737200&an=8.0.0&cfrom=2&target=local&cs=0&plat_key_ver=&platApkVerName=null&u=1234567890&av=26&page_index={1}&imei=864360034762768&build_number=MHA-AL00+8.0.0.374%28C00%29&sshow=110&patch_sup=1&s=2%7C3756974092'.format(program,page)

detail_url = u'http://info.appstore.vivo.com.cn/port/package/?pos=16&build_number=PD1415D_A_1.20.0&elapsedtime=90284021&content_complete=1&screensize=1080_1920&ct=2&density=3.0&pictype=webp&cs=0&av=22&u=150100525831344d42017604d4152351&listpos=16&an=5.1&app_version=1063&imei=860832035794309&nt=WIFI&module_id=116&id={0}&target=local&cfrom=150&need_comment=0&model=vivo+X6D'.format(app_id)

headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
}

print(search_url,'\n',detail_url)

search_url_res=requests.get(search_url,headers=headers)

print(search_url_res.text)