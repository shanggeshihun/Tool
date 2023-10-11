# _*_coding:utf-8 _*_
# @Time　　 :2021/4/16/016   14:44
# @Author　 : Antipa
# @File　　 :developers_mapping_abbre.py
# @Theme    :比较企业简称是否在企业联结字符串中出现过，返回企业联结字符串对应的企业简称

import pandas as pd,os
with open(os.path.join(os.getcwd(),'inner_qiye.txt'),'r',encoding='utf-8') as f:
    # 企业简称
    will_developer_list=[l.strip() for l in f.readlines()]

with open(os.path.join(os.getcwd(),'developer_set.txt'),'r',encoding='utf-8') as f:
    # 多个企业组成的企业字符串
    developer_list=[l.strip() for l in f.readlines()]


d_dict={}
for d in developer_list:
    d_list=d.split('^')
    for d_tmp in d_list:
        for w_d in will_developer_list:
            if w_d in d_tmp:
                d_dict[d_tmp]=w_d
                break
        break
df=pd.DataFrame()

for k, v in d_dict.items():
    df = df.append([(k, v)])
print(df)
df.columns=['d','flag']
target_file = os.path.join(os.getcwd(),'developer_mapping_substring.xlsx')
df.to_excel(target_file)
