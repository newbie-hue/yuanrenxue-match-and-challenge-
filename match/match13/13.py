import requests
import re



row_headers= '''
accept: application/json, text/javascript, */*; q=0.01
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: no-cache
cookie: Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1630897441,1632454454; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1632707942,1632728505,1632733631,1632790862; qpfccr=true; no-alert3=true; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1632704870,1632707945,1632733639,1632790865; tk=-6599390201333590565; sessionid=3pmfv0iyccvl9lr4pcy047itddt63o07; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1632791446; yuanrenxue_cookie=1632791447|G27G1BPClf7lf62s7Ds1MjQI4J1Jg3d5CLxA0M1VbDyXB4qDBahX05woSLJyQFX0nMx5VhT0N0MPCOggEWm9CEjIvkd6d62Fipw0fKsAsk3VZbIciKChnNrGg9AIs8K3cY2GJuw8N1gPInoCfi; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1632791449
pragma: no-cache
referer: https://match.yuanrenxue.com/match/13
sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"
sec-ch-ua-mobile: ?0
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: yuanrenxue.project
x-requested-with: XMLHttpRequest
'''


headers = { i.split(":")[0].strip():i.split(":")[1].strip()  for i in row_headers.split("\n") if i != ""}

res=requests.get(r"https://match.yuanrenxue.com/match/13",headers=headers)
#print(res.content.decode())
Cookie = re.findall("<script>document.cookie=(.*?)</script>",res.content.decode())[0].split(";")[0].replace("'","").replace("(","").replace(")","").replace("+","").replace("\n","")
#print("Cookie:",Cookie)
headers["cookie"]=headers["cookie"].split("yuanrenxue_cookie=")[0]+Cookie
#print(headers["Cookie"])
sum=0
for i in range(1,6):
    url = r"https://match.yuanrenxue.com/api/match/13?page=%d" % i
    print(url)
    res=requests.get(url=url,headers=headers).json()
    #print(res.text)
    for data in res["data"]:
        sum += data["value"]
    print("第", i, "页", res["data"], "sum:", sum)
print("sum", sum)













