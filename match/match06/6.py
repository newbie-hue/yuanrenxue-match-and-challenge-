import subprocess
import time
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")


import requests
import execjs

chrome_headers = """
Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: no-cache
Connection: keep-alive
Cookie: Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1626325085; qpfccr=true; no-alert3=true; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1626325088; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1626325088; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1626325368
Host: match.yuanrenxue.com
Pragma: no-cache
Referer: http://match.yuanrenxue.com/match/6
User-Agent: yuanrenxue.project
X-Requested-With: XMLHttpRequest
"""



headers = {i.split(":", maxsplit=1)[0].strip(): i.split(":", maxsplit=1)[1].strip() for i in chrome_headers.split("\n") if i != ''}


def run_js_get_q( ):
    with open("6.js", "r", encoding="utf-8") as f:
        file = f.read()
    js_env = execjs.get()
    ctx = js_env.compile(file)
    result = ctx.call("make_q")
    return result

def run_js_get_encrypt():
    with open("6.js", "r", encoding="utf-8") as f:
        file = f.read()
    js_env = execjs.get()
    ctx = js_env.compile(file)
    result = ctx.call("encrypt")
    return result




numbers = []
for i in range(1, 6):
    time.sleep(1)
    url = "http://match.yuanrenxue.com/api/match/6"


    rq  = run_js_get_q()

    m = run_js_get_encrypt()

    param = {
        "page": i,
        "m":m,
        "q":rq
    }

    data = res = requests.get(url=url, headers=headers, params=param,).json()
    print(data)
    for d in data["data"]:
        numbers.append(d["value"]*8)
        numbers.append(d["value"]*15)
        numbers.append(d["value"])
print(numbers)
total = 0
for i in numbers:
    total += i
print(total)











