import requests
from PIL import Image
import re
import base64
from collections import Counter


row_headers = """
accept: application/json, text/javascript, */*; q=0.01
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: no-cache
cookie: Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1630897441,1632454454; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1632707942,1632728505,1632733631,1632790862; no-alert3=true; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1632704870,1632707945,1632733639,1632790865; tk=-6599390201333590565; yuanrenxue_cookie=1632791447|G27G1BPClf7lf62s7Ds1MjQI4J1Jg3d5CLxA0M1VbDyXB4qDBahX05woSLJyQFX0nMx5VhT0N0MPCOggEWm9CEjIvkd6d62Fipw0fKsAsk3VZbIciKChnNrGg9AIs8K3cY2GJuw8N1gPInoCfi; sessionid=p1g7ulcwzss0k8kmlmfwnjjo8cq5vcpx; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1632816801; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1632818763
pragma: no-cache
referer: https://match.yuanrenxue.com/match/8
sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"
sec-ch-ua-mobile: ?0
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: yuanrenxue.project
x-requested-with: XMLHttpRequest
"""

session = requests.Session()
session.headers = {i.split(":")[0].strip():i.split(":")[1].strip() for i in row_headers.split("\n") if i != ""}



def get_verify_img():
    url = r"https://match.yuanrenxue.com/api/match/8_verify"
    response = session.get(url)
    #print(response.content.decode())
    img_str = re.search(r"<img src=\"data:image/jpeg;base64,(.*?)\" alt=\"\">\n",response.json()["html"])[1]
    #print(img_str)
    words = re.findall(r"<p>(.*?)</p>",response.json()["html"])
    print(words)
    #['佯', '儮', '聃', '冤']
    with open("08.png","wb") as f:
        f.write(base64.b64decode(img_str.encode()))
    image = Image.open("08.png").convert("RGB")
    image.save("08.png")
    image.show()


def answer(indexes):
    img_idx_list = []
    for index in indexes:
        row = (index + 2) // 3
        col = index % 3
        if col == 0:
            col = 3
        img_idx_list.append(str(col + (col - 1) * 10 + (row - 1) * 300))
    answer = '|'.join(img_idx_list) + '|'
    return answer

def main():
    numbers_list = []
    for i in range(1,6):
        get_verify_img()
        indexes = map(int, input('请输入依次序号，空格隔开，序号从1开始，从左到右，从上到下').split(' '))
        answer_ = answer(indexes)
        url = r"http://match.yuanrenxue.com/api/match/8?"
        param = {
            'page':i,
            'answer':answer_
        }

        res = session.get(url,params=param).json()
        print("第",i , "页",res["data"])
        for data in res["data"]:
            numbers_list.append(data["value"])

    max_count = Counter(numbers_list).most_common(1)
    print(max_count)

main()



























