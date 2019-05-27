# python3.6

import traceback
import requests
import urllib3
urllib3.disable_warnings()
from common.utils import MyPool

s = requests.Session()


class HttpTool:
    @staticmethod
    def get(url, params=None, headers=None, retFormat='text', timeout=10, allow_redirects=True):
        res = None
        try:
            res = s.get(url, params=params, headers=headers, timeout=timeout, allow_redirects=allow_redirects, verify=False)
        except:
            traceback.print_exc()
        result = HttpTool.beforeReturn(res, retFormat)
        return (result, res.status_code) if res else (result, -1)

    @staticmethod
    def post(url, data=None, json=None, headers=None, retFormat='text', timeout=10, verify=True):
        res = None
        try:
            res = s.post(url, data=data, json=json, headers=headers, timeout=timeout, verify=verify)
        except:
            traceback.print_exc()
        return HttpTool.beforeReturn(res, retFormat)

    @staticmethod
    def beforeReturn(res, retFormat):
        assert retFormat == 'text' or retFormat == 'json' or 'raw'
        if retFormat == 'text':
            return res.text if isinstance(res, requests.Response) else ''
        elif retFormat == 'json':
            return res.json() if isinstance(res, requests.Response) and res else {}
        else:
            return res


class HttpPool(MyPool):
    def __init__(self, n=5):
        MyPool.__init__(self, n)

    def http_get(self, uid, url, callback, params=None, headers=None, retFormat='text', timeout=10, allow_redirects=True):
        req = (uid, url, callback, params, headers, retFormat, timeout, allow_redirects)
        self.put(req)

    def process(self, req, i):
        uid, url, callback, params, headers, retFormat, timeout, allow_redirects = req
        res, status_code = HttpTool.get(url, params, headers, retFormat, timeout, allow_redirects)
        callback(uid, res, status_code)