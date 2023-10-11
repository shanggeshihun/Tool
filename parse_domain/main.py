# _*_coding:utf-8 _*_
# @Time　　 :2021/4/22/022   10:14
# @Author　 : Antipa
# @File　　 :main_single_threading_7881.py
# @Theme    :PyCharm
import pandas as pd
import re,os

df=pd.read_csv(os.path.join(os.getcwd(),'sha_20210422.csv'))

df_result=pd.DataFrame()
for idx,item in df.iterrows():
    sample_sha256=item['sample_sha256']
    sensitive_strings_url=item['sensitive_strings_url']
    if not sensitive_strings_url:
        print(sample_sha256,'敏感字符串为空')
        continue
    try:
        tmp_sensitive_strings_url_list=sensitive_strings_url.split(',')
    except Exception as e:
        print(sample_sha256,'敏感字符串无法按照逗号分隔',sensitive_strings_url)
    for t in tmp_sensitive_strings_url_list:
        ip_domain=re.findall(r'https?://(.*?)/',t)
        try:
            if not ip_domain:
                result_ip_domain=t.split('//')[1]
            else:
                result_ip_domain=ip_domain[0]
            part_str=result_ip_domain.split('.')[0]
            if re.search(r'\d+',part_str):
                type='ip'
            else:
                type='domain'
            df_result=df_result.append([(sample_sha256,result_ip_domain,type)])
        except Exception as e:
            print(sample_sha256,'其他异常',ip_domain)
df_result.to_excel(os.path.join(os.getcwd(),'se_1.xlsx'))


