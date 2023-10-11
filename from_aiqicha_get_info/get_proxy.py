# _*_coding:utf-8 _*_
# @Time　　 :2021/5/7/007   15:07
# @Author　 : Antipa
# @File　　 :get_proxy.py
# @Theme    :PyCharm

import requests
def get_proxy():
    url='http://darwin.v4.dailiyun.com/query.txt?key=NP750C667D&word=&count=1&rand=false&ltime=0&norepeat=false&detail=false'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }

    res=requests.get(url,headers=headers)
    return  res.text.strip()

def check_proxy():
    """
    :param proxy代理
    :return: 返回bool
    """
    import json
    url='http://httpbin.org/get'
    flag=True
    proxy_value=get_proxy()
    proxy_1={'http':proxy_value}
    # proxy_1={'http':'1111111111'}
    # proxy_2={'https':'1111111111'}
    proxy_2={'https':proxy_value}
    response_dict={}
    print(proxy_2)
    try:
        response = requests.get(url, proxies=proxy_1,timeout=(3,7))
        if response.status_code==200:
            response_dict=json.loads(response.text)
        else:
            flag=False
    except:
        response2 = requests.get(url, proxies=proxy_2, timeout=(3, 7))
        if response2.status_code==200:
            response_dict=json.loads(response2.text)
        else:
            flag=False
    return flag,response_dict

if __name__ == '__main__':
    f=check_proxy()
    print(f)