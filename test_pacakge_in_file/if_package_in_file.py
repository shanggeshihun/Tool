# _*_coding:utf-8 _*_
# @Time　　 :2021/5/19/019   9:33
# @Author　 : Antipa
# @File　　 :if_package_in_file.py
# @Theme    :PyCharm

import pandas as pd,os

cwd=os.getcwd()

file_path=r'E:\工作文档\antiy\AT\下载数据\CSV数据\part-00000-3d7f127b-b77d-4c20-a329-c5c81039d5e4-c000 (2).csv'

f=pd.read_csv(file_path,error_bad_lines=False)

df_package=f['package_name']

df_package_list=list(df_package)

with open(os.path.join(cwd,'package.conf'),'r') as f:
	package_list=[lst.strip() for lst in f.readlines()]

package_flag={}
for p in package_list:
	if p in df_package_list:
		package_flag[p]='True'
		print(p)
	else:
		package_flag[p]='False'

df=pd.DataFrame()
for k, v in package_flag.items():
	df = df.append([(k, v)])
df.columns=['p','flag']
target_file = os.path.join(cwd,'package_mapping.xlsx')
df.to_excel(target_file)