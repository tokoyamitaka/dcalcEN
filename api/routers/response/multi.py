
import importlib
import traceback

from uuid import uuid1
from core.basic.character import createCharcter
from core.util.minheap import MinHeap


from core.basic.character import Character
from core.store import store

from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count, freeze_support, Value, Manager, Lock
import itertools


def calc_single_rank(alter, equipList, setInfo, lock):
    # print(set, alter, setName)
    character = createCharcter(alter)
    try:
        temp = character.calc(equipList=list(equipList), info=setInfo)
    except Exception as ex:
        print(traceback.format_exc())
    # 加了锁之后CPU拉不满 要等待
    # lock.acquire()
    sval.value += 1
    # lock.release()
    return (temp.get("total_data"), equipList)


def set_global(args):
    global sval
    sval = args


def get_process():
    return


def calc_multi(state, setInfo):
    # 取每个部位
    sort = setInfo["equip_list"]
    # ["称号", "宠物", "武器", "上衣", "下装", "头肩", "腰带", "鞋", "手镯", "项链", "戒指", "辅助装备", "魔法石", "耳环"]
    sval = Value('i', 0)
    lock = Manager().Lock()
    combos = list(itertools.product(*sort))
    number = len(combos)
    batch_size = 20000
    result = []
    top_number = 100
    freeze_support()

    executor = ProcessPoolExecutor(max_workers=max(
        cpu_count()-1, 1), initializer=set_global, initargs=(sval,))
    # 1W个处理一次
    batch_numbers = int(number/batch_size)+1

    minheap = MinHeap(batch_numbers*top_number)

    for batch in range(0, batch_numbers):
        batch_combo = combos[batch_size*(batch):batch_size*(batch+1)]
        batch_heap = MinHeap(batch_size)
        result = None
        result = executor.map(calc_single_rank, [state.alter]*len(batch_combo),
                              batch_combo, [setInfo]*len(batch_combo), [lock]*len(batch_combo))
        for item in result:
            batch_heap.add(item)
        minheap.merge(MinHeap(top_number,batch_heap.getTop()[:top_number]))
    executor.shutdown()
    executor = None
    # result = None
    # result = executor.map(calc_single_rank, [alter]*number,
    #                       combos, [setInfo]*number)
    result = {
        "rank": minheap.getTop()[:top_number],
        "token": state.token,
        "id": uuid1().hex
    }
    store.set("/calc/ranks/"+result.get("id"), result)
    result["setInfo"] = setInfo
    return result
