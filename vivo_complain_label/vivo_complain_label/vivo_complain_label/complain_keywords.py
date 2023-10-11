# _*_coding:utf-8 _*_
# @Time　　 :2020/10/12/012   12:52
# @Author　 : Antipa
# @File　   :resourceStr_classify.py
# @Theme    :PyCharm

def complain_desc_keywords():

    desc_keyword_list=[
        '提现', '诈骗', '欺骗', '骗人', '赌博', '广告', '病毒', '催收', '扣费', '泄露', '骚扰', '缴费', '色情', '裸聊', '裸照', '敲诈', '威胁','杀猪', '博彩', '资金盘','区块',"数字货币",'空气币','虚拟货币'
    ]
    return desc_keyword_list

def risk_label_keywords():
    risk_keyword_list=[
        '杀猪盘','全民反诈','套路贷'
    ]
    return risk_keyword_list

def report_type_keywords():
    report_keyword_list=[
        '恶意扣费', '携带病毒', '反动内容', '色情内容', '暴力内容', '含有不良插件', '侵权内容'
    ]
    return report_keyword_list

def finance_fake_keywords():
    fake_keyword_list=[
        '小米金融','蚂蚁金服'
    ]
    return fake_keyword_list

