import random
import hashlib
import requests
import time
import json

class Youdao():
    def __init__(self,content):
        self.content=content
        self.url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.ts=self.get_ts()
        self.salt=self.get_salt()
        self.sign=self.get_sign()

    def get_salt(self):
        return self.ts + str(random.randint(0, 10))

    def get_md5(self,value):
        m = hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()

    def get_sign(self):
        s = "fanyideskweb" + self.content + self.salt + "Nw(nmmbP%A-r6U3EUn]Aj"
        return self.get_md5(s)


    def get_ts(self):
        t = time.time()
        return str(int(round(t * 1000)))

    def yield_form_data(self):
        return {
            'i': self.content,
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


    def yield_headers(self):
        return {
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-715101748@10.108.160.17; JSESSIONID=aaam7kNNEvn887axRKIfx; OUTFOX_SEARCH_USER_ID_NCOO=1372491966.423369; ___rl__test__cookies=1586496832856',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        }


    def fanyi(self):
        response = requests.post(self.url, data=self.yield_form_data(), headers=self.yield_headers())
        content=json.loads(response.text)
        return content['translateResult'][0][0]['tgt']


if __name__ == '__main__':
    while(True):
        i=input("please input : ")
        youdao=Youdao(i)
        print("fanyi result  : ",youdao.fanyi())