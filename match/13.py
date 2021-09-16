import requests
import re



headers={
    "Accept":  'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    "Accept-Encoding":  'gzip, deflate, br',
    "Accept-Language":  'zh-CN,zh;q=0.9',
    "Cache-Control":  'no-cache',
    "Connection":  'keep-alive',
    "Cookie":  'Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1630897441; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1630745561,1630919351,1630924187,1630977211; m=a2dd2415dc3c4d51d29c1caa1338b9b9; RM4hZBv0dDon443M=UVAnlt2EKL4ltc5zCeaZXKb8xL+Wbd8bgceFBol2af2P9ymn5D4MwEQJ6a3ck0PRs4eRjNCl28RMiC1/ugG2aQqs5HoSYKgOA+QUYUOOq9wwRB9xM5SVXdWMwClJxB+elVucrqFUPRfra6b9CqPBX8tgIEWDOJUmhQ5cZm5QjwspVG9Fn6vg2cqKvHGfrIjbId3FsD4Cuy+Ae/spyQV+8apqvkIOl7HE/vxTF5ouktI=; qpfccr=true; no-alert3=true; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1630747081,1630924205,1630977227; tk=-6599390201333590565; sessionid=swgke8kzr60sjwru2bgt7g724z0al3x9; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1630979996; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1630980214;yuanrenxue_cookie=1630980212|wWkLOEyOa4KMMeDkLTZzIIkT1atyUI2jM5KA1x7xfg5cR7HuZuXoXMMlj18F1lA39jcEr39jSukvNLF9goX6RPGmdDCsSLWu7OkTkq8rLJ0u6YcnwP7T8y9Z',
    "Host":  'match.yuanrenxue.com',
    "Pragma":  'no-cache',
    "Referer":  'https://match.yuanrenxue.com/match/13',
    "sec-ch-ua":  '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    "sec-ch-ua-mobile":  '?0',
    "Sec-Fetch-Dest":  'document',
    "Sec-Fetch-Mode":  'navigate',
    "Sec-Fetch-Site":  'same-origin',
    "Sec-Fetch-User":  '?1',
    "Upgrade-Insecure-Requests":  '1',
    "User-Agent":  'yuanrenxue.project'
}
res=requests.get(r"https://match.yuanrenxue.com/match/13",headers=headers)
#print(res.content.decode())
Cookie = re.findall("<script>document.cookie=(.*?)</script>",res.content.decode())[0].split(";")[0].replace("'","").replace("(","").replace(")","").replace("+","").replace("\n","")
#print("Cookie:",Cookie)
headers["Cookie"]=headers["Cookie"].split("yuanrenxue_cookie=")[0]+Cookie
sum=0
for i in range(1,6):
    res=requests.get(url=f"https://match.yuanrenxue.com/api/match/13?page={i}",headers=headers).json()
    for data in res["data"]:
        sum += data["value"]
    print("第", i, "页", res["data"], "sum:", sum)
print("sum", sum)