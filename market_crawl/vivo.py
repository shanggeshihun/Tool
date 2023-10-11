# !/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import pymysql
import datetime
import requests
import StringIO
import pytz
import logging
import json
import redis
from spider import Spider
from item import AppItem
from user_agent import get_random_agent
LOG = logging.getLogger(__name__)


class VIVOSpider(Spider):
    search_url = u'https://search.appstore.vivo.com.cn/port/packages/?screensize=1080_1808&plateformVersion=0&apps_per_page=5&app_version=1704&nt=WIFI&plateformVersionName=null&abtest=0&pictype=webp&model=MHA-AL00&platApkVer=0&key={program}&density=3.0&session_id=1547948539292&elapsedtime=751737200&an=8.0.0&cfrom=2&target=local&cs=0&plat_key_ver=&platApkVerName=null&u=1234567890&av=26&page_index={page}&imei=864360034762768&build_number=MHA-AL00+8.0.0.374%28C00%29&sshow=110&patch_sup=1&s=2%7C3756974092'
    detail_url = u'http://info.appstore.vivo.com.cn/port/package/?pos=16&build_number=PD1415D_A_1.20.0&elapsedtime=90284021&content_complete=1&screensize=1080_1920&ct=2&density=3.0&pictype=webp&cs=0&av=22&u=150100525831344d42017604d4152351&listpos=16&an=5.1&app_version=1063&imei=860832035794309&nt=WIFI&module_id=116&id={app_id}&target=local&cfrom=150&need_comment=0&model=vivo+X6D'

    def __init__(self, *args, **kwargs):
        super(VIVOSpider, self).__init__(*args, **kwargs)
        self.name = 'vivo'

    def parse_search(self,
                     program,
                     package,
                     page=1,
                     match=0,
                     found_item=0,
                     max_match=10000,
                     max_found=10000,
                     wild_search=False):
        search_full_url = self.search_url.format(program=program, page=page)
        ret = self.request_get_with_proxy(
            url=search_full_url, headers=self.get_agent())
        ret.encoding = 'utf-8'

        apps = []
        if ret.status_code != 200:
            app = AppItem()
            app = self.set_common_field(app, 1, 1, 500)
            apps.append(app)
            return apps
        data = json.loads(ret.text)
        if not data.get('result', False) or data.get('result',
                                                     'false') == 'false':
            return apps
        max_page = data['maxPage']
        total = data['totalCount']
        LOG.info(
            u'search {} in page {},total{}'.format(program, page, max_page))
        for item in data.get('value', []):
            match = match + 1
            if (set(item.get('title_zh', '').lower()) &
                    set(program.lower())) or wild_search:
                if not package or (package and item.get('package_name',
                                                        '') == package):
                    app = self.parse_app_detail(item.get('id'))
                    found_item = found_item + 1
                    self.set_common_field(app, match, total)
                    apps.append(app)
                    if found_item >= max_found:
                        break
        # if find:
        #     return self.set_common_field(app, match, total)
        if found_item < max_found and match < max_match and page < max_page:
            LOG.info('search next page {}'.format(page))
            ret = self.parse_search(program, package, page + 1, match,
                                    found_item, max_match, max_found,
                                    wild_search)
            apps.extend(ret)
        if not apps and page == 1:
            app = AppItem()
            app = self.set_common_field(app, match, total, 404)
            apps.append(app)
        return apps

    def set_common_field(self, item, match_cnt, total_cnt, status=200):
        item['dt'] = datetime.datetime.now(
            pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
        item['market'] = self.name
        item['match'] = '{}/{}'.format(match_cnt, total_cnt)
        item['status'] = status
        return item

    def _parse(self, check_id, check_field):
        args = self.extract_input(check_id, check_field)
        apps = []
        if 'program' in check_field:
            program = args.get('program', '')
            package = args.get('package', '')
            # conn = pymysql.connect(host='10.251.23.11',user='root', password='123456', port=3306, db = 'antiy_q')
            # cur = conn.cursor()
            # sql = 'select app_id from t_yingyong_status where check_package = \'{0}\' and status = 200 and market = "vivo" limit 1'.format(package)
            # cur.execute(sql)
            # appids = cur.fetchone()
            # cur.close()
            # conn.close()
            key_redis = package + "_vivo"
            r = redis.StrictRedis(host='10.251.23.11', port=6379, db=5)
            str = r.get(key_redis)
            if str:
                j = json.loads(str)
                appids = j['app_id']
		if j['app_id'] == '' :
		  appids = None
            else:
                appids = None
            print appids
            if appids is not None:
                check_id1 = appids
                ret = self.parse_app_detail(check_id1)
                ret = self.set_common_field(ret, '1', '1', ret['status'])
                apps.append(ret)
            else:
                ret = self.parse_search(
                    program=program,
                    package=package,
                    page=1,
                    match=0,
                    found_item=0,
                    max_match=10,
                    max_found=1)
                apps = ret
        elif 'keyword' in check_field:
            program = args.get('keyword', '')
            ret = self.parse_search(
                program=program,
                package='',
                page=1,
                match=0,
                found_item=0,
                max_match=1000,
                max_found=1000,
                wild_search=True)
            apps = ret
        else:
            ret = self.parse_app_detail(check_id)
            ret = self.set_common_field(ret, '1', '1', ret['status'])
            apps.append(ret)
        return self.set_check_field(check_id, check_field, apps)

    def parse_app_detail(self, app_id):
        search_full_url = self.detail_url.format(app_id=app_id)
        ret = self.request_get_with_proxy(
            url=search_full_url, headers=self.get_agent())
        ret.encoding = 'utf-8'
        data = json.loads(ret.text)
        data = data.get('value', {})
        app = AppItem()
        app['status'] = 200
        app['market'] = self.name
        app['dt'] = datetime.datetime.now(
            pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
        if ret.status_code not in (200, 404):
            app['status'] = 500
        if not data or not data.get('package_name', ''):
            app['status'] = 404
            return app

        app['program'] = data.get('title_zh', '')
        app['package'] = data.get('package_name', '')
        app['developer'] = data.get('developer', '')
        app['score'] = data.get('score', '')
        app['icon_url'] = data.get('icon_url', '')
        app['download_url'] = data.get('download_url', '')
        app['number_of_downloads'] = data.get('download_count', '')
        app['app_id'] = data.get('id', '')
        #app['description'] = data.get('introduction', '')
        app['app_page'] = data.get('sharedUrl', '')
        app['version'] = data.get('version_name', '')
        app['release_time'] = data.get('upload_time')
        if data.get('size', ''):
            app['size'] = '{}MB'.format(round(data['size'] * 1.0 / 1024, 2))
        else:
            app['size'] = ''
        return app


if __name__ == "__main__":
    logging.basicConfig()
    vivo = VIVOSpider()
    # info = vivo.parse(check_id=u'支付宝', check_field='program')
    # print json.dumps(info, ensure_ascii=False)
    # print map(lambda x: x.check_field(), info)

    info1 = vivo.parse(check_id='2171761', check_field='app_id')
    print json.dumps(info1, ensure_ascii=False)
    print map(lambda x: x.check_field(), info1)

    info1 = vivo.parse(
        check_id=u"一键清理大师,com.yjqlds.clean", check_field='program,package')
    print json.dumps(info1, ensure_ascii=False)
    print map(lambda x: x.check_field(), info1)
    # info1 = vivo.parse(check_id=u"抖音", check_field='keyword')
    # print json.dumps(info1, ensure_ascii=False)
    # print map(lambda x: x.check_field(), info1)
