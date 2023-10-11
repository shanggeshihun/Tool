# _*_coding:utf-8 _*_
# @Time　　 :2021/5/7/007   10:08
# @Author　 : Antipa
# @File　　 :main_single_threading_7881.py
# @Theme    :PyCharm

from get_fake_useragent import UserAgent
import numpy as np
import requests,time,json,re
from get_proxy import get_proxy

ua=UserAgent()
def get_comany_id(company_name):
    proxies=get_proxy()
    url = 'https://aiqicha.baidu.com/s?q={}&t=0'.format(company_name)
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': np.random.choice(ua),
        'Cookie': 'BIDUPSID=C991F2EDAC6ED71F272C15E1C756F2AF; PSTM=1603676437; BDPPN=c9aba638f10b217d3db1050519ec6067; log_guid=9cd89223cfe28f42926af26c06a19f89; BAIDUID=33A50057BF3230D3AC8C3C142F53AE54:FG=1; BDUSS=XNiQ2VXcGduUlJaak1DeTBhZElpbS05dmpTZ2RrUVZVeWJBcTdvUE40V0JHekpnRVFBQUFBJCQAAAAAAAAAAAEAAAC~OlAjuvO72tP2vPvE41~A4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIGOCmCBjgpge; BDUSS_BFESS=XNiQ2VXcGduUlJaak1DeTBhZElpbS05dmpTZ2RrUVZVeWJBcTdvUE40V0JHekpnRVFBQUFBJCQAAAAAAAAAAAEAAAC~OlAjuvO72tP2vPvE41~A4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIGOCmCBjgpge; _j54_6ae_=xlTM-TogKuTwjdLrYW7HPR-ULR9zWvVr5Amd; MCITY=-218%3A; _j47_ka8_=57; Hm_lvt_baca6fe3dceaf818f5f835b0ae97e4cc=1615861369,1615975692,1616481348,1616485544; __yjs_duid=1_32887f07cec18ee8651affe5764947271619403128006; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=33A50057BF3230D3AC8C3C142F53AE54:FG=1; _fb537_=xlTM-TogKuTwHEnk6ldS9Ivw4oIDNJkZwoEIfx7NVJTImd; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1619745885,1620279345,1620358782,1620448913; delPer=0; PSINO=7; H_PS_PSSID=; BA_HECTOR=840l0581al2g2h20go1g9c6150r; ___rl__test__cookies=1620449595337; OUTFOX_SEARCH_USER_ID_NCOO=148579702.6024874; __yjs_st=2_NWJlZGIyNmVkZGZlMGQxMDljZDI3ZGU5ZTk2ZDIzYzVkNzJhZWRiOGM4NGZiMzJiNGE0MmNjNzAxOTA2NzZhMzUxOWNiZmEzNGQ1YTM4NmFhZGY0MmUwYzE0YzFhNzYwM2RhMDNjMGIyNGVlYzZlMmE3YzcyMzEzNzkxNGExOTQ3MTg5ZWRlNDY2YTM1NjAzY2NkM2FhZTYwYTMxYzVjMTMwNjkxM2Q1ZDg2MzA3YmY4NTgwYWZiNDQ4OTUwZDliOTU0MTVjNWExZjhlZDA3NjEzOTgyN2IwNjJiYTRiOTA4NmQ3MWYyZDExY2M4Mzg1OGU4N2RjOTRkMDc4MGJmY183Xzc0ZTUxNjQ3; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1620449612; ab_sr=1.0.0_OWQzZjIxMjgyNjg1YmVhZjNlMGJhZDZiZTQwNDVkOTJmYzA1NGNmYjI5YTUzYzliYzI4MTc5ZTBiYTg2MjY1ODhkZDM3YjZjM2MzZTUxY2ZmZTdjNzllMmEwZWMxZjVj; _s53_d91_=93c39820170a0a5e748e1ac9ecc79371df45a908d7031a5e0e6df033fcc8068df8a85a45f59cb9faa0f164dd33ed0c726bd31357aa0c35d6bedaf99f8f29964c42f87e84287d217a10716923511e9bc30742b300c5b9c229026e537cf1d3954bdf32049361ca518f5a0ec3b01c9ee1fe8ba0193aad39eada2542fce3dbde3b9457c158480c362b40642e79b9c63fd7b30a7bab2c0fae93897851ca85cf702b90220963306f2e0d4de331b5121627b0ba5ae68a5054708522241c0fa225df49efdbbab82282f0a8f7ba6bef61f14cd652; _y18_s21_=a95daaf7'
    }
    try_times=3
    flag=True
    while try_times>0:
        time.sleep(1.5)
        res = requests.get(url, headers=headers,proxies={'http':proxies},timeout=(5,7))
        res.encoding='utf-8'
        # print(res.text)
        status=res.status_code
        if status!=200:
            print('{}获取id，网络连接失败'.format(company_name))
            flag=False
        else:
            try:
                r = re.findall(r'"result":(.*?)};', res.text)[0]
            except Exception as e:
                print('{}获取id，'.format(company_name),e)
                flag = False
                time.sleep(5)
            else:
                r_to_json = json.loads(r)
                resultList = r_to_json['resultList']
                resultList0 = resultList[0]
                pid = resultList0['pid']
                flag = True
        if flag==True:
            return company_name,pid
        else:
            try_times=try_times-1
    return flag


def get_company_info_by_id(id):
    ua=UserAgent()
    url='https://aiqicha.baidu.com/detail/basicAllDataAjax?pid={}'.format(id)
    headers={
        'User-Agent':np.random.choice(ua),
        'Cookie': 'BIDUPSID=C991F2EDAC6ED71F272C15E1C756F2AF; PSTM=1603676437; BDPPN=c9aba638f10b217d3db1050519ec6067; log_guid=9cd89223cfe28f42926af26c06a19f89; BAIDUID=33A50057BF3230D3AC8C3C142F53AE54:FG=1; BDUSS=XNiQ2VXcGduUlJaak1DeTBhZElpbS05dmpTZ2RrUVZVeWJBcTdvUE40V0JHekpnRVFBQUFBJCQAAAAAAAAAAAEAAAC~OlAjuvO72tP2vPvE41~A4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIGOCmCBjgpge; BDUSS_BFESS=XNiQ2VXcGduUlJaak1DeTBhZElpbS05dmpTZ2RrUVZVeWJBcTdvUE40V0JHekpnRVFBQUFBJCQAAAAAAAAAAAEAAAC~OlAjuvO72tP2vPvE41~A4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIGOCmCBjgpge; _j54_6ae_=xlTM-TogKuTwjdLrYW7HPR-ULR9zWvVr5Amd; MCITY=-218%3A; _j47_ka8_=57; Hm_lvt_baca6fe3dceaf818f5f835b0ae97e4cc=1615861369,1615975692,1616481348,1616485544; __yjs_duid=1_32887f07cec18ee8651affe5764947271619403128006; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=33A50057BF3230D3AC8C3C142F53AE54:FG=1; _fb537_=xlTM-TogKuTwHEnk6ldS9Ivw4oIDNJkZwoEIfx7NVJTImd; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1619745885,1620279345,1620358782,1620448913; delPer=0; PSINO=7; H_PS_PSSID=; BA_HECTOR=840l0581al2g2h20go1g9c6150r; ___rl__test__cookies=1620449595337; OUTFOX_SEARCH_USER_ID_NCOO=148579702.6024874; __yjs_st=2_NWJlZGIyNmVkZGZlMGQxMDljZDI3ZGU5ZTk2ZDIzYzVkNzJhZWRiOGM4NGZiMzJiNGE0MmNjNzAxOTA2NzZhMzUxOWNiZmEzNGQ1YTM4NmFhZGY0MmUwYzE0YzFhNzYwM2RhMDNjMGIyNGVlYzZlMmE3YzcyMzEzNzkxNGExOTQ3MTg5ZWRlNDY2YTM1NjAzY2NkM2FhZTYwYTMxYzVjMTMwNjkxM2Q1ZDg2MzA3YmY4NTgwYWZiNDQ4OTUwZDliOTU0MTVjNWExZjhlZDA3NjEzOTgyN2IwNjJiYTRiOTA4NmQ3MWYyZDExY2M4Mzg1OGU4N2RjOTRkMDc4MGJmY183Xzc0ZTUxNjQ3; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1620449612; ab_sr=1.0.0_OWQzZjIxMjgyNjg1YmVhZjNlMGJhZDZiZTQwNDVkOTJmYzA1NGNmYjI5YTUzYzliYzI4MTc5ZTBiYTg2MjY1ODhkZDM3YjZjM2MzZTUxY2ZmZTdjNzllMmEwZWMxZjVj; _s53_d91_=93c39820170a0a5e748e1ac9ecc79371df45a908d7031a5e0e6df033fcc8068df8a85a45f59cb9faa0f164dd33ed0c726bd31357aa0c35d6bedaf99f8f29964c42f87e84287d217a10716923511e9bc30742b300c5b9c229026e537cf1d3954bdf32049361ca518f5a0ec3b01c9ee1fe8ba0193aad39eada2542fce3dbde3b9457c158480c362b40642e79b9c63fd7b30a7bab2c0fae93897851ca85cf702b90220963306f2e0d4de331b5121627b0ba5ae68a5054708522241c0fa225df49efdbbab82282f0a8f7ba6bef61f14cd652; _y18_s21_=a95daaf7'
    }
    ## np.random.choice(ua)
    res=requests.get(url,headers=headers)
    print(res.text)
    res_to_json=json.loads(res.text)
    status=res_to_json['status']
    if status!=0:
        return False
    res = requests.get(url, headers=headers)
    res_to_json = json.loads(res.text)
    status = res_to_json['status']
    data = res_to_json['data']
    basicData = data['basicData']

    entName = basicData['entName']
    email = basicData['email']
    website = basicData['website']
    regAddr = basicData['regAddr']
    return entName, email, website, regAddr


if __name__ == '__main__':
    with open(r'E:\工作文档\antiy\NOTE\Python\Tool\from_aiqicha_get_info\company.txt','r',encoding='utf-8') as f:
        company_name_list=[c.strip() for c in f.readlines()]
    for t in company_name_list:
        print('\n--------------------------------------------------------------------------------')
        print('开始爬取',t,'企业信息')
        result_id=get_comany_id(t)
        if not result_id:
            continue
        else:
            company_name, pid=result_id
            try:
                result=get_company_info_by_id(pid)
            except Exception as e:
                print(company_name,'获取id成功，获取详情失败:',e)
            else:
                info=(company_name,)+result
                print(info)
            time.sleep(2)