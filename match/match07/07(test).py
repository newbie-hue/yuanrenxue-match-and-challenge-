import  requests
from fontTools.ttLib import TTFont
import base64
import xmltodict
from functools import reduce


row_headers= '''
accept: application/json, text/javascript, */*; q=0.01
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: no-cache
cookie: Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1630897441,1632454454; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1632707942,1632728505,1632733631,1632790862; qpfccr=true; no-alert3=true; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1632704870,1632707945,1632733639,1632790865; tk=-6599390201333590565; sessionid=3pmfv0iyccvl9lr4pcy047itddt63o07; yuanrenxue_cookie=1632791447|G27G1BPClf7lf62s7Ds1MjQI4J1Jg3d5CLxA0M1VbDyXB4qDBahX05woSLJyQFX0nMx5VhT0N0MPCOggEWm9CEjIvkd6d62Fipw0fKsAsk3VZbIciKChnNrGg9AIs8K3cY2GJuw8N1gPInoCfi; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1632792090; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1632792092
pragma: no-cache
referer: https://match.yuanrenxue.com/match/7
sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"
sec-ch-ua-mobile: ?0
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
x-requested-with: XMLHttpReques
'''


headers = { i.split(":")[0].strip():i.split(":")[1].strip()  for i in row_headers.split("\n") if i != ""}



number_list = []


def get_value(i):
    url = r"https://match.yuanrenxue.com/api/match/7?page=%d" % i
    response = requests.get(url=url,headers=headers).json()
    woff = response["woff"]
    woff = "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"
    number_dict = handle_woff(woff)
    data = response["data"]
    handle_data(number_dict, data)

def handle_woff(woff):
    with open("07woff.woff","wb") as f:
        f.write(base64.b64decode(woff.encode()))
    TTFont("07woff.woff").saveXML("07xml.xml")
    #exit()
    with open("07xml.xml","r") as f:
        xmldict = xmltodict.parse(f.read())
    number_dict = {}
    for each in xmldict["ttFont"]["glyf"]["TTGlyph"]:
        if "uni" in each["@name"]:
            number_key = each["@name"].replace("uni", "&#x")
            print(number_key)
            print(number_dict)
            if type(each["contour"]) == list:
                pt = each["contour"][0]["pt"]
            else:
                pt = each["contour"]["pt"]

            if pt[0]["@x"] == "289":
                number_dict[number_key] = 4
            elif pt[0]["@x"] == "304" :
                    if pt[0]["@y"] == "723":
                        number_dict[number_key] = 1
                    elif pt[0]["@y"] == "714":
                        if pt[1]["@x"] == "196":
                            number_dict[number_key] = 2
                        elif pt[1]["@x"] == "169":
                            number_dict[number_key] = 8
            elif pt[0]["@x"] == "374":
                number_dict[number_key] = 5
            elif pt[0]["@x"] == "94":
                number_dict[number_key] = 0
            elif pt[0]["@x"] == "307":
                if pt[1]["@x"] == "208":
                    number_dict[number_key] = 7
                elif pt[1]["@x"] == "226":
                    number_dict[number_key] = 3
                elif pt[1]["@x"] == "181":
                    number_dict[number_key] = 6
            elif pt[0]["@x"] == "52":
                number_dict[number_key] = 9
    return number_dict


def handle_data(number_dict,data):
    for value in data:
        every_value_list = map(lambda x:number_dict[x],value.split(" "))
        every_value = reduce(lambda x,y:x*10+y,every_value_list)
        print(every_value)



if __name__ == '__main__':
    print("此方法已失效，但是比较有借鉴意义~~~")
    get_value(1)






































