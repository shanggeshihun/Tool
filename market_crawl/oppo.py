# !/usr/bin/python
#coding:utf-8
# from gevent import monkey
# monkey.patch_all()
import os
import time
import datetime
import requests
import StringIO
import pytz
import logging
import re
import json
import hashlib
import copy
import pymysql
import redis
from lxml import etree
from lxml import html
from spider import Spider
from item import AppItem
from urlparse import urlparse, parse_qs
from urllib import unquote
LOG = logging.getLogger(__name__)


class OPPOSign(object):
    def init_keys(self, str1, str2):
        v2 = map(lambda x: '', range(48))
        for i in range(16):
            v2[i] = str1[i]
        for i in range(16):
            v2[i + 16] = str2[i + 18]
            v2[i + 32] = str2[i + 2]
        return ''.join(v2)

    def ocstoolc(self, input_str):
        md5 = hashlib.md5()
        md5.update(input_str)
        return md5.hexdigest()

    def sign(self, url, timestamp):
        url = url.encode('utf-8')
        key = self.init_keys('cdb09c43063ea6bb',
                             '09bdc58acb383220be08f4fe8a43775179')
        sb = key
        sb2 = "SAMSUNG%2FGalaxy+S7+Edge%2F23%2F6.0.1%2FUNKNOWN%2F2%2FMXC89K+dev-keys%2F7902"
        uri = urlparse(url)
        sb2 = sb2 + str(timestamp) + '866329024874246///' + uri.path + unquote(
            uri.query)
        chinese_cnt = 0
        for k, v in parse_qs(uri.query).items():
            if k == 'keyword':
                for words in v:
                    words = words.decode('utf-8')
                    for word in words:
                        if word >= u'\u4e00' and word <= u'\u9fff':
                            chinese_cnt = chinese_cnt + 1
        sb = sb + sb2 + str(len(sb2) + 48 - chinese_cnt * 2)
        sb = sb + 'STORENEWMIICeAIBADANBgkqhkiG9w0BAQEFAASCAmIwggJeAgEAAoGBANYFY/UJGSzhIhpx6YM5KJ9yRHc7YeURxzb9tDvJvMfENHlnP3DtVkOIjERbpsSd76fjtZnMWY60TpGLGyrNkvuV40L15JQhHAo9yURpPQoI0eg3SLFmTEI/MUiPRCwfwYf2deqKKlsmMSysYYHX9JiGzQuWiYZaawxprSuiqDGvAgMBAAECgYEAtQ0QV00gGABISljNMy5aeDBBTSBWG2OjxJhxLRbndZM81OsMFysgC7dq+bUS6ke1YrDWgsoFhRxxTtx/2gDYciGp/c/h0Td5pGw7T9W6zo2xWI5oh1WyTnn0Xj17O9CmOk4fFDpJ6bapL+fyDy7gkEUChJ9+p66WSAlsfUhJ2TECQQD5sFWMGE2IiEuz4fIPaDrNSTHeFQQr/ZpZ7VzB2tcG7GyZRx5YORbZmX1jR7l3H4F98MgqCGs88w6FKnCpxDK3AkEA225CphAcfyiH0ShlZxEXBgIYt3V8nQuc/g2KJtiV6eeFkxmOMHbVTPGkARvt5VoPYEjwPTg43oqTDJVtlWagyQJBAOvEeJLno9aHNExvznyD4/pR4hec6qqLNgMyIYMfHCl6d3UodVvC1HO1/nMPl+4GvuRnxuoBtxj/PTe7AlUbYPMCQQDOkf4sVv58tqslO+I6JNyHy3F5RCELtuMUR6rG5x46FLqqwGQbO8ORq+m5IZHTV/Uhr4h6GXNwDQRh1EpVW0gBAkAp/v3tPI1riz6UuG0I6uf5er26yl5evPyPrjrD299L4Qy/1EIunayC7JYcSGlR01+EDYYgwUkec+QgrRC/NstV'
        return self.ocstoolc(sb)


class OPPOSpider(Spider):
    detail_url = u'https://api-cn.store.heytapmobi.com/detail/v4/{app_id}?query=1,4,7&source=1'
    search_url = u'https://api-cn.store.heytapmobi.com/search/v1/search?start={start}&tabId=&searchType=3&size={page_size}&keyword={program}'
    page_size = 10

    headers = {
        # 'sign':
        # '%{sign_key}',
        'ch':
        '2101',
        'pid':
        '001',
        'token':
        '-1',
        'locale':
        'zh-CN;CN',
        'appid':
        'SAMSUNG#001#CN',
        'nw':
        '1',
        'ocp':
        'download#3_security#0_network#0',
        'oak':
        'cdb09c43063ea6bb',
        'User-Agent':
        'SAMSUNG%2FGalaxy+S7+Edge%2F23%2F6.0.1%2FUNKNOWN%2F2%2F2101%2F7902',
        # 't':
        # '%{timestamp}',
        'appversion':
        '7.9.0',
        'id':
        '866329024874246///',
        'sg':
        '0b37c0daa7c2dc6740ef40ce5e3bc2e99494dd5e',
        'traceId':
        'CzqPgln6-1586755815173',
        'pkg-ver':
        '0',
        'romver':
        '-1',
        'ocs':
        'SAMSUNG%2FGalaxy+S7+Edge%2F23%2F6.0.1%2FUNKNOWN%2F2%2FMXC89K+dev-keys%2F7902',
        'Accept':
        'application/json; charset=UTF-8',
        'pr':
        '0'
    }

    def __init__(self, *args, **kwargs):
        super(OPPOSpider, self).__init__(*args, **kwargs)
        self.name = 'oppo'

    def parse_search(self,
                     program,
                     package,
                     start=0,
                     match=0,
                     total_match=0,
                     max_search=10,
                     found_item=0,
                     max_found=1000,
                     wild_search=False):
        search_full_url = self.search_url.format(
            program=program, start=start, page_size=self.page_size)
        ret = self.request_get_with_proxy(
            url=search_full_url, headers=self.get_headers(search_full_url))
        ret.encoding = 'utf-8'

        apps = []
        data = json.loads(ret.text)
        is_end = data.get('isEnd', 0)
        total_match = data.get('total', 0)

        if ret.status_code == 200:
            for index, item in enumerate(data.get('cards', [])):
                if item.get('app') and (wild_search or
                                        set(item['app'].get('appName', '')
                                            .lower()) & set(program.lower())):
                    match = match + 1
                    LOG.info(u"check {} with {}".format(
                        program.lower(), item.get('appName', '')))
                    if not package or (package and item['app'].get(
                            'pkgName', '') == package):
                        app_info = self.parse_app_detail(
                            item['app'].get('appId'))
                        app_info = self.set_common_field(
                            app_info, match, total_match)
                        apps.append(app_info)
                        found_item = found_item + 1
                        if found_item >= max_found:
                            break
                for app in item.get('apps', []):
                    match = match + 1
                    LOG.info(u"check {} with {}".format(
                        program.lower(), app.get('appName', '')))
                    if set(app.get('appName', '').lower()) & set(
                            program.lower()) or wild_search:
                        if not package or (package and app.get('pkgName',
                                                               '') == package):
                            app_info = self.parse_app_detail(app.get('appId'))
                            app_info = self.set_common_field(
                                app_info, match, total_match)
                            found_item = found_item + 1
                            apps.append(app_info)
                            if found_item >= max_found:
                                break
        else:
            app = AppItem()
            app = self.set_common_field(app, 1, 1, 500)
            apps.append(app)
        # if found_item > max_found or is_end or start >= max_search:
        #     return self.set_common_field(app_info, match, total_match)
        if not is_end and (start <= max_search) and found_item < max_found:
            LOG.info('search next page ')
            ret = self.parse_search(program, package, start + self.page_size,
                                    match, total_match, max_search,
                                    wild_search)
            apps.extend(ret)
        if not apps and start == 0:
            app = AppItem()
            app = self.set_common_field(app, match, total_match, 404)
            apps.append(app)
        return apps

    def _parse(self, check_id, check_field):
        args = self.extract_input(check_id, check_field)
        apps = []
        if 'program' in check_field:
            program = args.get('program', '')
            package = args.get('package', '')
            # conn = pymysql.connect(host='10.251.23.11',user='root', password='123456', port=3306, db = 'antiy_q')
            # cur = conn.cursor()
            # sql = 'select app_id from t_yingyong_status where check_package = \'{0}\' and status = 200 and market = "oppo" limit 1'.format(package)
        #     cur.execute(sql)
        #     appids = cur.fetchone()
        #     cur.close()
        #     conn.close()
	    # print appids
            r = redis.StrictRedis(host='10.251.23.11', port=6379, db=9)
	    key_redis = package + "_oppo"
            str = r.get(key_redis)
            if str:
                j = json.loads(str)
                appids = j['app_id']
                if j['app_id'] == '' :
                  appids = None
            else:
                appids = None
            if appids is not None:
                check_id1 = appids
                print appids
                ret = self.parse_app_detail(check_id1)
                ret = self.set_common_field(ret, '1', '1', ret['status'])
                apps.append(ret)
            else:
                ret = self.parse_search(
                    program=program,
                    package=package,
                    start=0,
                    match=0,
                    total_match=0,
                    max_search=10,
                    max_found=1)
                apps = ret
        elif 'keyword' in check_field:
            program = args.get('keyword', '')
            ret = self.parse_search(
                program=program,
                package='',
                start=0,
                match=0,
                total_match=0,
                max_search=10,
                found_item=0,
                max_found=1000,
                wild_search=True)
            apps = ret
        else:
            ret = self.parse_app_detail(check_id)
            ret = self.set_common_field(ret, '1', '1', ret['status'])
            apps.append(ret)
        return self.set_check_field(check_id, check_field, apps)

    def get_headers(self, url):
        time_stamp = int(round(time.time() * 1000))
        headers = copy.deepcopy(self.headers)
        headers['t'] = str(time_stamp)
        oppo = OPPOSign()
        headers['sign'] = oppo.sign(url, time_stamp)
        return headers

    def parse_app_detail(self, app_id):
        search_full_url = self.detail_url.format(app_id=app_id)
        ret = self.request_get_with_proxy(
            url=search_full_url, headers=self.get_headers(search_full_url))
        ret.encoding = 'utf-8'
        app = AppItem()
        app['status'] = 200
        app['market'] = self.name
        app['dt'] = datetime.datetime.now(
            pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
        if ret.status_code != 200:
            LOG.info(ret.text)
            app['status'] = 500
            return app
        data = json.loads(ret.text)
        if data['base']['appId'] == -404:
            app['status'] = 404
            return app
        if not data:
            return app

        app['program'] = data['base']['appName']
        app['package'] = data['base']['pkgName']
        if data['developer']:
            app['developer'] = data['developer'].get('developer', '')
            app['release_time'] = datetime.datetime.fromtimestamp(
                data['developer']['releaseTime'] /
                1000).strftime('%Y-%m-%d %H:%M:%S')
        else:
            app['developer'] = ''
            app['release_time'] = ''
        app['score'] = data['base']['grade']
        app['icon_url'] = data['base']['iconUrl']
        app['download_url'] = data['base']['url']
        app['number_of_downloads'] = data['base']['dlDesc']
        app['app_id'] = data['base']['appId']
        #app['description'] = data['base']['desc']
        app['app_page'] = ''
        app['version'] = data['base']['verName']
        app['size'] = data['base']['sizeDesc']
        app['category'] = data['base']['catName']
        if data['appTags']:
            app['classification'] = ','.join(
                map(lambda x: x['tagName'], data['appTags']))
        return app


if __name__ == "__main__":
    import sys
    # # sys.path.append(
    # #     os.path.abspath(os.path.dirname(os.path.join(os.path.dirname(__file__), os.path.pardir))))
    # # print os.path.abspath(os.path.dirname(os.path.join(os.path.dirname(__file__), os.path.pardir)))
    # sys.path.append('C:\\Users\\chengcong\\Desktop\\app_developer')
    # from utils.proxy_helper import ProxyHelper
    # logging.basicConfig(
    #     level=logging.INFO,
    #     format=
    #     '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    #     datefmt='%a, %d %b %Y %H:%M:%S')
    # proxy = ProxyHelper()
    # oppo = OPPOSpider(proxy_helper=proxy)
    # apps_info = []
    # with open('oppo.csv') as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         app_info = dict(
    #             zip(['package', 'program'], line.strip().split(',')))
    #         apps_info.append(app_info)
    # with open('oppo.output', 'w') as f:
    #     for app in apps_info:
    #         #print app
    #         fields = []
    #         fields_value = []
    #         if app.get('program'):
    #             fields.append('program')
    #             fields_value.append(app.get('program').decode('utf-8'))

    #         # if app.get('package'):
    #         #     fields.append('package')
    #         #     fields_value.append(app.get('package').decode('utf-8'))
    #         info = oppo.parse(u','.join(fields_value), ','.join(fields))
    #         f.write(json.dumps(info) + "\n")
    logging.basicConfig(
        level=logging.INFO,
        format=
        '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S')

    oppo = OPPOSpider()
    # app id直接爬取
    # a = oppo.parse('3394680', 'app_id')
    # print json.dumps(a, ensure_ascii=False)
    # print map(lambda x: x.check_field(), a)

    #多条件匹配，应用名加包名
    b = oppo.parse(u'立清,cn.fast.clean.now', 'program,package')
    print json.dumps(b, ensure_ascii=False)
    print map(lambda x: x.check_field(), b)

    # # # 应用名匹配
    # c = oppo.parse(u'抖音', 'program')
    # print json.dumps(c, ensure_ascii=False)
    # print map(lambda x: x.check_field(), c)

    # a = oppo.parse('33946801', 'app_id')
    # print json.dumps(a, ensure_ascii=False)
    # print map(lambda x: x.check_field(), a)

    # # # 应用名匹配
    # c = oppo.parse(u'抖音', 'keyword')
    # print json.dumps(c, ensure_ascii=False)
    # print map(lambda x: x.check_field(), c)
