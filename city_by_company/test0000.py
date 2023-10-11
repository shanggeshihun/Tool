# _*_coding:utf-8 _*_
# @Time　　 :2021/4/12/012   15:07
# @Author　 : Antipa
# @File　　 :test0000.py
# @Theme    :PyCharm

import pandas as pd
hubei={
    '武汉':['武汉','江岸','江汉','汉阳','武昌','硚口','青山','洪山','汉南','蔡甸','江夏','黄陂','新洲','东西湖'],
    '黄石':['黄石','下陆','铁山','黄石港','西塞山','大冶','阳新'],
    '十堰':['十堰','茅箭','张湾','郧阳','丹江口','房县','郧西','竹山','竹溪'],
    '宜昌':['宜昌','西陵','点军','猇亭','夷陵','伍家岗','宜都','当阳','枝江','远安','兴山','秭归','长阳土家族自治','五峰土家族自治'],
    '襄阳':['襄阳','襄城','樊城','襄州','枣阳','宜城','老河口','南漳','谷城','保康'],
    '鄂州':['鄂州','华容','鄂城','梁子湖'],
    '荆门':['荆门','东宝','掇刀','钟祥','京山','沙洋'],
    '孝感':['孝感','孝南 ','应城','汉川','安陆','孝昌','大悟','云梦'],
    '荆州':['荆州','沙市','荆州','松滋','石首','洪湖','监利','江陵','公安'],
    '黄冈':['黄冈','黄州','武穴','麻城','团风','红安','罗田','英山','黄梅','浠水','蕲春'],
    '咸宁':['咸宁','咸安','赤壁','嘉鱼','崇阳','通城','通山'],
    '随州':['随州','曾都','广水','随县'],
    '恩施州':['恩施','利川','建始','巴东','宣恩','咸丰','来凤','鹤峰'],
    '省直辖':['神农架'],
    '天门':['天门'],
    '潜江':['潜江'],
    '仙桃':['仙桃']
}


dict={}
with open(r"E:\工作文档\antiy\NOTE\Python\Tool\test\city_by_company\company.txt",'r',encoding='utf-8') as f:
    company_list=[l.strip() for l in f.readlines()]
    for c in company_list:
        for main_city,v in hubei.items():
            for sub_v in v:
                if sub_v in c:
                    dict[c]=main_city
                    break
df=pd.DataFrame()
for k, v in dict.items():
    df = df.append([(k, v)])
target_file = r"C:\Users\Administrator\Desktop\company_belong_to_city.xlsx"
df.to_excel(target_file)