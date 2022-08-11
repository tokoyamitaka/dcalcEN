
from core.basic.skill import 技能
from core.basic.character import Character
from core.basic.skill import 主动技能, 被动技能

class classChange(Character):
    def __init__(self):
        self.实际名称 = 'soul_bender'
        self.名称 = '极诣·鬼泣'
        self.角色 = '鬼剑士(男)'
        self.类型 = '输出'
        self.职业 = '鬼泣'
        self.武器选项 = ['太刀', '短剑']
        self.输出类型选项 = ['魔法百分比']
        self.防具精通属性 = ['智力']
        self.类型 = '魔法百分比'
        self.武器类型 = '短剑'
        self.防具类型 = '布甲'
        技能列表 = []
        技能序号 = {}
        i = 0
        while i >= 0:
            try:
                tem = eval('技能'+str(i)+'()')
                tem.基础等级计算()
                技能序号[tem.名称] = i
                技能列表.append(tem)
                i += 1
            except:
                i = -1
        self.技能栏 = 技能列表
        self.技能序号 = 技能序号
        self.buff = 2.16

        super().__init__()

