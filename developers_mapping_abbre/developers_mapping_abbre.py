# _*_coding:utf-8 _*_
# @Time　　 :2021/4/16/016   14:44
# @Author　 : Antipa
# @File　　 :developers_mapping_abbre.py
# @Theme    :开发者集合字符中是否含有企业简称

import pandas as pd
import os,sys
with open(os.path.join(sys.path[0],'inner_qiye.txt'),'r',encoding='utf-8') as f:
    # 企业简称
    developer_abbre_list=[l.strip() for l in f.readlines()]

with open(os.path.join(sys.path[0],'developer_set.txt'),'r',encoding='utf-8') as f:
    # 多个企业组成的企业字符串
    developers_list=[l.strip() for l in f.readlines()]

developers_abbre_dict={}
for developers in developers_list:
    developers_abbre_dict[developers] ='None'
    for dev in developer_abbre_list:
        if dev in developers:
            developers_abbre_dict[developers]=dev
        continue

df=pd.DataFrame()
for developers, developer_abbre in developers_abbre_dict.items():
    df = df.append([(developers, developer_abbre)])
df.columns=['developers','developer_abbre']

target_file = os.path.join(sys.path[0],'developers_abbre.xlsx')
df.to_excel(target_file)