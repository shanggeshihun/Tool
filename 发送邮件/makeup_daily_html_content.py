# _*_coding:utf-8 _*_
# @Time　　 :2024/4/29 00:30
# @Author　 : Antipa
# @File　　 :makeup_daily_html_content.py
# @Theme    :PyCharm

def get_metrics_color_change(vlaue):
    if vlaue > 0:
        color, change = "green", "增长"
    elif vlaue < 0:
        color, change = "red", "下降"
    elif vlaue == 0:
        color, change = "black", "持平"
    else:
        pass
    return color, change


def demo1():
    # 假设这是从数据库或其他来源获取的数据
    merchant_data = {
        "商户A": {"交易量": 40, "支付成功率": 20, "支付转化率": -20},  # 假设商户A的交易量增长了20%
        "商户B": {"支付成功率": -10, "支付转化率": 15}  # 假设商户B的交易量下降了10%
    }

    body = ''
    # 遍历商户数据并生成邮件内容
    for merchant, main_dict in merchant_data.items():
        body += f"<b>商户{merchant}：</b>"
        for metric_name, mertric in main_dict.items():
            color, change = get_metrics_color_change(mertric)
            body += f"{metric_name}<font color=\"{color}\">{change}{mertric}%</font>"
        body += "<br>"
    return body
