# _*_coding:utf-8 _*_
# @Time　　 :2020/8/18/018   19:51
# @Author　 : 
#@ File　   :test_2.py
#@ Desc     :

f_title=open(r'E:\工作文档\antiy\NOTE_NEW\test\title_set.txt', encoding='utf-8')
f_app=open(r'E:\工作文档\antiy\NOTE_NEW\test\title_set.txt', encoding='utf-8')

for title in f_title.readlines():
    app_list = []
    for app in f_app.readlines():
        print(title,app)
        if app in title:
            app_list.append(app)
            break
    print(app_list)
for t in zip(f_title.readlines(), app_list):
    print(t)

