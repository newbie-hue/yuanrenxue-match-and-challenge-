# -*- coding: utf-8 -*-

import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

from functools import reduce
import execjs
import requests
import time


raw_header = """
accept: application/json, text/javascript, */*; q=0.01
accept-encoding: gzip, deflate, br
accept-language: zh
cookie: Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1633536771; tk=-6599390201333590565; sessionid=krmoml0axhi5stxa6h70qxc8ag130njo; qpfccr=true; no-alert3=true; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1633536880; mz=TW96aWxsYSxOZXRzY2FwZSw1LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkxLjAuNDQ3Mi4xMDYgU2FmYXJpLzUzNy4zNixbb2JqZWN0IE5ldHdvcmtJbmZvcm1hdGlvbl0sdHJ1ZSwsW29iamVjdCBHZW9sb2NhdGlvbl0sNCx6aCx6aCwwLFtvYmplY3QgTWVkaWFDYXBhYmlsaXRpZXNdLFtvYmplY3QgTWVkaWFTZXNzaW9uXSxbb2JqZWN0IE1pbWVUeXBlQXJyYXldLHRydWUsW29iamVjdCBQZXJtaXNzaW9uc10sV2luMzIsW29iamVjdCBQbHVnaW5BcnJheV0sR2Vja28sMjAwMzAxMDcsW29iamVjdCBVc2VyQWN0aXZhdGlvbl0sTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkxLjAuNDQ3Mi4xMDYgU2FmYXJpLzUzNy4zNixHb29nbGUgSW5jLiwsW29iamVjdCBEZXByZWNhdGVkU3RvcmFnZVF1b3RhXSxbb2JqZWN0IERlcHJlY2F0ZWRTdG9yYWdlUXVvdGFdLDgyNCwwLDAsMTUzNiwyNCw4NjQsW29iamVjdCBTY3JlZW5PcmllbnRhdGlvbl0sMjQsMTUzNixbb2JqZWN0IERPTVN0cmluZ0xpc3RdLGZ1bmN0aW9uIGFzc2lnbigpIHsgW25hdGl2ZSBjb2RlXSB9LCxtYXRjaC55dWFucmVueHVlLmNvbSxtYXRjaC55dWFucmVueHVlLmNvbSxodHRwczovL21hdGNoLnl1YW5yZW54dWUuY29tL21hdGNoLzE0LGh0dHBzOi8vbWF0Y2gueXVhbnJlbnh1ZS5jb20sL21hdGNoLzE0LCxodHRwczosZnVuY3Rpb24gcmVsb2FkKCkgeyBbbmF0aXZlIGNvZGVdIH0sZnVuY3Rpb24gcmVwbGFjZSgpIHsgW25hdGl2ZSBjb2RlXSB9LCxmdW5jdGlvbiB0b1N0cmluZygpIHsgW25hdGl2ZSBjb2RlXSB9LGZ1bmN0aW9uIHZhbHVlT2YoKSB7IFtuYXRpdmUgY29kZV0gfQ==; m=b2787d27cef431b4404097c5f2b09a4a|1633537199000|13068297592000|1; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1633537218; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1633537372
referer: https://match.yuanrenxue.com/match/16
sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"
sec-ch-ua-mobile: ?0
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: yuanrenxue.project
x-requested-with: XMLHttpRequest
"""

headers = {i.split(":", maxsplit=1)[0].strip(): i.split(":", maxsplit=1)[1].strip() for i in raw_header.split("\n") if i != ''}

def get_value():
    with open("16.js","r",encoding="utf-8") as f:
        js_code = f.read()
    res = execjs.compile(js_code).call("get_value")
    return res

data_list = []
url = r"https://match.yuanrenxue.com/api/match/16?"
session = requests.session()
for i in range(1,6):
    enc_value = get_value()
    #print(enc_value)
    param = {
        "page": str(i),
        "m":enc_value[0],
        "t":enc_value[1]
    }
    res = session.get(url,headers=headers,params=param)
    print(res.text)
    for j in res.json()["data"]:
        data_list.append(j["value"])
sum = reduce(lambda x,y:x+y,data_list)
print("sum:",sum)







