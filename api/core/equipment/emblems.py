from core.basic.property import CharacterProperty

emblems_func_list = {}

# 名望 部位 颜色 品质 属性
index = ("maxFame", "position", "type", "rarity", "props")


def emblems_25000(char: CharacterProperty = {}, text=False):
    if text:
        return (0, '', '其它', '华丽', '无徽章')


def emblems_25001(char: CharacterProperty = {}, text=False):
    if text:
        return (0, '戒指,腰带,皮肤,光环', '红色', '玲珑', '力智+35')
    char.基础属性加成(力智=35)


def emblems_25021(char: CharacterProperty = {}, text=False):
    if text:
        return (0, '戒指,腰带,皮肤,光环', '红色', '玲珑', '体精+35')
    char.基础属性加成(体精=35)


def emblems_25002(char: CharacterProperty = {}, text=False):
    if text:
        return (0, '戒指,腰带,皮肤,光环', '红色', '灿烂', '力智+25')
    char.基础属性加成(力智=25)


def emblems_25022(char: CharacterProperty = {}, text=False):
    if text:
        return (0, '戒指,腰带,皮肤,光环', '红色', '玲珑', '体精+25')
    char.基础属性加成(体精=25)


def emblems_25003(char: CharacterProperty = {}, text=False):
    if text:
        return (0, '戒指,腰带,皮肤,光环', '红色', '华丽', '力智+17')
    char.基础属性加成(力智=17)


def emblems_25023(char: CharacterProperty = {}, text=False):
    if text:
        return (0, '戒指,腰带,皮肤,光环', '红色', '玲珑', '体精+17')
    char.基础属性加成(体精=17)


def emblems_25004(char: CharacterProperty = {}, text=False):
    if text:
        return (0, '上衣,下装,戒指,腰带,皮肤,光环', '红绿', '玲珑', '力智+20 暴击+2.2%')
    char.基础属性加成(力智=20, 暴击率=0.022)


def emblems_25005(char: CharacterProperty = {}, text=False):
    if text:
        return (0, '上衣,下装,戒指,腰带,皮肤,光环', '红绿', '玲珑', '力智+15 暴击+1.5%')
    char.基础属性加成(力智=15, 暴击率=0.015)


def emblems_25006(char: CharacterProperty = {}, text=False):
    if text:
        return (0, '上衣,下装,戒指,腰带,皮肤,光环', '红绿', '玲珑', '力智+10 暴击+1.1%')
    char.基础属性加成(力智=10, 暴击率=0.011)


def emblems_25007(char: CharacterProperty = {}, text=False):
    if text:
        return (0, '头肩,项链', '黄色', '灿烂', '力智+15')
    char.基础属性加成(力智=15)


def emblems_25008(char: CharacterProperty = {}, text=False):
    if text:
        return (0, '头肩,项链', '黄色', '华丽', '力智+10')
    char.基础属性加成(力智=10)


def emblems_25027(char: CharacterProperty = {}, text=False):
    if text:
        return (0, '头肩,项链', '黄色', '灿烂', '体精+15')
    char.基础属性加成(体精=15)


def emblems_25028(char: CharacterProperty = {}, text=False):
    if text:
        return (0, '头肩,项链', '黄色', '华丽', '体精+10')
    char.基础属性加成(体精=10)


def emblems_25009(char: CharacterProperty = {}, text=False):
    if text:
        return (0, '手镯,鞋,皮肤,光环', '蓝色', '玲珑', '三攻+20')
    char.基础属性加成(三攻=20)


def emblems_25010(char: CharacterProperty = {}, text=False):
    if text:
        return (0, '手镯,鞋,皮肤,光环', '蓝色', '灿烂', '三攻+15')
    char.基础属性加成(三攻=15)


def emblems_25011(char: CharacterProperty = {}, text=False):
    if text:
        return (0, '手镯,鞋,皮肤,光环', '蓝色', '华丽', '三攻+10')
    char.基础属性加成(三攻=10)


def emblems_25012(char: CharacterProperty = {}, text=False):
    if text:
        return (0, '上衣,下装,皮肤,光环', '绿色', '灿烂', '体精+15')
    char.基础属性加成(体精=15)

def emblems_25013(char: CharacterProperty = {}, text=False):
    if text:
        return (0, '上衣,下装,皮肤,光环', '绿色', '华丽', '体精+10')
    char.基础属性加成(体精=10)

def emblems_25014(char: CharacterProperty = {}, text=False):
    if text:
        return (0, '头肩,项链,皮肤,光环', '黄色', '玲珑', '攻速+2%')
    char.攻击速度增加(0.02)

def emblems_25015(char: CharacterProperty = {}, text=False):
    if text:
        return (0, '头肩,项链,皮肤,光环', '黄色', '灿烂', '攻速+1.5%')
    char.攻击速度增加(0.015)

def emblems_25016(char: CharacterProperty = {}, text=False):
    if text:
        return (0, '头肩,项链,皮肤,光环', '黄色', '华丽', '攻速+1.1%')
    char.攻击速度增加(0.011)

# 徽章效果id范围 25001~25999
for i in range(25001, 25030):
    try:
        if i not in emblems_func_list.keys():
            emblems_func_list[i] = eval('emblems_{}'.format(i))
    except:
        pass


def get_embfunc_by_id(id):
    return emblems_func_list.get(id, emblems_25000)


def get_emblems_setinfo(char: CharacterProperty = {}):
    infolist = []
    for i in emblems_func_list.keys():
        data = {}
        data['id'] = i
        emblems = emblems_func_list[i]
        info = emblems(text=True)

        char.评分开始()
        emblems(char)
        评分 = char.评分结束()
        data['rate'] = 评分
        num = 0
        for k in index:
            value = info[num]
            if(k == 'position'):
                value = [i.strip() for i in value.split(",")]
            data[k] = value
            num += 1
        infolist.append(data)
    return infolist
