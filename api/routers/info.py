import json
from typing import List, Tuple

import core.set as set
from core.basic.equipment import get_equ
from fastapi import APIRouter, Body, Depends
from pydantic import BaseModel
from utils.apiTools import Return, response

from .response import characterInfo, equipmentInfo
from .token import AlterState, authorize, createToken

infoRouter = APIRouter()


class adventureinfo(BaseModel):
    name: str
    alters: List[str]
class notice(BaseModel):
    time: str
    info: str


class characterSkillInfo(BaseModel):
    # 技能信息
    skillInfo: dict
    # 个性化设置，技能选项等
    individuation: dict
    # 护石及符文信息
    # 药剂等相关信息设置

@infoRouter.get('/adventure')
async def get_adventure_info():
    adventure_info = {}
    with open("./dataFiles/adventure-info.json", encoding='utf-8') as fp:
        adventure_info = json.load(fp)
    return response(data=adventure_info)

@infoRouter.get('/monster')
async def get_monster_info():
    monster = []
    from core.basic.monster import data
    for i in data.keys():
        monster.append(data[i])
    return response(data=data)

@infoRouter.get('/character')
async def get_character_info(state: AlterState = Depends(authorize)):
    return response(data=characterInfo.get_character_info(state.alter))


@infoRouter.get('/equips')
async def get_equipment(state: AlterState = Depends(authorize)):
    return response(data=equipmentInfo.get_equipment_info(state.alter))


@infoRouter.get('/equip/{equID}')
async def get_equipment_detail_info(equID):
    return response(data=equipmentInfo.get_equipment_detail_info(equID))


@infoRouter.get('/token/{alter}', response_model=Return[str])
async def getToken(alter: str, version: str = None):
    if version is not None and version != 'default' and version != '':
        alter = version + '.' + alter
    token = createToken(alter)
    return response(data=token)


@infoRouter.get("/triggers")
async def get_triggers(state: AlterState = Depends(authorize)):
    return response(data=get_equ().get_chose_set(alter = state.alter))


@infoRouter.get("/entries")
async def get_entry_info():
    return response(data=get_equ().entry_info)


@infoRouter.get("/config/{name}")
async def get_config(name, state: AlterState = Depends(authorize)):
    return response(data=set.get(state.origin, name))


@infoRouter.get("/configs")
async def get_config_list(state: AlterState = Depends(authorize)):
    return response(data=set.get_set_list(state.origin))


@infoRouter.get("/global/detail")
async def get_global():
    return response(data=set.get_global())


@infoRouter.post("/global/save")
async def get_global(setInfo=Body(None)):
    return response(data=set.set_global(setInfo))
