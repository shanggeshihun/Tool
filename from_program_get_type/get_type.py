# _*_coding:utf-8 _*_
# @Time　　 :2020/12/23/023   10:48
# @Author　 : Antipa
# @File　　 :get_type.py
# @Theme    :PyCharm

from program_type_mapping import get_mapping
import os
import pandas as pd
m=get_mapping()

def get_type(program,package,falg):
    """
    :param program: 应用名称
    :param package: 应用包名
    :param falg: 参考 应用包名 则 flag=1，否则flag=0
    :return:所属的应用类型
    """
    for k,v in m.items():
        program_list=v[0]
        for p in program_list:
            if p in program:
                return k

if __name__ == '__main__':
    df=pd.DataFrame()
    program_package_file_path = os.path.join(os.getcwd(), 'program_package.txt')
    i=0
    with open(program_package_file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            program=line.split()[0]
            package=line.split()[1]
            r=get_type(program,package,1)

            df=df.append([[program,package,r]],ignore_index=True)
    df.columns = ['program', 'package', 'type']

    result_file_path = os.path.join(os.getcwd(), 'result.xlsx')
    df.to_excel(result_file_path)


