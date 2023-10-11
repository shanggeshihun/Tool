from sim import sent_sim
import pandas as pd

df=pd.read_csv(r'E:\antiy\NOTE_NEW\similarity\hive_liuan_sample_same_bjmyym.csv')

sim_list=[]
for idx,item in df.iterrows():
    m_packagename=item['i.m_packagename']
    packagename=item['i.packagename']
    try:
        sim=sent_sim(m_packagename,packagename)
    except:
        sim=0
    sim_list.append(sim)
df_addsim=df.copy()
df_addsim['sim']=sim
print(df_addsim.head(4))
df_addsim.to_csv(r'E:\antiy\NOTE_NEW\similarity\hive_liuan_sample_same_bjmyym.xlsx')