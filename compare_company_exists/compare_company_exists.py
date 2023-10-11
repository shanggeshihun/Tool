# _*_coding:utf-8 _*_
# @Time　　 :2021/4/16/016   14:44
# @Author　 : Antipa
# @File　　 :developers_mapping_abbre.py
# @Theme    :比较企业简称是否在企业联结字符串中出现过，返回企业简称与返回结果的标识

import pandas as pd,os
with open(os.path.join(os.getcwd(),'inner_qiye.txt'),'r',encoding='utf-8') as f:
    # 企业简称
    will_developer_list=[l.strip() for l in f.readlines()]

with open(os.path.join(os.getcwd(),'developer_set.txt'),'r',encoding='utf-8') as f:
    # 多个企业组成的企业字符串
    developer_list=[l.strip() for l in f.readlines()]

will_d_dict={}
for will_d in will_developer_list:
    will_d_list=will_d.split('^')
    print(will_d_list)
    for w in will_d_list:
        for d in developer_list:
            d_list=d.split('^')
            for d in d_list:
                if w in d:
                    tmp='是子串'
                    will_d_dict[will_d]=tmp
                    break
df=pd.DataFrame()
for k, v in will_d_dict.items():
    df = df.append([(k, v)])
print(df)
df.columns=['will_d','flag']
target_file = os.path.join(os.getcwd(),'substring_mapping_label.xlsx')
df.to_excel(target_file)