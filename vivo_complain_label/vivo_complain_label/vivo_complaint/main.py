# 导入扩展库
import re # 正则表达式库
import collections # 词频统计库
import numpy as np # numpy数据处理库
import jieba # 结巴分词
from PIL import Image # 图像处理库
import matplotlib.pyplot as plt # 图像展示库
import pandas as pd
import os,sys
import shutil

from stop_words import StopWords
sw=StopWords()

# 读取文件
source_name='complaint.txt'
file_path=os.path.join(sys.path[0],source_name)

stop_words =sw.get_chinese_stopwords()

object_list = []
with open(file_path,encoding='utf-8') as f:
    for line in f.readlines():
        if len(line)==0:
            continue
        seg_list_exact = jieba.cut(line, cut_all=False)  # 精确模式分词
        for word in seg_list_exact:  # 循环读出每个分词
            if word not in stop_words:  # 如果不在去除词库中
                object_list.append(word)  # 分词追加到列表

# 词频统计,返回<class 'collections.Counter'> 类似字典
word_counts = collections.Counter(object_list) # 对分词做词频统计
print(type(word_counts))
print(word_counts)
# word_counts_top10 = word_counts.most_common(200) # 获取前10最高频的词
name_list=[l for l in word_counts.keys()]
c_list=[l for l in word_counts.values()]
df_result=pd.DataFrame({'name_list':name_list,'c_list':c_list})
df_result.to_excel(r'E:\antiy\NOTE_NEW\vivo_complain_label\vivo_complain_label\vivo_complaint\result.xlsx')