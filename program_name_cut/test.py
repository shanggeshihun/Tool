# 词频展示
import jieba
aa=jieba.cut('com.quanmincai.bizhong', cut_all = False)
for a in aa:
    print(a)