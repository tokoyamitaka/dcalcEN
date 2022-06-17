
from core.baseClass.property import 角色属性


class 技能:
    名称 = ''
    备注 = ''
    所在等级 = 0
    等级上限 = 0
    等级 = 0
    基础等级 = 0
    是否主动 = 0
    站街生效 = 0
    等级溢出 = 0

    是否启用 = 1
    技能序号 = 0
    技能表 = {}

    是否有伤害 = 0

    def 等级加成(self, x):
        if self.等级 != 0:
            if self.等级 + x > self.等级上限:
                self.等级 = self.等级上限
                if self.基础等级 != self.等级上限:
                    self.等级溢出 = 1
            else:
                self.等级 += x

    def 结算统计(self, context=None):
        return [0, 0, 0, 0]
        # 智力 体力 精神  力量  智力  物攻  魔攻 独立


class 被动技能(技能):
    是否主动 = 0
    进图加成 = 0


class 主动技能(技能):
    是否主动 = 1
    适用数值 = 0


class 觉醒技能(主动技能):
    所在等级 = 50
    等级精通 = 30
    等级上限 = 40
    基础等级 = 12
    一觉力智 = 0
    一觉力智per = 0
    # 28 原力智 941  测试修改为 939
    力智 = [
        0, 43, 57, 74, 91, 111, 131, 153, 176, 201, 228, 255, 284, 315, 346,
        379, 414, 449, 487, 526, 567, 608, 651, 696, 741, 789, 838, 888, 939,
        993, 1047, 1103, 1160, 1219, 1278, 1340, 1403, 1467, 1533, 1600, 1668
    ]

    def 结算统计(self, context, compute_3rd_awake=False):

        if not compute_3rd_awake and self.名称 in context.技能表['三次觉醒'].关联技能:
            return [0] * 4
        倍率 = (self.适用数值 / 750 + 1) * context.BUFF强化比率()
        x = (self.力智[self.等级] + self.一觉力智) * 倍率
        values = [
            0, 0,
            int(round(x * self.一觉力智per)), 0
        ]
        return values
        # 智力 体力 精神  力量  智力  物攻  魔攻 独立


class 三觉技能(主动技能):
    所在等级 = 100
    等级精通 = 30
    等级上限 = 40
    基础等级 = 2
    绑定一觉力智per = 1.08
    绑定二觉力智per = 0.23
    关联技能 = []

    def 结算统计(self, context):
        技能表 = context.技能表
        awake = 技能表['一次觉醒']
        if awake.是否启用:
            values = awake.结算统计(context, True)
            倍率 = self.加成倍率(awake.名称 in self.关联技能)
            return [int(round(i * 倍率)) for i in values]
        return [0] * 8

    def 加成倍率(self, bind_awake):
        if bind_awake:
            return round(1.08 + self.等级 * 0.01, 2)
        else:
            return round(0.23 + self.等级 * 0.01, 2)


class Buffer(角色属性):

    def BUFF强化比率(self):
        return 1


BUFF影响技能 = ['勇气祝福', '勇气圣歌', '荣誉祝福', '禁忌诅咒', '死命召唤']
