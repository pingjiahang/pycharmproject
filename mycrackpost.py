import hashlib
import time
import random
import requests

class Youdao():
    def __init__(self):
        self.ts=self.get_ts()
        self.salt=self.get_salt()
        self.sign=self.get_sign()

    def get_url(self):
        url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        return url

    def yeild_form_data(self):
        form_data = {
            'i': self.content(),
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'ts': self.ts,
            'bv': '9ef61dc3d2f65f61d71a16bd47c6e9ee',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
        }
        return form_data

    def get_salt(self):
        s = str(random.randint(0, 10))
        t=self.get_ts()
        print("%s , %s = %s" % (s,t,t+s))
        return t + s
        # return str(self.get_ts()+random.randint(0,10))

    def get_sign(self):
        value = "fanyideskweb" + self.content() + self.salt + "Nw(nmmbP%A-r6U3EUn]Aj"
        return self.get_md5(value)

    def get_md5(self, value):
        m = hashlib.md5()
        # m.update(value)
        m.update(value.encode('utf-8'))
        return m.hexdigest()

    def get_ts(self):
        return  str(int(time.time()*1000))
        # return int(time.time()*1000)

    def content(self):
        return '我好人'

    def fanyi(self):
        response = requests.post(self.get_url(), data=self.yeild_form_data(),headers=self.get_headers())
        print(response.text)

    def get_headers(self):
        headers = {
            # 'Accept': 'application/json, text/javascript, */*; q=0.01',
            # 'Accept-Encoding': 'gzip, deflate',
            # 'Accept-Language': 'zh-CN,zh;q=0.9,mt;q=0.8',
            # 'Connection': 'keep-alive',
            # 'Content-Length': '240',
            # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-2022895048@10.168.8.76;',
            # 'Host': 'fanyi.youdao.com',
            # 'Origin': 'http://fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:51.0) Gecko/20100101 Firefox/51.0',
            # 'X-Requested-With': 'XMLHttpRequest'
        }
        return headers

if __name__ == '__main__':
    youdao=Youdao()
    youdao.fanyi()