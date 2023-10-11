# _*_coding:utf-8 _*_
# @Time　　 :2021/5/20   0:41
# @Author　 :
# @File　　 :split_workbook.py
# @Theme    :PyCharm
import pandas as pd
import os

def split_workbook_to_workbooks_by_filed(file_path,sheet_name,save_file_dir,by_field_name):
    """
    :param file_path: 文件路径
    :param sheet_name: 工作表名
    :param save_file_dir: 存储文件夹路径
    :param by_field_name:按照某个字段切分表
    :return:
    """
    df1 = pd.read_excel(file_path, sheet_name=sheet_name)
    data = list(df1.groupby([by_field_name]))
    for d in data:
        data_tuple_field_name = d[0]
        data_tuple_df = d[1]
        print(data_tuple_df)
        data_tuple_df.to_excel(save_file_dir + '\\'+str(data_tuple_field_name) + '.xlsx', sheet_name=data_tuple_field_name, index=False)
        print(1)

if __name__ == '__main__':
    file_path=r"E:\工作文件\在刀锋\dofun\Python\Python\Tool\split_workbook_to_workbooks_by_fileds\excel_file\hue_tool_qiye_list.xlsx"
    sheet_name='Sheet1'
    by_field_name='qiye'
    save_file_dir=r"E:\工作文件\在刀锋\dofun\Python\Python\Tool\split_workbook_to_workbooks_by_fileds\save_dir"
    split_workbook_to_workbooks_by_filed(file_path,sheet_name,save_file_dir,by_field_name)