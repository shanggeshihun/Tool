# 导入扩展库
import re # 正则表达式库
import collections # 词频统计库
import numpy as np # numpy数据处理库
import jieba # 结巴分词
import wordcloud # 词云展示库
from PIL import Image # 图像处理库
import matplotlib.pyplot as plt # 图像展示库
import pandas as pd
import os,sys
import shutil
# 读取文件
source_name='complaint.txt'
file_path=os.path.join(sys.path[0],source_name)


remove_words = [u'的', u'，',u'和', u'是', u'随着', u'对于', u'对',u'等',u'能',u'都',u'。',u' ',u'、',u'中',u'在',u'了',u'通常',u'如果',u'我们',u'需要',u'null',u'什么'] # 自定义去除词库

object_list = []
with open(file_path) as f:
    for line in f.readlines():
        seg_list_exact = jieba.cut(line, cut_all=False)  # 精确模式分词
        for word in seg_list_exact:  # 循环读出每个分词
            if word not in remove_words:  # 如果不在去除词库中
                object_list.append(word)  # 分词追加到列表

# 词频统计
word_counts = collections.Counter(object_list) # 对分词做词频统计
word_counts_top10 = word_counts.most_common(50) # 获取前10最高频的词
print (word_counts_top10) # 输出检查