# _*_coding:utf-8 _*_
# @Time　　 :2021/2/25/025   12:36
# @Author　 : Antipa
# @File　　 :multi_to_single.py
# @Theme    :PyCharm

import pandas as pd
import os

def main():
    """

    """
    file_path=os.path.join(os.getcwd(),'model.xlsx')

    df=pd.read_excel(file_path)
    print(df)
    d={}
    for idx,items in df.iterrows():
        keyword=items['keyword']
        item=items['item']
        if keyword not in d.keys():
            d[keyword]=item.strip()
        else:
            d[keyword]=d[keyword]+(item.strip())

    to_file_path=os.path.join(os.getcwd(),'model_transformed.xlsx')
    df1=pd.DataFrame()
    for item in d.items():
        df1=df1.append([item],ignore_index=True)
    df1.columns=['keyword','items']
    df1.to_excel(to_file_path)

if __name__ == '__main__':
    main()