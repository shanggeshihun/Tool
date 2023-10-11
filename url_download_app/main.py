# _*_coding:utf-8 _*_
# @Time　　 : 2020/1/13   1:38
# @Author　 : zimo
# @File　   :
# @Software :PyCharm
# @Theme    :

import requests,json,re
import os,time
from queue import Queue
from lxml import etree
import numpy as np
from read_write_file import ReadWriteFile

rwf=ReadWriteFile(os.path.join(os.getcwd(),'write_info.txt'))

import threading

Download_Flag=True

class DownloadApp(threading.Thread):
    def __init__(self,thread_id,download_url_queue):
        threading.Thread.__init__(self)
        self.thread_id=thread_id
        self.download_url_quque=download_url_queue
        self.download_url_quque=download_url_queue

    def run(self):
        while Download_Flag:
            download=self.download_url_quque.get()
            download_name=download.split(',')[0].strip()
            download_url=download.split(',')[1].strip()
            try:
                self.save(download_name,download_url)
            except Exception as e:
                print(download_name,download_url,e)

    def save(self,download_name,download_url):
        print('当前下载应用是：',download_name,download_url)
        try:
            res=requests.get(download_url,stream=True)
        except Exception as e:
            print(download_name,'请求失败',e)
        else:
            with open(os.path.join(os.getcwd(),'app',download_name + '.apk'),'wb') as f:
                for chunk in res.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                print(download_name,'_ready')

def main():
    download_url_queue=Queue()

    with open(os.path.join(os.getcwd(),'program_download_url.txt'), 'r',encoding='utf-8') as f:
        program_download_url=f.readlines()[1:]
        for line in program_download_url:
            download_url_queue.put(line)

    main_thread_name_list = ['main_thread_' + str(i) for i in range(1,9)]
    main_thread_list=[]
    for thread_id in main_thread_name_list:
        thread=DownloadApp(thread_id,download_url_queue)
        thread.start()
        main_thread_list.append(thread)

    while not download_url_queue.empty():
        pass
    #
    global Download_Flag
    Download_Flag=False

    for t in main_thread_list:
        t.join()

if __name__ == '__main__':
    t1=time.time()
    main()
    t2=time.time()
    print(t2-t1)