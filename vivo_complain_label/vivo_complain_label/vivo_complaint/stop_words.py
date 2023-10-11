# _*_coding:utf-8 _*_
# @Time     :2020/10/13 0013   上午 12:06
# @Author   : Antipa
# @File     :stop_words.py
# @Theme    :PyCharm
import os
english_path=os.path.join(os.getcwd(),'stop_words','EN_stopwords.txt')
chinese_path=os.path.join(os.getcwd(),'stop_words','NLPIR_stopwords.txt')

class StopWords():
    def __init__(self):
        pass
    def get_english_stopwords(self):
        with open(english_path,'r',encoding='utf-8') as f:
            return [l.strip() for l in f.readlines()]

    def get_chinese_stopwords(self):
        with open(chinese_path,'r',encoding='utf-8') as f:
            return [l.strip() for l in f.readlines()]

if __name__ == '__main__':
    sw=StopWords()
    print(sw.get_chinese_stopwords())

