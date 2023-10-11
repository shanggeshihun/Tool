# _*_coding:utf-8 _*_
# @Time　　 :2020/11/25/025   12:21
# @Author　 : Antipa
# @File　　 :test_selenium.py
# @Theme    :通过手机型号代码查询手机型号以及品牌名称

import requests,json,os,time
import pandas as pd
import numpy as np
from fake_useragent import UserAgent
ua=UserAgent()

def get_mobil_code_info(model):
    """
    :param model:手机型号代码
    :return:{"msg":"success","code":0,"data":{"name":"HUAWEI nova 4 全网通版","brand":"HUAWEI"}}
    """
    url='https://model-lib.4kb.cn/api/model/{}'.format(model.upper())
    headers={
        'User-Agent':np.random.choice(ua)
    }
    res=requests.get(url=url,headers=headers)
    res_to_json=json.loads(res.text)
    return res_to_json

if __name__ == '__main__':
    model_code_file=os.path.join(os.getcwd(),'model_code.txt')
    with open(model_code_file,'r',encoding='utf-8') as f:
        model_list=f.readlines()

    m_list,name_list,brand_list=[],[],[]
    i=0
    for m in model_list:
        i=i+1
        m=m.strip()
        info=get_mobil_code_info(m)
        print(info)
        if 'msg' not in info.keys():
            continue
        msg=info['msg']
        if not msg=='success':
            continue
        m_list.append(m)
        data=info['data']
        name=data['name']
        name_list.append(name)
        brand=data['brand']
        brand_list.append(brand)
        time.sleep(0.5)

    df=pd.DataFrame()
    df['model']=m_list
    df['name']=name_list
    df['brand']=brand_list

    print(df)
    df.to_excel(os.path.join(os.getcwd(),'model_code_info.xlsx'))
