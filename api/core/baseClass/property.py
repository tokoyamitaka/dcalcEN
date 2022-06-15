from core.baseClass.skill import 技能, 主动技能, 被动技能


class 角色属性:
    __物理攻击力: float = 65
    __魔法攻击力: float = 65
    __独立攻击力: float = 1045

    __火属性强化: float = 0
    __冰属性强化: float = 0
    __暗属性强化: float = 0
    __光属性强化: float = 0

    __力量: float = 0
    __智力: float = 0
    __体力: float = 0
    __精神: float = 0
    __移动速度: float = 0
    __攻击速度: float = 0
    __施放速度: float = 0
    __物理暴击率: float = 0
    __魔法暴击率: float = 0

    def 基础属性加成(self,
               物理攻击力=0.00, 魔法攻击力=0.00, 独立攻击力=0.00, 三攻=0.00,
               力量=0.00, 智力=0.00, 力智=0.00, 体力=0.00, 精神=0.00, 体精=0.00, 四维=0.00,
               物理暴击率=0.00, 魔法暴击率=0.00, 暴击率=0.00,
               攻击速度=0.00, 施放速度=0.00, 移动速度=0.00,   三速=0.00, **kwargs):
        self.__物理攻击力 += float(物理攻击力) + float(三攻)
        self.__魔法攻击力 += float(魔法攻击力) + float(三攻)
        self.__独立攻击力 += float(独立攻击力) + float(三攻)
        self.__力量 += float(力量) + float(力智) + float(四维)
        self.__智力 += float(智力) + float(力智) + float(四维)
        self.__体力 += float(体力) + float(体精) + float(四维)
        self.__精神 += float(精神) + float(体精) + float(四维)
        self.__物理暴击率 += float(物理暴击率) + float(暴击率)
        self.__魔法暴击率 += float(魔法暴击率) + float(暴击率)
        self.__攻击速度 += float(攻击速度) + float(三速)
        self.__施放速度 += float(施放速度) + float(三速)
        self.__移动速度 += float(移动速度) + float(三速)

    def 属性强化加成(self, 所有属性强化=0.00, 冰属性强化=0.00, 火属性强化=0.00, 暗属性强化=0.00, 光属性强化=0.00):
        self.__火属性强化 += 火属性强化 + 所有属性强化
        self.__冰属性强化 += 冰属性强化 + 所有属性强化
        self.__暗属性强化 += 暗属性强化 + 所有属性强化
        self.__光属性强化 += 光属性强化 + 所有属性强化

    def get_skill_by_name(self, name):
        pass
