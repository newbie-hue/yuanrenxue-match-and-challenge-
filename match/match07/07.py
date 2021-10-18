import time

import requests
import base64
import xmltodict
import os
from fontTools.ttLib import TTFont
from io import BytesIO
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
user-agent: yuanrenxue.project
x-requested-with: XMLHttpReques
'''

headers = { i.split(":")[0].strip():i.split(":")[1].strip()  for i in row_headers.split("\n") if i != ""}



def standard_dict():
    font = TTFont("./07woff.woff")
    font_names = font.getGlyphNames()
    #print(font_names)  #['.notdef', 'unia143', 'unia628', 'unia657', 'unia927', 'unib236', 'unib416', 'unib893', 'unic347', 'unie123', 'unif245']

    standard_relation_dict = {}

    standard_dict_key = [2,8,4,7,3,0,1,6,9,5]
    for index,name in enumerate(font_names[1:]):
        items_on = list(font["glyf"][name].flags)  #[1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0]
        #print(items_on)

        key = standard_dict_key[index]
        standard_relation_dict[key] = items_on
    #print(standard_dict)
    """
    {2: [1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0], 4: [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0], 8: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 7: [1, 1, 1, 1, 1, 1, 1], 0: [1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0], 5: [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0], 9: [1, 0, 0, 1, 1, 0, 1, 1, 1, 1], 6: [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0], 3: [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0], 1: [1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1]}
    """
    return standard_relation_dict

def make_relation(woff):
    standard_relation_dict = standard_dict()
    font = TTFont(BytesIO(woff))
    result_dict = {}
    names = font.getGlyphNames()
    for index,name in enumerate(names[1:]):
        items_on = list(font["glyf"][name].flags)
        for key,value in standard_relation_dict.items():
            if items_on == value:
                result_dict[name[3:]] = key
    print(result_dict)
    #{'a253': 9, 'a683': 1, 'a973': 3, 'c728': 0, 'c781': 5, 'e821': 6, 'f248': 4, 'f397': 7, 'f623': 8, 'f974': 2}
    return result_dict


def main():
    name = ['极镀ギ紬荕', '爷灬霸气傀儡', '梦战苍穹', '傲世哥', 'мaη肆風聲', '一刀メ隔世', '横刀メ绝杀', 'Q不死你R死你', '魔帝殤邪', '封刀不再战', '倾城孤狼', '戎马江湖', '狂得像风', '影之哀伤', '謸氕づ独尊', '傲视狂杀', '追风之梦', '枭雄在世', '傲视之巅', '黑夜刺客', '占你心为王', '爷来取你狗命', '御风踏血', '凫矢暮城', '孤影メ残刀', '野区霸王', '噬血啸月', '风逝无迹', '帅的睡不着', '血色杀戮者', '冷视天下', '帅出新高度', '風狆瑬蒗', '灵魂禁锢', 'ヤ地狱篮枫ゞ', '溅血メ破天', '剑尊メ杀戮', '塞外う飛龍', '哥‘K纯帅', '逆風祈雨', '恣意踏江山', '望断、天涯路', '地獄惡灵', '疯狂メ孽杀', '寂月灭影', '骚年霸称帝王', '狂杀メ无赦', '死灵的哀伤', '撩妹界扛把子', '霸刀☆藐视天下', '潇洒又能打', '狂卩龙灬巅丷峰', '羁旅天涯.', '南宫沐风', '风恋绝尘', '剑下孤魂', '一蓑烟雨', '领域★倾战', '威龙丶断魂神狙', '辉煌战绩', '屎来运赚', '伱、Bu够档次', '九音引魂箫', '骨子里的傲气', '霸海断长空', '没枪也很狂', '死魂★之灵']
    name_index = 1
    name_value_list = []
    for i in range(1,6):
        #time.sleep(1)
        url  = r"https://match.yuanrenxue.com/api/match/7?page=%d" % i
        response = requests.get(url=url,headers=headers).json()
        woff = base64.b64decode(response["woff"].encode())
        result_dict = make_relation(woff)
        for data in response["data"]:
            name_value = {}
            str_value = data["value"]
            value_list = map(lambda x:result_dict[x[3:]],str_value.split(" ")[0:-1])
            value = reduce(lambda x,y:x*10+y,value_list)
            name_value[name[name_index]] = value
            name_index += 1
            name_value_list.append(name_value)

    #print(name_value_list)
    #[{'爷灬霸气傀儡': 3236}, {'梦战苍穹': 5041}, {'傲世哥': 3958}, {'мaη肆風聲': 8550}, {'一刀メ隔世': 7037}, {'横刀メ绝杀': 8898}, {'Q不死你R死你': 2190}, {'魔帝殤邪': 8400}, {'封刀不再战': 4500}, {'倾城孤狼': 7478}]
    result = sorted(name_value_list,key=lambda x:list(x.values())[0],reverse=True)
    print(result)
    print("最终结果是:",result[0])

if __name__ == '__main__':
    main()






















