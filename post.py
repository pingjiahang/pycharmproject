import requests
url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
    return '15848417180161'


def get_sign():
    return '039b6c51c66ba62540119833ad93d999'


def get_ts():
    import time
    t = time.time()
    ts = str(int(round(t * 1000)))
    return ts

form_data={
    'i':'我和你',
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt': get_salt(),
    'sign': get_sign(),
    'ts': get_ts(),
    'bv':'cc652a2ad669c22da983a705e3bca726',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_REALTlME',
}

response=requests.post(url,data=form_data)
print(response.text)