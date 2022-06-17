
from copy import deepcopy

from core.baseClass.character import Character
from core.baseClass.skill import 主动技能, 被动技能

# class 主动技能(主动技能):
# def 等效CD(self, 武器类型):
#     if 武器类型 == '法杖':
#         return round(self.CD / self.恢复 * 1.1, 1)
#     if 武器类型 == '魔杖':
#         return round(self.CD / self.恢复 * 1, 1)

#脱手 = 1

# def 实际技能次数(self, 输出时间, 武器类型, 输出类型):

#技能CD = self.等效CD(武器类型, 输出类型)
# 能够打满的技能次数计算
# 技能次数 = int((输出时间 - self.演出时间) /
#           self.等效CD(武器类型, 输出类型) + 1 + self.基础释放次数)
# 剩余时间 = 输出时间 - (技能次数 - 1 - self.基础释放次数) * \
#    self.等效CD(武器类型, 输出类型) - 技能CD - (技能次数-1)*0.5
# 最后一次技能小数点技能次数计算
# if 剩余时间 > 0 and 剩余时间 < self.演出时间:
#    技能次数 += self.最后一次伤害估算(剩余时间)
# return round(技能次数, 2)

# def 最后一次伤害估算(self, 剩余时间):
# return 0


class 技能0(主动技能):
    名称 = '烈焰冲击'
    所在等级 = 15
    学习间隔 = 2
    等级上限 = 70
    等级精通 = 60
    data0 = [int(i*1.0) for i in [0, 2742, 3021, 3300, 3578, 3857, 4135, 4412, 4691, 4969, 5247, 5526, 5805, 6083, 6362, 6639, 6917, 7196, 7474, 7753, 8031, 8308, 8587, 8867, 9144, 9423, 9701, 9979, 10258, 10536, 10813, 11092, 11370, 11650, 11928, 12206,
                                  12485, 12763, 13040, 13319, 13597, 13875, 14154, 14433, 14712, 14990, 15267, 15546, 15824, 16102, 16381, 16659, 16936, 17215, 17494, 17772, 18051, 18329, 18608, 18886, 19163, 19443, 19720, 19998, 20278, 20556, 20834, 21113, 21391, 21668, 21947]]
    hit0 = 1
    CD = 7.0
    TP成长 = 0.1
    TP上限 = 7
    演出时间 = 0.4
    MP = [40, 462]


class 技能1(被动技能):
    名称 = '属性精通'
    所在等级 = 30
    等级上限 = 15
    基础等级 = 5
    圣灵符文倍率 = 1.0

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + (0.30 + 0.02 * self.等级) * self.圣灵符文倍率, 5)


class 技能2(主动技能):
    名称 = '虚无之球'
    所在等级 = 20
    学习间隔 = 2
    等级上限 = 70
    等级精通 = 60
    data0 = [int(i*1.151) for i in [0, 379, 416, 457, 494, 532, 569, 609, 646, 685, 723, 763, 799, 839, 877, 916, 953, 993, 1031, 1068, 1109, 1146, 1185, 1222, 1262, 1299, 1338, 1376, 1416, 1452, 1491, 1530, 1568, 1605, 1645,
                                    1682, 1721, 1758, 1799, 1837, 1875, 1914, 1952, 1990, 2027, 2067, 2104, 2144, 2182, 2221, 2258, 2297, 2335, 2374, 2411, 2452, 2489, 2527, 2567, 2604, 2643, 2680, 2721, 2757, 2795, 2835, 2873, 2911, 2949, 2988, 3027]]
    hit0 = 8
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 7
    演出时间 = 8.0
    MP = [60, 616]


class 技能3(主动技能):
    名称 = '冰墙'
    所在等级 = 25
    学习间隔 = 2
    等级上限 = 70
    等级精通 = 60
    data0 = [int(i*1.159) for i in [0, 5858, 6451, 7043, 7636, 8235, 8825, 9418, 10011, 10609, 11202, 11795, 12388, 12981, 13578, 14171, 14763, 15356, 15955, 16547, 17140, 17733, 18329, 18922, 19515, 20108, 20706, 21299, 21892, 22485, 23082, 23675, 24267, 24860,
                                    25459, 26049, 26642, 27235, 27833, 28426, 29019, 29612, 30209, 30802, 31395, 31987, 32586, 33179, 33771, 34364, 34960, 35553, 36146, 36739, 37337, 37930, 38523, 39116, 39713, 40306, 40899, 41491, 42086, 42680, 43273, 43866, 44463, 45057, 45650, 46246, 46838]]
    hit0 = 1
    CD = 15.0
    TP成长 = 0.10
    TP上限 = 7
    演出时间 = 1.0
    MP = [60, 616]


class 技能4(主动技能):
    名称 = '雷旋'
    所在等级 = 25
    学习间隔 = 2
    等级上限 = 70
    等级精通 = 60
    data0 = [int(i*1.152) for i in [0, 2809, 3093, 3380, 3668, 3953, 4237, 4522, 4808, 5092, 5377, 5664, 5948, 6233, 6518, 6804, 7089, 7374, 7658, 7944, 8229, 8513, 8800, 9085, 9369, 9656, 9941, 10225, 10510, 10796, 11080, 11365, 11651, 11935, 12221, 12507,
                                    12793, 13079, 13364, 13648, 13933, 14220, 14503, 14789, 15075, 15359, 15644, 15931, 16215, 16500, 16785, 17069, 17355, 17641, 17925, 18211, 18496, 18780, 19068, 19353, 19640, 19923, 20209, 20493, 20779, 21064, 21348, 21633, 21920, 22205, 22489]]
    hit0 = 1
    CD = 5.0
    TP成长 = 0.10
    TP上限 = 7
    演出时间 = 1.5
    MP = [40, 462]


class 技能5(主动技能):
    名称 = '天雷冲击'
    所在等级 = 35
    学习间隔 = 2
    等级上限 = 70
    等级精通 = 60
    data0 = [int(i*1.155) for i in [0, 2680, 2952, 3224, 3496, 3768, 4039, 4312, 4584, 4856, 5128, 5399, 5672, 5943, 6216, 6487, 6759, 7031, 7303, 7575, 7847, 8118, 8391, 8663, 8935, 9207, 9478, 9751, 10022, 10295, 10566, 10838, 11110, 11382, 11654, 11926,
                                    12198, 12470, 12742, 13014, 13286, 13557, 13830, 14101, 14374, 14645, 14917, 15189, 15461, 15733, 16005, 16277, 16549, 16821, 17093, 17365, 17636, 17909, 18180, 18453, 18724, 18996, 19268, 19540, 19812, 20084, 20356, 20628, 20900, 21172, 21444]]
    hit0 = 3
    天雷攻击力增加率 = 1.55
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.5
    MP = [125, 436]
    无色消耗 = 1

    def 等效百分比(self, **argv):
        self.倍率 *= self.天雷攻击力增加率
        return super().等效百分比(**argv)

    def 装备护石(self):
        self.hit = 1
        self.天雷攻击力增加率 = 6.35


class 技能6(主动技能):
    名称 = '极冰盛宴'
    所在等级 = 40
    学习间隔 = 2
    等级上限 = 70
    等级精通 = 60
    data0 = [int(i*1.154) for i in [0, 1307, 1439, 1571, 1704, 1837, 1969, 2101, 2234, 2367, 2499, 2632, 2764, 2896, 3030, 3162, 3294, 3427, 3560, 3692, 3825, 3957, 4090, 4223, 4355, 4487, 4621, 4753, 4885, 5018, 5150, 5283, 5416, 5548,
                                    5680, 5814, 5946, 6078, 6211, 6344, 6476, 6609, 6741, 6874, 7006, 7139, 7271, 7404, 7537, 7669, 7801, 7934, 8067, 8199, 8332, 8464, 8597, 8730, 8862, 8994, 9128, 9260, 9392, 9525, 9657, 9790, 9923, 10055, 10187, 10321, 10453]]
    hit0 = 8
    CD = 19.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 4.7
    MP = [380, 3192]
    无色消耗 = 2


class 技能7(主动技能):
    名称 = '湮灭黑洞'
    所在等级 = 40
    学习间隔 = 2
    等级上限 = 70
    等级精通 = 60
    data0 = [int(i*1.239) for i in [0, 854, 942, 1028, 1115, 1201, 1289, 1375, 1462, 1548, 1636, 1722, 1809, 1895, 1983, 2069, 2156, 2242, 2330, 2416, 2503, 2589, 2677, 2763, 2850, 2936, 3023, 3110, 3197, 3283, 3370, 3457, 3544, 3630,
                                    3717, 3803, 3891, 3977, 4064, 4150, 4238, 4324, 4411, 4497, 4585, 4671, 4758, 4844, 4932, 5018, 5105, 5191, 5279, 5365, 5452, 5538, 5626, 5712, 5799, 5885, 5973, 6059, 6146, 6232, 6320, 6406, 6493, 6579, 6667, 6753, 6840]]
    hit0 = 15
    data1 = [int(i*1.239) for i in [0, 4280, 4714, 5147, 5581, 6016, 6450, 6884, 7319, 7753, 8187, 8620, 9055, 9489, 9923, 10358, 10792, 11226, 11661, 12094, 12528, 12963, 13397, 13831, 14266, 14700, 15134, 15567, 16002, 16436, 16870, 17305, 17739, 18173, 18608,
                                    19041, 19475, 19910, 20344, 20778, 21213, 21647, 22081, 22514, 22949, 23383, 23817, 24252, 24686, 25120, 25555, 25988, 26422, 26856, 27291, 27725, 28159, 28594, 29028, 29461, 29896, 30330, 30764, 31199, 31633, 32067, 32502, 32935, 33369, 33803, 34238]]
    hit1 = 1
    CD = 35.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 6.2
    无色消耗 = 2
    MP = [300, 2520]
    形态 = ['打满', '秒炸']

    def 形态变更(self, 形态: str = "", 武器类型: str = ""):
        if 形态 == "秒炸":
            self.hit0 = 2
        if 形态 == "打满":
            self.hit0 = 15

    def 装备护石(self):
        self.倍率 *= 1.37
        self.演出时间 *= 0.6


class 技能8(主动技能):
    名称 = '杰克降临'
    所在等级 = 45
    学习间隔 = 2
    等级上限 = 70
    等级精通 = 60
    data0 = [int(i*1.147) for i in [0, 3998, 4405, 4811, 5217, 5621, 6027, 6434, 6839, 7246, 7651, 8055, 8462, 8868, 9275, 9680, 10084, 10491, 10896, 11303, 11709, 12116, 12519, 12925, 13332, 13737, 14144, 14550, 14953, 15360, 15766, 16173, 16578, 16982, 17389,
                                    17794, 18201, 18607, 19012, 19419, 19823, 20230, 20635, 21041, 21448, 21852, 22259, 22664, 23071, 23476, 23882, 24287, 24693, 25099, 25505, 25910, 26317, 26721, 27128, 27533, 27939, 28346, 28750, 29157, 29562, 29967, 30374, 30780, 31187, 31591, 31996]]
    hit0 = 1
    data1 = [int(i*1.147) for i in [0, 15999, 17622, 19244, 20867, 22490, 24113, 25736, 27360, 28983, 30606, 32229, 33852, 35475, 37099, 38722, 40343, 41967, 43591, 45213, 46836, 48461, 50082, 51706, 53329, 54952, 56575, 58198, 59822, 61445, 63066, 64691, 66313, 67936, 69561,
                                    71182, 72805, 74430, 76052, 77675, 79300, 80921, 82544, 84166, 85791, 87414, 89036, 90660, 92284, 93905, 95530, 97152, 98775, 100399, 102021, 103644, 105269, 106891, 108514, 110135, 111760, 113383, 115005, 116630, 118253, 119874, 121499, 123121, 124744, 126369, 127990]]
    hit1 = 1
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.6
    无色消耗 = 2
    MP = [160, 1344]

    def 装备护石(self):
        self.power0 *= 0.1 * 4
        self.power1 *= 1.54


class 技能9(主动技能):
    名称 = '元素之幕'
    所在等级 = 60
    学习间隔 = 2
    等级上限 = 50
    等级精通 = 40
    data0 = [int(i*1.151) for i in [0, 370, 406, 444, 483, 519, 557, 595, 632, 669, 708, 745, 782, 819, 857, 895, 931, 970, 1008, 1044, 1082, 1119, 1156, 1195, 1233, 1270, 1307, 1344, 1383, 1420, 1457, 1495, 1533, 1569, 1608,
                                    1646, 1682, 1720, 1758, 1795, 1833, 1871, 1908, 1945, 1982, 2020, 2059, 2095, 2133, 2171, 2207, 2245, 2284, 2322, 2358, 2396, 2433, 2470, 2509, 2546, 2584, 2620, 2658, 2697, 2733, 2771, 2809, 2847, 2883, 2921, 2960]]
    hit0 = 20
    data1 = [int(i*1.151) for i in [0, 11098, 12225, 13350, 14475, 15602, 16727, 17854, 18979, 20104, 21231, 22357, 23482, 24610, 25734, 26862, 27987, 29113, 30239, 31365, 32491, 33617, 34742, 35869, 36994, 38119, 39246, 40371, 41500, 42625, 43750, 44877, 46002, 47129,
                                    48254, 49380, 50506, 51632, 52757, 53884, 55009, 56136, 57261, 58386, 59514, 60640, 61767, 62892, 64017, 65144, 66269, 67394, 68521, 69646, 70773, 71899, 73024, 74151, 75276, 76404, 77529, 78655, 79781, 80907, 82032, 83159, 84284, 85411, 86536, 87661, 88788]]
    hit1 = 1
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 3.0

    MP = [400, 100]
    无色消耗 = 2

    def 装备护石(self):
        self.CDR *= 0.95
        self.power0 *= 1 + 0.45
        self.power1 *= 1.32


class 技能10(被动技能):
    名称 = '魔力增幅'
    所在等级 = 48
    等级上限 = 50
    等级精通 = 40
    学习间隔 = 3
    倍率 = 1.0

    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.075 + 0.015 * self.等级, 5)


class 技能11(主动技能):
    名称 = '陨星幻灭'
    所在等级 = 50
    学习间隔 = 5
    等级上限 = 50
    等级精通 = 40
    data0 = [int(i*1.157) for i in [0, 159, 196, 233, 270, 307, 344, 381, 418, 540, 575, 610, 646, 682, 718, 753, 789, 825, 861, 896, 932, 968, 1003, 1039, 1075, 1111, 1146, 1182, 1218, 1254, 1289, 1324, 1360, 1396, 1432,
                                    1467, 1503, 1539, 1574, 1610, 1646, 1682, 1717, 1753, 1789, 1825, 1860, 1896, 1932, 1967, 2003, 2039, 2074, 2110, 2146, 2182, 2217, 2253, 2289, 2324, 2360, 2395, 2431, 2467, 2503, 2539, 2574, 2610, 2645, 2681, 2717]]
    hit0 = 40
    data1 = [int(i*1.157) for i in [0, 638, 785, 932, 1080, 1228, 1375, 1523, 1672, 2162, 2300, 2442, 2584, 2727, 2871, 3014, 3156, 3301, 3443, 3584, 3729, 3871, 4014, 4157, 4300, 4442, 4584, 4727, 4871, 5014, 5156, 5298, 5441, 5584,
                                    5728, 5870, 6012, 6154, 6298, 6440, 6583, 6727, 6870, 7012, 7154, 7298, 7441, 7583, 7727, 7870, 8012, 8155, 8298, 8441, 8582, 8727, 8869, 9012, 9155, 9296, 9440, 9581, 9725, 9868, 10010, 10154, 10295, 10439, 10582, 10725, 10868]]
    hit1 = 40
    data2 = [int(i*1.157) for i in [0, 1275, 1570, 1865, 2160, 2455, 2750, 3046, 3345, 4324, 4600, 4883, 5169, 5454, 5742, 6028, 6311, 6601, 6885, 7168, 7457, 7742, 8028, 8313, 8600, 8884, 9168, 9454, 9742, 10029, 10312, 10595, 10881, 11168, 11456, 11740,
                                    12023, 12309, 12596, 12880, 13166, 13455, 13740, 14024, 14308, 14597, 14881, 15166, 15454, 15739, 16025, 16310, 16595, 16881, 17164, 17453, 17737, 18023, 18309, 18592, 18879, 19163, 19450, 19737, 20020, 20309, 20590, 20878, 21163, 21450, 21737]]
    hit2 = 5
    data3 = [int(i*1.157) for i in [0, 5101, 6279, 7459, 8638, 9822, 11000, 12186, 13379, 17294, 18400, 19533, 20675, 21816, 22968, 24112, 25245, 26405, 27542, 28670, 29829, 30967, 32111, 33254, 34401, 35537, 36674, 37818, 38966, 40115, 41248, 42381, 43525, 44672,
                                    45825, 46959, 48092, 49235, 50383, 51519, 52665, 53819, 54958, 56096, 57234, 58387, 59526, 60664, 61817, 62956, 64099, 65239, 66380, 67525, 68656, 69812, 70948, 72094, 73237, 74368, 75517, 76651, 77799, 78946, 80081, 81235, 82361, 83512, 84654, 85799, 86947]]
    hit3 = 5
    CD = 145.0
    技能施放时间 = 1.44
    脱手 = 0
    无色消耗 = 5
    MP = [1200, 10080]


class 技能12(主动技能):
    名称 = '元素震荡'
    所在等级 = 70
    学习间隔 = 2
    等级上限 = 50
    等级精通 = 40
    data0 = [int(i*1.151) for i in [0, 4673, 5149, 5622, 6097, 6572, 7046, 7519, 7996, 8469, 8943, 9416, 9892, 10366, 10842, 11315, 11789, 12262, 12739, 13212, 13688, 14161, 14636, 15109, 15585, 16058, 16532, 17007, 17482, 17955, 18431, 18904, 19379, 19853, 20328,
                                    20801, 21277, 21750, 22223, 22699, 23172, 23647, 24120, 24596, 25069, 25545, 26019, 26493, 26966, 27442, 27915, 28390, 28865, 29339, 29812, 30289, 30762, 31236, 31711, 32185, 32659, 33135, 33608, 34082, 34557, 35032, 35505, 35981, 36454, 36929, 37402]]
    hit0 = 3
    data1 = [int(i*1.151) for i in [0, 21038, 23172, 25307, 27442, 29577, 31711, 33845, 35981, 38114, 40248, 42383, 44516, 46652, 48786, 50920, 53055, 55190, 57325, 59457, 61593, 63727, 65861, 67996, 70131, 72264, 74400, 76534, 78670, 80803, 82937, 85073, 87205, 89341, 91475, 93609,
                                    95744, 97879, 100012, 102146, 104282, 106416, 108551, 110685, 112821, 114953, 117087, 119223, 121356, 123492, 125626, 127760, 129894, 132030, 134164, 136297, 138433, 140567, 142701, 144835, 146971, 149104, 151240, 153374, 155506, 157642, 159776, 161912, 164045, 166181, 168315]]
    hit1 = 1
    data2 = []
    hit2 = 0
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 4.0
    MP = [860, 1500]
    无色消耗 = 3

    def 装备护石(self):
        self.hit0 += 0.14 * 17


class 技能13(主动技能):
    名称 = '圣灵水晶'
    所在等级 = 75
    学习间隔 = 2
    等级上限 = 50
    等级精通 = 40
    data0 = [int(i*1.15) for i in [0, 51418, 56634, 61850, 67067, 72284, 77501, 82715, 87932, 93148, 98366, 103582, 108798, 114014, 119232, 124447, 129663, 134879, 140095, 145312, 150529, 155746, 160962, 166178, 171393, 176611, 181827, 187043, 192259, 197477, 202693, 207910, 213124, 218341, 223558,
                                   228775, 233991, 239207, 244425, 249641, 254856, 260072, 265288, 270504, 275722, 280938, 286155, 291371, 296589, 301803, 307020, 312236, 317452, 322670, 327886, 333102, 338319, 343533, 348751, 353967, 359184, 364400, 369617, 374834, 380050, 385265, 390481, 395699, 400915, 406131, 411347]]
    hit0 = 1
    CD = 40.0
    演出时间 = 1.6
    是否有护石 = 1
    无色消耗 = 3
    MP = [580, 4500]

    def 装备护石(self):
        self.倍率 *= 1.25
        self.演出时间 -= 4.2


class 技能14(被动技能):
    名称 = '元素奥义'
    所在等级 = 75
    学习间隔 = 3
    等级上限 = 50
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能15(主动技能):
    名称 = '元素之门'
    所在等级 = 80
    学习间隔 = 2
    等级上限 = 50
    等级精通 = 40
    data0 = [int(i*1.151) for i in [0, 5398, 5947, 6494, 7042, 7589, 8141, 8681, 9230, 9777, 10326, 10878, 11420, 11972, 12519, 13068, 13615, 14162, 14709, 15257, 15799, 16350, 16898, 17445, 17996, 18543, 19093, 19637, 20187, 20734, 21283, 21833, 22373, 22924,
                                    23471, 24021, 24568, 25117, 25662, 26211, 26758, 27308, 27859, 28406, 28949, 29494, 30047, 30588, 31141, 31688, 32236, 32785, 33332, 33884, 34426, 34978, 35520, 36069, 36614, 37163, 37709, 38262, 38810, 39357, 39906, 40451, 41000, 41540, 42094, 42639, 43188]]
    hit0 = 10
    CD = 45.0
    演出时间 = 2.2
    是否有护石 = 1
    MP = [800, 6000]
    无色消耗 = 5
    # 根据外门数量的攻击力最大增幅率110%
    倍率 = 1.1

    def 装备护石(self, x):
        self.hit0 = 1
        self.power0 *= 13.25
        self.演出时间 *= 0.8


class 技能17(主动技能):
    名称 = '第六元素'
    所在等级 = 85
    学习间隔 = 5
    等级上限 = 50
    等级精通 = 40
    data0 = [int(i*1.151) for i in [0, 2458, 3029, 3598, 4168, 4735, 5309, 5876, 6446, 7016, 7586, 8155, 8726, 9295, 9865, 10432, 11006, 11572, 12145, 12713, 13283, 13858, 14426, 14996, 15563, 16138, 16705, 17275, 17845, 18415, 18983, 19555, 20123, 20693, 21260,
                                    21833, 22400, 22970, 23541, 24111, 24680, 25254, 25821, 26391, 26961, 27531, 28100, 28673, 29241, 29811, 30378, 30951, 31518, 32088, 32658, 33228, 33798, 34370, 34940, 35508, 36080, 36650, 37220, 37790, 38360, 38928, 39501, 40070, 40640, 41207, 41780]]
    hit0 = 20
    data1 = [int(i*1.151) for i in [0, 114681, 141273, 167868, 194459, 221054, 247648, 274238, 300833, 327427, 354017, 380612, 407205, 433800, 460395, 486987, 513579, 540174, 566766, 593361, 619952, 646544, 673139, 699731, 726326, 752920, 779512, 806107, 832702, 859293, 885886, 912480, 939073, 965669, 992256, 1018851,
                                    1045446, 1072038, 1098634, 1125226, 1151818, 1178413, 1205005, 1231600, 1258194, 1284787, 1311381, 1337970, 1364565, 1391159, 1417751, 1444346, 1470941, 1497531, 1524125, 1550720, 1577312, 1603907, 1630498, 1657091, 1683687, 1710277, 1736872, 1763466, 1790056, 1816651, 1843244, 1869839, 1896432, 1923026, 1949619]]
    hit1 = 1
    CD = 180.0
    技能施放时间 = 4.23
    脱手 = 0
    MP = [2500, 8000]
    无色消耗 = 10


class 技能16(主动技能):
    名称 = '圣灵符文'
    所在等级 = 75
    学习间隔 = 3
    等级上限 = 11
    等级精通 = 1
    是否有伤害 = 0
    是否主动 = 1
    data0 = [int(i*1.0) for i in [0, 131, 144, 156, 169, 181, 194, 206, 219, 231,
                                  244, 256, 269, 281, 294, 306, 319, 331, 344, 356, 369]]
    data1 = [int(i*1.0) for i in [0, 160, 174, 188, 201, 216, 229, 244, 257, 272,
                                  285, 299, 313, 327, 341, 355, 369, 383, 397, 411, 424]]


class 技能18(主动技能):
    名称 = '魔法秀'
    所在等级 = 20
    等级上限 = 15
    基础等级 = 10
    魔法秀数值 = [0, 22, 43, 65, 86, 108, 130, 151, 173, 194, 216,
             238, 259, 281, 302, 324, 346, 367, 389, 410, 432]
    是否有伤害 = 0
    冷却关联技能 = ['冰墙', '元素之门', '元素之幕', '元素震荡', '圣灵水晶', '烈焰冲击',
              '天雷冲击', '雷旋', '杰克降临', '湮灭黑洞', '极冰盛宴', '虚无之球', '光与暗的交响']

    圣灵符文倍率 = 1.0

    def CD缩减倍率(self, 武器类型):
        return round(1 - 0.001 * self.魔法秀数值[self.等级] * self.圣灵符文倍率, 3)


class 技能19(被动技能):
    名称 = '元素之源'
    所在等级 = 95
    学习间隔 = 3
    等级上限 = 50
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能20(主动技能):
    名称 = '光与暗的交响'
    所在等级 = 95
    学习间隔 = 2
    等级上限 = 50
    等级精通 = 40
    data0 = [int(i*1.151) for i in [0, 7853, 8650, 9447, 10244, 11040, 11837, 12634, 13430, 14227, 15024, 15821, 16617, 17414, 18211, 19008, 19804, 20601, 21398, 22194, 22991, 23788, 24585, 25381, 26178, 26975, 27771, 28568, 29365, 30162, 30958, 31755, 32552, 33349,
                                    34145, 34942, 35739, 36536, 37332, 38129, 38926, 39722, 40519, 41316, 42113, 42909, 43706, 44503, 45300, 46096, 46893, 47690, 48486, 49283, 50080, 50877, 51673, 52470, 53267, 54063, 54860, 55657, 56454, 57250, 58047, 58844, 59641, 60437, 61234, 62031, 62828]]
    hit0 = 15
    脱手 = 0
    技能施放时间 = 1.82
    CD = 60.0
    演出时间 = 3.0
    无色消耗 = 7
    MP = [833, 2666]


class 技能21(主动技能):
    名称 = '宇宙寂灭-冰火之歌'
    所在等级 = 100
    学习间隔 = 5
    等级上限 = 50
    等级精通 = 40
    data0 = [int(i*1.153) for i in [0, 263047, 324042, 385040, 446037, 507032, 568030, 629027, 690023, 751020, 812015, 873013, 934010, 995005, 1056003, 1116998, 1177995, 1238993, 1299988, 1360986, 1421983, 1482978, 1543976, 1604971, 1665968, 1726966, 1787961, 1848958, 1909954, 1970951, 2031949, 2092944, 2153941, 2214937, 2275934,
                                    2336931, 2397927, 2458924, 2519921, 2580917, 2641914, 2702909, 2763907, 2824904, 2885900, 2946897, 3007892, 3068890, 3129887, 3190882, 3251880, 3312875, 3373872, 3434870, 3495865, 3556863, 3617860, 3678855, 3739853, 3800848, 3861845, 3922843, 3983838, 4044835, 4105831, 4166828, 4227826, 4288821, 4349818, 4410814, 4471811]]
    hit0 = 1
    data1 = [int(i*1.153) for i in [0, 25052, 30861, 36670, 42480, 48289, 54098, 59907, 65716, 71526, 77335, 83144, 88953, 94762, 100572, 106381, 112190, 117999, 123808, 129618, 135427, 141236, 147045, 152854, 158664, 164473, 170282, 176091, 181900, 187710, 193519, 199328, 205137, 210946, 216756,
                                    222565, 228374, 234183, 239993, 245802, 251611, 257420, 263229, 269038, 274848, 280657, 286466, 292275, 298084, 303894, 309703, 315512, 321321, 327130, 332940, 338749, 344558, 350367, 356176, 361986, 367795, 373604, 379413, 385222, 391032, 396841, 402650, 408459, 414268, 420077, 425887]]
    hit1 = 7
    脱手 = 0
    技能施放时间 = 6.81
    关联技能 = ['无']
    CD = 290.0
    MP = [4027, 12888]
    无色消耗 = 15


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'elementalist'
        self.名称 = '知源·元素师'
        self.角色 = '魔法师(女)'
        self.职业类型 = '输出'
        self.职业 = '元素师'
        self.武器选项 = ['魔杖', '法杖']
        self.输出类型选项 = ['魔法百分比']
        self.防具精通属性 = ['智力']
        self.类型 = '魔法百分比'
        self.武器类型 = '魔杖'
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
        self.buff = 1.85

        super().__init__()

    def 职业特殊计算(self):
        圣灵符文 = self.get_skill_by_name('圣灵符文')
        self.get_skill_by_name('属性精通').圣灵符文倍率 = 1 + 圣灵符文.data0[圣灵符文.等级] / 1000
        self.get_skill_by_name('魔法秀').圣灵符文倍率 = 1 + 圣灵符文.data1[圣灵符文.等级] / 1000
        self.skills_passive['圣灵符文']['info'] = [{
            "type": "增幅",
            "info": [圣灵符文.data0[圣灵符文.等级] / 10, '属性精通', '无']
        }, {
            "type": "增幅",
            "info": [圣灵符文.data1[圣灵符文.等级] / 10, '魔法秀', '无']
        },
        ]

    def __set_individuation(self, info):
        info['individuation'] = [
            {"type": "checkbox", "value": "测试checkbox",
                "items": [], "row":0, "column":0, "key":0},
            {"type": "select", "value": "", "items": [
                1, 2, 3, 4, 5, 6, 7], "row":1, "column":0, "key":1},
            {"type": "label", "value": "测试label",
             "items": [], "row":2, "column":0, "key":2}
        ]
