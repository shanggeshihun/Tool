# _*_coding:utf-8 _*_
# @Time　　 :2020/12/28/028   15:34
# @Author　 : Antipa
# @File　　 :test_selenium.py
# @Theme    :PyCharm
import requests, os, execjs, json
import base64

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
}

cookies = dict()

resp = requests.get('https://www.qimai.cn/rank', headers=headers, verify=False)
cookies.update(resp.cookies.get_dict())
synct = cookies.get('synct')

i = int(float(synct)*1000-411-1515125653845)
url = '/rank/indexPlus/brand_id/1'

fixed_url = '@#'+url+'@#'+str(i)+'@#1'

def getanaly(fixed_url):
    js_path = '/Users/xingyuzhao3/Desktop/工作/临时需求/2020/0925_qimai_spider/encpr.js'
    with open(js_path, 'r') as f:
        js_content = f.read()
        ctx = execjs.compile(js_content)
        new_pwd = ctx.call("j", fixed_url, "00000008d78d46a")
        return new_pwd


new_pwd = getanaly(fixed_url)

analysis = base64.b64encode(new_pwd.encode('utf-8')).decode()

params = {
    'analysis' : analysis
}

resp = requests.get('https://api.qimai.cn/rank/indexPlus/brand_id/1',params=params, headers=headers, verify=False)

rsp = json.loads(resp.text)