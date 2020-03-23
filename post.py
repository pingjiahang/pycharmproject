import requests
url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
form_data={
    'i':'我和你',
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':'15848417180161',
    'sign':'039b6c51c66ba62540119833ad93d999',
    'ts':'1584841718016',
    'bv':'cc652a2ad669c22da983a705e3bca726',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_REALTlME',
}

response=requests.post(url,form_data)
print(response.text)