'''
Filename : get_relation_package.py
Author : guochen
Email : guochen@antiy.cn
Company: 武汉安天信息科技有限公司
Created: 2021-05-17 20:20:56
Last Modified: 2021-05-17 22:12:18
Description: 利用泰尔接口进行种子APP关联扩展
'''

import requests
import json
from tqdm import tqdm
import argparse
import os


def get_content(node_type,package_name):
    # 请求查询
    url = ("https://app-r618e96j.avlyun.com/related_package?input_type=%s&property_value=%s") %(node_type,package_name)
    response = requests.get(url=url)
    print()
    if response.status_code==200:
        return response.content
    else:
        print("暂无 %s 的信息" % (package_name,))
        return None


def read_data(input_file_path):
    # 读取文件
    data_list = []
    with open(input_file_path,encoding='utf-8',mode='r')as rd:
        for package in rd.readlines():
            data_list.append(('Package',package.strip()))
    return data_list


def save_data(content,out_file_path):
    # 保存数据
    if content is not None:
        data_json = json.loads(content)
        with open(out_file_path,encoding='utf-8',mode='a+')as wt:
            company = data_json['data']['company']
            downloads = data_json['data']['downloads']
            package_name = data_json['data']['package_name']
            program_name = data_json['data']['program_name']
            for related_app in data_json['data']['related_app']:
                re_company = related_app['company']
                re_downloads = related_app['downloads']
                re_package_name = related_app['package_name']
                re_program_name = related_app['program_name']
                is_huanpi = related_app['is_huanpi']
                wt.write(str(package_name)+','+str(program_name)+','+str(company)+','+str(downloads)+','+str(re_package_name)+','+str(re_program_name)+','+str(re_company)+','+str(re_downloads)+','+str(is_huanpi)+'\n')

def main():
    # 获取当前文件路径
    default_input = os.path.join(os.getcwd(),'input\input_package.csv')
    default_output = os.path.join(os.getcwd(),'output\output_package.csv')


    # 读取配置参数
    parser = argparse.ArgumentParser()
    # Required parameters
    parser.add_argument("--input_file", default=default_input, type=str, 
                        help="The input data file.")
    parser.add_argument("--out_file", default=default_output, type=str, 
                        help="The output data file.")
    args = parser.parse_args()
    input_file_path = args.input_file
    out_file_path = args.out_file
    
    data_list = read_data(input_file_path)
    
    for node_type,package_name in tqdm(data_list,"Processing ... ..."):
        content = get_content(node_type,package_name)
        save_data(content,out_file_path)
 
if __name__=="__main__":
    main()