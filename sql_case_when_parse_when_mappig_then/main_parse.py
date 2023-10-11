# _*_coding:utf-8 _*_
# @Time　　 :2021/6/9/009   15:09
# @Author　 : Antipa
# @File　　 :main_parse.py
# @Theme    :PyCharm



import re,os
import pandas as pd

path = os.path.join(os.getcwd(),'case_when_sql.txt')

with open(path, 'r', encoding='utf-8') as f:
    kw_when_split = f.read().split('when')[1:]

rule_dict = {}

for k in kw_when_split:
    when_then = k.split('then')

    pattern = re.compile(r"like\s*\"?\'?%?(.*?)%\"?\'?")
    when_result = pattern.findall(when_then[0])

    then_result = when_then[1].split('else')[0].strip().replace("'", '').replace('"', '')

    for r in when_result:
        rule_dict[r.strip()] = then_result

df = pd.DataFrame()
for k, v in rule_dict.items():
    df = df.append([(k, v)])
df.columns = ['rule', 'company']
df.reindex()
save_path =os.path.join(os.getcwd(),'case_when_sql.xlsx')
df.to_excel(save_path,index=False)