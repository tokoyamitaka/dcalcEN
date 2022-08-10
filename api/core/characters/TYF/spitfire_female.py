
from core.basic.skill import 技能
from core.basic.character import Character
from core.basic.skill import 主动技能, 被动技能
from typing import Dict, List, Union


class 职业主动技能(主动技能):
    技能施放时间 = 0.0
    脱手 = 1


class 技能0(被动技能):
    名称 = '单兵推进器'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    等级精通 = 10
    关联技能 = ['交叉射击', '聚合弹', '凝固汽油弹', '超真空弹：切莉']
    关联技能1 = ['爆裂弹']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + (10 + self.等级) / 100, 3)

    def 加成倍率1(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + (2 * self.等级) / 100, 3)


class 技能1(被动技能):
    名称 = '兵器研究'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    等级精通 = 10
    冷却关联技能 = ['所有']
    非冷却关联技能 = ['EMP磁暴', '决战之日', '终解·制空霸权']

    def 独立攻击力倍率(self, 武器类型):
        return (1.1 + (self.等级 - 10) * 0.02) if self.等级 >= 10 else (1 + self.等级 * 0.01)

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 - 0.01 * self.等级, 3)


class 技能2(被动技能):
    名称 = '手雷精通'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    等级精通 = 10
    关联技能 = ['G35感电手雷', 'G18冰冻手雷']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + 1.2*(0.1 * self.等级), 3)


class 技能3(被动技能):
    名称 = '弹药改良'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    等级精通 = 10
    关联技能 = ['所有']
    技能加成描述 = ''
    加成数值 = 1.0
    关联技能1 = ['所有']

    def 加成倍率(self, 武器类型):
        return 1.1

    def 加成倍率1(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1.03 + min(10, self.等级) * 0.02 + max(0, self.等级 - 10) * 0.01


class 技能4(职业主动技能):
    名称 = 'M18阔剑地雷'
    所在等级 = 20
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    data0 = [int(i*1.132*1.137)for i in [0, 700, 771, 842, 913, 984, 1055, 1126, 1197, 1268, 1340, 1411, 1482, 1553, 1624, 1695, 1766, 1837, 1908, 1979, 2050, 2121, 2192, 2263, 2334, 2406, 2477, 2548, 2619, 2690, 2761, 2832, 2903, 2974,
                                         3045, 3116, 3187, 3258, 3329, 3400, 3471, 3543, 3614, 3685, 3756, 3827, 3898, 3969, 4040, 4111, 4182, 4253, 4324, 4395, 4466, 4537, 4609, 4680, 4751, 4822, 4893, 4964, 5035, 5106, 5177, 5248, 5319, 5390, 5461, 5532, 5603]]
    hit0 = 3
    CD = 6.0
    TP成长 = 0.10
    TP基础 = 7
    TP上限 = 7

    MP = [70, 585]


class 技能5(职业主动技能):
    名称 = 'G35感电手雷'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [0, 655, 722, 788, 853, 920, 987, 1053, 1120, 1186, 1253, 1319, 1386, 1453, 1519, 1586, 1651, 1718, 1784, 1851, 1917, 1984, 2050, 2117, 2184, 2250, 2317, 2383, 2449, 2515, 2582, 2648, 2715, 2781, 2848, 2915,
             2981, 3048, 3114, 3181, 3247, 3313, 3379, 3446, 3512, 3579, 3646, 3712, 3779, 3845, 3912, 3978, 4045, 4110, 4177, 4243, 4310, 4377, 4443, 4510, 4576, 4643, 4709, 4776, 4843, 4908, 4974, 5041, 5108, 5174, 5241]
    hit0 = 1
    感电data0 = [0, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14,
               14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14,
               14, 14, 14, 14, 14, 14, 14]
    感电hit0 = 18
    感电power0 = 1
    CD = 3.0
    TP成长 = 0.10
    TP基础 = 7
    TP上限 = 7
    基础施放次数 = 3

    MP = [40, 350]

    形态 = ["70普", "70特", "特化", "普通"]

    def 形态变更(self, 形态, char):
        if 形态 == "70特":
            if char.get_skill_by_name("超真空弹：切莉").等级 > 0:
                self.power0 = 1.1
                self.感电power0 = 1.1
            if char.get_skill_by_name("手雷精通").等级 > 0:
                self.power0 *= 1.2
                self.感电power0 *= 1.2
        if 形态 == "70普":
            if char.get_skill_by_name("超真空弹：切莉").等级 > 0:
                self.power0 = 1.1
                self.感电power0 = 1.1
        if 形态 == "特化":
            if char.get_skill_by_name("手雷精通").等级 > 0:
                self.power0 = 1.2
                self.感电power0 = 1.2
        if 形态 == "普通":
            self.power0 = 1
            self.感电power0 = 1
    # def 等效CD(self, 武器类型, 输出类型):
    #     # 经过测试,手雷恢复速度无法享受技能冷却恢复加成
    #     return round(self.CD, 1)


class 技能6(职业主动技能):
    名称 = '交叉射击'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.153*1.054)for i in [0, 1329, 1463, 1598, 1733, 1868, 2003, 2138, 2272, 2407, 2542, 2677, 2812, 2947, 3081, 3216, 3351, 3486, 3621, 3756, 3890, 4025, 4160, 4295, 4430, 4565, 4699, 4834, 4969, 5104, 5239, 5374, 5508, 5643,
                                         5778, 5913, 6048, 6183, 6317, 6452, 6587, 6722, 6857, 6992, 7126, 7261, 7396, 7531, 7666, 7801, 7935, 8070, 8205, 8340, 8475, 8610, 8744, 8879, 9014, 9149, 9284, 9419, 9553, 9688, 9823, 9958, 10093, 10228, 10362, 10497, 10632]]
    hit0 = 3
    CD = 8.0
    TP成长 = 0.10
    TP基础 = 7
    TP上限 = 7

    MP = [70, 588]


class 技能7(职业主动技能):
    名称 = '爆裂弹'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10
    data0 = [int(i*1.157)for i in [0, 662, 768, 873, 978, 1084, 1189, 1294, 1400,
                                   1506, 1611, 1717, 1822, 1927, 2033, 2138, 2244, 2350, 2455, 2561, 2666]]
    hit0 = 1
    CD = 5.0
    MP = [357, 2765]


class 技能8(职业主动技能):
    名称 = 'G18冰冻手雷'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.115*1.076)for i in [0, 666, 733, 801, 869, 936, 1004, 1071, 1139, 1207, 1274, 1342, 1409, 1477, 1545, 1612, 1680, 1747, 1815, 1883, 1950, 2018, 2085, 2153, 2220, 2288, 2356, 2423, 2491, 2558, 2626, 2694, 2761,
                                         2829, 2896, 2964, 3032, 3099, 3167, 3234, 3302, 3370, 3437, 3505, 3572, 3640, 3708, 3775, 3843, 3910, 3978, 4046, 4113, 4181, 4248, 4316, 4384, 4451, 4519, 4586, 4654, 4722, 4789, 4857, 4924, 4992, 5060, 5127, 5195, 5262, 5330]]
    hit0 = 1
    基础施放次数 = 3
    CD = 4.0
    TP成长 = 0.10
    TP基础 = 7
    TP上限 = 7

    MP = [70, 560]

    形态 = ["70普", "70特", "特化", "普通"]

    def 形态变更(self, 形态, char):
        if 形态 == "70特":
            if char.get_skill_by_name("超真空弹：切莉").等级 > 0:
                self.power0 = 1.1
            if char.get_skill_by_name("手雷精通").等级 > 0:
                self.power0 *= 1.2
        if 形态 == "70普":
            if char.get_skill_by_name("超真空弹：切莉").等级 > 0:
                self.power0 = 1.1
        if 形态 == "特化":
            if char.get_skill_by_name("手雷精通").等级 > 0:
                self.power0 = 1.2
        if 形态 == "普通":
            self.power0 = 1
    # def 等效CD(self, 武器类型, 输出类型):
    #     # 经过测试,手雷恢复速度无法享受技能冷却恢复加成
    #     return round(self.CD, 1)


class 技能9(职业主动技能):
    名称 = '聚合弹'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.216*1.092)for i in [0, 8804, 9698, 10591, 11484, 12377, 13271, 14164, 15057, 15951, 16844, 17737, 18630, 19524, 20417, 21310, 22203, 23097, 23990, 24883, 25776, 26670, 27563, 28456, 29349, 30243, 31136, 32029, 32922, 33816, 34709, 35602, 36495, 37389,
                                         38282, 39175, 40068, 40962, 41855, 42748, 43641, 44535, 45428, 46321, 47215, 48108, 49001, 49894, 50788, 51681, 52574, 53467, 54361, 55254, 56147, 57040, 57934, 58827, 59720, 60613, 61507, 62400, 63293, 64186, 65080, 65973, 66866, 67759, 68653, 69546, 70439]]
    hit0 = 1
    CD = 18.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5

    MP = [150, 1232]


class 技能10(职业主动技能):
    名称 = 'C4飞弹'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.151*1.082)for i in [0, 8305, 9148, 9990, 10833, 11676, 12518, 13361, 14203, 15046, 15889, 16731, 17574, 18416, 19259, 20102, 20944, 21787, 22629, 23472, 24315, 25157, 26000, 26842, 27685, 28528, 29370, 30213, 31055, 31898, 32741, 33583, 34426, 35268,
                                         36111, 36954, 37796, 38639, 39481, 40324, 41167, 42009, 42852, 43694, 44537, 45380, 46222, 47065, 47907, 48750, 49593, 50435, 51278, 52120, 52963, 53806, 54648, 55491, 56333, 57176, 58019, 58861, 59704, 60546, 61389, 62232, 63074, 63917, 64759, 65602, 66445]]
    hit0 = 1
    CD = 20.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1

    MP = [150, 1232]

    def 装备护石(self):
        self.power0 *= 1.25


class 技能11(职业主动技能):
    名称 = '凝固汽油弹'
    所在等级 = 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.204*1.053)for i in [0, 9616, 10591, 11566, 12541, 13518, 14493, 15468, 16444, 17420, 18395, 19370, 20345, 21322, 22297, 23272, 24248, 25224, 26199, 27174, 28150, 29125, 30101, 31076, 32052, 33027, 34003, 34979, 35954, 36929, 37905, 38880, 39856, 40831,
                                         41806, 42783, 43758, 44733, 45710, 46685, 47660, 48635, 49610, 50587, 51562, 52537, 53513, 54489, 55464, 56439, 57414, 58391, 59366, 60341, 61317, 62292, 63268, 64244, 65219, 66194, 67170, 68145, 69121, 70096, 71072, 72048, 73023, 73998, 74973, 75949, 76925]]
    hit0 = 1
    data1 = [int(i*1.204*1.053)for i in [0, 50, 53, 59, 63, 69, 73, 79, 83, 89, 93, 98, 104, 108, 114, 118, 124, 128, 134, 137, 143, 148, 153, 159, 163, 169, 173, 178, 182, 188, 193, 198, 203, 208,
                                         214, 218, 223, 227, 233, 238, 243, 248, 253, 258, 262, 268, 273, 278, 283, 288, 293, 298, 302, 307, 312, 318, 323, 328, 333, 338, 343, 347, 352, 357, 363, 367, 373, 378, 383, 387, 392]]
    hit1 = 15
    CD = 20.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1

    MP = [200, 1812]
    无色消耗 = 1

    def 装备护石(self):
        self.power0 *= 1.4
        self.hit1 = 0
        self.CDR *= 0.94


class 技能12(职业主动技能):
    名称 = '镭射狙击'
    所在等级 = 45
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.161*1.056)for i in [0, 3351, 3691, 4031, 4371, 4711, 5051, 5391, 5731, 6071, 6411, 6752, 7092, 7432, 7772, 8112, 8452, 8792, 9132, 9472, 9812, 10152, 10492, 10832, 11172, 11512, 11852, 12192, 12532, 12872, 13212, 13552, 13892, 14232, 14572,
                                         14912, 15252, 15592, 15932, 16272, 16612, 16952, 17292, 17632, 17973, 18313, 18653, 18993, 19333, 19673, 20013, 20353, 20693, 21033, 21373, 21713, 22053, 22393, 22733, 23073, 23413, 23753, 24093, 24433, 24773, 25113, 25453, 25793, 26133, 26473, 26813]]
    hit0 = 5
    CD = 45.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1

    MP = [400, 3360]
    无色消耗 = 2

    def 装备护石(self):
        self.power0 *= 0.28
        self.hit0 = 24
        self.技能施放时间 = 3.0


class 技能13(被动技能):
    名称 = '弹药强化'
    所在等级 = 48
    等级上限 = 50
    等级精通 = 40
    学习间隔 = 3
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        return 1.105 + self.等级 * 0.015 if self.等级 > 0 else 1


class 技能14(职业主动技能):
    名称 = 'EMP磁暴'
    所在等级 = 50
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    MP = [880, 7392]
    无色消耗 = 5

    data0 = [int(i*1.232*1.067)for i in [0, 11718, 14435, 17152, 19870, 22587, 25304, 28021, 30739, 33456, 36173, 38891, 41608, 44325, 47042, 49760, 52477, 55194, 57912, 60629, 63346, 66063, 68781, 71498, 74215, 76932, 79650, 82367, 85084, 87802, 90519, 93236, 95953, 98671, 101388, 104105,
                                         106823, 109540, 112257, 114974, 117692, 120409, 123126, 125844, 128561, 131278, 133995, 136713, 139430, 142147, 144864, 147582, 150299, 153016, 155734, 158451, 161168, 163885, 166603, 169320, 172037, 174755, 177472, 180189, 182906, 185624, 188341, 191058, 193776, 196493, 199210]]
    hit0 = 3
    data1 = [int(i*1.232*1.067)for i in [0, 585, 721, 857, 993, 1129, 1265, 1401, 1536, 1672, 1808, 1944, 2080, 2216, 2352, 2488, 2623, 2759, 2895, 3031, 3167, 3303, 3439, 3574, 3710, 3846, 3982, 4118, 4254, 4390, 4525, 4661, 4797, 4933,
                                         5069, 5205, 5341, 5477, 5612, 5748, 5884, 6020, 6156, 6292, 6428, 6563, 6699, 6835, 6971, 7107, 7243, 7379, 7514, 7650, 7786, 7922, 8058, 8194, 8330, 8466, 8601, 8737, 8873, 9009, 9145, 9281, 9417, 9552, 9688, 9824, 9960]]
    hit1 = 20
    CD = 145.0


class 技能15(职业主动技能):
    名称 = 'G61重力手雷'
    所在等级 = 60
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.166*1.054)for i in [0, 6165, 6791, 7417, 8042, 8668, 9293, 9919, 10544, 11170, 11795, 12421, 13046, 13672, 14297, 14923, 15549, 16174, 16800, 17425, 18051, 18676, 19302, 19927, 20553, 21178, 21804, 22429, 23055, 23680, 24306, 24932, 25557, 26183,
                                         26808, 27434, 28059, 28685, 29310, 29936, 30561, 31187, 31812, 32438, 33063, 33689, 34315, 34940, 35566, 36191, 36817, 37442, 38068, 38693, 39319, 39944, 40570, 41195, 41821, 42446, 43072, 43698, 44323, 44949, 45574, 46200, 46825, 47451, 48076, 48702, 49327]]
    hit0 = 1
    data1 = [int(i*1.166*1.054)for i in [0, 205, 226, 247, 268, 288, 309, 330, 351, 372, 393, 414, 434, 455, 476, 497, 518, 539, 560, 580, 601, 622, 643, 664, 685, 705, 726, 747, 768, 789, 810, 831, 851, 872, 893,
                                         914, 935, 956, 977, 997, 1018, 1039, 1060, 1081, 1102, 1122, 1143, 1164, 1185, 1206, 1227, 1248, 1268, 1289, 1310, 1331, 1352, 1373, 1394, 1414, 1435, 1456, 1477, 1498, 1519, 1540, 1560, 1581, 1602, 1623, 1644]]
    hit1 = 29
    CD = 20.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    技能施放时间 = 3
    是否有护石 = 1

    MP = [400, 1120]
    无色消耗 = 2

    def 装备护石(self):
        self.power0 *= 2.34
        self.技能施放时间 = 0.5
        self.hit1 = 5


class 技能16(职业主动技能):
    名称 = '超真空弹：切莉'
    脱手 = 0
    所在等级 = 70
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [0]+[int(i*12 + 188) for i in range(1, 60)]
    hit0 = 20

    data1 = [0]+[int(i*49 + 432) for i in range(1, 60)]
    hit1 = 5

    data2 = [0]+[int(i*1955 + 17314) for i in range(1, 60)]
    hit2 = 1

    CD = 30.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    技能施放时间 = 1
    是否有护石 = 1

    MP = [800, 1680]
    无色消耗 = 3

    def 装备护石(self):
        self.倍率 *= 1.25
        self.CDR *= 0.95


class 技能17(被动技能):
    名称 = '制空掌握'
    所在等级 = 75
    等级上限 = 50
    等级精通 = 40
    学习间隔 = 3
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 3)


class 技能18(职业主动技能):
    名称 = '开火'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.139*1.052*1.051)for i in [0, 8299, 9141, 9982, 10824, 11666, 12508, 13350, 14192, 15034, 15876, 16718, 17560, 18402, 19244, 20086, 20928, 21770, 22612, 23453, 24295, 25137, 25979, 26821, 27663, 28505, 29347, 30189, 31031, 31873, 32715, 33557, 34399, 35241,
                                               36082, 36924, 37766, 38608, 39450, 40292, 41134, 41976, 42818, 43660, 44502, 45344, 46186, 47028, 47870, 48712, 49553, 50395, 51237, 52079, 52921, 53763, 54605, 55447, 56289, 57131, 57973, 58815, 59657, 60499, 61341, 62183, 63024, 63866, 64708, 65550, 66392]]
    hit0 = 6
    CD = 45.0
    脱手 = 0
    技能施放时间 = 1
    是否有护石 = 1
    护石选项 = ['圣痕']

    MP = [160, 1600]
    无色消耗 = 5

    def 装备护石(self):
        self.power0 *= 1.35


class 技能19(职业主动技能):
    名称 = '光子增强炮'
    所在等级 = 80
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [0]+[int(944*i+8355) for i in range(1, 60)]
    hit0 = 8

    CD = 45.0
    是否有护石 = 1
    护石选项 = ['圣痕']

    MP = [800, 6000]

    无色消耗 = 5

    def 装备护石(self):
        self.hit0 = 1
        self.power0 = 1 + 8.66 + 0.96
        self.CDR *= 0.93


class 技能20(职业主动技能):
    名称 = '决战之日'
    所在等级 = 85
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40
    技能施放时间 = 5

    MP = [2500, 8000]

    无色消耗 = 10

    data0 = [int(i*1.182*1.068)for i in [0, 3284, 4046, 4808, 5570, 6331, 7093, 7855, 8616, 9378, 10140, 10902, 11663, 12425, 13187, 13949, 14710, 15472, 16234, 16995, 17757, 18519, 19281, 20042, 20804, 21566, 22328, 23089, 23851, 24613, 25374, 26136, 26898, 27660, 28421,
                                         29183, 29945, 30706, 31468, 32230, 32992, 33753, 34515, 35277, 36039, 36800, 37562, 38324, 39085, 39847, 40609, 41371, 42132, 42894, 43656, 44417, 45179, 45941, 46703, 47464, 48226, 48988, 49750, 50511, 51273, 52035, 52796, 53558, 54320, 55082, 55843]]
    hit0 = 40
    CD = 180.0


class 技能21(被动技能):
    名称 = '单兵推进器-02X'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能22(职业主动技能):
    名称 = '空袭战略'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40
    # 脱手 = 1
    # 技能施放时间 = 3
    持续时间 = 6

    MP = [800, 6000]

    # samle：待选择的形态
    # 形态 = ["毛冰", "毛电", "冰电"]

    无色消耗 = 7

    CD = 60.0

    data0 = [0] + [int(i*12663+112153) for i in range(1, 60)]

    # 不同形态下的技能数值，每个形态都要有对应的判断和修改，没有进行拷贝，可能会出错
    # def 形态变更(self, 形态, char:Character):
    #     if 形态 == "毛电":
    #         self.hit0 = 7
    #     else:
    #         self.hit0 = 6
    #     pass


class 技能23(职业主动技能):
    名称 = '终解·制空霸权'
    所在等级 = 100
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    CD = 290.0
    脱手 = 0
    技能施放时间 = 6.8
    data0 = [int(i*1.23*1.067)for i in [0, 17492, 21548, 25604, 29660, 33716, 37773, 41829, 45885, 49941, 53997, 58054, 62110, 66166, 70222, 74278, 78334, 82391, 86447, 90503, 94559, 98615, 102671, 106728, 110784, 114840, 118896, 122952, 127009, 131065, 135121, 139177, 143233, 147289, 151346, 155402,
                                        159458, 163514, 167570, 171626, 175683, 179739, 183795, 187851, 191907, 195963, 200020, 204076, 208132, 212188, 216244, 220301, 224357, 228413, 232469, 236525, 240581, 244638, 248694, 252750, 256806, 260862, 264918, 268975, 273031, 277087, 281143, 285199, 289256, 293312, 297368]]
    hit0 = 7
    data1 = [int(i*1.23*1.067)for i in [0, 57141, 70391, 83641, 96891, 110142, 123392, 136642, 149892, 163142, 176392, 189643, 202893, 216143, 229393, 242643, 255893, 269144, 282394, 295644, 308894, 322144, 335395, 348645, 361895, 375145, 388395, 401645, 414896, 428146, 441396, 454646, 467896, 481146,
                                        494397, 507647, 520897, 534147, 547397, 560648, 573898, 587148, 600398, 613648, 626898, 640149, 653399, 666649, 679899, 693149, 706399, 719650, 732900, 746150, 759400, 772650, 785900, 799151, 812401, 825651, 838901, 852151, 865402, 878652, 891902, 905152, 918402, 931652, 944903, 958153, 971403]]
    hit1 = 5

    MP = [4028, 8056]

    无色消耗 = 15


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'spitfire_female'
        self.名称 = '重霄·弹药专家'
        self.角色 = '神枪手(女)'

        self.职业 = '弹药专家'
        # 用来筛CP武器的
        self.转职 = '弹药专家(女)'
        self.武器选项 = ['手弩', '步枪']
        self.输出类型选项 = ['魔法固伤', '物理固伤']
        self.防具精通属性 = ['智力', '力量']
        self.类型 = '魔法固伤'
        self.武器类型 = '手弩'
        self.防具类型 = '皮甲'
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
        self.buff = 1.84

        super().__init__()

    # def __set_individuation(self, info):
    #     info['individuation'] = [
    #         {"type": "checkbox", "value": "测试checkbox",
    #             "items": [], "row":0, "column":0, "key":0},
    #         {"type": "select", "value": "", "items": [
    #             1, 2, 3, 4, 5, 6, 7], "row":1, "column":0, "key":1},
    #         {"type": "label", "value": "测试label",
    #          "items": [], "row":2, "column":0, "key":2}
    #     ]

    def set_skill_info(self, info, rune_except=[], clothes_pants=[]):
        super().set_skill_info(info, rune_except=[
            '爆裂弹'], clothes_pants=['远古记忆'])

    # def get_skill_by_name(self, name) -> Union[技能, 主动技能, 被动技能]:
    #     if name == "G96热压手雷":
    #         name = "光子增强炮"
    #     return self.技能栏[self.技能序号.get(name, 0)]
