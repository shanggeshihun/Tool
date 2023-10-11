# _*_coding:utf-8 _*_
# @Time　　 :2020/10/12/012   12:52
# @Author　 : Antipa
# @File　   :resourceStr_classify.py
# @Theme    :PyCharm

dict_inner={'a':1}
print(id(dict_inner))
dict_outer={'b':dict_inner}
m=dict_outer['b']
print(id(m))
m['a']=m['a']+1
print(id(m))
# m与dict_inner指向同一个地址

import copy
dict_inner={'a':1}
print(id(dict_inner))
dict_outer={'b':dict_inner}
dict_inner_=copy.deepcopy(dict_outer['b'])
dict_inner_['a']=dict_inner_['a']+1
print(id(dict_inner_))
# m与dict_inner指向同一个地址


d=1
print(id(d))
dict_outer={'b':d}
m=dict_outer['b']
m=m+1
print(id(m))
# 此时m与d指向不同地址

