# _*_coding:utf-8 _*_
# @Time　　 :2021/4/29/029   13:43
# @Author　 : Antipa
# @File　　 :main_single_threading_7881.py
# @Theme    :PyCharm

with open(r'E:\工作文档\antiy\NOTE\Python\Tool\developer_if_in_keywords\developer_new.txt','r',encoding='utf-8') as f:
    developer_new_list=[l.strip() for l in f.readlines()]
with open(r'E:\工作文档\antiy\NOTE\Python\Tool\developer_if_in_keywords\developer_from_crawl.txt','r',encoding='utf-8') as f2:
    developer_list=[l.strip() for l in f2.readlines()]

developer_logit={}
for dev in developer_list:
    for d in developer_new_list:
        if d in dev:
            developer_logit[dev]='True'
            break

import pandas as pd
df=pd.DataFrame()
for k,v in developer_logit.items():
    print(k,v)
    df=df.append([[k,v]],ignore_index=True)
df.columns = ['developer', 'flag']
result_file_path=r'E:\工作文档\antiy\NOTE\Python\Tool\developer_if_in_keywords\tmp.xlsx'
df.to_excel(result_file_path)
