# _*_coding:utf-8 _*_
# @Time　　 :2021/3/18   23:31
# @Author　 :
# @File　　 :test_selenium.py
# @Theme    :PyCharm

import os,shutil
def copy_file(dir,new_dir,program_name_list):
    for file in os.listdir(dir):
        if file.split('.')[0] in program_name_list:
            shutil.copy(os.path.join(dir,file),os.path.join(new_dir,file))

if __name__ == '__main__':
    dir=r'D:\learn\software_learn\NOTE\Python\TEST\copy_file\dir'
    new_dir=r'D:\learn\software_learn\NOTE\Python\TEST\copy_file\new_dir'
    program_name_list=[
        '腾讯手机管家','诸葛天气','2345天气王','荔枝新闻','即刻充电管家','手机管家','洪铟八字算命','手机万年历','讯飞配音','最美天气','相册制作','爱豆','悦跑圈','来电万能宝','草料二维码','闪电清理大师','积目','极安全','一键WiFi大师','WiFi全能助手','本地头条','证件照','动感来电秀','Well文件管理','万年历','飞鱼清理极速版','万能清理大师','365手机卫士','招财日历','强力清理卫士','美图证件照','降温宝','免费全能扫描王','一键卸载大师','P图大神','文字图片制作','马卡龙玩图','微商助手水印相册','方舟浏览器','我是谜','网络测速助手','耳觅','咔萌交友聊天','趣看天下','迅捷PDF转换器','DJI GO 4','照片恢复精灵软件','21财经','微微电话','电商头条','一寸证件照','一键群发','久久浏览器','猎豹清理大师'
    ]
    copy_file(dir,new_dir,program_name_list)