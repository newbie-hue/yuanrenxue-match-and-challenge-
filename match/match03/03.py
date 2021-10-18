import requests







def get_cookie():
    value_list = []
    for i in range(1,6):
        session_url2 = r"https://match.yuanrenxue.com/jssm"
        session = requests.Session()
        headers = {
            "Host": 'match.yuanrenxue.com',
            "Connection": 'keep-alive',
            "Content-Length": '0',
            "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            "sec-ch-ua-mobile": '?0',
            "User-Agent": 'yuanrenxue.project',
            "Accept": '*/*',
            "Origin": 'https://match.yuanrenxue.com',
            "Sec-Fetch-Site": 'same-origin',
            "Sec-Fetch-Mode": 'cors',
            "Sec-Fetch-Dest": 'empty',
            "Referer": 'https://match.yuanrenxue.com/match/3',
            "Accept-Encoding": 'gzip, deflate, br',
            "Accept-Language": 'zh-CN,zh;q=0.9',
            "Cookie": 'Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1629895807; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1629895808; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1629895808; qpfccr=true; no-alert3=true; sessionid=wfd223dx440q904rguqtf9p8w65klkmu; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1629898484',
        }
        session.headers = headers
        session.post(session_url2)
        url = f"https://match.yuanrenxue.com/api/match/3?page={i}"
        res = session.post( url = url).json()
        print(res["data"])
        for j in res["data"]:
            value_list.append(j['value'])
    return max(value_list,key = value_list.count)



if __name__ == '__main__':
    print(get_cookie())

