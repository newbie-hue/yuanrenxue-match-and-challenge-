import execjs
import requests
import time


with open("5.2.js", "r", encoding="utf-8") as f:
    js_code = f.read()
count = 0
sum = 0
for i in range(1, 6):
    the_value = execjs.compile(js_code).call("get_value")
    # print(the_value)
    m_url = int(the_value[0])
    f_url = int(time.time() * 1000)
    cookie_value = "m=%s;RM4hZBv0dDon443M=%s;" % (the_value[1], the_value[2])
    #print(cookie_value)
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'cookie': cookie_value + "sessionid=oz55vi9cq1500kzev3ih45uj686zjuqc;",
        'pragma': 'no-cache',
        'referer': 'https://match.yuanrenxue.com/match/5',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'yuanrenxue.project',
        'x-requested-with': 'XMLHttpRequest'
    }

    url = f"https://match.yuanrenxue.com/api/match/5?page={i}&m={m_url}&f={f_url}"

    res = requests.get(url=url, headers=headers)
    print(res.text)
    # for j in res["data"]:
    #     sum += j["value"]
    #     count += 1
    #     print(sum, count)





