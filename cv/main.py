import pandas as pd
import numpy as np
def coefficient_of_variation(data):
    mean=np.mean(data) #计算平均值
    std=np.std(data,ddof=0) #计算标准差
    cv=std/mean
    return cv

if __name__ == '__main__':
    kh_pack_df=pd.read_excel(r'E:\antiy\NOTE_NEW\cv\keyhash变异系数_per_eq0.xlsx',sheet_name='kh_pack')
    kh_pron_df=pd.read_excel(r'E:\antiy\NOTE_NEW\cv\keyhash变异系数_per_eq0.xlsx',sheet_name='kh_pron')

    kh_pack=kh_pack_df.drop_duplicates(subset=['f.keyhash'],keep='first')['f.keyhash']
    kh_pron=kh_pron_df.drop_duplicates(subset=['f.keyhash'],keep='first')['f.keyhash']

    k_pack_lst,kh_pack_cv_lst=[],[]
    for k in kh_pack:
        data=kh_pack_df[kh_pack_df['f.keyhash']==k]['汇总']
        kh_pack_cv=coefficient_of_variation(data)
        k_pack_lst.append(k)
        kh_pack_cv_lst.append(kh_pack_cv)
    kh_pack_cv_df=pd.DataFrame({'k_pack_lst':k_pack_lst,'kh_pack_cv_lst':kh_pack_cv_lst})
    kh_pack_cv_df.to_excel(r'E:\antiy\NOTE_NEW\cv\keyhash变异系数_per_eq0_kh_pack.xlsx')

    k_pron_lst,kh_pron_cv_lst=[],[]
    for k in kh_pron:
        data=kh_pron_df[kh_pron_df['f.keyhash']==k]['汇总']
        kh_pron_cv=coefficient_of_variation(data)
        k_pron_lst.append(k)
        kh_pron_cv_lst.append(kh_pron_cv)
    kh_pron_cv_df=pd.DataFrame({'k_pron_lst':k_pron_lst,'kh_pron_cv_lst':kh_pron_cv_lst})
    kh_pron_cv_df.to_excel(r'E:\antiy\NOTE_NEW\cv\keyhash变异系数_per_eq0_kh_pron.xlsx')