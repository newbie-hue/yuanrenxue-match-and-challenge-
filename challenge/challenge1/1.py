import base64

import  requests
import time
import hashlib
import base64


def md5(message,slat):
    key = slat + message
    #print(key)
    key_ = base64.b64encode(key.encode())
    #print(key_)
    md5 = hashlib.md5()
    md5.update(key_)
    return md5.hexdigest()

def get_data():
    session = requests.session()
    sum = 0
    for i in range(1, 86):
        timestamp = str(int(time.time()))
        session.get(url=r"https://www.python-spider.com/cityjson")
        safe =md5(timestamp,"9622")

        url = f"https://www.python-spider.com/challenge/api/json?page={i}&count=14"
        headers = {
            "accept": 'application/json, text/javascript, */*; q=0.01',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'zh-CN,zh;q=0.9',
            "cache-control": 'no-cache',
            "cookie": 'Hm_lvt_337e99a01a907a08d00bed4a1a52e35d=1630748760; vaptchaNetway=cn; no-alert=true; sessionid=gck2aujmumxzyeqpix3la4bokppdzyil; Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d=1630749125',
            "pragma": 'no-cache',
            "referer": 'https://www.python-spider.com/challenge/1',
            "safe": safe,
            "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            "sec-ch-ua-mobile": '?0',
            "sec-fetch-dest": 'empty',
            "sec-fetch-mode": 'cors',
            "sec-fetch-site": 'same-origin',
            "timestamp": timestamp,
            "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
            "x-requested-with": 'XMLHttpRequest',
        }

        res = session.get(url = url,headers=headers).json()
        print(res)
        for info in res["infos"]:
            if   "招" in info["message"]:
                sum += 1
        print("第",i,"页",res["infos"],sum)


if __name__ == '__main__':
    get_data()