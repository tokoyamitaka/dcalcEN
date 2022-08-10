from core.basic.skill import 技能
from core.basic.character import Character
from core.basic.skill import 主动技能, 被动技能


class 技能0(被动技能):
    名称 = '基础精通'
    倍率 = 1.0

    所在等级 = 1
    等级上限 = 200
    学习间隔 = 1
    等级精通 = 110

    关联技能 = ['念兽：龙虎啸']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)


class 技能1(主动技能):
    名称 = '分身'
    所在等级 = 5
    等级上限 = 20
    学习间隔 = 2
    等级精通 = 10
    MP = [6, 84]
    基础个数 = 0
    是否有伤害 = 0
    TP上限 = 0
    关联技能 = ['幻影爆碎']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return self.基础个数 + self.等级


class 技能2(主动技能):
    名称 = '气玉弹'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [20, 168]
    data0 = [int(i) for i in [0, 418, 458, 501, 543, 585, 628, 668, 710, 753, 796, 836, 882, 921, 964, 1005, 1050, 1091, 1132, 1173, 1217, 1258, 1302, 1343, 1387, 1428, 1472, 1512, 1553, 1598, 1639, 1680, 1725, 1764, 1808,
                              1848, 1894, 1934, 1976, 2018, 2060, 2102, 2146, 2188, 2230, 2269, 2317, 2355, 2398, 2441, 2482, 2524, 2564, 2609, 2650, 2691, 2737, 2775, 2823, 2861, 2907, 2945, 2986, 3032, 3072, 3118, 3158, 3197, 3242, 3283, 3328]]
    hit0 = 11
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 7


class 技能3(主动技能):
    名称 = '念气波'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [15, 154]
    data0 = [int(i*1.085*1.1822*1.117) for i in [0, 658, 725, 792, 859, 926, 991, 1060, 1127, 1192, 1259, 1326, 1393, 1460, 1527, 1594, 1660, 1728, 1795, 1860, 1927, 1994, 2061, 2128, 2195, 2262, 2329, 2395, 2463, 2530, 2596, 2663, 2730,
                                                 2796, 2863, 2930, 2997, 3064, 3131, 3198, 3264, 3331, 3398, 3465, 3532, 3599, 3666, 3732, 3799, 3866, 3933, 3999, 4066, 4134, 4200, 4267, 4334, 4401, 4468, 4535, 4602, 4668, 4734, 4802, 4868, 4935, 5002, 5069, 5136, 5203, 5270]]
    hit0 = 1
    感电data0 = [int(i) for i in [0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
                                6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]]
    感电hit0 = 1
    CD = 1.0
    TP成长 = 0.10
    TP上限 = 7

    形态 = ['蓄力', '普通']

    蓄念炮加成 = 1.0

    CP武器 = False

    def 形态变更(self, 形态, char):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if self.CP武器:
            self.CD = 5
            形态 = '蓄力'
        if 形态 == '蓄力':
            self.power0 = self.蓄念炮加成
            if not self.CP武器:
                self.CD = 4
        elif 形态 == '普通':
            self.power0 = 1
            self.CD = 1


class 技能4(被动技能):
    名称 = '蓄念炮'

    所在等级 = 20
    等级上限 = 11
    学习间隔 = 2
    等级精通 = 1

    基础等级 = 1

    关联技能 = ['念气波']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(2.26 + 0.05 * self.等级, 5)

    def 加成描述(self, 武器类型):
        return [round((self.加成倍率(武器类型) - 1)*100), "念气波(蓄力)", "无"]

# 幻爆的伤害实质属于被动技能，不能受1-35主动技能+xx的加成
# MP消耗也是按分身的等级来


class 技能5(主动技能):
    名称 = '幻影爆碎'
    是否主动 = 0
    所在等级 = 20
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    data0 = [int(i*1.085*1.182*1.121) for i in [0, 431, 474, 518, 562, 606, 650, 694, 736, 781, 825, 868, 913, 957, 999, 1044, 1088, 1131, 1176, 1218, 1262, 1306, 1350, 1395, 1438, 1481, 1526, 1569, 1612, 1658, 1700, 1743, 1789, 1832,
                                                1874, 1921, 1963, 2006, 2051, 2095, 2137, 2181, 2226, 2269, 2313, 2358, 2400, 2444, 2489, 2533, 2576, 2621, 2664, 2707, 2750, 2796, 2839, 2881, 2927, 2970, 3013, 3059, 3101, 3144, 3189, 3233, 3276, 3321, 3364, 3407, 3452]]
    CD = 10
    TP上限 = 7

    def TP加成(self):
        return 1.0


class 技能6(主动技能):
    名称 = '念雷破'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [48, 403]
    data0 = [int(i) for i in [0, 4760, 5244, 5727, 6210, 6694, 7177, 7660, 8142, 8625, 9108, 9592, 10074, 10558, 11039, 11523, 12007, 12489, 12973, 13456, 13938, 14421, 14904, 15387, 15871, 16353, 16836, 17318, 17802, 18286, 18768, 19252, 19734, 20217, 20700,
                              21184, 21666, 22150, 22631, 23115, 23597, 24081, 24565, 25047, 25531, 26013, 26496, 26979, 27463, 27945, 28429, 28910, 29394, 29876, 30360, 30844, 31326, 31809, 32292, 32775, 33258, 33742, 34224, 34707, 35189, 35673, 36157, 36639, 37123, 37604, 38088]]
    hit0 = 1
    CD = 6
    TP成长 = 0.10
    TP上限 = 7


class 技能7(主动技能):
    名称 = '念兽螺旋波'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [96, 806]
    data0 = [int(i) for i in [0, 1155, 1272, 1389, 1506, 1624, 1740, 1858, 1975, 2092, 2208, 2327, 2444, 2561, 2677, 2794, 2913, 3030, 3146, 3263, 3381, 3497, 3615, 3732, 3850, 3966, 4083, 4201, 4318, 4434, 4552, 4669, 4786, 4903,
                              5021, 5138, 5255, 5371, 5488, 5607, 5724, 5840, 5957, 6075, 6193, 6309, 6426, 6544, 6661, 6777, 6895, 7012, 7128, 7246, 7363, 7480, 7597, 7715, 7832, 7949, 8065, 8184, 8301, 8418, 8534, 8651, 8769, 8887, 9003, 9120, 9238]]
    hit0 = 3
    data1 = [int(i) for i in [0, 1299, 1432, 1563, 1695, 1827, 1959, 2090, 2223, 2354, 2485, 2618, 2749, 2881, 3012, 3145, 3276, 3408, 3540, 3672, 3803, 3935, 4067, 4198, 4331, 4462, 4594, 4726, 4858, 4989, 5122, 5253, 5385, 5517,
                              5648, 5780, 5912, 6044, 6175, 6308, 6439, 6571, 6703, 6835, 6966, 7099, 7230, 7361, 7494, 7625, 7757, 7888, 8021, 8152, 8284, 8416, 8548, 8679, 8810, 8943, 9073, 9207, 9337, 9470, 9602, 9734, 9865, 9998, 10129, 10261, 10393]]
    hit1 = 4
    感电data0 = [int(i) for i in [0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
                                12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]]
    感电hit0 = 7
    CD = 12
    TP成长 = 0.10
    TP上限 = 7


class 技能8(主动技能):
    名称 = '念气环绕'
    所在等级 = 30
    等级上限 = 20
    学习间隔 = 2
    等级精通 = 10
    MP = [268, 1694]
    data0 = [int(i*1.085*1.0*1.116) for i in [0, 359, 395, 431, 469, 505, 542, 578, 614, 651, 688, 724, 761, 797, 834, 870, 906, 942, 979, 1016, 1052, 1088, 1125, 1161, 1197, 1235, 1271, 1307, 1344, 1380, 1418, 1454, 1490, 1527,
                                              1563, 1599, 1636, 1672, 1709, 1745, 1782, 1818, 1854, 1890, 1927, 1963, 2001, 2037, 2073, 2110, 2146, 2182, 2220, 2256, 2293, 2329, 2365, 2402, 2439, 2475, 2511, 2548, 2584, 2620, 2656, 2693, 2730, 2766, 2803, 2839, 2876]]
    hit0 = 1
    CD = 0.5
    TP成长 = 0.10
    TP上限 = 5
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.03 + 0.02 * self.等级, 3)


class 技能9(主动技能):
    名称 = '狮子吼'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.085*1.1820*1.127) for i in [0, 6298, 6937, 7576, 8214, 8854, 9491, 10131, 10770, 11410, 12047, 12687, 13326, 13965, 14604, 15243, 15882, 16521, 17160, 17799, 18437, 19076, 19715, 20355, 20993, 21633, 22271, 22910, 23549, 24189, 24828, 25468, 26102,
                                                 26741, 27381, 28021, 28660, 29297, 29937, 30577, 31215, 31855, 32494, 33133, 33771, 34409, 35049, 35687, 36326, 36965, 37604, 38243, 38883, 39521, 40160, 40799, 41439, 42079, 42716, 43354, 43993, 44632, 45272, 45912, 46549, 47188, 47828, 48468, 49106, 49746, 50384]]
    hit0 = 1
    CD = 15
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [120, 1008]
    无色消耗 = 1

    def 装备护石(self):
        self.倍率 *= 1.36


class 技能10(主动技能):
    名称 = '螺旋念气场'
    所在等级 = 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.085*1.1811*1.122) for i in [0, 1039, 1144, 1248, 1354, 1457, 1564, 1667, 1773, 1881, 1982, 2089, 2194, 2298, 2403, 2510, 2614, 2719, 2825, 2929, 3035, 3140, 3246, 3351, 3455, 3561, 3667, 3771, 3876, 3982, 4087, 4190,
                                                 4295, 4401, 4508, 4612, 4718, 4821, 4925, 5031, 5135, 5244, 5349, 5455, 5557, 5663, 5769, 5873, 5979, 6084, 6188, 6293, 6399, 6505, 6608, 6714, 6818, 6924, 7030, 7135, 7239, 7344, 7449, 7552, 7662, 7763, 7870, 7976, 8081, 8185, 8291]]
    hit0 = 10
    演出时间 = 1
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [120, 1008]
    无色消耗 = 1

    def 装备护石(self):
        self.倍率 *= 1.22


class 技能11(主动技能):
    名称 = '念兽：龙虎啸'
    所在等级 = 40
    等级上限 = 20
    学习间隔 = 2
    等级精通 = 10
    # 第1击魔法武器攻击力：<int>%
    data0 = [int(i*1.085*1.125) for i in [0, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104,
                                          104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104]]
    hit0 = 1
    # 第2击魔法武器攻击力：<int>%
    data1 = [int(i*1.085*1.125) for i in [0, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117,
                                          117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117]]
    hit1 = 1
    # 第3击魔法武器攻击力：<int>%
    data2 = [int(i*1.085*1.125) for i in [0, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138,
                                          138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138]]
    hit2 = 1
    # 第4击魔法武器攻击力：<int>%
    data3 = [int(i*1.085*1.125) for i in [0, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157,
                                          157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157]]
    hit3 = 1
    # 第5击魔法武器攻击力：<int>%
    data4 = [int(i*1.085*1.125) for i in [0, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216,
                                          216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216]]
    hit4 = 1
    CD = 1.0
    TP成长 = 0.10
    TP上限 = 5
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.04 + 0.02 * self.等级, 5)


class 技能12(主动技能):
    名称 = '念兽：雷龙出海'
    所在等级 = 45
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.085*1.1828*1.121) for i in [0, 468, 515, 564, 608, 660, 707, 757, 807, 854, 900, 946, 996, 1046, 1093, 1142, 1188, 1237, 1287, 1334, 1384, 1434, 1479, 1526, 1576, 1625, 1673, 1722, 1769, 1817, 1865, 1915, 1962,
                                                 2010, 2057, 2105, 2156, 2203, 2253, 2299, 2347, 2396, 2443, 2494, 2540, 2590, 2638, 2687, 2733, 2782, 2832, 2879, 2926, 2975, 3024, 3072, 3121, 3167, 3217, 3264, 3314, 3360, 3409, 3458, 3505, 3555, 3603, 3651, 3698, 3747, 3795]]
    hit0 = 29
    data1 = [int(i*1.085*1.1828*1.121) for i in [0, 468, 515, 564, 608, 660, 707, 757, 807, 854, 900, 946, 996, 1046, 1093, 1142, 1188, 1237, 1287, 1334, 1384, 1434, 1479, 1526, 1576, 1625, 1673, 1722, 1769, 1817, 1865, 1915, 1962,
                                                 2010, 2057, 2105, 2156, 2203, 2253, 2299, 2347, 2396, 2443, 2494, 2540, 2590, 2638, 2687, 2733, 2782, 2832, 2879, 2926, 2975, 3024, 3072, 3121, 3167, 3217, 3264, 3314, 3360, 3409, 3458, 3505, 3555, 3603, 3651, 3698, 3747, 3795]]
    hit1 = 20
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [450, 3780]
    无色消耗 = 2

    形态 = ["打满", "秒C"]

    # 秒C 多段攻击次数为1 且爆炸攻击力随着剩余时间增加而增加 极限秒c加成为78.75%
    def 形态变更(self, 形态, char):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "打满":
            self.hit0 = 29
            self.hit1 = 20
        if 形态 == "秒C":
            self.hit0 = 1
            self.hit1 = 20
            self.power1 = 1.7875

    def 装备护石(self):
        self.倍率 *= 1.21


class 技能13(被动技能):
    名称 = '乱舞千叶花'
    所在等级 = 48
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.15 + 0.01 * self.等级, 5)


# 仅录入最高阶段
class 技能14(主动技能):
    名称 = '千莲怒放'
    所在等级 = 50
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i*1.085*1.1835*1.125) for i in [0, 7429, 9151, 10876, 12598, 14322, 16044, 17765, 19488, 21211, 22934, 24657, 26380, 28102, 29824, 31548, 33270, 34994, 36717, 38440, 40161, 41885, 43607, 45331, 47053, 48778, 50499, 52222, 53944, 55668, 57390, 59112, 60837, 62558,
                                                 64282, 66004, 67727, 69450, 71172, 72895, 74616, 76341, 78063, 79785, 81509, 83231, 84954, 86676, 88400, 90123, 91846, 93568, 95292, 97013, 98738, 100460, 102183, 103906, 105629, 107350, 109074, 110796, 112520, 114243, 115966, 117689, 119410, 121133, 122855, 124580, 126302]]
    hit0 = 6
    CD = 145

    MP = [900, 7560]
    无色消耗 = 5


class 技能15(主动技能):
    名称 = '奔雷掌'
    所在等级 = 60
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.085*1.1808*1.128) for i in [0, 1648, 1815, 1983, 2150, 2316, 2483, 2652, 2818, 2985, 3153, 3318, 3487, 3655, 3821, 3988, 4157, 4322, 4490, 4658, 4825, 4992, 5159, 5325, 5492, 5660, 5828, 5993, 6162, 6328, 6496, 6662, 6831, 6996,
                                                 7165, 7333, 7499, 7665, 7835, 8000, 8168, 8335, 8502, 8669, 8836, 9005, 9169, 9339, 9506, 9672, 9839, 10009, 10173, 10342, 10509, 10675, 10843, 11010, 11176, 11344, 11511, 11679, 11845, 12013, 12179, 12348, 12513, 12682, 12848, 13015, 13183]]
    hit0 = 6
    data1 = [int(i*1.085*1.1808*1.128) for i in [0, 6592, 7260, 7929, 8599, 9266, 9933, 10603, 11272, 11940, 12610, 13279, 13947, 14616, 15285, 15953, 16621, 17289, 17959, 18628, 19297, 19966, 20633, 21303, 21973, 22639, 23308, 23978, 24646, 25315, 25983, 26653, 27323,
                                                 27990, 28658, 29327, 29996, 30665, 31333, 32002, 32672, 33339, 34009, 34675, 35345, 36014, 36682, 37351, 38021, 38689, 39358, 40026, 40696, 41365, 42031, 42701, 43371, 44037, 44708, 45378, 46045, 46714, 47382, 48052, 48720, 49387, 50057, 50727, 51395, 52064, 52731]]
    hit1 = 1
    power1 = 1
    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [450, 1260]
    无色消耗 = 1

    def 装备护石(self):
        self.hit0 = 0
        self.power1 = 3.22
        self.CDR *= 0.90


class 技能16(主动技能):
    名称 = '狂狮怒吼'
    所在等级 = 70
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.085*1.1860*1.125) for i in [0, 3884, 4277, 4671, 5065, 5460, 5853, 6247, 6639, 7035, 7429, 7822, 8215, 8609, 9003, 9397, 9791, 10185, 10578, 10973, 11369, 11762, 12155, 12551, 12944, 13337, 13731, 14125, 14518, 14913, 15307, 15701, 16094, 16489,
                                                 16883, 17276, 17670, 18064, 18459, 18852, 19246, 19640, 20033, 20428, 20822, 21215, 21609, 22004, 22398, 22791, 23185, 23579, 23975, 24368, 24762, 25156, 25549, 25944, 26338, 26731, 27125, 27520, 27913, 28307, 28701, 29093, 29489, 29883, 30277, 30669, 31063]]
    hit0 = 5
    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [800, 1680]
    无色消耗 = 2

    def 装备护石(self):
        self.hit0 += 6
        self.倍率 *= 0.57
        self.CDR *= 0.90


class 技能17(主动技能):
    名称 = '奇袭幻影'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.085*1.1857*1.124) for i in [0, 10842, 11942, 13044, 14144, 15243, 16343, 17443, 18543, 19644, 20744, 21844, 22945, 24043, 25144, 26245, 27345, 28444, 29544, 30645, 31744, 32843, 33944,
                                                 35044, 36145, 37245, 38344, 39444, 40545, 41645, 42745, 43845, 44945, 46047, 47146, 48246, 49346, 50446, 51546, 52647, 53747, 54846, 55945, 57045, 58146, 59246, 60346, 61445, 62546, 63646, 64747]]
    hit0 = 4
    CD = 40
    是否有护石 = 1

    MP = [580, 4500]
    无色消耗 = 3

    def 装备护石(self):
        self.倍率 *= 1.33


class 技能18(主动技能):
    名称 = '聚能念气炮'
    所在等级 = 80
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.085*1.1663*1.126) for i in [0, 10681, 11766, 12849, 13933, 15016, 16101, 17184, 18268, 19351, 20436, 21520, 22601, 23687, 24769, 25853, 26936, 28021, 29104, 30188, 31270, 32354, 33438, 34521, 35605, 36688, 37773, 38857, 39940, 41025, 42107, 43191, 44274,
                                                 45359, 46442, 47526, 48609, 49694, 50778, 51861, 52946, 54029, 55113, 56195, 57280, 58363, 59447, 60530, 61615, 62699, 63782, 64865, 65950, 67031, 68115, 69198, 70283, 71367, 72450, 73535, 74618, 75702, 76784, 77869, 78952, 80036, 81119, 82204, 83287, 84371, 85454]]
    hit0 = 5
    CD = 45
    是否有护石 = 1

    MP = [800, 6000]
    无色消耗 = 5

    def 装备护石(self):
        self.倍率 *= 1.26


class 技能19(被动技能):
    名称 = '心之念意'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.24 + 0.03 * self.等级, 5)


class 技能20(主动技能):
    名称 = '念帝旋天破'
    所在等级 = 85
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i) for i in [0, 148974, 183517, 218062, 252607, 287152, 321695, 356241, 390785, 425329, 459875, 494420, 528964, 563507, 598051, 632594, 667139, 701683, 736227, 770772, 805316, 839861, 874407, 908950, 943494, 978040, 1012584, 1047127, 1081673, 1116218, 1150761, 1185304, 1219847, 1254391, 1288940, 1323483,
                              1358027, 1392571, 1427115, 1461659, 1496206, 1530749, 1565294, 1599838, 1634381, 1668927, 1703474, 1738017, 1772560, 1807104, 1841647, 1876194, 1910737, 1945280, 1979824, 2014370, 2048915, 2083460, 2118004, 2152547, 2187092, 2221635, 2256182, 2290726, 2325270, 2359814, 2394357, 2428900, 2463446, 2497994, 2532536]]
    hit0 = 0
    data1 = [int(i) for i in [0, 171319, 211044, 250771, 290497, 330224, 369949, 409677, 449402, 489128, 528856, 568582, 608308, 648033, 687758, 727482, 767209, 806935, 846660, 886387, 926113, 965840, 1005567, 1045292, 1085018, 1124746, 1164471, 1204196, 1243923, 1283650, 1323375, 1363099, 1402824, 1442549, 1482281, 1522005,
                              1561730, 1601456, 1641182, 1680907, 1720636, 1760361, 1800087, 1839813, 1879538, 1919266, 1958994, 1998719, 2038444, 2078169, 2117893, 2157623, 2197347, 2237072, 2276797, 2316525, 2356252, 2395978, 2435704, 2475429, 2515155, 2554880, 2594609, 2634334, 2674060, 2713786, 2753510, 2793235, 2832962, 2872692, 2912416]]
    hit1 = 1
    CD = 180

    MP = [2500, 5000]
    无色消耗 = 10

    形态 = ["蓄满", "秒炸"]

    # 秒C 多段攻击次数为1 且爆炸攻击力随着剩余时间增加而增加 极限秒c加成为78.75%
    def 形态变更(self, 形态, char):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "蓄满":
            self.hit0 = 0
            self.hit1 = 1
        if 形态 == "秒炸":
            self.hit0 = 1
            self.hit1 = 0


class 技能21(主动技能):
    名称 = '天雷分身步'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.085*1.2138*1.151) for i in [0, 17630, 19419, 21207, 22996, 24784, 26573, 28362, 30150, 31939, 33727, 35516, 37305, 39093, 40882, 42670, 44459, 46248, 48036, 49825, 51613, 53402, 55191, 56979, 58768, 60556, 62345, 64134, 65922, 67711, 69499, 71288, 73077, 74865, 76654,
                                                 78442, 80231, 82020, 83808, 85597, 87385, 89174, 90963, 92751, 94540, 96328, 98117, 99906, 101694, 103483, 105271, 107060, 108849, 110637, 112426, 114214, 116003, 117792, 119580, 121369, 123157, 124946, 126735, 128523, 130312, 132100, 133889, 135678, 137466, 139255, 141043]]
    hit0 = 1
    data1 = [int(i*1.085*1.2138*1.151) for i in [0, 2644, 2912, 3181, 3449, 3717, 3986, 4254, 4522, 4790, 5059, 5327, 5595, 5864, 6132, 6400, 6668, 6937, 7205, 7473, 7742, 8010, 8278, 8546, 8815, 9083, 9351, 9620, 9888, 10156, 10424, 10693, 10961, 11229, 11498,
                                                 11766, 12034, 12303, 12571, 12839, 13107, 13376, 13644, 13912, 14181, 14449, 14717, 14985, 15254, 15522, 15790, 16059, 16327, 16595, 16863, 17132, 17400, 17668, 17937, 18205, 18473, 18741, 19010, 19278, 19546, 19815, 20083, 20351, 20619, 20888, 21156]]
    hit1 = 10
    data2 = [int(i*1.085*1.2138*1.151) for i in [0, 44076, 48547, 53019, 57490, 61962, 66433, 70905, 75376, 79848, 84319, 88791, 93262, 97734, 102205, 106677, 111148, 115620, 120091, 124563, 129034, 133506, 137977, 142449, 146920, 151392, 155863, 160335, 164806, 169278, 173749, 178221, 182692, 187164,
                                                 191635, 196107, 200578, 205050, 209521, 213993, 218464, 222936, 227407, 231879, 236350, 240822, 245293, 249765, 254236, 258708, 263179, 267651, 272122, 276594, 281065, 285537, 290008, 294480, 298951, 303423, 307894, 312366, 316837, 321309, 325780, 330252, 334723, 339195, 343666, 348138, 352609]]
    hit2 = 1
    CD = 60.0

    MP = [833, 1667]
    无色消耗 = 7


class 技能22(主动技能):
    名称 = '念印幻流破'
    所在等级 = 100
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i*1.085*1.1840*1.132) for i in [0, 6459, 7957, 9455, 10953, 12451, 13949, 15447, 16945, 18442, 19940, 21438, 22936, 24434, 25932, 27430, 28928, 30426, 31924, 33421, 34919, 36417, 37915, 39413, 40911, 42409, 43907, 45405, 46903, 48401, 49898, 51396, 52894, 54392,
                                                 55890, 57388, 58886, 60384, 61882, 63380, 64877, 66375, 67873, 69371, 70869, 72367, 73865, 75363, 76861, 78359, 79857, 81354, 82852, 84350, 85848, 87346, 88844, 90342, 91840, 93338, 94836, 96333, 97831, 99329, 100827, 102325, 103823, 105321, 106819, 108317, 109815]]
    hit0 = 5
    data1 = [int(i*1.085*1.1840*1.132) for i in [0, 6459, 7957, 9455, 10953, 12451, 13949, 15447, 16945, 18442, 19940, 21438, 22936, 24434, 25932, 27430, 28928, 30426, 31924, 33421, 34919, 36417, 37915, 39413, 40911, 42409, 43907, 45405, 46903, 48401, 49898, 51396, 52894, 54392,
                                                 55890, 57388, 58886, 60384, 61882, 63380, 64877, 66375, 67873, 69371, 70869, 72367, 73865, 75363, 76861, 78359, 79857, 81354, 82852, 84350, 85848, 87346, 88844, 90342, 91840, 93338, 94836, 96333, 97831, 99329, 100827, 102325, 103823, 105321, 106819, 108317, 109815]]
    hit1 = 5
    data2 = [int(i*1.085*1.1840*1.132) for i in [0, 64597, 79576, 94555, 109534, 124513, 139492, 154471, 169450, 184429, 199408, 214387, 229366, 244345, 259324, 274303, 289282, 304261, 319240, 334219, 349198, 364178, 379157, 394136, 409115, 424094, 439073, 454052, 469031, 484010, 498989, 513968, 528947, 543926,
                                                 558905, 573884, 588863, 603842, 618821, 633800, 648779, 663758, 678737, 693716, 708696, 723675, 738654, 753633, 768612, 783591, 798570, 813549, 828528, 843507, 858486, 873465, 888444, 903423, 918402, 933381, 948360, 963339, 978318, 993297, 1008276, 1023255, 1038234, 1053214, 1068193, 1083172, 1098151]]
    hit2 = 1
    data3 = [int(i*1.085*1.1840*1.132) for i in [0, 64597, 79576, 94555, 109534, 124513, 139492, 154471, 169450, 184429, 199408, 214387, 229366, 244345, 259324, 274303, 289282, 304261, 319240, 334219, 349198, 364178, 379157, 394136, 409115, 424094, 439073, 454052, 469031, 484010, 498989, 513968, 528947, 543926,
                                                 558905, 573884, 588863, 603842, 618821, 633800, 648779, 663758, 678737, 693716, 708696, 723675, 738654, 753633, 768612, 783591, 798570, 813549, 828528, 843507, 858486, 873465, 888444, 903423, 918402, 933381, 948360, 963339, 978318, 993297, 1008276, 1023255, 1038234, 1053214, 1068193, 1083172, 1098151]]
    hit3 = 1
    data4 = [int(i*1.085*1.1840*1.132) for i in [0, 129194, 159152, 189110, 219068, 249026, 278984, 308942, 338900, 368858, 398817, 428775, 458733, 488691, 518649, 548607, 578565, 608523, 638481, 668439, 698397, 728356, 758314, 788272, 818230, 848188, 878146, 908104, 938062, 968020, 997978, 1027936, 1057894, 1087853, 1117811,
                                                 1147769, 1177727, 1207685, 1237643, 1267601, 1297559, 1327517, 1357475, 1387433, 1417392, 1447350, 1477308, 1507266, 1537224, 1567182, 1597140, 1627098, 1657056, 1687014, 1716972, 1746930, 1776889, 1806847, 1836805, 1866763, 1896721, 1926679, 1956637, 1986595, 2016553, 2046511, 2076469, 2106428, 2136386, 2166344, 2196302]]
    hit4 = 1
    CD = 290.0

    MP = [4028, 4028]
    无色消耗 = 15

# 念气归元
class 技能23(被动技能):
    名称 = '念气归元'
    所在等级 = 95
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30

    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class classChange(Character):
    def __init__(self):
        self.实际名称 = 'nenmaster_female'
        self.名称 = '归元·气功师'
        self.角色 = '格斗家(女)'
        self.角色类型 = '输出'
        self.职业 = '气功师'
        # 用来筛CP武器的
        self.转职 = '气功师(女)'
        self.武器选项 = ['手套']
        self.输出类型选项 = ['魔法百分比']
        self.防具精通属性 = ['智力']
        self.类型 = '魔法百分比'
        self.武器类型 = '手套'
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
        self.buff = 1.57*1.21

        super().__init__()

    def 职业特殊计算(self):
        幻影碎爆 = self.get_skill_by_name('幻影碎爆')
        分身 = self.get_skill_by_name('分身')
        分身.基础个数 = 幻影碎爆.TP等级

        念气波 = self.get_skill_by_name('念气波')
        蓄念炮倍率 = self.get_skill_by_name('蓄念炮').加成倍率(self.武器类型)

        念气波.倍率 /= 蓄念炮倍率
        念气波.蓄念炮加成 = 蓄念炮倍率

        pass
