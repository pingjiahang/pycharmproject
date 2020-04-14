import requests
import random
import time
import hashlib
url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
content="我和你"

class   Youdao():
    def __init__(self,content):
        self.content=content
        self.url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.ts=self.get_ts()
        self.salt=self.get_salt()
        self.sign=self.get_sign()
        self.md5=self.get_md5()


    def get_salt(self):
        s=str(random.randint(0,10))
        t=self.ts
        print("random=",s)
        print("ts=",t)
        print("salt=",t+s)
        return  t+s
        #return '15848417180161'

    def get_md5(self,value):
        import hashlib
        m=hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()

    def get_sign(self):
        i=self.salt
        e=self.content
        s="fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj"
        print("s=",s,"md5=",self.md5)
        return self.md5
        #return '039b6c51c66ba62540119833ad93d999'


    def get_ts(self):
        import time
        t = time.time()
        ts = str(int(round(t * 1000)))
        return ts


   # def get_content(self):
     #   return content

    def yieid_form_date():
        form_data={
            'i':self.content,
            'from':'AUTO',
            'to':'AUTO',
            'smartresult':'dict',
            'client':'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'ts': self.ts,
            'bv':'cc652a2ad669c22da983a705e3bca726',
            'doctype':'json',
            'version':'2.1',
            'keyfrom':'fanyi.web',

            'action':'FY_BY_REALTlME',}

        return form_data

    def get_headers(self):
        headers={
                'Cookie': 'OUTFOX_SEARCH_USER_ID = -1600189075 @ 10.108.160.19',
                'Referer': 'http: // fanyi.youdao.com /',
                'User - Agent': '              8                                                                                                    Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 78.0.3904.108Safari / 537.36',
            }
        return headers

    def fanyi(self):
        response=requests.post(self.url,data=self.yield_form_date(),headers=self.get_headers())
        import json
        content=json.loads(response.text)
        return content('translateResult')[0][0]['tgt']


if __name__=='__main__':
    i=input("please input: ")
    youdao=Youdao('我们')
    print(youdao.fanyi())
    #print(get_headers())
    #ts=self.ts()
    #response=requests.post(url,data=form_data,headers=get_headers())
    #print(response.text)