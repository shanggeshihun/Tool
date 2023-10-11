import pandas as pd

import time
from fuzzywuzzy import fuzz

df=pd.read_csv(r'E:\antiy\NOTE_NEW\similarity\hive_liuan_sample_same_bjmyym.csv')
max_row=df.shape[0]
step=50000
lst=list(range(0,max_row,step))
if lst[-1]<max_row:
    lst.append(max_row)
elif lst[-1]>max_row:
    lst[-1]=max_row
thread_num=len(lst)-1
pair=[lst[i:i+2] for i in range(thread_num)]

df['sim']=0
def sub_df_sim(df,start_index,end_index):
    sub_df=df[start_index:end_index]
    for idx,item in sub_df.iterrows():
        sent_1=item['i.packagename'].replace('.com','')
        sent_2=item['i.m_packagename'].replace('.com','')
        try:
            sim = fuzz.partial_ratio(sent_1, sent_2)
        except:
            sim=0
        print(idx)
        df['sim'].iloc[idx] = sim

import threading
# 多线程部分
threads = []
t1=time.time()
for n in range(thread_num):
    p=pair[n]
    t=threading.Thread(target=sub_df_sim, args=(df,p[0],p[1]))
    threads.append(t)

for t in threads:
    t.start()
for t in threads:
    t.join()
print(time.time()-t1)