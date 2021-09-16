import base64
import time
import requests

headers={
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'referer': 'https://match.yuanrenxue.com/match/4',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'yuanrenxue.project',
        'x-requested-with': 'XMLHttpRequest',
        "cookie": "Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1630897441; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1630745561,1630919351,1630924187,1630977211; m=a2dd2415dc3c4d51d29c1caa1338b9b9; RM4hZBv0dDon443M=UVAnlt2EKL4ltc5zCeaZXKb8xL+Wbd8bgceFBol2af2P9ymn5D4MwEQJ6a3ck0PRs4eRjNCl28RMiC1/ugG2aQqs5HoSYKgOA+QUYUOOq9wwRB9xM5SVXdWMwClJxB+elVucrqFUPRfra6b9CqPBX8tgIEWDOJUmhQ5cZm5QjwspVG9Fn6vg2cqKvHGfrIjbId3FsD4Cuy+Ae/spyQV+8apqvkIOl7HE/vxTF5ouktI=; no-alert3=true; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1630747081,1630924205,1630977227; tk=-6599390201333590565; sessionid=swgke8kzr60sjwru2bgt7g724z0al3x9; yuanrenxue_cookie=1630980951|Vqnu9H25YF7giI1XrIUhs3hwoezk2Hhoc06hSRfwCWkRcQtMxsa8v8VX0Ti33XYT04PrhT1QqiZXqwN90mCnYeUBuRZwofH67TYEIa6cVEPsUWsF3IBTYmficOrj; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1630997356; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1630997364"

    }




url=r"https://match.yuanrenxue.com/api/match/16?"
for i in range(1,6):
    timestamp = str(int(time.time()) * 1000)
    m = base64.b64encode(timestamp.encode())
    print(str(timestamp), str(m, "utf-8"))
    params={
        'page': str(i),
        'm': m,
        't': timestamp
    }
    res = requests.get(url=url, headers=headers, params=params)
    print(res.content.decode())
    for data in res.json()["data"]:
        sum += data["value"]
    print("第", i, "页", res.json()["data"], "sum:", sum)
print("sum", sum)