import requests
from lxml import etree

def get_ip():
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    }
    ip_lists = []
    for j in range(1, 11):
        url = r'https://www.kuaidaili.com/ops/proxylist/{}'.format(j)
        print(url)
        source = requests.get(url=url, headers=headers)
        html = etree.HTML(source.content)
        for i in range(1, 11):
            ipa = html.xpath(f'//*[@id="freelist"]/table/tbody/tr[{i}]/td[1]/text()')[0]
            port = html.xpath(f'//*[@id="freelist"]/table/tbody/tr[{i}]/td[2]/text()')[0]
            ip = ipa + ":" + port
            ip_lists.append(ip)
        print(ip_lists)
    return ip_lists



def check_ip(ip_lists):
    cheecked_ip_lists = []
    for ip in ip_lists:
        proxies = {
            'HTTPS': ip,
            'HTTP': ip
        }
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
        }
        try:
            res = requests.get(url="https://www.baidu.com/", headers=headers, proxies=proxies)
            if res.status_code == 200:
                print(len(ip_lists), ip_lists.index(ip), "检测通过", ip)
                cheecked_ip_lists.append(proxies)
            else:
                print(len(ip_lists), ip_lists.index(ip), "检测失败", ip)
        except:
            pass
    print(cheecked_ip_lists)
    return cheecked_ip_lists




def get_data(cheecked_ip_lists = None):



    sum = 0
    raw_headers = '''
    accept: application/json, text/javascript, */*; q=0.01
    accept-encoding: gzip, deflate, br
    accept-language: zh-CN,zh;q=0.9
    cache-control: no-cache
    content-length: 6
    content-type: application/x-www-form-urlencoded; charset=UTF-8
    cookie: Hm_lvt_337e99a01a907a08d00bed4a1a52e35d=1633491399; no-alert=true; vaptchaNetway=cn; sessionid=6m76nurbvdgm1obkekntcesdc3ogy6oi; Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d=1633491739
    origin: https://www.python-spider.com
    pragma: no-cache
    referer: https://www.python-spider.com/challenge/4
    sec-ch-ua: "Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"
    sec-ch-ua-mobile: ?0
    sec-ch-ua-platform: "Windows"
    sec-fetch-dest: empty
    sec-fetch-mode: cors
    sec-fetch-site: same-origin
    user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36
    x-requested-with: XMLHttpRequest
    '''
    headers = {i.split(":", maxsplit=1)[0].strip(): i.split(":", maxsplit=1)[-1].strip() for i in
               raw_headers.split("\n") if i != ""}
    print(headers)
    for i in range(1,101):
        response = requests.post(url = r"https://www.python-spider.com/api/challenge4",headers=headers,data={'page':i},proxies=cheecked_ip_lists[i-1])
        print(response.text)
        response = response.json()
        for data in response["data"]:
            value = float(data["value"].replace("\r",""))
            sum += value
        print(f"第{i}页,sum为{sum},{response}")



if __name__ == '__main__':
    ip_lists = get_ip()
    cheecked_ip_lists = check_ip(ip_lists)
    get_data(cheecked_ip_lists)


















