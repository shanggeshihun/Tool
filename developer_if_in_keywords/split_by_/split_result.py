# _*_coding:utf-8 _*_
# @Time　　 :2021/4/29/029   14:10
# @Author　 : Antipa
# @File　　 :split_result.py
# @Theme    :PyCharm
from collections import Counter
with open(r'E:\工作文档\antiy\NOTE\Python\Tool\developer_if_in_keywords\split_by_\developer.txt','r',encoding='utf-8') as f:
    developer_list=[l.strip() for l in f.readlines()]
d_=[]
for d in developer_list:
    d_list=d.split('^')
    d_list=[d.strip() for d in d_list]
    d_.extend(d_list)
d_counter=Counter(d_)
for d in d_counter:
    print(d)
