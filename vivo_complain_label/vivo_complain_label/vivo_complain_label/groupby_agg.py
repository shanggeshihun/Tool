# _*_coding:utf-8 _*_
# @Time　　 :2020/10/12/012   16:00
# @Author　 : Antipa
# @File　   :groupby_agg.py
# @Theme    :根据分组字段统计关键出现次数

import numpy as np
import pandas as pd
import time,copy

def groupby_statistic(file_path,sheet_name,groupby_column,keywords_list,in_str,save_file_path):
    """
    :param file_path: 读取文件的路径
    :param sheet_name:读取文件的sheet名称
    :param groupby_column:分类统计的字段名称
    :param keywords_list:关键词列表
    :param in_str:与关键词对比的字段名称
    :param save_file_path:分类统计完成后保存文件的路径
    :return:None
    """
    df=pd.read_excel(file_path,sheet_name=sheet_name)

    # 初始化 外层字典
    suspect_appname_dict={}
    # 初始化 内层字典 keywords_list_dict
    keywords_list_dict={}
    for d in keywords_list:
        keywords_list_dict[d]=0

    for idx,item in df.iterrows():
        suspect_appname = item[groupby_column]
        desc = str(item[in_str])
        if suspect_appname in suspect_appname_dict.keys():
            suspect_appname_value=suspect_appname_dict[suspect_appname]
        else:
            # 此处不能直接赋值或者copy，否则会导致keywords_list_dict与suspect_appname_value同地址
            suspect_appname_dict[suspect_appname] = copy.deepcopy(keywords_list_dict)
            suspect_appname_value = suspect_appname_dict[suspect_appname]
        for k,v in suspect_appname_value.items():
            if k in desc:
                suspect_appname_value[k]=suspect_appname_value[k]+1

    df_1=pd.DataFrame()
    for k,v in suspect_appname_dict.items():
        tmp_df=pd.DataFrame(v,index=[k])
        df_1=df_1.append(tmp_df)

    df_1.to_excel(save_file_path)
    return df_1
    # import xlsxwriter
    # df_1.to_excel(save_file_path,engine='xlsxwriter')

if __name__ == '__main__':
    start_time = time.time()

    keywords_list=complain_desc_keywords()
    file_path=r"D:\work\antiy\AT\品类\20200820_网赚\网赚(零撸)应用列表\vivo用户举报信息.xlsx"
    sheet_name='Sheet1'
    groupby_column='可能可信程序名'
    in_str='其他描述'
    save_file_path=r"D:\work\antiy\AT\品类\20200820_网赚\网赚(零撸)应用列表\brief.xlsx"
    groupby_statistic(file_path, sheet_name, groupby_column,keywords_list, in_str, save_file_path)

    end_time=time.time()

    print(end_time-start_time)