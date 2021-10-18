import requests
import re

session = requests.session()
url = r"https://www.python-spider.com/api/challenge6"
session.headers = {
        "accept": 'application/json, text/javascript, */*; q=0.01',
        "accept-encoding": 'gzip, deflate, br',
        "accept-language": 'zh-CN,zh;q=0.9',
        "cache-control": 'no-cache',
        "content-length": '6',
        "content-type": 'application/x-www-form-urlencoded; charset=UTF-8',
        "origin": 'https://www.python-spider.com',
        "pragma": 'no-cache',
        "referer": 'https://www.python-spider.com/challenge/6',
        "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        "cookie": 'Hm_lvt_337e99a01a907a08d00bed4a1a52e35d=1630894116; vaptchaNetway=cn; no-alert=true; sessionid=1r2ar36clh30ztpfhvrmwb187xbian4x; Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d=1630918244; sign=cdxlrqmnou',
        "sec-ch-ua-mobile": '?0',
        "sec-fetch-dest": 'empty',
        "sec-fetch-mode": 'cors',
        "sec-fetch-site": 'same-origin',
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        "x-requested-with": 'XMLHttpRequest'
    }
sum = 0
for i in range(1,101):
    data = {
        'page': str(i)
    }
    res = session.post(url = url,json=data)
    session.headers["cookie"] = session.headers["cookie"].split("sign=")[0] + res.headers["set-cookie"].split(";")[0]
    #print(session.headers["cookie"])
    session.post(r"https://www.python-spider.com/challenge/api/check",json={'anw': 5411200,'id': 6})
    res=res.json()
    for data in res["data"]:
        sum+=int(data["value"].replace("\r",""))
    print("第", i, "页", res["data"],sum)
print("sum:",sum)
