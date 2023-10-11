# _*_coding:utf-8 _*_
# @Time     :2020/10/24 0024   下午 8:08
# @Author   : Antipa
# @File     :resourceStr_classify.py
# @Theme    :PyCharm


# 开启多个线程，同时执行任务，有几个线程就执行几个任务

import threading
import time
import queue


class MyThread(threading.Thread):
    def __init__(self, func):
        threading.Thread.__init__(self)
        self.func = func

    def run(self):
        self.func()


def worker():
    while not q.empty():
        item = q.get()  # 或得任务
        print('Processing : ', item)
        time.sleep(1)


def main():
    threads = []
    for task in range(100):
        q.put(task)
    for i in range(threadNum):  # 开启三个线程
        thread = MyThread(worker)
        thread.start()
        threads.append(thread)
    while not q.empty():
        pass
    print('test1')
    for thread in threads:
        thread.join()
    print('test2')

if __name__ == '__main__':
    q = queue.Queue()
    threadNum = 3
    main()