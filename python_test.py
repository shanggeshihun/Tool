# _*_coding:utf-8 _*_
# @Time     :2020/10/23 0023   下午 11:28
# @Author   : Antipa
# @File     :fs.py
# @Theme    :PyCharm

import pandas as pd

file_path=r'E:\工作文档\antiy\AT\下载数据\CSV数据\part-00000-3d7f127b-b77d-4c20-a329-c5c81039d5e4-c000 (2).csv'

f=pd.read_csv(file_path,error_bad_lines=False)

df_package=f['package_name']

df_package_list=list(df_package)

package_list=['com.mobile.iroaming','com.snda.lantern.wifilocating']

for p in package_list:
	if p in df_package_list:
		print(p)