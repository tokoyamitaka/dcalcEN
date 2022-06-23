from typing import Union

from core.baseClass.skill import 主动技能, 技能, 被动技能


class 角色属性:

    def 基础属性加成(self,
               物理攻击力=0.00, 魔法攻击力=0.00, 独立攻击力=0.00, 三攻=0.00,
               力量=0.00, 智力=0.00, 力智=0.00, 体力=0.00, 精神=0.00, 体精=0.00, 四维=0.00,
               物理暴击率=0.00, 魔法暴击率=0.00, 暴击率=0.00,
               攻击速度=0.00, 施放速度=0.00, 移动速度=0.00,   三速=0.00, **kwargs):
        pass

    def 属性强化加成(self, 所有属性强化=0.00, 冰属性强化=0.00, 火属性强化=0.00, 暗属性强化=0.00, 光属性强化=0.00):
        pass

    # region 其它函数
    #     def get_skill_by_name(self, name) -> 技能 | 主动技能 | 被动技能:
    def get_skill_by_name(self, name) -> Union[技能, 主动技能, 被动技能]:
        pass
