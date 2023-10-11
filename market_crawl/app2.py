#!/usr/bin/python
# coding: utf-8
# from gevent import monkey
# monkey.patch_all()
import logging
import logging.config
import sys
import os
import pymysql
import json
import multiprocessing
from multiprocessing import Process, cpu_count, Queue
import traceback
import time
import argparse
import json
from kafka import KafkaProducer



sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from task import Task
from kombu import Connection
from functools import partial
from setting import AppSpiderSetting as Setting
from utils.rmq import RMQConProdWorker
from utils.logging_conf import get_logging_conf
import pandas as pd


reload(sys)
sys.setdefaultencoding('utf-8')

LOG = logging.getLogger(__name__)


def init_logging(path):
    try:
        conf = get_logging_conf(path)
        logging.config.dictConfig(conf)
    except Exception as ex:
        print traceback.format_exc()





def run_spider_work():
    from gevent import monkey
    monkey.patch_all()
    init_logging(os.path.join(Setting.LOG_DIR, 'spider'))
    task = Task()
    conn = Connection(Setting.RMQ_URL)
    rmq = RMQConProdWorker(conn, Setting.RMQ_QUEUE, task.handle_task)
    rmq.run()


def run_spider():
    try:
        init_logging(os.path.join(Setting.LOG_DIR, 'spider'))
        process_list = []
        for i in range(Setting.CONCURRENCY_CNT):
            p = Process(target=run_spider_work, args=())
            process_list.append(p)
            p.start()
        for p in process_list:
            p.join()
    except Exception as ex:
        print traceback.format_exc()


def worker(queue):
    # import multiprocessing.Queue.Empty
    from spiders import XiaoMiSpider, HuaWeiSpider, VIVOSpider, WanDouJiaSpider, BaiDuSpider, QiHooSpider, \
        YingYongBaoSpider, OPPOSpider, Spider
    import Queue
    logging.basicConfig(
        level=logging.INFO,
        format=
        '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S')
    #print os.getpid(), "working"
    # db = pymysql.connect(host='10.251.23.11',user='root', password='123456', port=3306, db = 'antiy_q')
    # cursor = db.cursor()
    op = KafkaProducer(bootstrap_servers=["10.251.23.11:9092"])
    while True:
        try:
            new_item = queue.get(True, 5)
            item = new_item[0]
            item_ca = new_item[1]
            if item is None:
                break
            #print os.getpid(), "got", item
            time.sleep(0.1)  # simula
            # spiders = [HuaWeiSpider, XiaoMiSpider, VIVOSpider, OPPOSpider,WanDouJiaSpider,BaiDuSpider,QiHooSpider,YingYongBaoSpider]
            # spiders = [OPPOSpider]
            spiders = [HuaWeiSpider, OPPOSpider]
            # spiders = [WanDouJiaSpider,BaiDuSpider,QiHooSpider,YingYongBaoSpider]
            # db = pymysql.connect(host='10.251.23.11', user='root', password='123456', port=3306, db='antiy_q')
            # cursor = db.cursor()
            for spider_cls in spiders:
                spider = spider_cls()
                print item, type(item)
                search_info = json.loads(item)
                json_item = json.loads(item_ca)
                info = spider.parse(','.join(search_info.values()),
                                    ','.join(search_info.keys()))
                #print("AAAAAAAAAAAAAAAAAAAA")
                #print(info)
                if info.__len__() == 0:
                    continue
                item5 = info[0]
                check_package = item5['check_id'].split(',')[1]
                if(item5['market'] == 'xiaomi' and item5['download_url'] == "https://app.mi.com/"):
                    item5['status'] = 404
                #if(check_package == 'com.yjqlds.clean' and item5['market'] == 'vivo'):
                   # item5['status'] = 200
                #dict = {"category":json_item['category_cn'],"device_cnt":json_item['device_cnt'],"number_of_downloads":item5['number_of_downloads']}
                ditct = {"check_package":check_package,"check_program":item5['check_id'].split(',')[0],"category":json_item['category_cn'],"category_2":json_item['category_cn2'],"device_cnt":json_item['device_cnt'],"my_developer":json_item['my_developer']}
                key_v = json.dumps(ditct).encode('utf-8')
                value = json.dumps(item5).encode('utf-8')
                op.send(topic="realtime_spider",key=key_v,value=value)
                # sql = "insert into t_yingyong_status(category,score,number_of_downloads,version,package,program,app_id,download_url,status,app_page,release_time,dt,developer,market,size,check_package,check_program,second_category,tag) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}')".format(
                #     json_item['category_cn'], json_item['device_cnt'], item5['number_of_downloads'], item5['version'],
                #     item5['package'], item5['program'], item5['app_id'], item5['download_url'], item5['status'],
                #     item5['app_page'], item5['release_time'], item5['dt'], item5['developer'], item5['market'],
                #     item5['size'], item5['check_id'].split(',')[1], item5['check_id'].split(',')[0],
                #     json_item['category_cn2'], 1)
                # cursor.execute("set names 'utf8'")
                # cursor.execute(sql.encode('utf8'))
            #     db.commit()
            #             # db.close()
        except Queue.Empty as ex:
            break


def spider_crawl_csv():
    lines = []
    # with open('keywords.csv', 'r') as f:
    #    lines = f.readlines()
    # records = map(lambda line: {'keyword': line.strip()}, lines)

    # df = pd.read_excel('/home/work/realtimeSpider/app-developer_2/app_checker_spider/qingli.xlsx')
    # df = df.loc[:, ['package', 'program', 'category_cn', 'category_cn2', 'device_cnt', 'my_developer']]
    # records = df.to_dict(orient='records')
    #
    # import multiprocessing
    # import os
    # queue = multiprocessing.Queue()
    # for record in records:
    #     new_dict_p = {}
    #     new_dict_p.update({'package': record['package']})
    #     new_dict_p.update({'program': record['program']})
    #     str1 = json.dumps(new_dict_p)
    #     new_dict_c = {}
    #     new_dict_c.update({'category_cn': record['category_cn']})
    #     new_dict_c.update({'category_cn2': record['category_cn2']})
    #     new_dict_c.update({'device_cnt': record['device_cnt']})
    #     new_dict_c.update({'my_developer': record['my_developer']})
    #
    #     str2 = json.dumps(new_dict_c)
    #     new_list = []
    #     new_list.append(str1)
    #     new_list.append(str2)
    #     queue.put(new_list)
    # the_pool = multiprocessing.Pool(
    #     processes=2, initializer=worker, initargs=(queue,))
    # the_pool.close()
    # the_pool.join()
    import multiprocessing
    import os
    queue = multiprocessing.Queue()
    import pymysql
    conn = pymysql.connect(host="10.251.23.11",port=3306,user="root",password="123456",db="antiy_q")
    sql = "select package_name as package,max(program_name) as program,max(category_cn) as category_cn,max(category_cn2) as category_cn2,'-1' as device_cnt,my_developer from t_gongju_spider_list group by package_name"
    cur = conn.cursor()
    cur.execute("set names 'utf8'")
    conn.commit()
    cur.execute(sql)
    lines = cur.fetchall()
    #print(lines.__len__())
    sum=0
    for line in lines:
        sum +=1
        if sum%1000==0:
            print("本轮中爬取数",sum)
        new_dict_p = {}
        new_dict_p.update({'package': line[0]})
        new_dict_p.update({'program': line[1]})
        str1 = json.dumps(new_dict_p)
        new_dict_c = {}
        new_dict_c.update({'category_cn': line[2]})
        new_dict_c.update({'category_cn2': line[3]})
        new_dict_c.update({'device_cnt': line[4]})
        new_dict_c.update({'my_developer': line[5]})
        str2 = json.dumps(new_dict_c)
        new_list = []
        new_list.append(str1)
        new_list.append(str2)
        queue.put(new_list)
    the_pool = multiprocessing.Pool(
        processes=10, initializer=worker, initargs=(queue,))
    the_pool.close()
    the_pool.join()


if __name__ == '__main__':
    # run_spider()
    n=0
    while(True):
        spider_crawl_csv()
        n+=1
        print("现在已经轮回数：",n)
