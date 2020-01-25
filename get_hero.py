import requests
import json
import os
import requests
import sqlite3
from dict2py import dumpDict2Py
from macros import *
header = {
    "Host": "api.maxjia.com:443",
    "Accept": "*/*",
    "Accept-Language": "zh-cn",
    "Referer": "http://api.maxjia.com",
}


def get_hero_detail(heroname:str, dump_to_py=True, dump_to_json=True, commit_to_db=False, get_img=True):
    retval = requests.get("http://api.maxjia.com/api/hero/detail/overview/?lang=zh-cn&game_type=dota2&name={}".format(heroname))
    text = retval.text
    key_vals = json.loads(text)
    try:
        os.mkdir(os.path.join(output_dir, heroname))
    except FileExistsError:
        pass
    if dump_to_py:
        dumpDict2Py(key_vals, os.path.join(output_dir, heroname, "{}.py".format(heroname)), heroname)
    if dump_to_json:
        with open(os.path.join(output_dir, heroname, "{}.json".format(heroname)), 'w+') as f:
            json.dump(key_vals, f)
    if get_img:
        res = requests.get(key_vals['result']['hero_img'])
        res.raise_for_status()
        playFile = open(os.path.join(output_dir, heroname, "{}.png".format(heroname)), 'wb')
        for chunk in res.iter_content(100000):
            playFile.write(chunk)
        playFile.close()
    if commit_to_db:
        # TODO
        pass


def get_all_heros(get_detail=True, dump_to_py=True, dump_to_json=True, commit_to_db=False, get_img=True):
    retval = requests.get(
        "http://api.maxjia.com/api/hero/stat/v3/?lang=zh-cn&game_type=dota2")
    text = retval.text.encode().decode("unicode_escape")
    key_vals = json.loads(text)
    dumpDict2Py(key_vals, "heroes.py", "heroes")
    if get_detail:
        result = key_vals['result']
        heroes = result['stat']
        heroes_count = len(heroes)
        finished_count = 0
        for hero in heroes:
            hero_name = hero['img_name']
            get_hero_detail(heroname=hero_name, dump_to_py=dump_to_py, dump_to_json=dump_to_json, commit_to_db=commit_to_db, get_img=get_img)
            finished_count += 1
            print("{}/{} finished.".format(finished_count,heroes_count))

def main():
    get_all_heros(
        get_detail=True,
        dump_to_py=True,
        dump_to_json=True,
        commit_to_db=False,
        get_img=True
    )
    # get_hero_detail("axe")


if __name__ == '__main__':
    main()