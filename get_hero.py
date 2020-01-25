import requests
import json
import os
from dict2py import dumpDict2Py

header = {
    "Host": "api.maxjia.com:443",
    "Accept": "*/*",
    "Accept-Language": "zh-cn",
    "Referer": "http://api.maxjia.com",
}

output_dir = 'data'


def get_hero_detail(heroname:str):
    retval = requests.get("http://api.maxjia.com/api/hero/detail/overview/?lang=zh-cn&game_type=dota2&name={}".format(heroname))
    text = retval.text
    key_vals = json.loads(text)
    dumpDict2Py(key_vals, os.path.join(output_dir,"{}.py".format(heroname)), heroname)


def get_all_heros(get_detail:bool):
    retval = requests.get(
        "http://api.maxjia.com/api/hero/stat/v3/?lang=zh-cn&game_type=dota2")
    text = retval.text.encode().decode("unicode_escape")
    key_vals = json.loads(text)
    dumpDict2Py(key_vals, "heroes.py", "heroes")
    if get_detail:
        result = key_vals['result']
        heroes = result['stat']
        for hero in heroes:
            hero_name = hero['img_name']
            get_hero_detail(heroname=hero_name)



def main():
    get_all_heros(get_detail=True)



if __name__ == '__main__':
    main()