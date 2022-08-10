
from core.basic.skill import 技能
from core.basic.character import Character
from core.basic.skill import 主动技能, 被动技能


class 职业主动技能(主动技能):
    技能施放时间 = 0.0
    脱手 = 1


class 技能0(被动技能):
    名称 = '弹夹改装'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    等级精通 = 10
    关联技能 = ['交叉射击', '聚合弹', '凝固汽油弹', '电磁弹：麦克斯韦']
    关联技能1 = ['爆裂弹', '贯穿弹', '狙击手增援']

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
    非冷却关联技能 = ['黑玫瑰特种战队', '超新星核爆', '赤魂风暴狙击']

    def 物理攻击力倍率(self, 武器类型):
        return (1.1 + (self.等级 - 10) * 0.02) if self.等级 >= 10 else (1 + self.等级 * 0.01)

    def 魔法攻击力倍率(self, 武器类型):
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
            return round(1 + 0.1 * self.等级, 3)


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
    data0 = [int(i*1.054) for i in [0, 2402, 2644, 2890, 3132, 3375, 3620, 3862, 4108, 4350, 4592, 4838, 5080, 5326, 5568, 5814, 6056, 6298, 6544, 6786, 7032, 7274, 7519, 7762, 8004, 8250, 8492, 8737, 8980, 9225, 9467, 9710, 9955, 10198, 10443, 10685,
                                    10928, 11173, 11415, 11661, 11903, 12149, 12391, 12633, 12879, 13121, 13367, 13609, 13855, 14097, 14339, 14585, 14827, 15073, 15315, 15557, 15803, 16045, 16290, 16533, 16778, 17021, 17263, 17508, 17751, 17996, 18238, 18484, 18726, 18969, 19214]]
    hit0 = 3
    CD = 6.0
    TP成长 = 0.10
    TP基础 = 7
    TP上限 = 7

    MP = [70, 588]


class 技能5(职业主动技能):
    名称 = 'G35感电手雷'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.1514*3.0945) for i in [0, 540, 595, 650, 705, 760, 814, 869, 924, 979, 1034, 1089, 1144, 1198, 1253, 1308, 1363, 1418, 1473, 1527, 1582, 1637, 1692, 1747, 1802, 1856, 1911, 1966,
                                            2021, 2076, 2131, 2185, 2240, 2295, 2350, 2405, 2460, 2515, 2569, 2624, 2679, 2734, 2789, 2844, 2898, 2953, 3008, 3063, 3118, 3173, 3227, 3282, 3337, 3392, 3447, 3502, 3557, 3611, 3666, 3721, 3776]]
    hit0 = 1
    感电data0 = [0, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14,
               14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14,
               14, 14, 14, 14, 14, 14, 14]
    感电hit0 = 18
    CD = 8.0
    TP成长 = 0.10
    TP基础 = 7
    TP上限 = 7

    MP = [40, 350]


class 技能6(职业主动技能):
    名称 = '交叉射击'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.052) for i in [0, 1677, 1847, 2017, 2187, 2357, 2528, 2697, 2867, 3038, 3208, 3377, 3548, 3718, 3889, 4058, 4228, 4399, 4569, 4738, 4909, 5079, 5250, 5419, 5589, 5760, 5930, 6099, 6270, 6440, 6610, 6780, 6950, 7121, 7291,
                                    7460, 7631, 7801, 7971, 8141, 8311, 8481, 8652, 8821, 8991, 9162, 9332, 9502, 9672, 9842, 10013, 10182, 10352, 10523, 10693, 10862, 11033, 11203, 11374, 11543, 11713, 11884, 12054, 12223, 12394, 12564, 12735, 12904, 13074, 13245, 13415]]
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
    data0 = [int(i*1.37*0.95) for i in [0, 768, 891, 1013, 1134, 1257, 1379, 1501,
                                        1624, 1747, 1869, 1992, 2114, 2235, 2358, 2480, 2603, 2726, 2848, 2971, 3093]]
    hit0 = 1
    CD = 5.0
    MP = [357, 2765]


class 技能8(职业主动技能):
    名称 = '贯穿弹'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10
    data0 = [int(i) for i in [0, 768, 891, 1013, 1134, 1257, 1379, 1501, 1624,
                              1747, 1869, 1992, 2114, 2235, 2358, 2480, 2603, 2726, 2848, 2971, 3093]]
    hit0 = 1
    出血data0 = [int(i*0.34*0.9) for i in [0, 768, 891, 1013, 1134, 1257, 1379, 1501,
                                         1624, 1747, 1869, 1992, 2114, 2235, 2358, 2480, 2603, 2726, 2848, 2971, 3093]]
    出血hit0 = 1
    CD = 5.0
    MP = [357, 2765]


class 技能9(职业主动技能):
    名称 = 'G18冰冻手雷'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.1567*3.175) for i in [0, 675, 744, 812, 881, 949, 1018, 1086, 1155, 1223, 1292, 1360, 1429, 1497, 1566, 1634, 1703, 1772, 1840, 1909, 1977, 2046, 2114, 2183, 2251, 2320, 2388, 2457, 2525, 2594, 2662, 2731, 2799,
                                           2868, 2936, 3005, 3073, 3142, 3210, 3279, 3347, 3416, 3485, 3553, 3622, 3690, 3759, 3827, 3896, 3964, 4033, 4101, 4170, 4238, 4307, 4375, 4444, 4512, 4581, 4649, 4718, 4786, 4855, 4923, 4992, 5060, 5129, 5197, 5266, 5335, 5403]]
    hit0 = 1
    CD = 10.0
    TP成长 = 0.10
    TP基础 = 7
    TP上限 = 7

    MP = [70, 560]

    # def 等效CD(self, 武器类型, 输出类型):
    #     # 经过测试,手雷恢复速度无法享受技能冷却恢复加成
    #     return round(self.CD, 1)


class 技能10(职业主动技能):
    名称 = '聚合弹'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.053)for i in [0, 10815, 11914, 13011, 14108, 15205, 16302, 17400, 18497, 19594, 20691, 21789, 22887, 23984, 25081, 26178, 27276, 28373, 29470, 30567, 31665, 32762, 33859, 34957, 36054, 37152, 38249, 39346, 40443, 41541, 42638, 43735, 44832, 45929,
                                   47028, 48125, 49222, 50319, 51416, 52514, 53611, 54708, 55805, 56904, 58001, 59098, 60195, 61292, 62390, 63487, 64584, 65681, 66779, 67877, 68974, 70071, 71168, 72266, 73363, 74460, 75557, 76655, 77752, 78849, 79947, 81044, 82142, 83239, 84336, 85433, 86530]]
    hit0 = 1
    data1 = [(0 if i == 0 else int(4178+(i-1)*424)) for i in range(0, 70)]
    data2 = [(0 if i == 0 else int(3249+(i-1)*330)) for i in range(0, 70)]
    hit1 = 0
    hit2 = 0
    CD = 18.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5

    CP武器 = False

    def 等效百分比(self, **argv):
        # 武器类型 额外等级 额外倍率 伤害类型 形态
        武器类型 = argv.get('武器类型', '')
        if 武器类型 == '手弩' and not self.CP武器:
            self.hit0 = 0
            self.hit1 = 1
            self.hit2 = 3
        else:
            self.hit0 = 1
            self.hit1 = 0
            self.hit2 = 0
        return super().等效百分比(**argv)

    MP = [150, 1232]


class 技能11(职业主动技能):
    名称 = 'C4飞弹'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.051) for i in [0, 9194, 10127, 11060, 11992, 12925, 13858, 14791, 15723, 16656, 17589, 18522, 19454, 20388, 21320, 22253, 23185, 24119, 25051, 25984, 26916, 27850, 28782, 29715, 30648, 31581, 32513, 33446, 34379, 35312, 36244, 37177, 38110, 39043,
                                    39975, 40908, 41842, 42774, 43706, 44640, 45573, 46505, 47437, 48371, 49304, 50236, 51168, 52102, 53035, 53967, 54901, 55833, 56766, 57698, 58632, 59564, 60497, 61429, 62363, 63295, 64228, 65160, 66094, 67026, 67959, 68892, 69825, 70757, 71690, 72623, 73556]]
    hit0 = 1
    CD = 20.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1

    MP = [150, 1232]

    def 装备护石(self):
        self.power0 *= 1.32


class 技能12(职业主动技能):
    名称 = '凝固汽油弹'
    所在等级 = 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.00) for i in [11648, 12829, 14011, 15193, 16375, 17556, 18738, 19920, 21101, 22284, 23465, 24646, 25828, 27010, 28192, 29373, 30555, 31737, 32918, 34101, 35282, 36463, 37646, 38827, 40009, 41190, 42372, 43554, 44735, 45918, 47099, 48280, 49463,
                                   50644, 51826, 53008, 54189, 55371, 56552, 57735, 58916, 60097, 61280, 62461, 63643, 64825, 66007, 67188, 68370, 69552, 70733, 71914, 73097, 74278, 75460, 76642, 77824, 79005, 80187, 81369, 82550, 83731, 84914, 86095, 87277, 88459, 89641, 90822, 92004, 93186]]
    hit0 = 1
    data1 = [int(i*1.00) for i in [63, 69, 76, 82, 88, 95, 101, 108, 114, 119, 127, 132, 140, 145, 151, 158, 164, 171, 177, 183, 190, 196, 203, 209, 215, 222, 228, 235, 241, 247, 254, 260, 267,
                                   273, 279, 286, 292, 299, 305, 311, 318, 324, 331, 337, 343, 350, 356, 363, 369, 375, 382, 388, 395, 401, 407, 414, 420, 427, 433, 439, 446, 452, 459, 465, 471, 478, 484, 491, 497, 503]]
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


class 技能13(职业主动技能):
    名称 = '狙击手增援'
    所在等级 = 45
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    data0 = [(0 if i == 0 else int(5361+(i-1)*605)) for i in range(0, 60)]

    # data0 = [int(i*1.161*1.056)for i in [0, 3351, 3691, 4031, 4371, 4711, 5051, 5391, 5731, 6071, 6411, 6752, 7092, 7432, 7772, 8112, 8452, 8792, 9132, 9472, 9812, 10152, 10492, 10832, 11172, 11512, 11852, 12192, 12532, 12872, 13212, 13552, 13892, 14232, 14572,
    #                                     14912, 15252, 15592, 15932, 16272, 16612, 16952, 17292, 17632, 17973, 18313, 18653, 18993, 19333, 19673, 20013, 20353, 20693, 21033, 21373, 21713, 22053, 22393, 22733, 23073, 23413, 23753, 24093, 24433, 24773, 25113, 25453, 25793, 26133, 26473, 26813]]
    hit0 = 5
    CD = 45.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1

    MP = [400, 3360]
    无色消耗 = 2

    def 装备护石(self):
        self.power0 *= 0.75*1.09
        self.hit0 = 8
        self.技能施放时间 = 2.0


class 技能14(被动技能):
    名称 = '弹药主宰'
    所在等级 = 48
    等级上限 = 50
    学习间隔 = 3
    关联技能 = ['所有']
    关联技能1 = ['爆裂弹', '贯穿弹']

    def 加成倍率(self, 武器类型):
        return 1.105 + self.等级 * 0.015 if self.等级 > 0 else 1

    def 加成倍率1(self, 武器类型):
        return 1.3 if self.等级 > 0 else 1


class 技能15(职业主动技能):
    名称 = '黑玫瑰特种战队'
    所在等级 = 50
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    MP = [1000, 8400]
    无色消耗 = 5

    data0 = [int(i*1.053) for i in [0, 2244, 2765, 3285, 3806, 4325, 4846, 5367, 5887, 6408, 6928, 7449, 7970, 8490, 9011, 9531, 10052, 10571, 11092, 11612, 12133, 12654, 13174, 13695, 14215, 14736, 15257, 15777, 16297, 16817, 17338, 17858, 18379, 18900, 19420,
                                    19941, 20461, 20982, 21503, 22023, 22542, 23063, 23584, 24104, 24625, 25145, 25666, 26187, 26707, 27228, 27748, 28269, 28788, 29309, 29830, 30350, 30871, 31391, 31912, 32433, 32953, 33474, 33994, 34514, 35034, 35555, 36075, 36596, 37117, 37637, 38158]]
    hit0 = 16
    data1 = [int(i*1.053) for i in [0, 399, 490, 583, 676, 769, 861, 953, 1046, 1139, 1231, 1323, 1416, 1509, 1602, 1694, 1786, 1879, 1972, 2064, 2156, 2249, 2342, 2434, 2526, 2619, 2712, 2804, 2897, 2989, 3082, 3174, 3267, 3359,
                                    3452, 3545, 3637, 3729, 3822, 3915, 4007, 4100, 4192, 4285, 4377, 4470, 4562, 4655, 4747, 4840, 4932, 5025, 5117, 5210, 5303, 5395, 5488, 5580, 5673, 5765, 5858, 5950, 6043, 6136, 6228, 6320, 6413, 6506, 6598, 6690, 6783]]
    hit1 = 82
    # 上下会有一个枪兵空掉一半
    CD = 145.0


class 技能16(职业主动技能):
    名称 = 'G61重力手雷'
    所在等级 = 60
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.0) for i in [0, 7374, 8122, 8870, 9618, 10367, 11114, 11863, 12612, 13359, 14108, 14856, 15603, 16352, 17101, 17848, 18597, 19345, 20093, 20841, 21589, 22337, 23086, 23833, 24582, 25330, 26078, 26826, 27575, 28322, 29071, 29819, 30567, 31315,
                                  32063, 32811, 33560, 34307, 35056, 35804, 36552, 37300, 38049, 38796, 39545, 40293, 41041, 41789, 42538, 43285, 44034, 44781, 45530, 46278, 47026, 47774, 48523, 49270, 50019, 50768, 51515, 52264, 53012, 53759, 54508, 55257, 56004, 56753, 57500, 58249, 58997]]
    data1 = [int(i*1.0) for i in [0, 245, 271, 295, 320, 345, 370, 394, 420, 445, 470, 494, 519, 545, 570, 594, 619, 644, 670, 694, 719, 744, 769, 793, 819, 844, 869, 893, 918, 944, 969, 993, 1018, 1043, 1069, 1093,
                                  1118, 1143, 1168, 1193, 1218, 1243, 1268, 1292, 1317, 1343, 1368, 1392, 1417, 1442, 1468, 1492, 1517, 1542, 1567, 1592, 1617, 1642, 1667, 1691, 1716, 1742, 1767, 1791, 1816, 1841, 1867, 1891, 1916, 1941, 1966]]
    hit0 = 1
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
        self.power0 *= 2.01
        self.技能施放时间 = 1.5
        self.hit1 = 15


class 技能17(职业主动技能):
    名称 = '电磁弹：麦克斯韦'
    脱手 = 1
    所在等级 = 70
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    # data0 = [int(i*1.16)for i in [0, 1233, 1359, 1484, 1609, 1734, 1859, 1984, 2110, 2235, 2360, 2485, 2610, 2735, 2861, 2986, 3111, 3236, 3361, 3486, 3612, 3737, 3862, 3987, 4112, 4237, 4363, 4488, 4613, 4738, 4863, 4989, 5114, 5239,
    #                              5364, 5489, 5614, 5740, 5865, 5990, 6115, 6240, 6365, 6491, 6616, 6741, 6866, 6991, 7116, 7242, 7367, 7492, 7617, 7742, 7867, 7993, 8118, 8243, 8368, 8493, 8618, 8744, 8869, 8994, 9119, 9244, 9370, 9495, 9620, 9745, 9870]]
    data0 = [(0 if i == 0 else int(22904+(i-1)*2587)) for i in range(0, 70)]
    hit0 = 1
    CD = 30.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    技能施放时间 = 1
    是否有护石 = 1

    MP = [800, 1680]
    无色消耗 = 3

    def 装备护石(self):
        self.power1 = 1.33
        self.CDR *= 0.95


class 技能18(被动技能):
    名称 = '战地功勋'
    所在等级 = 75
    等级上限 = 30
    学习间隔 = 3
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 3)


class 技能19(职业主动技能):
    名称 = '重火力支援'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.0) for i in [6136, 6758, 7380, 8003, 8625, 9247, 9870, 10492, 11114, 11737, 12359, 12981, 13604, 14226, 14848, 15471, 16093, 16717, 17339, 17960, 18584, 19206, 19828, 20451, 21073, 21695, 22318, 22940, 23562, 24185, 24807, 25429, 26052, 26674,
                                  27296, 27919, 28541, 29163, 29787, 30409, 31032, 31654, 32276, 32899, 33521, 34143, 34766, 35388, 36010, 36633, 37255, 37877, 38500, 39122, 39744, 40367, 40989, 41611, 42235, 42857, 43480, 44102, 44724, 45347, 45969, 46591, 47214, 47836, 48458, 49081]]
    hit0 = 10
    CD = 45.0
    脱手 = 0
    技能施放时间 = 1
    是否有护石 = 1
    护石选项 = ['圣痕']

    MP = [880, 1848]
    无色消耗 = 5

    def 装备护石(self):
        self.脱手 = 1
        self.power0 *= 1.35


class 技能20(职业主动技能):
    名称 = 'G38ARG智能手雷'
    所在等级 = 80
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.052) for i in [0, 18994, 20922, 22848, 24775, 26703, 28629, 30556, 32484, 34410, 36337, 38265, 40192, 42118, 44045, 45973, 47899, 49826, 51754, 53681, 55607, 57535, 59462, 61388, 63316, 65243, 67169, 69096, 71024, 72951, 74877, 76805, 78732, 80658, 82586, 84513,
                                    86439, 88367, 90294, 92221, 94147, 96075, 98002, 99928, 101856, 103783, 105709, 107637, 109564, 111491, 113418, 115345, 117272, 119198, 121126, 123053, 124981, 126907, 128834, 130761, 132688, 134615, 136542, 138469, 140396, 142323, 144251, 146177, 148104, 150032, 151958]]
    hit0 = 1
    data1 = [int(i*1.052) for i in [0, 4431, 4881, 5331, 5781, 6230, 6679, 7129, 7579, 8029, 8479, 8927, 9377, 9827, 10277, 10727, 11177, 11625, 12075, 12525, 12975, 13425, 13874, 14323, 14773, 15223, 15673, 16122, 16572, 17021, 17471, 17921, 18370, 18820, 19270,
                                    19719, 20169, 20618, 21068, 21518, 21968, 22417, 22866, 23316, 23766, 24216, 24665, 25114, 25564, 26014, 26464, 26914, 27362, 27812, 28262, 28712, 29162, 29612, 30060, 30510, 30960, 31410, 31860, 32309, 32758, 33208, 33658, 34108, 34557, 35007, 35456]]
    hit1 = 10
    CD = 45.0
    是否有护石 = 1
    护石选项 = ['圣痕']

    MP = [580, 4500]

    无色消耗 = 5

    def 装备护石(self):
        self.power0 *= 4.22
        self.hit1 = 0


class 技能21(职业主动技能):
    名称 = '超新星核爆'
    所在等级 = 85
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40
    技能施放时间 = 5

    MP = [2500, 8000]

    无色消耗 = 10

    data0 = [int(i*1.063) for i in [0, 88516, 109042, 129568, 150093, 170619, 191145, 211670, 232195, 252721, 273246, 293772, 314298, 334824, 355349, 375875, 396401, 416926, 437452, 457978, 478502, 499028, 519554, 540080, 560605, 581131, 601657, 622182, 642708, 663234, 683760, 704285, 724811, 745335, 765861, 786387,
                                    806913, 827438, 847964, 868490, 889016, 909541, 930067, 950593, 971118, 991644, 1012169, 1032694, 1053220, 1073746, 1094271, 1114797, 1135323, 1155849, 1176374, 1196900, 1217426, 1237952, 1258476, 1279002, 1299527, 1320053, 1340579, 1361105, 1381630, 1402156, 1422682, 1443207, 1463733, 1484259, 1504785]]
    data1 = [int(i*1.063) for i in [0, 2528, 3115, 3701, 4288, 4874, 5461, 6047, 6634, 7221, 7807, 8392, 8979, 9565, 10152, 10738, 11325, 11911, 12498, 13084, 13671, 14258, 14844, 15431, 16017, 16604, 17190, 17777, 18362, 18948, 19535, 20121, 20708, 21295, 21881,
                                    22468, 23054, 23641, 24227, 24814, 25400, 25987, 26573, 27160, 27746, 28332, 28918, 29505, 30091, 30678, 31264, 31851, 32437, 33024, 33610, 34197, 34783, 35370, 35956, 36543, 37129, 37715, 38301, 38888, 39474, 40061, 40647, 41234, 41820, 42407, 42993]]
    hit0 = 1
    hit1 = 15
    CD = 180.0


class 技能22(被动技能):
    名称 = '赤诚之心'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40
    关联技能 = ['所有']
    关联技能1 = ['交叉射击']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

    def 加成倍率1(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1.16


class 技能23(职业主动技能):
    名称 = '皇鹰特战队'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40
    脱手 = 0
    技能施放时间 = 0.7
    持续时间 = 6

    MP = [1067, 8000]

    无色消耗 = 7

    CD = 60.0
    data0 = [int(i*1.0) for i in [0, 2492, 2745, 2998, 3251, 3504, 3757, 4010, 4263, 4516, 4769, 5021, 5274, 5527, 5780, 6033, 6286, 6539, 6792, 7045, 7297, 7550, 7803, 8056, 8309, 8562, 8815, 9068, 9321, 9574, 9826, 10079, 10332, 10585, 10838, 11091,
                                  11344, 11597, 11850, 12103, 12355, 12608, 12861, 13114, 13367, 13620, 13873, 14126, 14379, 14631, 14884, 15137, 15390, 15643, 15896, 16149, 16402, 16655, 16908, 17160, 17413, 17666, 17919, 18172, 18425, 18678, 18931, 19184, 19436, 19689, 19942]]
    hit0 = 16
    data1 = [int(i*1.0) for i in [0, 62322, 68644, 74967, 81289, 87611, 93934, 100256, 106580, 112902, 119224, 125547, 131869, 138192, 144514, 150836, 157160, 163482, 169805, 176127, 182449, 188772, 195094, 201416, 207740, 214062, 220385, 226707, 233029, 239352, 245674, 251998, 258320, 264642, 270965,
                                  277287, 283610, 289932, 296254, 302578, 308900, 315223, 321545, 327867, 334190, 340512, 346835, 353158, 359480, 365803, 372125, 378448, 384770, 391092, 397415, 403738, 410060, 416383, 422705, 429028, 435350, 441672, 447996, 454318, 460641, 466963, 473285, 479608, 485930, 492253, 498576]]
    hit1 = 1
    data2 = [int(i*1.0) for i in [0, 9348, 10296, 11245, 12192, 13141, 14090, 15038, 15986, 16935, 17883, 18832, 19780, 20728, 21677, 22625, 23574, 24521, 25470, 26419, 27367, 28315, 29263, 30212, 31161, 32109, 33057, 34005, 34954, 35903, 36850, 37799, 38748, 39696,
                                  40645, 41592, 42541, 43490, 44438, 45386, 46334, 47283, 48232, 49179, 50128, 51076, 52025, 52974, 53921, 54870, 55818, 56767, 57715, 58663, 59612, 60561, 61508, 62457, 63405, 64354, 65303, 66250, 67199, 68147, 69096, 70044, 70992, 71941, 72889, 73837, 74786]]
    hit2 = 4


class 技能24(职业主动技能):
    名称 = '赤魂风暴狙击'
    所在等级 = 100
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    CD = 290.0
    脱手 = 0
    技能施放时间 = 6.3
    data0 = [int(i*1.0) for i in [0, 4186, 5156, 6127, 7098, 8069, 9040, 10011, 10982, 11952, 12923, 13894, 14865, 15836, 16807, 17777, 18748, 19719, 20689, 21660, 22631, 23602, 24573, 25544, 26515, 27486, 28457, 29426, 30397, 31368, 32339, 33310, 34281, 35252,
                                  36223, 37194, 38164, 39135, 40106, 41076, 42047, 43018, 43989, 44960, 45931, 46901, 47872, 48843, 49814, 50785, 51756, 52727, 53697, 54668, 55638, 56609, 57580, 58551, 59522, 60493, 61464, 62435, 63406, 64375, 65346, 66317, 67288, 68259, 69230, 70201, 71172]]
    hit0 = 12
    data1 = [int(i*1.0) for i in [0, 175837, 216610, 257384, 298158, 338932, 379705, 420480, 461253, 502027, 542800, 583575, 624348, 665122, 705895, 746670, 787444, 828217, 868992, 909765, 950539, 991312, 1032087, 1072860, 1113634, 1154407, 1195182, 1235956, 1276729, 1317504, 1358277, 1399051, 1439824, 1480599, 1521372, 1562146,
                                  1602919, 1643694, 1684467, 1725241, 1766016, 1806789, 1847563, 1888336, 1929111, 1969884, 2010658, 2051431, 2092206, 2132979, 2173753, 2214527, 2255301, 2296074, 2336848, 2377623, 2418396, 2459170, 2499943, 2540718, 2581491, 2622265, 2663039, 2703813, 2744586, 2785360, 2826134, 2866908, 2907681, 2948456, 2989230]]
    hit1 = 1
    data2 = [int(i*1.0) for i in [0, 62799, 77360, 91922, 106485, 121047, 135608, 150171, 164733, 179295, 193857, 208419, 222981, 237544, 252105, 266667, 281230, 295792, 310353, 324915, 339478, 354040, 368601, 383164, 397726, 412288, 426851, 441412, 455974, 470537, 485099, 499660, 514223, 528785, 543347,
                                  557908, 572471, 587033, 601595, 616158, 630719, 645281, 659844, 674406, 688967, 703530, 718092, 732654, 747216, 761778, 776340, 790902, 805464, 820026, 834588, 849151, 863712, 878274, 892837, 907399, 921960, 936523, 951085, 965647, 980210, 994771, 1009333, 1023895, 1038458, 1053019, 1067581]]
    hit2 = 4
    data3 = [int(i*1.0) for i in [0, 3348, 4126, 4902, 5679, 6455, 7232, 8008, 8785, 9561, 10338, 11116, 11892, 12669, 13445, 14222, 14998, 15775, 16551, 17328, 18106, 18882, 19659, 20435, 21212, 21988, 22765, 23541, 24318, 25094, 25872, 26648, 27425, 28201, 28978,
                                  29754, 30531, 31307, 32084, 32862, 33638, 34415, 35191, 35968, 36744, 37521, 38297, 39074, 39851, 40628, 41404, 42181, 42957, 43734, 44511, 45287, 46064, 46841, 47618, 48394, 49171, 49947, 50724, 51500, 52277, 53053, 53831, 54608, 55384, 56161, 56937]]
    hit3 = 3
    data4 = [int(i*1.0) for i in [0, 15071, 18566, 22061, 25556, 29051, 32546, 36040, 39535, 43030, 46525, 50020, 53515, 57010, 60505, 64000, 67495, 70989, 74484, 77979, 81474, 84969, 88464, 91959, 95454, 98949, 102444, 105939, 109433, 112928, 116423, 119918, 123413, 126908, 130403, 133898,
                                  137393, 140888, 144382, 147877, 151372, 154867, 158362, 161857, 165352, 168847, 172342, 175837, 179332, 182826, 186321, 189816, 193311, 196806, 200301, 203796, 207291, 210786, 214281, 217775, 221270, 224765, 228260, 231755, 235250, 238745, 242240, 245735, 249230, 252725, 256219]]
    hit4 = 1

    MP = [4028, 8056]

    无色消耗 = 15



class classChange(Character):
    def __init__(self):
        self.实际名称 = 'spitfire_male'
        self.名称 = '重霄·弹药专家'
        self.角色 = '神枪手(男)'
        self.职业类型 = '输出'
        self.职业 = '弹药专家'
        # 用来筛CP武器的
        self.转职 = '弹药专家(男)'
        self.武器选项 = ['手弩', '步枪']
        self.输出类型选项 = ['魔法百分比', '物理百分比']
        self.防具精通属性 = ['智力', '力量']
        self.类型 = '魔法百分比'
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
            '爆裂弹', '贯穿弹'], clothes_pants=['远古记忆'])
