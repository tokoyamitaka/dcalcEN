import importlib
import json
import os
from math import fabs
from core.basic.equipment import refresh_equ

from core.basic.character import Character, createCharcter
from core.basic.equipment import get_equ
from core.equipment.emblems import get_emblems_setinfo
from core.equipment.enchanting import get_enchanting_setinfo
from core.store import store


def save(alter: str, setName: str, setInfo):
    """
    保存存档
    """
    store.set('/{}/setinfo/{}'.format(alter, setName), setInfo)
    # 创建配置文件夹
    path = './sets/{}/{}'.format(alter, setName)
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
    with open(path + "/store.json", "w", encoding='utf-8') as fp:
        json.dump(setInfo, fp, ensure_ascii=False, indent=2)
    fp.close()
    return get_set_list(alter)

# 获取存档列表


def get_set_list(alter: str):
    """
    获取存档列表
    """
    setList = []
    if not os.path.exists('./sets/{}'.format(alter)):
        os.makedirs('./sets/{}'.format(alter), exist_ok=True)
    setList = os.listdir('./sets/{}'.format(alter))
    if len(setList) == 0:
        setList.append("set")
    return setList


def get(alter: str, setName: str):
    """
    取存档
    """
    set_info = {}
    character = createCharcter(alter)
    info = character.getinfo()
    alter = alter.split(".")[-1]
    skillInfo = info['skills']
    buff = info['buff_ratio']
    skill_set = []
    equ = get_equ()
    trigger = equ.get_chose_set(mode=1, alter=alter)
    dress_set = {
        "头发": {
            "id": 0,
            "option": 0
        },
        "帽子": {
            "id": 1,
            "option": 0
        },
        "脸部": {
            "id": 2,
            "option": 0
        },
        "胸部": {
            "id": 3,
            "option": 0
        },
        "上衣": {
            "id": 4,
            "option": 0
        },
        "腰带": {
            "id": 5,
            "option": 0
        },
        "下装": {
            "id": 6,
            "option": 0
        },
        "鞋": {
            "id": 7,
            "option": 0
        },

    }
    for item in skillInfo:
        skill_set.append({
            "name": item["name"],
            "tp": 0,
            "count": 0,
            "pet": 0,
            "direct": False,
            "level": item["current_level"],
            "directNumber": 0,
            "damage": item["type"] == 1,
            "mode": item.get("mode", [])
        })
    if not os.path.exists('./sets/{}/{}/store.json'.format(alter, setName)):
        forge_set = {}
        enchantings = get_enchanting_setinfo(character)
        enblems = get_emblems_setinfo(character)
        for 部位 in equ.parts:
            ens = [i for i in enchantings if 部位 in i['position']]
            enchanting = ens[0] if len(ens) > 0 else {}

            ems = [i for i in enblems if 部位 in i['position']]
            emblem = ems[0] if len(ems) > 0 else {}
            forge_set[部位] = {
                'cursed_number': 0 if 部位 in ['称号', '宠物'] else 12,
                'enchanting': enchanting.get('id', 0),
                'socket_left': emblem.get('id', 0),
                'socket_right': emblem.get('id', 0),
                'growth_first': 0 if 部位 in ['称号', '宠物'] else 40,
                'growth_second': 0 if 部位 in ['称号', '宠物'] else 40,
                'growth_third': 0 if 部位 in ['称号', '宠物'] else 40,
                'growth_fourth': 0 if 部位 in ['称号', '宠物'] else 40,
            }
            pass
        set_info = {
            "skill_set": skill_set,
            "skill_que": [],
            "forge_set": forge_set,
            "clothes_set": {},
            "single_set": [],
            "equip_list": [],
            "lv110_list": [],
            "fusion_list": [],
            "weapons_list": [],
            "myths_list": [],
            "wisdom_list": [],
            "trigger_set": trigger,
            "talisman_set": ['']*3,
            "rune_set": ['']*9,
            "buff_ratio": round((buff-1)*100, 1),
            "hotkey_set": ['']*14,
            "carry_type": info["carry_type_list"][0], "dress_set": dress_set, "monster": 0}

    else:
        with open('./sets/{}/{}/store.json'.format(alter, setName), "r", encoding='utf-8') as fp:
            set_info = json.load(fp)
        fp.close()
        cur_skills_set = list(map(lambda x: x['name'], set_info['skill_set']))
        ac_skills = list(map(lambda x: x['name'], skillInfo))
        # for skill in set_info['skill_set']:
        #     cur_skills_set.append(skill['name'])
        for skill in ac_skills:
            if skill not in cur_skills_set:
                set_info['skill_set'].append(list(
                    filter(lambda x: x['name'] == skill, skill_set))[0])
        set_info['skill_que'] = list(
            filter(lambda x: x['name'] in ac_skills, set_info['skill_que']))
        # for index in range(0, len(set_info['skill_que'])):
        #     skill = set_info['skill_que'][index]
        #     if skill['name'] not in ac_skills:
        #         set_info['skill_set'].remove(index)
        # for item in set_info['skill_que']:

        for key in trigger.keys():
            if set_info['trigger_set'].get(str(key), None) == None:
                set_info['trigger_set'][str(key)] = trigger[key]
        # print(trigger)
        # if not len(trigger) == len(set_info['trigger_set']):
        #     set_info['trigger_set'] = trigger

    return set_info


def get_global():
    info = []
    with open("./dataFiles/set-info.json", encoding='utf-8') as fp:
        info = json.load(fp)
    detail = [0] * len(info)
    with open('./sets/global.json', encoding='utf-8') as fp:
        detail = json.load(fp)
    # store.set('/global', detail)
    return {"info": info, "detail": detail}


def set_global(setInfo):
    with open('./sets/global.json', "w", encoding='utf-8') as fp:
        json.dump(setInfo, fp, ensure_ascii=False, indent=2)
    from core.basic.equipment import refresh_equ
    refresh_equ()
    return setInfo
    # store.set('/global', setInfo)
