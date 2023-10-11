# 导入扩展库
import re # 正则表达式库
import collections # 词频统计库
import numpy as np # numpy数据处理库
import jieba # 结巴分词
import pandas as pd
# 读取文件
source_name='sample.csv'
file_path=os.path.join(sys.path[0],source_name)
df=pd.read_csv(file_path)

object_list = []
remove_words = [u'的', u'，',u'和', u'是', u'随着', u'对于', u'对',u'等',u'能',u'都',u'。',u' ',u'、',u'中',u'在',u'了',
                u'通常',u'如果',u'我们',u'需要'] # 自定义去除词库

for idx,item in df.iterrows():
    try:
        pn=item['m.program_name']
        # 文本预处理
        pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')  # 定义正则表达式匹配模式
        pn = re.sub(pattern, '',pn)  # 将符合模式的字符去除
        # 文本分词
        seg_list_exact = jieba.cut(pn, cut_all = False) # 精确模式分词

        for word in seg_list_exact: # 循环读出每个分词
            if word not in remove_words: # 如果不在去除词库中
                object_list.append(word) # 分词追加到列表
    except Exception as e:
        continue

# 词频统计
word_counts = collections.Counter(object_list) # 对分词做词频统计
word_counts_top10 = word_counts.most_common(10) # 获取前10最高频的词
print (word_counts_top10) # 输出检查
df=pd.DataFrame()
for item in word_counts.items():
    df=df.append([item])
df.columns=['keyword','sample_hash_cnt']
target_file_name='program_name_freq.xlsx'
df.to_excel(os.path.join(sys.path[0],target_file_name))