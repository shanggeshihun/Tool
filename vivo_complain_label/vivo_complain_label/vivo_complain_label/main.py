# _*_coding:utf-8 _*_
# @Time     :2020/10/12 0012   下午 11:45
# @Author   : Antipa
# @File     :ad_decision_tree_classifier.py
# @Theme    :PyCharm

# 导入 投诉描述 关键词
import complain_keywords
from groupby_agg import groupby_statistic

import time
import pandas as pd

def main():
    start_time = time.time()

    # 其他描述
    keywords_list=complain_keywords.complain_desc_keywords()
    file_path=r"E:\antiy\AT\品类\20200820_网赚\网赚(零撸)应用列表\vivo用户举报信息.xlsx"
    sheet_name='投诉详情'
    groupby_column='包名'
    in_str='其他描述'
    save_file_path=r"E:\antiy\AT\品类\20200820_网赚\网赚(零撸)应用列表\vivo用户举报信息_complain.xlsx"
    df_complain=groupby_statistic(file_path, sheet_name, groupby_column,keywords_list, in_str, save_file_path)

    # 疑似诈骗风险应用
    keywords_list = complain_keywords.risk_label_keywords()
    file_path = r"E:\antiy\AT\品类\20200820_网赚\网赚(零撸)应用列表\vivo用户举报信息.xlsx"
    sheet_name = '投诉详情'
    groupby_column = '包名'
    in_str = '疑似诈骗风险应用'
    save_file_path = r"E:\antiy\AT\品类\20200820_网赚\网赚(零撸)应用列表\vivo用户举报信息_risk.xlsx"
    df_risk = groupby_statistic(file_path, sheet_name, groupby_column, keywords_list, in_str, save_file_path)

    # 举报类型
    keywords_list = complain_keywords.report_type_keywords()
    file_path = r"E:\antiy\AT\品类\20200820_网赚\网赚(零撸)应用列表\vivo用户举报信息.xlsx"
    sheet_name = '投诉详情'
    groupby_column = '包名'
    in_str = '举报类型'
    save_file_path = r"E:\antiy\AT\品类\20200820_网赚\网赚(零撸)应用列表\vivo用户举报信息_report.xlsx"
    df_report = groupby_statistic(file_path, sheet_name, groupby_column, keywords_list, in_str, save_file_path)

    # 是否金融仿冒
    keywords_list = complain_keywords.finance_fake_keywords()
    file_path = r"E:\antiy\AT\品类\20200820_网赚\网赚(零撸)应用列表\vivo用户举报信息.xlsx"
    sheet_name = '投诉详情'
    groupby_column = '包名'
    in_str = '是否金融仿冒'
    save_file_path = r"E:\antiy\AT\品类\20200820_网赚\网赚(零撸)应用列表\vivo用户举报信息_fake.xlsx"
    df_fake = groupby_statistic(file_path, sheet_name, groupby_column, keywords_list, in_str, save_file_path)

    tmp_df_merge=pd.merge(df_complain,df_risk,left_index=True,right_index=True,how='left')
    tmp_df_merge=pd.merge(tmp_df_merge,df_fake,left_index=True,right_index=True,how='left')
    tmp_df_merge=pd.merge(tmp_df_merge,df_report,left_index=True,right_index=True,how='left')

    tmp_df_merge.to_excel(r"E:\antiy\AT\品类\20200820_网赚\网赚(零撸)应用列表\vivo用户举报信息_final.xlsx")

    end_time=time.time()
    print(end_time-start_time)

if __name__ == '__main__':
    main()