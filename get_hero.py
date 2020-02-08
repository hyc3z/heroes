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
    match_ups = requests.get("http://api.maxjia.com/api/hero/match_ups/?lang=zh-cn&game_type=dota2&hero={}".format(heroname))
    text = retval.text
    match_ups_text = match_ups.text
    key_vals = json.loads(text)
    key_match_ups = json.loads(match_ups_text)
    try:
        os.mkdir(os.path.join(output_dir, heroname))
    except FileExistsError:
        pass
    if dump_to_py:
        dumpDict2Py(key_vals, os.path.join(output_dir, heroname, "{}.py".format(heroname)), heroname)
        dumpDict2Py(key_match_ups, os.path.join(output_dir, heroname, "{}_matchups.py".format(heroname)), heroname)
    if dump_to_json:
        with open(os.path.join(output_dir, heroname, "{}.json".format(heroname)), 'w+') as f:
            json.dump(key_vals, f)
        with open(os.path.join(output_dir, heroname, "{}_matchups.json".format(heroname)), 'w+') as f:
            json.dump(key_match_ups, f)
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


def get_hero_info_local(heroname:str, source='json'):
    if source == 'json':
        with open(os.path.join(output_dir, heroname, "{}.json".format(heroname))) as f:
            hero_data = json.load(f)
        return hero_data


def get_hero_matchups_data_local(heroname:str, source='json'):
    if source == 'json':
        with open(os.path.join(output_dir, heroname, "{}_matchups.json".format(heroname))) as f:
            hero_data = json.load(f)
        return hero_data

def get_hero_matchups_data_local_precise(heroname:str):
    data = get_hero_matchups_data_local(heroname)['result']
    result = {}
    for i in data:
        result[i['hero_b_info']['img_name']] = [
            i['enemy_match_count'],
            i['enemy_match_ups'],
            i['enemy_win_rate']
        ]
    result = sorted(result.items(), key=lambda x: float(x[1][1]))
    return result

def get_trans_dict():
    heroes = os.listdir(output_dir)
    hero_dict = {}
    for hero in heroes:
        info = get_hero_info_local(hero)
        name_cn = info['result']['hero_base_info']['name']
        hero_dict[name_cn] = hero
        hero_dict[hero] = name_cn
    return hero_dict


def get_heroes_icons_local():
    heroes = os.listdir(output_dir)
    hero_icon_dict = {}
    for hero in heroes:
        info = get_hero_info_local(hero)
        name_cn = info['result']['hero_base_info']['name']
        icon = os.path.join(output_dir, hero, "{}.png".format(hero))
        hero_icon_dict[name_cn] = icon
    return hero_icon_dict

def gen_heroes_aliases():
    heroes = os.listdir(output_dir)
    result = {}
    for i in heroes:
        result[i] = []
    dumpDict2Py(result, "hero_aliases.py", "hero_aliases")

def main():
    get_all_heros(
        get_detail=True,
        dump_to_py=True,
        dump_to_json=True,
        commit_to_db=False,
        get_img=True
    )
    # get_hero_detail("axe")
    # get_hero_matchups_data_local_precise('axe')
    # get_hero_winrate_opponent("axe")
    # gen_heroes_aliases()


if __name__ == '__main__':
    main()