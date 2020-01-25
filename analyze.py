from macros import *
import os
import json


def get_hero_info(heroname:str, source='json'):
    if source == 'json':
        with open(os.path.join(output_dir, heroname, "{}.json".format(heroname))) as f:
            hero_data = json.load(f)
        # print(hero_data['result']['hero_img'])


if __name__ == '__main__':
    get_hero_info("axe")