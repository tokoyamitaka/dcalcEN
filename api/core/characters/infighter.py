from core.basic.skill import 技能
from core.basic.character import Character
from core.basic.skill import 主动技能, 被动技能


class 技能0(被动技能):  # 基础精通
    名称 = '基础精通'
    倍率 = 1.0

    所在等级 = 1
    等级上限 = 200
    学习间隔 = 1
    等级精通 = 110

    关联技能 = ['基本攻击']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)


class 技能1(主动技能):
    名称 = '基本攻击'
    备注 = '一轮'
    是否主动 = 0
    关联技能 = ['无']
    所在等级 = 1
    等级上限 = 1
    基础等级 = 1
    CD = 1  # 也没有CD
    # 共5击，127.96+143.96+158.99+174.97+190.96
    data0 = [0, 796.84]
    hit0 = 1
    TP成长 = 0.10
    TP上限 = 5


class 技能2(主动技能):
    名称 = '直拳冲击'
    所在等级 = 5
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [15, 154]
    # 第一击和第二击物理攻击力：<data0>%
    data0 = [int(i*1.074) for i in [0, 343, 377, 412, 447, 482, 517, 551, 587, 622, 655, 691, 726, 760, 795, 831, 865, 899, 935, 969, 1004, 1038, 1074, 1109, 1143, 1178, 1214, 1247, 1282, 1318, 1352, 1387, 1422, 1457, 1492,
                                    1526, 1561, 1596, 1631, 1665, 1701, 1736, 1769, 1805, 1840, 1874, 1909, 1945, 1979, 2014, 2049, 2084, 2118, 2153, 2188, 2223, 2258, 2292, 2328, 2363, 2396, 2432, 2466, 2501, 2536, 2571, 2606, 2640, 2675, 2710, 2745]]
    hit0 = 2
    # 最后一击物理攻击力：<data1>%
    data1 = [int(i*1.074) for i in [0, 1029, 1133, 1238, 1343, 1447, 1551, 1656, 1760, 1865, 1970, 2074, 2178, 2283, 2387, 2491, 2597, 2701, 2805, 2909, 3014, 3117, 3224, 3327, 3431, 3535, 3640, 3744, 3849, 3954, 4058, 4162, 4267,
                                    4371, 4476, 4581, 4685, 4789, 4893, 4998, 5102, 5208, 5312, 5416, 5520, 5625, 5729, 5834, 5939, 6043, 6147, 6252, 6356, 6461, 6566, 6670, 6774, 6879, 6983, 7088, 7193, 7296, 7400, 7504, 7609, 7713, 7818, 7923, 8027, 8131, 8236]]
    hit1 = 1
    CD = 3.0
    TP成长 = 0.10
    TP上限 = 7


class 技能3(主动技能):
    名称 = '俯冲直拳'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [18, 196]
    # 物理攻击力：<data0>%
    data0 = [int(i*1.075) for i in [0, 2448, 2695, 2944, 3193, 3442, 3689, 3938, 4186, 4434, 4683, 4931, 5180, 5427, 5676, 5925, 6173, 6421, 6670, 6918, 7167, 7414, 7663, 7912, 8159, 8408, 8657, 8905, 9153, 9401, 9650, 9899, 10146, 10395, 10644, 10892,
                                    11140, 11388, 11637, 11885, 12133, 12382, 12631, 12878, 13127, 13376, 13624, 13872, 14120, 14369, 14618, 14865, 15114, 15363, 15610, 15859, 16107, 16356, 16604, 16852, 17101, 17350, 17597, 17846, 18094, 18343, 18591, 18839, 19088, 19335, 19584]]
    hit0 = 1
    CD = 3.5
    TP成长 = 0.10
    TP上限 = 7


class 技能4(主动技能):
    名称 = '俯冲翔拳'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [18, 196]
    # 物理攻击力：<data0>%
    data0 = [int(i*1.075) for i in [0, 2448, 2695, 2944, 3193, 3442, 3689, 3938, 4186, 4434, 4683, 4931, 5180, 5427, 5676, 5925, 6173, 6421, 6670, 6918, 7167, 7414, 7663, 7912, 8159, 8408, 8657, 8905, 9153, 9401, 9650, 9899, 10146, 10395, 10644, 10892,
                                    11140, 11388, 11637, 11885, 12133, 12382, 12631, 12878, 13127, 13376, 13624, 13872, 14120, 14369, 14618, 14865, 15114, 15363, 15610, 15859, 16107, 16356, 16604, 16852, 17101, 17350, 17597, 17846, 18094, 18343, 18591, 18839, 19088, 19335, 19584]]
    hit0 = 1
    CD = 3.5
    TP成长 = 0.10
    TP上限 = 7


class 技能5(主动技能):
    名称 = '圣拳锤击'
    所在等级 = 20
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [12, 137]
    # 直接攻击物理攻击力：<int>%
    data0 = [int(i*1.074) for i in [0, 338, 372, 406, 441, 475, 509, 544, 578, 612, 647, 681, 715, 750, 784, 818, 853, 887, 921, 956, 990, 1024, 1059, 1093, 1127, 1162, 1196, 1230, 1265, 1299, 1333, 1368, 1402, 1436, 1471,
                                    1505, 1539, 1573, 1608, 1642, 1676, 1711, 1745, 1779, 1814, 1848, 1882, 1917, 1951, 1985, 2020, 2054, 2088, 2123, 2157, 2191, 2226, 2260, 2294, 2329, 2363, 2397, 2432, 2466, 2500, 2535, 2569, 2603, 2636, 2672, 2706]]
    hit0 = 1
    # 冲击波攻击力：<int>%
    data1 = [int(i*1.074) for i in [0, 3043, 3352, 3661, 3970, 4279, 4588, 4897, 5206, 5515, 5824, 6133, 6441, 6750, 7059, 7368, 7677, 7986, 8295, 8604, 8913, 9222, 9531, 9840, 10148, 10456, 10765, 11074, 11383, 11692, 12001, 12310, 12619, 12928, 13237,
                                    13545, 13854, 14163, 14472, 14781, 15090, 15399, 15708, 16017, 16326, 16635, 16943, 17252, 17561, 17870, 18179, 18488, 18797, 19106, 19415, 19724, 20033, 20340, 20649, 20958, 21267, 21576, 21885, 22194, 22503, 22812, 23121, 23430, 23738, 24047, 24356]]
    hit1 = 1
    CD = 5.0
    TP成长 = 0.1
    TP上限 = 7


class 技能6(主动技能):
    名称 = '俯冲腹拳'
    所在等级 = 20
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [18, 196]
    # 物理攻击力：<data0>%
    data0 = [int(i*1.075) for i in [0, 2623, 2889, 3154, 3420, 3686, 3953, 4219, 4485, 4752, 5017, 5283, 5549, 5815, 6082, 6348, 6613, 6879, 7146, 7412, 7678, 7944, 8211, 8476, 8742, 9008, 9275, 9541, 9807, 10073, 10338, 10605, 10871, 11137, 11404, 11670,
                                    11935, 12201, 12467, 12734, 13000, 13266, 13533, 13798, 14064, 14330, 14596, 14863, 15129, 15395, 15660, 15927, 16193, 16459, 16725, 16992, 17257, 17523, 17789, 18056, 18322, 18588, 18854, 19119, 19386, 19652, 19918, 20184, 20451, 20717, 20982]]
    CD = 3.5
    TP成长 = 0.10
    TP上限 = 7

    # def 神圣反击攻击力(self):
    #     # 神圣反击基础百分比与腹拳一样，但在修炼场手动开只有80%(和技巧精通等级相关,10级时80%，每级成长4%)
    #     # 技巧精通对于俯冲腹拳的额外加成不算在内
    #     return int(self.data0[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率)


class 技能7(被动技能):
    名称 = '技巧精通'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    关联技能 = ['俯冲直拳', '俯冲腹拳', '俯冲翔拳']
    关联技能1 = ['圣拳连击']
    # 关联技能4 = ['神圣反击']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 10:
            return round(1.00 + 0.01 * self.等级, 5)
        else:
            return round(1.10 + 0.015 * (self.等级 - 10), 5)

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10, 5)

    def 加成倍率1(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.03, 5)

    # def 加成倍率4(self, 武器类型):
    #     if self.等级 == 0:
    #         return 1.0
    #     else:
    #         return round(0.40+0.04 * self.等级, 5)


class 技能8(主动技能):
    名称 = '瞬拳'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [22, 231]
    data0 = [int(i*1.074) for i in [0, 2635, 2903, 3170, 3438, 3705, 3973, 4240, 4508, 4775, 5043, 5311, 5578, 5846, 6113, 6381, 6648, 6914, 7182, 7450, 7717, 7985, 8252, 8520, 8787, 9055, 9322, 9590, 9857, 10125, 10392, 10660, 10928, 11194, 11461, 11729,
                                    11996, 12264, 12531, 12799, 13067, 13334, 13602, 13869, 14137, 14404, 14672, 14939, 15207, 15474, 15741, 16008, 16276, 16543, 16811, 17078, 17346, 17613, 17881, 18148, 18416, 18684, 18951, 19219, 19486, 19754, 20020, 20287, 20555, 20823, 21090]]
    hit0 = 1
    data1 = [int(i*1.074) for i in [0, 658, 725, 793, 859, 926, 992, 1060, 1127, 1193, 1260, 1328, 1394, 1461, 1527, 1595, 1662, 1728, 1795, 1861, 1929, 1996, 2062, 2129, 2197, 2263, 2330, 2397, 2464, 2531, 2597, 2664, 2732, 2798,
                                    2865, 2932, 2998, 3066, 3133, 3199, 3266, 3334, 3400, 3467, 3533, 3601, 3668, 3734, 3801, 3869, 3935, 4002, 4068, 4135, 4203, 4269, 4336, 4402, 4470, 4537, 4603, 4670, 4738, 4804, 4871, 4937, 5004, 5072, 5138, 5205, 5272]]
    hit1 = 1
    CD = 4
    TP成长 = 0.10
    TP上限 = 7


class 技能9(主动技能):
    名称 = '圣拳连击'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [45, 462]
    # 刺拳物理攻击力：<data0>%
    data0 = [int(i*1.075) for i in [0, 1318, 1451, 1585, 1718, 1853, 1986, 2120, 2254, 2387, 2522, 2655, 2789, 2922, 3056, 3190, 3324, 3457, 3591, 3725, 3859, 3993, 4126, 4260, 4393, 4528, 4661, 4795, 4928, 5062, 5197, 5330, 5464, 5597,
                                    5731, 5864, 5999, 6132, 6266, 6399, 6533, 6668, 6801, 6935, 7068, 7202, 7335, 7470, 7603, 7737, 7870, 8005, 8139, 8272, 8406, 8539, 8674, 8807, 8941, 9074, 9208, 9341, 9476, 9609, 9743, 9877, 10010, 10145, 10278, 10412, 10545]]
    hit0 = 1
    # 直拳物理攻击力：<data1>%
    data1 = [int(i*1.075) for i in [0, 1610, 1774, 1938, 2101, 2264, 2428, 2591, 2755, 2918, 3082, 3245, 3409, 3572, 3736, 3899, 4062, 4226, 4389, 4553, 4716, 4880, 5043, 5207, 5370, 5533, 5697, 5861, 6024, 6187, 6351, 6515, 6678, 6841, 7004,
                                    7169, 7332, 7495, 7658, 7823, 7986, 8149, 8312, 8475, 8640, 8803, 8966, 9129, 9294, 9457, 9620, 9783, 9946, 10111, 10274, 10437, 10600, 10763, 10928, 11091, 11254, 11417, 11582, 11745, 11908, 12071, 12235, 12399, 12562, 12725, 12889]]
    hit1 = 1
    # 摆拳物理攻击力：<data2>%
    data2 = [int(i*1.075) for i in [0, 1952, 2150, 2349, 2547, 2745, 2943, 3141, 3339, 3537, 3736, 3934, 4132, 4330, 4528, 4726, 4924, 5123, 5321, 5519, 5716, 5915, 6113, 6311, 6510, 6708, 6905, 7103, 7302, 7500, 7698, 7897, 8095, 8292, 8490, 8689,
                                    8887, 9085, 9284, 9481, 9679, 9877, 10076, 10274, 10472, 10671, 10868, 11066, 11264, 11463, 11661, 11859, 12056, 12255, 12453, 12651, 12850, 13048, 13245, 13443, 13642, 13840, 14038, 14237, 14435, 14632, 14830, 15029, 15227, 15425, 15624]]
    hit2 = 1
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 7


# class 技能10(主动技能):
    # 名称 = '神圣反击'
    # 所在等级 = 30
    # 等级上限 = 11
    # 学习间隔 = 3
    # 等级精通 = 1
    # MP = [22, 231]
    # data0 = [0]*11
    # data1 = [0]
    # CD = 6
    # TP上限 = 1

    # def 等效百分比(self, **argv):
    #     char: Character = argv.get('char', {})
    #     腹拳 = char.get_skill_by_name("俯冲腹拳").神圣反击攻击力(
    #     )/char.get_skill_by_name("技巧精通").加成倍率4('')
    #     return super().等效百分比(**argv)+腹拳+self.TP等级*303


class 技能10(主动技能):
    名称 = '破碎之锤'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [45, 462]
    # 物理攻击力：<data0>%
    data0 = [int(i*1.074) for i in [0, 3245, 3575, 3904, 4233, 4563, 4892, 5221, 5550, 5880, 6209, 6538, 6868, 7197, 7526, 7856, 8185, 8514, 8843, 9173, 9502, 9831, 10161, 10490, 10819, 11149, 11478, 11807, 12136, 12466, 12795, 13124, 13454, 13783, 14112,
                                    14442, 14771, 15100, 15428, 15759, 16088, 16416, 16747, 17076, 17404, 17735, 18064, 18392, 18721, 19052, 19380, 19709, 20040, 20368, 20697, 21028, 21356, 21685, 22014, 22344, 22673, 23002, 23332, 23661, 23990, 24320, 24649, 24978, 25307, 25637, 25966]]
    hit0 = 1
    # 冲击波物理攻击力：<data1>
    data1 = [int(i*1.074) for i in [0, 2163, 2383, 2602, 2822, 3042, 3261, 3480, 3699, 3920, 4139, 4359, 4578, 4797, 5018, 5237, 5456, 5675, 5895, 6115, 6334, 6554, 6773, 6992, 7213, 7432, 7651, 7871, 8090, 8310, 8530, 8749, 8968, 9188, 9408, 9627,
                                    9847, 10066, 10285, 10506, 10725, 10944, 11164, 11383, 11603, 11823, 12042, 12261, 12481, 12701, 12920, 13140, 13359, 13578, 13799, 14018, 14237, 14456, 14676, 14896, 15116, 15335, 15554, 15773, 15994, 16213, 16432, 16652, 16871, 17092, 17311]]
    hit1 = 1
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 7


class 技能11(主动技能):
    名称 = '刺拳猛击'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [50, 546]
    # 刺拳连击物理攻击力：<data0>%
    data0 = [int(i*1.075) for i in [0, 607, 668, 730, 791, 853, 914, 976, 1037, 1099, 1161, 1222, 1285, 1346, 1408, 1470, 1531, 1593, 1654, 1716, 1777, 1839, 1900, 1962, 2023, 2085, 2147, 2208, 2270, 2331, 2393, 2454, 2517, 2579,
                                    2640, 2702, 2763, 2825, 2886, 2948, 3009, 3071, 3133, 3194, 3256, 3317, 3379, 3440, 3502, 3563, 3625, 3686, 3748, 3811, 3872, 3934, 3995, 4057, 4119, 4180, 4242, 4303, 4365, 4426, 4488, 4549, 4611, 4672, 4734, 4796, 4857]]
    hit0 = 10
    # 最后锤击物理攻击力：<data1>%
    data1 = [int(i*1.075) for i in [0, 1812, 1996, 2180, 2364, 2547, 2732, 2915, 3100, 3283, 3467, 3651, 3835, 4019, 4203, 4387, 4571, 4754, 4939, 5122, 5307, 5490, 5674, 5858, 6042, 6226, 6410, 6594, 6778, 6961, 7146, 7329, 7514, 7697, 7880,
                                    8065, 8248, 8433, 8616, 8801, 8984, 9168, 9352, 9536, 9720, 9904, 10087, 10272, 10455, 10640, 10823, 11008, 11191, 11375, 11559, 11743, 11927, 12111, 12294, 12479, 12662, 12847, 13030, 13215, 13398, 13582, 13766, 13950, 14134, 14318, 14501]]
    hit1 = 1
    # 追击攻击物理攻击力：<data2>%
    data2 = [int(i*1.075) for i in [0, 1178, 1297, 1417, 1536, 1655, 1775, 1895, 2015, 2134, 2253, 2373, 2492, 2613, 2732, 2851, 2971, 3090, 3209, 3330, 3449, 3568, 3688, 3807, 3928, 4047, 4166, 4286, 4405, 4524, 4645, 4764, 4883,
                                    5003, 5122, 5241, 5362, 5481, 5601, 5720, 5839, 5959, 6079, 6199, 6318, 6437, 6557, 6676, 6796, 6916, 7035, 7154, 7274, 7393, 7514, 7633, 7752, 7872, 7991, 8110, 8231, 8350, 8469, 8589, 8708, 8827, 8948, 9067, 9187, 9306, 9425]]
    hit2 = 1
    CD = 10
    TP成长 = 0.1
    TP上限 = 5

    def TP加成(self):
        return 1.0

    def 等效百分比(self, **argv):
        if self.TP等级 > 0:
            self.hit0 = 10+self.TP等级
            self.power1 = 1+self.TP等级 * self.TP成长
            self.power2 = 1+self.TP等级 * self.TP成长
        return super().等效百分比(**argv)


class 技能12(主动技能):
    名称 = '旋涡重拳'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    # 旋转多段攻击力：<int>% x 10
    data0 = [int(i*1.075) for i in [0, 595, 656, 717, 777, 838, 898, 958, 1019, 1080, 1140, 1201, 1261, 1321, 1382, 1443, 1503, 1564, 1624, 1684, 1745, 1806, 1866, 1927, 1987, 2047, 2108, 2168, 2229, 2290, 2350, 2410, 2471, 2531,
                                    2592, 2653, 2713, 2773, 2834, 2894, 2955, 3016, 3076, 3136, 3197, 3257, 3318, 3379, 3439, 3499, 3560, 3620, 3681, 3742, 3802, 3862, 3923, 3983, 4044, 4105, 4165, 4225, 4286, 4346, 4407, 4468, 4528, 4588, 4649, 4709, 4769]]
    hit0 = 10
    # 最后一击攻击力：<int>%
    data1 = [int(i*1.075) for i in [0, 8944, 9851, 10759, 11666, 12573, 13481, 14388, 15296, 16203, 17111, 18018, 18926, 19833, 20740, 21648, 22555, 23463, 24370, 25278, 26185, 27093, 28000, 28906, 29815, 30721, 31629, 32536, 33444, 34351, 35259, 36166, 37073, 37981,
                                    38888, 39796, 40703, 41611, 42518, 43426, 44333, 45240, 46148, 47055, 47963, 48870, 49778, 50685, 51593, 52500, 53407, 54315, 55222, 56130, 57037, 57945, 58852, 59760, 60667, 61573, 62482, 63388, 64296, 65203, 66111, 67018, 67925, 68833, 69740, 70648, 71555]]
    hit1 = 1
    CD = 20
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [158, 1327]
    无色消耗 = 1

    def 装备护石(self):
        self.power0 = 1.4
        self.power1 = 1.35


class 技能13(主动技能):
    名称 = '神圣组合拳'
    所在等级 = 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    # 第一击物理攻击力：<data0>%
    data0 = [int(i*1.074) for i in [0, 3264, 3595, 3925, 4256, 4588, 4919, 5251, 5581, 5912, 6243, 6575, 6906, 7236, 7568, 7899, 8230, 8562, 8893, 9223, 9555, 9886, 10217, 10549, 10879, 11210, 11542, 11873, 12204, 12535, 12866, 13197, 13529, 13860, 14190,
                                    14522, 14853, 15184, 15516, 15846, 16177, 16509, 16840, 17171, 17501, 17833, 18164, 18496, 18827, 19157, 19488, 19820, 20151, 20483, 20813, 21144, 21475, 21807, 22138, 22468, 22800, 23131, 23463, 23794, 24124, 24455, 24787, 25118, 25450, 25781, 26111]]
    hit0 = 1
    # 第二击物理攻击力：<data1>%
    data1 = [int(i*1.074) for i in [0, 4256, 4688, 5120, 5553, 5985, 6417, 6848, 7280, 7712, 8144, 8576, 9007, 9439, 9871, 10304, 10736, 11168, 11599, 12031, 12463, 12895, 13327, 13758, 14190, 14622, 15055, 15487, 15919, 16350, 16782, 17214, 17646, 18078, 18509,
                                    18941, 19373, 19806, 20238, 20670, 21101, 21533, 21965, 22397, 22829, 23260, 23692, 24124, 24557, 24989, 25421, 25852, 26284, 26716, 27148, 27580, 28011, 28443, 28876, 29308, 29740, 30172, 30603, 31035, 31467, 31899, 32331, 32762, 33194, 33627, 34059]]
    hit1 = 1
    # 第三击物理攻击力：<data2>%
    data2 = [int(i*1.074) for i in [0, 6669, 7346, 8022, 8699, 9376, 10053, 10730, 11406, 12083, 12759, 13436, 14112, 14789, 15466, 16142, 16819, 17496, 18173, 18850, 19526, 20203, 20879, 21556, 22232, 22909, 23586, 24262, 24939, 25615, 26293, 26970, 27646, 28323,
                                    28999, 29676, 30352, 31029, 31706, 32382, 33059, 33735, 34412, 35090, 35766, 36443, 37119, 37796, 38472, 39149, 39826, 40502, 41179, 41855, 42532, 43208, 43886, 44563, 45239, 45916, 46592, 47269, 47946, 48622, 49299, 49975, 50652, 51328, 52005, 52683, 53359]]
    hit2 = 1
    CD = 16
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    MP = [150, 1260]
    无色消耗 = 1

    def 装备护石(self):
        self.倍率 *= 1.26


class 技能14(主动技能):
    名称 = '极速飓风拳'
    所在等级 = 45
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    # 摆拳物理攻击力：<data0>%
    data0 = [int(i*1.075) for i in [0, 2192, 2415, 2638, 2859, 3082, 3305, 3527, 3750, 3971, 4195, 4417, 4639, 4862, 5085, 5307, 5529, 5752, 5973, 6197, 6420, 6641, 6864, 7086, 7309, 7532, 7753, 7977, 8199, 8421, 8644, 8867, 9089, 9311, 9533, 9756,
                                    9979, 10201, 10423, 10646, 10869, 11091, 11314, 11535, 11759, 11982, 12203, 12426, 12648, 12871, 13094, 13315, 13538, 13761, 13983, 14205, 14427, 14651, 14873, 15095, 15317, 15541, 15763, 15985, 16208, 16429, 16653, 16876, 17097, 17320, 17543]]
    hit0 = 10
    # 上勾拳物理攻击力：<data1>%
    data1 = [int(i*1.075) for i in [0, 9398, 10351, 11304, 12258, 13211, 14166, 15118, 16071, 17025, 17978, 18932, 19885, 20839, 21792, 22746, 23699, 24653, 25605, 26559, 27513, 28466, 29420, 30372, 31327, 32279, 33234, 34187, 35139, 36094, 37046, 38001, 38953, 39907,
                                    40861, 41814, 42768, 43721, 44674, 45627, 46581, 47535, 48488, 49441, 50395, 51348, 52302, 53255, 54209, 55162, 56116, 57069, 58022, 58976, 59929, 60883, 61836, 62790, 63742, 64697, 65650, 66603, 67557, 68509, 69464, 70416, 71371, 72324, 73277, 74231, 75184]]
    hit1 = 1
    CD = 45
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    MP = [311, 2612]
    无色消耗 = 2

    def 装备护石(self):
        self.power0 = 1.04
        self.hit0 = 6
        self.hit1 = 0
        self.CD = 15
        self.基础释放次数 = 2


class 技能15(被动技能):
    名称 = '干涸之泉'
    所在等级 = 48
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)


class 技能16(主动技能):
    名称 = '泯灭神击'
    所在等级 = 50
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    # 第1击物理攻击力：<data0>%
    data0 = [int(i) for i in [0, 8255, 10169, 12083, 13997, 15911, 17826, 19740, 21654, 23568, 25482, 27397, 29311, 31225, 33139, 35053, 36968, 38882, 40796, 42710, 44624, 46539, 48454, 50368, 52282, 54197, 56111, 58025, 59939, 61853, 63768, 65682, 67596, 69510, 71424, 73339,
                              75253, 77167, 79081, 80995, 82910, 84824, 86738, 88652, 90566, 92481, 94395, 96309, 98223, 100137, 102052, 103966, 105880, 107794, 109710, 111624, 113538, 115452, 117367, 119281, 121195, 123109, 125023, 126937, 128852, 130766, 132680, 134594, 136508, 138423, 140337]]
    hit0 = 1
    # 第2击物理攻击力：<data1>%
    data1 = [int(i) for i in [0, 12758, 15716, 18673, 21633, 24591, 27549, 30508, 33466, 36424, 39383, 42341, 45299, 48258, 51216, 54174, 57133, 60091, 63049, 66008, 68966, 71924, 74884, 77842, 80800, 83757, 86717, 89675, 92633, 95592, 98550, 101508, 104467, 107425, 110383, 113342,
                              116300, 119258, 122217, 125175, 128133, 131092, 134050, 137008, 139968, 142926, 145884, 148843, 151801, 154759, 157717, 160676, 163634, 166592, 169551, 172509, 175467, 178426, 181384, 184342, 187301, 190259, 193217, 196176, 199134, 202092, 205052, 208010, 210968, 213927, 216885]]
    hit1 = 1
    # 第3击物理攻击力：<data2>%
    data2 = [int(i) for i in [0, 16509, 20338, 24166, 27995, 31824, 35653, 39481, 43309, 47138, 50966, 54795, 58623, 62451, 66280, 70108, 73937, 77765, 81593, 85422, 89250, 93079, 96908, 100737, 104565, 108393, 112222, 116050, 119879, 123707, 127535, 131364, 135192, 139021, 142849, 146677,
                              150506, 154334, 158164, 161992, 165821, 169649, 173477, 177306, 181134, 184963, 188791, 192619, 196448, 200276, 204105, 207933, 211761, 215590, 219419, 223248, 227076, 230905, 234733, 238561, 242390, 246218, 250047, 253875, 257703, 261532, 265360, 269189, 273017, 276845, 280674]]
    hit2 = 1
    # 第4击物理攻击力：<data3>%
    data3 = [int(i) for i in [0, 37523, 46223, 54925, 63626, 72328, 81028, 89729, 98431, 107131, 115833, 124533, 133234, 141936, 150636, 159338, 168039, 176741, 185441, 194142, 202844, 211544, 220246, 228946, 237647, 246349, 255049, 263751, 272452, 281152, 289854, 298555, 307257, 315957, 324659,
                              333359, 342060, 350762, 359462, 368164, 376865, 385565, 394267, 402968, 411670, 420370, 429071, 437772, 446473, 455175, 463875, 472577, 481278, 489978, 498680, 507381, 516083, 524783, 533484, 542185, 550886, 559588, 568288, 576989, 585691, 594391, 603093, 611794, 620496, 629196, 637897]]
    hit3 = 1
    CD = 145.0

    MP = [800, 6720]
    无色消耗 = 5

    def 等效百分比(self, **argv):
        return super().等效百分比(**argv) * (1.1 if self.等级 >= 9 else 1)


class 技能17(主动技能):
    名称 = '破碎之拳'
    所在等级 = 60
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    # 连续物理攻击力：<data0>%
    data0 = [int(i*1.075) for i in [0, 1978, 2179, 2380, 2581, 2781, 2981, 3182, 3383, 3584, 3784, 3986, 4186, 4387, 4587, 4789, 4990, 5190, 5391, 5591, 5792, 5992, 6193, 6395, 6595, 6796, 6996, 7198, 7398, 7599, 7799, 8000, 8201, 8401, 8602, 8803,
                                    9004, 9204, 9405, 9606, 9807, 10008, 10209, 10410, 10609, 10810, 11010, 11212, 11412, 11613, 11815, 12015, 12216, 12416, 12618, 12818, 13019, 13218, 13419, 13621, 13821, 14022, 14223, 14424, 14624, 14825, 15027, 15227, 15428, 15627, 15829]]
    hit0 = 10
    # 最后下勾拳物理攻击：<data1>%
    data1 = [int(i*1.075) for i in [0, 4946, 5447, 5949, 6452, 6954, 7455, 7957, 8459, 8961, 9463, 9963, 10466, 10968, 11470, 11972, 12473, 12975, 13477, 13980, 14482, 14982, 15484, 15986, 16488, 16991, 17492, 17994, 18496, 18998, 19500, 20000, 20502, 21005, 21507,
                                    22009, 22510, 23012, 23514, 24016, 24519, 25019, 25521, 26023, 26525, 27027, 27528, 28030, 28533, 29035, 29537, 30038, 30539, 31041, 31544, 32046, 32548, 33049, 33551, 34053, 34554, 35057, 35558, 36060, 36562, 37064, 37566, 38067, 38569, 39072, 39573]]
    hit1 = 1
    # 爆炸物理攻击力：<data2>%
    data2 = [int(i*1.075) for i in [0, 8245, 9080, 9916, 10753, 11590, 12426, 13263, 14098, 14934, 15772, 16608, 17444, 18281, 19117, 19953, 20790, 21626, 22462, 23300, 24135, 24971, 25809, 26645, 27481, 28317, 29153, 29990, 30827, 31663, 32499, 33336, 34172, 35008,
                                    35845, 36681, 37518, 38354, 39190, 40026, 40864, 41700, 42536, 43372, 44209, 45045, 45882, 46718, 47553, 48391, 49227, 50064, 50900, 51737, 52574, 53409, 54245, 55083, 55919, 56755, 57591, 58428, 59264, 60101, 60937, 61773, 62610, 63446, 64282, 65119, 65956]]
    hit2 = 1
    CD = 35.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [350, 680]
    无色消耗 = 2

    def 装备护石(self):
        self.power0 = 1+0.3*1.78
        self.CDR *= 0.88


class 技能18(主动技能):
    名称 = '破坏之拳'
    所在等级 = 70
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    # 物理攻击力：<data0>%
    data0 = [int(i*1.074) for i in [0, 36911, 40655, 44401, 48145, 51889, 55635, 59379, 63123, 66869, 70613, 74357, 78103, 81847, 85591, 89337, 93081, 96825, 100571, 104315, 108059, 111805, 115549, 119293, 123039, 126783, 130527, 134273, 138017, 141761, 145507, 149251, 152995, 156741, 160485,
                                    164229, 167975, 171719, 175463, 179209, 182953, 186697, 190443, 194187, 197931, 201677, 205421, 209165, 212911, 216655, 220399, 224145, 227889, 231633, 235379, 239123, 242867, 246613, 250357, 254101, 257847, 261591, 265335, 269081, 272825, 276569, 280315, 284059, 287803, 291549, 295293]]
    hit0 = 1
    # 冲击波物理攻击力：<data1>%
    data1 = [int(i*1.074) for i in [0, 4101, 4517, 4932, 5349, 5765, 6181, 6597, 7014, 7429, 7845, 8261, 8678, 9094, 9509, 9925, 10342, 10758, 11174, 11589, 12006, 12422, 12838, 13254, 13671, 14086, 14502, 14919, 15335, 15751, 16166, 16583, 16999, 17415, 17831,
                                    18248, 18663, 19079, 19495, 19912, 20328, 20743, 21159, 21576, 21992, 22408, 22823, 23240, 23656, 24072, 24488, 24905, 25320, 25736, 26153, 26569, 26985, 27400, 27817, 28233, 28649, 29065, 29482, 29897, 30313, 30729, 31146, 31562, 31977, 32393, 32810]]
    hit1 = 1
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [350, 2700]
    无色消耗 = 2

    def 装备护石(self):
        self.倍率 *= 1.28


class 技能19(主动技能):
    名称 = '仲裁怒击'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    # 物理攻击力：<data0>%
    data0 = [int(i*1.074) for i in [0, 55109, 60700, 66290, 71881, 77472, 83063, 88655, 94245, 99836, 105427, 111018, 116608, 122199, 127790, 133381, 138971, 144562, 150153, 155745, 161335, 166926, 172517, 178108, 183698, 189289, 194880, 200471, 206061, 211652, 217243, 222835, 228426, 234016, 239607,
                                    245198, 250788, 256379, 261970, 267561, 273151, 278742, 284333, 289925, 295516, 301106, 306697, 312288, 317879, 323469, 329060, 334651, 340241, 345832, 351423, 357015, 362606, 368196, 373787, 379378, 384969, 390559, 396150, 401741, 407332, 412922, 418513, 424105, 429696, 435286, 440877]]
    hit0 = 1
    # 冲击波物理攻击力：<data1>%
    data1 = [int(i*1.074) for i in [0, 23618, 26014, 28411, 30806, 33202, 35598, 37994, 40390, 42787, 45183, 47579, 49975, 52370, 54766, 57163, 59559, 61955, 64351, 66747, 69144, 71540, 73935, 76331, 78727, 81123, 83520, 85916, 88312, 90708, 93104, 95501, 97896, 100292, 102688, 105084,
                                    107480, 109877, 112273, 114669, 117065, 119460, 121856, 124253, 126649, 129045, 131441, 133837, 136234, 138630, 141025, 143421, 145817, 148213, 150610, 153006, 155402, 157798, 160194, 162591, 164986, 167382, 169778, 172174, 174570, 176967, 179363, 181759, 184155, 186550, 188946]]
    hit1 = 1
    CD = 40.0
    是否有护石 = 1

    MP = [580, 4500]
    无色消耗 = 3

    def 装备护石(self):
        self.倍率 *= 1.36


class 技能20(被动技能):
    名称 = '正义惩戒'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


class 技能21(主动技能):
    名称 = '超重拳'
    所在等级 = 80
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.074) for i in [0, 17912, 19729, 21546, 23363, 25181, 26998, 28815, 30632, 32450, 34266, 36084, 37901, 39719, 41535, 43353, 45170, 46988, 48804, 50622, 52439, 54255, 56073, 57891, 59708, 61524, 63342, 65160, 66977, 68793, 70611, 72429, 74245, 76062, 77880, 79697,
                                    81514, 83331, 85149, 86966, 88783, 90600, 92418, 94234, 96052, 97869, 99687, 101503, 103321, 105138, 106956, 108772, 110590, 112407, 114223, 116041, 117859, 119676, 121492, 123310, 125128, 126945, 128761, 130579, 132396, 134213, 136030, 137848, 139665, 141482, 143299]]
    hit0 = 1
    data1 = [int(i*1.074) for i in [0, 71649, 78918, 86187, 93456, 100725, 107994, 115263, 122532, 129801, 137068, 144337, 151606, 158875, 166144, 173413, 180682, 187951, 195220, 202489, 209758, 217026, 224295, 231564, 238833, 246102, 253370, 260639, 267908, 275177, 282446, 289714, 296983, 304252,
                                    311521, 318790, 326059, 333328, 340597, 347866, 355135, 362404, 369671, 376940, 384209, 391478, 398747, 406016, 413285, 420554, 427823, 435092, 442361, 449629, 456898, 464167, 471435, 478704, 485973, 493242, 500511, 507780, 515049, 522318, 529586, 536855, 544124, 551393, 558662, 565931, 573200]]
    hit1 = 1
    CD = 50.0
    是否有护石 = 1

    MP = [800, 6000]
    无色消耗 = 5

    def 装备护石(self):
        self.倍率 *= 1.35


class 技能22(主动技能):
    名称 = '制裁：怒火疾风'
    所在等级 = 85
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    # 连续攻击物理攻击力：<data0>%
    data0 = [int(i) for i in [0, 4466, 5502, 6537, 7573, 8608, 9644, 10681, 11716, 12752, 13787, 14823, 15858, 16894, 17930, 18965, 20002, 21037, 22073, 23109, 24144, 25180, 26215, 27251, 28286, 29323, 30359, 31394, 32430, 33465, 34501, 35536, 36572, 37609, 38644,
                              39680, 40715, 41751, 42787, 43822, 44858, 45893, 46930, 47966, 49001, 50037, 51072, 52108, 53143, 54179, 55216, 56251, 57287, 58322, 59358, 60393, 61429, 62465, 63500, 64537, 65573, 66608, 67644, 68679, 69715, 70750, 71786, 72821, 73858, 74894, 75929]]
    hit0 = 19
    # 最后一击物理攻击力：<data1>%
    data1 = [int(i) for i in [0, 6513, 8025, 9535, 11046, 12556, 14067, 15577, 17089, 18599, 20109, 21620, 23130, 24641, 26151, 27662, 29172, 30684, 32194, 33704, 35215, 36725, 38236, 39746, 41258, 42768, 44279, 45789, 47300, 48810, 50320, 51832, 53342, 54853, 56363,
                              57874, 59384, 60896, 62406, 63916, 65427, 66937, 68448, 69958, 71470, 72980, 74491, 76001, 77512, 79022, 80532, 82043, 83553, 85065, 86575, 88086, 89596, 91107, 92617, 94127, 95639, 97149, 98660, 100170, 101681, 103191, 104703, 106213, 107724, 109234, 110744]]
    hit1 = 2
    # 最后一击的爆炸物理攻击力：<data2>%
    data2 = [int(i) for i in [0, 98646, 121521, 144395, 167270, 190145, 213019, 235894, 258769, 281644, 304518, 327393, 350268, 373142, 396017, 418892, 441766, 464641, 487516, 510390, 533265, 556140, 579014, 601889, 624764, 647638, 670513, 693388, 716262, 739137, 762012, 784886, 807761, 830636, 853510, 876385,
                              899260, 922134, 945009, 967884, 990757, 1013633, 1036508, 1059381, 1082256, 1105132, 1128005, 1150880, 1173755, 1196629, 1219504, 1242379, 1265254, 1288128, 1311003, 1333878, 1356752, 1379627, 1402502, 1425376, 1448251, 1471126, 1494000, 1516875, 1539750, 1562624, 1585499, 1608374, 1631248, 1654123, 1676998]]
    hit2 = 1
    CD = 180.0

    MP = [2500, 5000]
    无色消耗 = 10


class 技能23(主动技能):
    名称 = '正义铁拳'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    # 下捶冲击波攻击力：<int>%
    data0 = [int(i*1.076) for i in [0, 28833, 31758, 34684, 37609, 40534, 43459, 46385, 49310, 52235, 55159, 58086, 61010, 63935, 66860, 69786, 72711, 75636, 78562, 81487, 84412, 87337, 90263, 93188, 96112, 99037, 101963, 104888, 107813, 110738, 113664, 116589, 119514, 122439, 125365, 128290,
                                    131214, 134141, 137065, 139990, 142915, 145841, 148766, 151691, 154616, 157542, 160467, 163392, 166316, 169243, 172167, 175092, 178017, 180943, 183868, 186793, 189718, 192644, 195569, 198494, 201420, 204345, 207269, 210194, 213120, 216045, 218970, 221895, 224821, 227746, 230671]]
    hit0 = 1
    # 连续攻击攻击力：<int>% x <int>
    data1 = [int(i*1.076) for i in [0, 2162, 2382, 2601, 2821, 3039, 3259, 3478, 3698, 3917, 4137, 4355, 4575, 4794, 5014, 5234, 5453, 5672, 5891, 6111, 6330, 6550, 6769, 6989, 7207, 7427, 7647, 7866, 8086, 8305, 8524, 8743, 8963, 9182, 9402, 9622,
                                    9841, 10059, 10279, 10499, 10718, 10938, 11157, 11376, 11595, 11815, 12034, 12254, 12474, 12693, 12912, 13131, 13351, 13570, 13790, 14009, 14228, 14447, 14667, 14887, 15106, 15326, 15544, 15764, 15983, 16203, 16422, 16642, 16862, 17080, 17299]]
    hit1 = 20
    # 最后勾拳攻击力：<int>%
    data2 = [int(i*1.076) for i in [0, 72084, 79398, 86710, 94023, 101336, 108649, 115961, 123276, 130588, 137901, 145214, 152527, 159839, 167152, 174466, 181779, 189092, 196404, 203717, 211030, 218344, 225657, 232969, 240282, 247595, 254908, 262220, 269535, 276847, 284160, 291473, 298786, 306098,
                                    313412, 320725, 328038, 335351, 342663, 349976, 357289, 364603, 371916, 379228, 386541, 393854, 401167, 408481, 415794, 423106, 430419, 437732, 445045, 452357, 459671, 466984, 474297, 481610, 488922, 496235, 503549, 510862, 518175, 525487, 532800, 540113, 547426, 554740, 562053, 569365, 576678]]
    hit2 = 1
    CD = 60.0

    MP = [960, 7200]
    无色消耗 = 7


class 技能24(被动技能):
    名称 = '绝对正义'
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


class 技能25(主动技能):
    名称 = '正义执行：雷米迪奥斯的圣座'
    所在等级 = 100
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40
    data0 = [int(i) for i in [0, 201000, 247609, 294217, 340827, 387436, 434044, 480653, 527263, 573871, 620480, 667088, 713698, 760307, 806915, 853524, 900133, 946742, 993351, 1039959, 1086568, 1133178, 1179786, 1226395, 1273004, 1319613, 1366222, 1412830, 1459439, 1506049, 1552657, 1599266, 1645875, 1692484, 1739093, 1785701,
                              1832310, 1878920, 1925528, 1972137, 2018746, 2065355, 2111964, 2158572, 2205181, 2251791, 2298399, 2345008, 2391617, 2438226, 2484835, 2531443, 2578052, 2624662, 2671270, 2717879, 2764488, 2811097, 2857706, 2904315, 2950923, 2997533, 3044141, 3090750, 3137359, 3183968, 3230577, 3277186, 3323794, 3370404, 3417012]]
    hit0 = 1
    data1 = [int(i) for i in [0, 301501, 371413, 441327, 511240, 581153, 651067, 720980, 790894, 860807, 930720, 1000634, 1070547, 1140460, 1210374, 1280287, 1350201, 1420114, 1490026, 1559940, 1629853, 1699766, 1769680, 1839593, 1909506, 1979420, 2049333, 2119247, 2189160, 2259073, 2328987, 2398900, 2468812, 2538727, 2608639,
                              2678553, 2748466, 2818379, 2888293, 2958206, 3028119, 3098033, 3167946, 3237859, 3307773, 3377686, 3447600, 3517513, 3587425, 3657340, 3727252, 3797165, 3867079, 3936992, 4006906, 4076819, 4146732, 4216646, 4286559, 4356472, 4426386, 4496299, 4566213, 4636126, 4706038, 4775953, 4845865, 4915778, 4985692, 5055605, 5125518]]
    hit1 = 1
    CD = 290.0

    MP = [4027, 8055]
    无色消耗 = 15


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'infighter'
        self.名称 = '神启·蓝拳圣使'
        self.角色 = '圣职者(男)'
        self.角色类型 = '输出'
        self.职业 = '蓝拳圣使'
        # 用来筛CP武器的
        self.转职 = '蓝拳圣使'
        self.武器选项 = ['图腾', '战斧', '镰刀', '念珠', '十字架']
        self.输出类型选项 = ['物理百分比']
        self.防具精通属性 = ['力量']
        self.类型 = '物理百分比'
        self.武器类型 = '图腾'
        self.防具类型 = '轻甲'
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
        self.buff = 1.99

        super().__init__()
