from core.basic.skill import 技能
from core.basic.character import Character
from core.basic.skill import 主动技能, 被动技能


class 技能0(主动技能):
    名称 = '恶魔之手'
    备注 = '魔化'
    所在等级 = 10
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [28, 308]
    data0 = [int(i*1.2) for i in [0, 426, 469, 512, 555, 599, 642, 685, 728, 772, 815, 858, 901, 945, 988, 1031, 1074, 1117, 1161, 1204, 1247, 1290,
           1334, 1377, 1420, 1463, 1507, 1550, 1593, 1636, 1680, 1723, 1766, 1809, 1852, 1896, 1939, 1982, 2025, 2069, 2112,
           2155, 2198, 2242, 2285, 2328, 2371, 2415, 2458, 2501, 2544, 2587, 2631, 2674, 2717, 2760, 2804, 2847, 2890, 2933,
           2977, 3020, 3063, 3106, 3150, 3193, 3236, 3279, 3322, 3366, 3409]]
    hit0 = 1
    data1 = [int(i*1.2) for i in [0, 852, 938, 1025, 1111, 1198, 1284, 1371, 1457, 1544, 1630, 1717, 1803, 1890, 1976, 2062, 2149, 2235, 2322, 2408,
           2495, 2581, 2668, 2754, 2841, 2927, 3014, 3100, 3187, 3273, 3360, 3446, 3532, 3619, 3705, 3792, 3878, 3965, 4051,
           4138, 4224, 4311, 4397, 4484, 4570, 4657, 4743, 4830, 4916, 5002, 5089, 5175, 5262, 5348, 5435, 5521, 5608, 5694,
           5781, 5867, 5954, 6040, 6127, 6213, 6300, 6386, 6472, 6559, 6645, 6732, 6818]]
    hit1 = 1
    倍率 = 2.24
    CD = 6 * 1.6
    TP成长 = 0.10
    TP上限 = 7

    形态 = ["魔化", "常规"]

    def 形态变更(self, 形态, char:Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "魔化":
            self.倍率 = 2.24
            self.CD = 6 * 1.6
        if 形态 == "常规":
            self.倍率 = 1.0
            self.CD = 6


class 技能1(主动技能):
    名称 = '死亡切割'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [30, 336]
    data0 = [int(i*1.2) for i in [0, 221, 243, 265, 288, 310, 333, 355, 378, 400, 422, 445, 467, 490, 512, 535, 557, 579, 602, 624, 647, 669, 692, 714, 736, 759, 781, 804, 826, 849, 871, 893, 916, 938, 961, 983, 1006, 1028, 1050, 1073, 1095, 1118, 1140, 1163, 1185, 1207, 1230, 1252, 1275, 1297, 1320, 1342, 1364, 1387, 1409, 1432, 1454, 1477, 1499, 1521, 1544, 1566, 1589, 1611, 1634, 1656, 1678, 1701, 1723, 1746, 1768]]
    hit0 = 6
    倍率 = 2.25
    CD = 5 * 1.6
    TP成长 = 0.1
    TP上限 = 7

    形态 = ["魔化", "常规"]

    def 形态变更(self, 形态, char:Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "魔化":
            self.倍率 = 2.25
            self.CD = 5 * 1.6
        if 形态 == "常规":
            self.倍率 = 1.0
            self.CD = 5


class 技能2(主动技能):
    名称 = '恶魔之力'
    是否主动 = 0
    所在等级 = 15
    等级上限 = 30
    学习间隔 = 3
    等级精通 = 20
    data0 = [int(i) for i in [0, 1206, 1264, 1326, 1384, 1440, 1504, 1560, 1618, 1680, 1738, 1800, 1854, 1912, 1974, 2032, 2088, 2152, 2208, 2266, 2328, 2386, 2442, 2506, 2562, 2620, 2682, 2740, 2796, 2856, 2914, 2970, 3034, 3090, 3148, 3210, 3268, 3324, 3388, 3444, 3508, 3564, 3622, 3684, 3738, 3798, 3858, 3916, 3976, 4032, 4092, 4152, 4210, 4270, 4330, 4386, 4446, 4506, 4564, 4624, 4680, 4740, 4800, 4858, 4918, 4976, 5035, 5094, 5153, 5211, 5270]]
    hit0 = 1
    CD = 1 #实际无冷却
    TP成长 = 0.1
    TP上限 = 7


class 技能3(主动技能):
    名称 = '裂地锤'
    所在等级 = 20
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [30, 336]
    data0 = [int(i*1.101) for i in [0, 441, 487, 532, 577, 620, 668, 714, 759, 805, 852, 896, 943, 986, 1034, 1079, 1124, 1170, 1216, 1260, 1307, 1351,
           1397, 1444, 1488, 1534, 1582, 1625, 1670, 1716, 1761, 1809, 1852, 1899, 1942, 1990, 2036, 2081, 2127, 2174, 2218,
           2265, 2308, 2354, 2401, 2444, 2492, 2538, 2582, 2629, 2673, 2719, 2765, 2810, 2855, 2902, 2947, 2992, 3038, 3083,
           3128, 3176, 3221, 3266, 3312, 3357, 3402, 3448, 3494, 3539, 3585]]
    hit0 = 4
    倍率 = 2.0
    CD = 5 * 1.55
    TP成长 = 0.10
    TP上限 = 7

    形态 = ["魔化", "常规"]

    def 形态变更(self, 形态, char:Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "魔化":
            self.hit0 = 4
            self.倍率 = 2.0
            self.CD = 5 * 1.55
        if 形态 == "常规":
            self.hit0 = 3
            self.倍率 = 1.0
            self.CD = 5


class 技能4(被动技能):
    名称 = '镰刀精通'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10

    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.02 * self.等级, 5)


class 技能5(主动技能):
    名称 = '回旋飞镰'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [45, 462]
    data0 = [int(i*1.131) for i in [0, 674, 733, 794, 861, 942, 995, 1056, 1131, 1190, 1251, 1311, 1385, 1446, 1507, 1574, 1634, 1694, 1768, 1829, 1903, 1964, 2031, 2091, 2150, 2211, 2286, 2353, 2414, 2481, 2540, 2601, 2668, 2729, 2804, 2863, 2932, 2990, 3051, 3119, 3179, 3260, 3320, 3388, 3447, 3508, 3575, 3636, 3697, 3764, 3838, 3898, 3965, 4026, 4093, 4154, 4214, 4282, 4341, 4415, 4475, 4543, 4603, 4671, 4731, 4797, 4858, 4933, 4993, 5060, 5121]]
    hit0 = 3
    data1 = [int(i*1.131) for i in [0, 396, 438, 480, 520, 558, 601, 643, 681, 723, 765, 807, 846, 888, 930, 970, 1012, 1054, 1093, 1135, 1174, 1216, 1256, 1298, 1340, 1382, 1421, 1461, 1503, 1544, 1584, 1626, 1667, 1708, 1748, 1789, 1830, 1872, 1914, 1954, 1996, 2034, 2076, 2116, 2158, 2200, 2240, 2282, 2324, 2364, 2402, 2444, 2485, 2527, 2567, 2609, 2651, 2691, 2733, 2772, 2814, 2854, 2896, 2937, 2978, 3019, 3061, 3100, 3142, 3182, 3224]]
    hit1 = 4
    倍率 = 1.9
    CD = 10 * 1.5
    TP成长 = 0.10
    TP上限 = 7

    形态 = ["魔化", "常规"]

    def 形态变更(self, 形态, char:Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "魔化":
            self.hit0 = 3
            self.hit1 = 4
            self.倍率 = 1.9
            self.CD = 10 * 1.5
        if 形态 == "常规":
            self.hit0 = 5
            self.hit1 = 2
            self.倍率 = 1.0
            self.CD = 10


class 技能6(主动技能):
    名称 = '复仇之刺'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [45, 462]
    data0 = [int(i*1.213) for i in [0, 2795, 3079, 3362, 3646, 3930, 4213, 4497, 4780, 5064, 5348, 5631, 5915, 6198, 6482, 6766, 7049, 7333, 7616, 7900, 8184, 8467, 8751, 9034, 9318, 9602, 9885, 10169, 10453, 10736, 11020, 11303, 11587, 11871, 12154, 12438, 12721, 13005, 13289, 13572, 13856, 14139, 14423, 14707, 14990, 15274, 15558, 15841, 16125, 16408, 16692, 16976, 17259, 17543, 17826, 18110, 18394, 18677, 18961, 19244, 19528, 19812, 20095, 20379, 20662, 20946, 21230, 21513, 21797, 22081, 22364]]
    hit0 = 1
    data1 = [int(i*1.213) for i in [0, 4072, 4484, 4897, 5312, 5724, 6137, 6550, 6963, 7375, 7789, 8203, 8616, 9029, 9441, 9855, 10267, 10680, 11095, 11507, 11921, 12333, 12746, 13160, 13573, 13986, 14400, 14812, 15225, 15638, 16051, 16467, 16879, 17291, 17705, 18117, 18529, 18943, 19358, 19771, 20184, 20595, 21010, 21421, 21836, 22250, 22662, 23074, 23489, 23900, 24313, 24729, 25141, 25555, 25967, 26380, 26793, 27206, 27620, 28033, 28446, 28858, 29272, 29684, 30096, 30512, 30924, 31338, 31750, 32163, 32577]]
    hit1 = 1
    CD = 10 * 1.6
    TP成长 = 0.10
    TP上限 = 7

    形态 = ["魔化", "常规"]

    def 形态变更(self, 形态, char:Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "魔化":
            self.hit0 = 1
            self.hit1 = 1
            self.CD = 10 * 1.6
        if 形态 == "常规":
            self.hit0 = 1
            self.hit1 = 0
            self.CD = 10


class 技能7(被动技能):
    名称 = '恶魔诅咒'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10
    关联技能 = ['不朽战吼', '地狱之门', '厄运之轮', '恶魔之拳', '恶魔之手', '恶魔之握', '复仇之刺', '黑暗权能',
            '回旋飞镰', '毁灭强击', '裂地锤', '末日浩劫', '死亡切割','恶魔之力', '永堕：混沌弑神', '审判', '极恶洪流', '末日福音：毁灭之翼']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.03 * self.等级, 5)


class 技能8(主动技能):
    名称 = '厄运之轮'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [180, 1512]
    data0 = [int(i*1.25) for i in [0, 685, 754, 824, 894, 963, 1033, 1102, 1172, 1241, 1311, 1380, 1450, 1519, 1589, 1658, 1728, 1797, 1867, 1937, 2006, 2076, 2145, 2215, 2284, 2354, 2423, 2493, 2562, 2632, 2701, 2771, 2841, 2910, 2980, 3049, 3119, 3188, 3258, 3327, 3397, 3466, 3536, 3605, 3675, 3744, 3814, 3884, 3953, 4023, 4092, 4162, 4231, 4301, 4370, 4440, 4509, 4579, 4648, 4718, 4787, 4857, 4927, 4996, 5066, 5135, 5205, 5274, 5344, 5413, 5483]]
    hit0 = 6
    倍率 = 2.34
    CD = 16 * 1.5
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    形态 = ["魔化", "常规"]

    def 形态变更(self, 形态, char:Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "魔化":
            self.hit0 = 6
            self.倍率 = 2.34
            self.CD = 16 * 1.5
        if 形态 == "常规":
            self.hit0 = 9
            self.倍率 = 1.0
            self.CD = 16

    def 装备护石(self):
        self.倍率 *= 1.34


class 技能9(主动技能):
    名称 = '恶魔之拳'
    所在等级 = 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    #魔化
    data0 = [int(i) for i in [0, 230, 254, 277, 301, 324, 348, 372, 395, 419, 442, 466, 489, 512, 535, 559, 582, 606, 629, 653, 677, 700, 724, 747, 771, 794, 818, 841, 865, 889, 911, 934, 958, 982, 1005, 1029, 1052, 1076, 1099, 1123, 1147, 1170, 1194, 1217, 1241, 1264, 1287, 1310, 1334, 1357, 1381, 1404, 1428, 1452, 1475, 1499, 1522, 1546, 1569, 1593, 1616, 1640, 1664, 1686, 1709, 1733, 1757, 1780, 1804, 1827, 1851]]
    hit0= 10
    data1 = [int(i) for i in [0, 8949, 9858, 10765, 11673, 12581, 13489, 14397, 15305, 16213, 17120, 18029, 18937, 19844, 20752, 21661, 22569, 23476, 24384, 25293, 26201, 27108, 28016, 28925, 29833, 30740, 31648, 32557, 33465, 34372, 35280, 36189, 37097, 38004, 38912, 39821, 40729, 41636, 42544, 43452, 44361, 45268, 46176, 47084, 47992, 48900, 49808, 50716, 51624, 52532, 53440, 54347, 55256, 56164, 57072, 57979, 58888, 59796, 60704, 61611, 62520, 63428, 64336, 65243, 66152, 67060, 67968, 68875, 69783, 70692, 71600]]
    hit1 = 1
    #常规
    data3 = [int(i) for i in [0, 178, 197, 215, 233, 251, 270, 287, 306, 324, 342, 360, 379, 396, 415, 434, 451, 469, 488, 505, 524, 543, 560, 579, 597, 615, 633, 652, 669, 688, 706, 724, 742, 761, 778, 797, 815, 833, 851, 870, 887, 906, 925, 942, 961, 979, 996, 1015, 1034, 1051, 1070, 1088, 1106, 1124, 1143, 1160, 1179, 1197, 1215, 1233, 1252, 1269, 1288, 1306, 1324, 1342, 1361, 1378, 1397, 1416, 1433]]
    hit3 = 0
    data4 = [int(i) for i in [0, 6591, 7260, 7929, 8598, 9267, 9936, 10604, 11274, 11942, 12610, 13280, 13950, 14618, 15286, 15955, 16623, 17294, 17962, 18631, 19299, 19967, 20638, 21306, 21975, 22643, 23312, 23981, 24651, 25319, 25987, 26656, 27325, 27994, 28663, 29332, 30000, 30670, 31338, 32006, 32676, 33346, 34014, 34682, 35351, 36019, 36690, 37358, 38027, 38695, 39363, 40032, 40703, 41371, 42039, 42708, 43377, 44047, 44715, 45384, 46052, 46721, 47390, 48059, 48728, 49396, 50066, 50734, 51402, 52072, 52740]]
    hit4 = 0
    CD = 20
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [300, 2604]
    无色消耗 = 1

    形态 = ["魔化", "常规"]

    def 形态变更(self, 形态, char:Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "魔化":
            self.hit0 = 1
            self.hit1 = 1
            self.hit2 = 0
            self.hit3 = 0
        if 形态 == "常规":
            self.hit0 = 0
            self.hit1 = 0
            self.hit2 = 1
            self.hit3 = 1

    def 装备护石(self,):
        self.power0 = 1.1
        self.power1 = 1.1*1.27
        self.power2 = 1.1
        self.power3 = 1.1*1.27
        self.CDR *= 0.85


class 技能10(主动技能):
    名称 = '恶魔之握'
    所在等级 = 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    #魔化
    data0 = [int(i) for i in [0, 631, 696, 761, 825, 888, 953, 1017, 1082, 1145, 1210, 1275, 1338, 1403, 1466, 1531, 1596, 1660, 1723, 1788, 1852, 1917, 1980, 2045, 2110, 2173, 2237, 2302, 2366, 2431, 2493, 2558, 2623, 2687, 2751, 2815, 2880, 2945, 3007, 3072, 3137, 3201, 3266, 3328, 3393, 3458, 3522, 3586, 3650, 3715, 3780, 3842, 3907, 3972, 4036, 4100, 4163, 4228, 4293, 4356, 4421, 4486, 4550, 4613, 4677, 4742, 4807, 4870, 4935, 4998, 5063]]
    hit0 = 2
    data1 = [int(i) for i in [0, 13601, 14980, 16360, 17741, 19120, 20500, 21878, 23258, 24640, 26018, 27398, 28778, 30157, 31538, 32918, 34297, 35677, 37057, 38437, 39817, 41197, 42576, 43956, 45337, 46716, 48096, 49476, 50856, 52236, 53616, 54995, 56375, 57756, 59135, 60515, 61895, 63273, 64655, 66035, 67413, 68793, 70175, 71553, 72933, 74312, 75692, 77073, 78452, 79832, 81212, 82591, 83972, 85352, 86731, 88111, 89491, 90871, 92251, 93631, 95010, 96390, 97771, 99150, 100530, 101910, 103288, 104670, 106050, 107428, 108808]]
    hit1 = 1
    #常规
    data2 = [int(i) for i in [0, 537, 592, 646, 701, 756, 811, 865, 920, 975, 1028, 1083, 1138, 1192, 1247, 1302, 1356, 1411, 1466, 1520, 1575, 1630, 1685, 1738, 1793, 1848, 1902, 1957, 2012, 2066, 2121, 2176, 2230, 2285, 2340, 2393, 2448, 2503, 2558, 2612, 2667, 2722, 2776, 2831, 2886, 2940, 2995, 3050, 3103, 3158, 3213, 3267, 3322, 3377, 3432, 3486, 3541, 3596, 3650, 3705, 3760, 3813, 3868, 3923, 3977, 4032, 4087, 4141, 4196, 4251, 4305]]
    hit2 = 2
    data3 = [int(i) for i in [0, 11252, 12395, 13536, 14677, 15820, 16961, 18102, 19245, 20386, 21527, 22670, 23811, 24952, 26095, 27236, 28377, 29520, 30661, 31802, 32945, 34086, 35227, 36370, 37511, 38652, 39795, 40936, 42077, 43220, 44361, 45502, 46645, 47786, 48927, 50070, 51211, 52352, 53495, 54636, 55777, 56920, 58061, 59202, 60345, 61486, 62627, 63770, 64911, 66052, 67195, 68336, 69477, 70620, 71761, 72902, 74045, 75186, 76327, 77470, 78611, 79752, 80895, 82036, 83177, 84320, 85461, 86602, 87745, 88886, 90027]]
    hit3 = 1
    CD = 30
    TP成长 = 0.10
    TP上限 = 5

    MP = [300, 2604]
    无色消耗 = 1

    形态 = ["魔化", "常规"]

    def 形态变更(self, 形态, char:Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "魔化":
            self.hit0 = 2
            self.hit1 = 1
            self.hit2 = 0
            self.hit3 = 0
        if 形态 == "常规":
            self.hit0 = 0
            self.hit1 = 0
            self.hit2 = 2
            self.hit3 = 1


class 技能11(主动技能):
    名称 = '黑暗权能'

    所在等级 = 45
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.102) for i in [0, 625, 688, 752, 815, 878, 942, 1006, 1068, 1132, 1196, 1259, 1323, 1385, 1449, 1513, 1577, 1640, 1703, 1766, 1830, 1894, 1956, 2020, 2084, 2147, 2211, 2274, 2337, 2401, 2465, 2527, 2591, 2655, 2718, 2782, 2844, 2908, 2972, 3036, 3099, 3162, 3225, 3289, 3353, 3415, 3479, 3543, 3606, 3670, 3733, 3796, 3860, 3924, 3987, 4050, 4114, 4177, 4241, 4303, 4367, 4431, 4495, 4558, 4621, 4684, 4748, 4812, 4876, 4938, 5002]]
    hit0 = 1
    data1 = [int(i*1.102) for i in [0, 371, 408, 446, 484, 522, 559, 597, 635, 673, 709, 747, 785, 823, 860, 898, 936, 974, 1011, 1049, 1087, 1125, 1161, 1199, 1237, 1275, 1312, 1350, 1388, 1426, 1463, 1501, 1539, 1575, 1613, 1651, 1689, 1726, 1764, 1802, 1840, 1877, 1915, 1953, 1991, 2027, 2065, 2103, 2141, 2178, 2216, 2254, 2292, 2329, 2367, 2405, 2443, 2479, 2517, 2555, 2593, 2630, 2668, 2706, 2744, 2781, 2819, 2857, 2895, 2931, 2969]]
    hit1 = 32
    data2 = [int(i*1.102) for i in [0, 5884, 6480, 7078, 7673, 8271, 8868, 9466, 10062, 10658, 11255, 11852, 12450, 13046, 13644, 14239, 14837, 15434, 16030, 16628, 17224, 17821, 18418, 19016, 19612, 20210, 20805, 21402, 22000, 22596, 23194, 23790, 24387, 24984, 25582, 26178, 26774, 27371, 27968, 28566, 29162, 29759, 30356, 30953, 31550, 32146, 32743, 33340, 33937, 34534, 35132, 35727, 36325, 36922, 37518, 38116, 38711, 39309, 39906, 40503, 41100, 41698, 42293, 42891, 43488, 44084, 44682, 45277, 45875, 46472, 47069]]
    hit2 = 1
    CD = 40
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [350, 2940]
    无色消耗 = 2

    形态 = ["魔化", "常规"]

    def 形态变更(self, 形态, char:Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "魔化":
            self.hit0 = 1
            self.hit1 = 32
            self.hit2 = 1
        if 形态 == "常规":
            self.hit0 = 1
            self.hit1 = 32
            self.hit2 = 0

    def 装备护石(self):
        self.hit1 = 42
        self.power1 = 1.09
        self.CDR *= 0.9


class 技能12(被动技能):
    名称 = '恶魔唤醒'
    所在等级 = 48
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40
    关联技能 = ['不朽战吼', '地狱之门', '厄运之轮', '恶魔之拳', '恶魔之手', '恶魔之握', '复仇之刺', '黑暗权能',
            '回旋飞镰', '毁灭强击', '裂地锤', '末日浩劫', '死亡切割','恶魔之力', '永堕：混沌弑神', '极恶洪流', '末日福音：毁灭之翼']
    关联技能2 = ['魔化：末日审判者']
    关联技能3 = ['审判']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.015 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.01 * self.等级, 5)

    def 加成倍率3(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.02 * self.等级, 5)


class 技能13(主动技能):
    名称 = '魔化：末日审判者'
    所在等级 = 50
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i*1.15) for i in [0, 822, 943, 1063, 1183, 1303, 1425, 1546, 1665, 1787, 1906, 2028, 2148, 2268, 2388, 2510, 2628, 2749, 2870, 2989, 3109, 3230, 3351, 3470, 3591, 3710, 3831, 3951, 4072, 4192, 4312, 4432, 4553, 4673, 4793, 4914, 5034, 5153, 5274, 5395, 5513]]
    hit0 = 0
    data1 = [int(i*1.15) for i in [0, 983, 1145, 1307, 1469, 1630, 1792, 1954, 2115, 2280, 2440, 2602, 2765, 2926, 3088, 3249, 3410, 3572, 3735, 3897, 4057, 4219, 4381, 4543, 4704, 4865, 5027, 5188, 5351, 5513, 5673, 5836, 5997, 6159, 6321, 6481, 6644, 6806, 6967, 7130, 7291]]
    hit1 = 0
    data2 = [int(i*1.15) for i in [0, 1503, 1800, 2097, 2393, 2688, 2986, 3281, 3577, 3876, 4173, 4468, 4765, 5061, 5357, 5654, 5950, 6245, 6543, 6839, 7135, 7431, 7728, 8024, 8319, 8616, 8912, 9209, 9505, 9801, 10097, 10395, 10689, 10985, 11283, 11578, 11873, 12171, 12467, 12765, 13059]]
    hit2 = 0
    data3 = [int(i*1.15) for i in [0, 1603, 1926, 2249, 2571, 2891, 3215, 3536, 3859, 4183, 4506, 4826, 5150, 5473, 5795, 6117, 6439, 6760, 7083, 7405, 7727, 8048, 8372, 8694, 9015, 9338, 9660, 9981, 10305, 10626, 10947, 11271, 11591, 11914, 12238, 12558, 12880, 13203, 13524, 13847, 14169]]
    hit3 = 0
    data4 = [int(i) for i in [0, 1817, 2199, 2589, 2972, 3356, 3744, 4128, 4512, 4900, 5284, 5669, 6054, 6438, 6825, 7209, 7592, 7978, 8362, 8749, 9132, 9518, 9901, 10287, 10673, 11057, 11442, 11827, 12213, 12599, 12982, 13368, 13751, 14135, 14522, 14906, 15290, 15676, 16060, 16446, 16831]]
    hit4 = 0
    data5 = [int(i) for i in [0, 2220, 2707, 3202, 3689, 4180, 4670, 5160, 5645, 6139, 6627, 7118, 7607, 8096, 8587, 9075, 9564, 10055, 10543, 11031, 11521, 12011, 12500, 12991, 13479, 13967, 14458, 14947, 15437, 15927, 16415, 16906, 17394, 17884, 18374, 18862, 19351, 19843, 20330, 20819, 21309]]
    hit5 = 0
    CD = 200 #变身CD

    形态 = ["变身", "普通攻击", "恶魔之爪", "恶魔之爪(蓄气)"]

    def 形态变更(self, 形态, char:Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "变身":
            self.hit0 = 0
            self.hit1 = 0
            self.hit2 = 0
            self.hit3 = 0
            self.hit4 = 0
            self.hit5 = 0
        if 形态 == "普通攻击":
            self.hit0 = 2
            self.hit1 = 2
            self.hit2 = 2
            self.hit3 = 2
            self.hit4 = 0
            self.hit5 = 0
            #self.CD = 1 #有实际CD
        if 形态 == "恶魔之爪":
            self.hit0 = 0
            self.hit1 = 0
            self.hit2 = 0
            self.hit3 = 0
            self.hit4 = 1
            self.hit5 = 0
            #self.CD = 2 #有实际CD
        if 形态 == "恶魔之爪(蓄气)":
            self.hit0 = 0
            self.hit1 = 0
            self.hit2 = 0
            self.hit3 = 0
            self.hit4 = 0
            self.hit5 = 1
            #self.CD = 2 #有实际CD

    MP = [1500, 12600]
    无色消耗 = 5

    关联技能 = ['所有']
    def 魔法攻击力倍率进图(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1.15


class 技能14(主动技能):
    名称 = '审判'
    所在等级 = 50
    等级上限 = 1
    学习间隔 = 1
    基础等级 = 1
    MP = [0, 0]
    #原地
    data0 = [int(i) for i in [0, 10504, 12940, 15377, 17812, 20248, 22684, 25121, 27557, 29993, 32429, 34865, 37300, 39736, 42172, 44608, 47044, 49480, 51916, 54353, 56787, 59224, 61660, 64096, 66532, 68968, 71404, 73840, 76275, 78711, 81149, 83585, 86021, 88457, 90893, 93329, 95764, 98200, 100636, 103072, 105508]]
    hit0 = 1
    data1 = [int(i) for i in [0, 29898, 36832, 43765, 50698, 57631, 64565, 71497, 78431, 85365, 92298, 99231, 106165, 113097, 120030, 126963, 133897, 140831, 147763, 154697, 161631, 168562, 175496, 182429, 189363, 196296, 203229, 210163, 217097, 224028, 230962, 237896, 244828, 251762, 258696, 265629, 272562, 279494, 286428, 293361, 300294]]
    hit1 = 1
    #拖动，可抓取
    data2 = [int(i) for i in [0, 4725, 5821, 6916, 8012, 9108, 10203, 11300, 12396, 13491, 14587, 15683, 16778, 17875, 18970, 20066, 21162, 22257, 23353, 24450, 25545, 26641, 27737, 28832, 29928, 31025, 32120, 33216, 34312, 35407, 36503, 37600, 38695, 39791, 40887, 41982, 43078, 44173, 45270, 46366, 47461]]
    hit2 = 0
    data3 = [int(i) for i in [0, 933, 1151, 1367, 1585, 1801, 2018, 2235, 2452, 2667, 2885, 3101, 3318, 3535, 3752, 3968, 4186, 4402, 4620, 4835, 5052, 5268, 5486, 5702, 5920, 6136, 6353, 6570, 6787, 7002, 7220, 7436, 7653, 7870, 8087, 8303, 8521, 8737, 8955, 9170, 9387]]
    hit3 = 0
    data4 = [int(i) for i in [0, 2907, 3581, 4256, 4930, 5605, 6280, 6953, 7627, 8302, 8976, 9650, 10325, 11000, 11673, 12348, 13022, 13697, 14371, 15045, 15720, 16395, 17068, 17743, 18417, 19091, 19766, 20440, 21113, 21790, 22463, 23137, 23812, 24486, 25161, 25835, 26508, 27185, 27858, 28532, 29207]]
    hit4 = 0
    data5 = [int(i) for i in [0, 11268, 13881, 16495, 19107, 21721, 24333, 26946, 29560, 32173, 34786, 37400, 40012, 42625, 45238, 47851, 50465, 53078, 55691, 58305, 60916, 63530, 66143, 68756, 71370, 73982, 76596, 79208, 81821, 84435, 87048, 89661, 92275, 94887, 97500, 100113, 102726, 105340, 107953, 110566, 113180]]
    hit5 = 0
    #拖动，不可抓取
    data6 = [int(i) for i in [0, 25691, 31657, 37610, 43575, 49531, 55496, 61447, 67415, 73367, 79332, 85286, 91253, 97205, 103171, 109125, 115090, 121042, 127008, 132962, 138927, 144881, 150847, 156798, 162766, 168720, 174685, 180638, 186603, 192556, 198523, 204476, 210441, 216396, 222361, 228312, 234280, 240232, 246198, 252153, 258118]]
    hit6 = 0
    倍率 = 1.1

    形态 = ["原地(魔化)", "原地(常规)", "拖动&可抓取(魔化)", "拖动&可抓取(常规)", "拖动&不可抓取(魔化)", "拖动&不可抓取(常规)"]

    def 形态变更(self, 形态, char:Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "原地(魔化)":
            self.hit0 = 1
            self.hit1 = 1
            self.倍率 = 1.1
        if 形态 == "原地(魔化)":
            self.hit0 = 1
            self.hit1 = 1
            self.倍率 = 1.0
        if 形态 == "拖动&可抓取(魔化)":
            self.hit0 = 0
            self.hit1 = 0
            self.hit2 = 2
            self.hit3 = 14
            self.hit4 = 1
            self.hit5 = 1
            self.倍率 = 1.1
        if 形态 == "拖动&可抓取(常规)":
            self.hit0 = 0
            self.hit1 = 0
            self.hit2 = 2
            self.hit3 = 14
            self.hit4 = 1
            self.hit5 = 1
            self.倍率 = 1.0
        if 形态 == "拖动&不可抓取(魔化)":
            self.hit0 = 0
            self.hit1 = 0
            self.hit6 = 1
            self.倍率 = 1.1
        if 形态 == "拖动&不可抓取(常规)":
            self.hit0 = 0
            self.hit1 = 0
            self.hit6 = 1
            self.倍率 = 1.0


class 技能15(主动技能):
    名称 = '地狱之门'
    所在等级 = 60
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.181) for i in [0, 1467, 1614, 1763, 1911, 2060, 2210, 2357, 2506, 2656, 2803, 2952, 3102, 3249, 3399, 3546, 3695, 3845, 3992, 4142, 4291, 4438, 4588, 4737, 4884, 5034, 5182, 5331, 5480, 5629, 5777, 5926, 6075, 6223, 6373, 6521, 6669, 6816, 6967, 7115, 7263, 7413, 7562, 7709, 7860, 8008, 8155, 8306, 8453, 8601, 8752, 8899, 9047, 9198, 9345, 9494, 9643, 9792, 9940, 10087, 10238, 10386, 10533, 10684, 10832, 10979, 11130, 11278, 11425, 11576, 11723]]
    hit0 = 8
    倍率 = 1.5
    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [600, 1680]
    无色消耗 = 1

    形态 = ["魔化", "常规"]

    def 形态变更(self, 形态, char:Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "魔化":
            self.倍率 = 1.5
        if 形态 == "常规":
            self.倍率 = 1.0

    def 装备护石(self):
        self.hit0 = 9
        self.倍率 *= 1.08
        self.CDR *= 0.88


class 技能16(主动技能):
    名称 = '末日浩劫'
    所在等级 = 70
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.219) for i in [0, 20616, 22708, 24800, 26891, 28983, 31075, 33165, 35257, 37349, 39440, 41532, 43624, 45716, 47807, 49898, 51990, 54081, 56173, 58265, 60356, 62448, 64540, 66631, 68722, 70814, 72906, 74997, 77089, 79181, 81271, 83363, 85455, 87546, 89638, 91730, 93822, 95913, 98004, 100096, 102187, 104279, 106371, 108462, 110554, 112646, 114737, 116828, 118920, 121012, 123103, 125195, 127287, 129377, 131469, 133561, 135653, 137744, 139836, 141928, 144019, 146110, 148202, 150293, 152385, 154477, 156569, 158660, 160752, 162843, 164934]]
    hit0 = 1
    倍率 = 1.35
    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [1200, 2520]
    无色消耗 = 2

    形态 = ["魔化", "常规"]

    def 形态变更(self, 形态, char:Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "魔化":
            self.倍率 = 1.35
        if 形态 == "常规":
            self.倍率 = 1.0

    def 装备护石(self):
        self.倍率 *= 1.08*1.18


class 技能17(主动技能):
    名称 = '不朽战吼'
    备注 = '追加操作'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i) for i in [0, 13527, 14900, 16274, 17645, 19018, 20389, 21762, 23135, 24508, 25881, 27253, 28624, 29998, 31369, 32742, 34116, 35487, 36859, 38233, 39604, 40977, 42350, 43722, 45094, 46468, 47839, 49212, 50586, 51957, 53329, 54703, 56075, 57447, 58821, 60191, 61563, 62937, 64309, 65682, 67055, 68426, 69798, 71172, 72544, 73916, 75290, 76663, 78033, 79406, 80780, 82151, 83525, 84895, 86268, 87641, 89013, 90386, 91759, 93130, 94503, 95876, 97249, 98621, 99994, 101367, 102738, 104110, 105484, 106856, 108228]]
    hit0 = 0
    data1 = [int(i) for i in [0, 9471, 10432, 11393, 12354, 13315, 14277, 15237, 16199, 17159, 18121, 19083, 20042, 21004, 21965, 22927, 23887, 24847, 25809, 26768, 27730, 28692, 29652, 30614, 31574, 32535, 33497, 34458, 35419, 36379, 37341, 38302, 39261, 40223, 41184, 42144, 43105, 44067, 45029, 45988, 46950, 47910, 48872, 49832, 50794, 51755, 52716, 53678, 54636, 55598, 56560, 57519, 58481, 59442, 60404, 61365, 62325, 63287, 64249, 65209, 66170, 67130, 68092, 69053, 70012, 70974, 71935, 72897, 73857, 74818, 75780]]
    hit1 = 5
    data2 = [int(i) for i in [0, 3384, 3730, 4073, 4413, 4757, 5102, 5443, 5789, 6132, 6477, 6821, 7163, 7506, 7848, 8194, 8537, 8880, 9226, 9566, 9910, 10255, 10597, 10940, 11286, 11627, 11970, 12314, 12657, 13002, 13345, 13689, 14033, 14375, 14719, 15061, 15404, 15750, 16092, 16434, 16778, 17122, 17466, 17810, 18154, 18496, 18839, 19185, 19527, 19869, 20213, 20558, 20900, 21245, 21588, 21929, 22275, 22617, 22960, 23304, 23649, 23993, 24334, 24678, 25021, 25363, 25709, 26052, 26395, 26741, 27082]]
    hit2 = 2 #追加操作

    CD = 40
    是否有护石 = 1

    MP = [580, 4500]
    无色消耗 = 3

    形态 = ["魔化", "常规"]

    def 形态变更(self, 形态, char:Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "魔化":
            self.hit0 = 0
            self.hit1 = 5
            self.hit2 = 2
        if 形态 == "常规":
            self.hit0 = 5
            self.hit1 = 0
            self.hit2 = 2

    def 装备护石(self):
        self.倍率 *= 1.29
        self.CDR *= 0.86


class 技能18(被动技能):
    名称 = '原罪之力'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40
    # 这里有个问题，关联技能1中实际应该还有魔化：末日审判者中的恶魔之爪部分，但恶魔之爪没单独拆出来
    关联技能 = ['不朽战吼', '地狱之门', '厄运之轮', '恶魔之拳', '恶魔之手', '恶魔之握', '复仇之刺', '黑暗权能',
            '回旋飞镰', '毁灭强击', '裂地锤', '末日浩劫', '死亡切割', '永堕：混沌弑神', '极恶洪流', '末日福音：毁灭之翼']
    关联技能2 = ['恶魔之力']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.17 + 0.02 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.09 + 0.015 * self.等级, 5)

class 技能19(主动技能):
    名称 = '毁灭强击'
    备注 = '追加操作'
    所在等级 = 80
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.231) for i in [0, 5066, 5580, 6094, 6609, 7123, 7636, 8150, 8664, 9179, 9692, 10206, 10720, 11235, 11749, 12262, 12776, 13291, 13805, 14318, 14832, 15346, 15861, 16375, 16888, 17402, 17917, 18431, 18945, 19458, 19973, 20487, 21001, 21514, 22028, 22543, 23057, 23571, 24084, 24599, 25113, 25627, 26140, 26655, 27169, 27683, 28197, 28710, 29225, 29739, 30253, 30768, 31281, 31795, 32309, 32823, 33337, 33851, 34365, 34879, 35394, 35907, 36421, 36935, 37450, 37964, 38477, 38991, 39505, 40020, 40533]]
    hit0 = 1
    data1 = [int(i*1.231) for i in [0, 23644, 26042, 28441, 30840, 33237, 35637, 38036, 40435, 42834, 45232, 47631, 50030, 52429, 54827, 57226, 59625, 62024, 64422, 66820, 69220, 71619, 74016, 76416, 78815, 81214, 83612, 86011, 88410, 90809, 93206, 95606, 98005, 100403, 102803, 105201, 107599, 109999, 112398, 114795, 117195, 119594, 121991, 124391, 126789, 129189, 131588, 133985, 136385, 138784, 141181, 143581, 145980, 148378, 150778, 153175, 155574, 157974, 160372, 162770, 165170, 167568, 169967, 172366, 174764, 177164, 179562, 181960, 184360, 186758, 189157]]
    hit1 = 1
    data2 = [int(i*1.231) for i in [0, 1012, 1116, 1219, 1321, 1424, 1526, 1629, 1733, 1836, 1938, 2041, 2143, 2246, 2350, 2452, 2555, 2658, 2760, 2863, 2966, 3069, 3172, 3275, 3377, 3480, 3582, 3686, 3789, 3891, 3994, 4097, 4199, 4302, 4406, 4508, 4611, 4714, 4816, 4919, 5023, 5125, 5228, 5330, 5433, 5536, 5639, 5742, 5845, 5947, 6050, 6153, 6255, 6359, 6462, 6564, 6667, 6769, 6872, 6976, 7078, 7181, 7284, 7386, 7489, 7593, 7695, 7798, 7901, 8003, 8106]]
    hit2 = 10  #追加操作
    倍率 = 1.35
    CD = 45.0
    是否有护石 = 1

    MP = [800, 6000]
    无色消耗 = 5

    形态 = ["魔化", "常规"]

    def 形态变更(self, 形态, char:Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "魔化":
            self.倍率 = 1.35
        if 形态 == "常规":
            self.倍率 = 1.00

    def 装备护石(self):
        self.倍率 *= 1.35


class 技能20(主动技能):
    名称 = '永堕：混沌弑神'
    备注 = '追加操作'
    所在等级 = 85
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i*1.15) for i in [0, 4013, 4944, 5875, 6805, 7736, 8667, 9597, 10528, 11459, 12389, 13320, 14251, 15181, 16112, 17043, 17974, 18904, 19835, 20766, 21696, 22627, 23558, 24488, 25419, 26350, 27280, 28211, 29142, 30073, 31003, 31934, 32865, 33795, 34726, 35657, 36587, 37518, 38449, 39380, 40310, 41241, 42172, 43102, 44033, 44964, 45894, 46825, 47756, 48686, 49617, 50548, 51479, 52409, 53340, 54271, 55201, 56132, 57063, 57993, 58924, 59855, 60786, 61716, 62647, 63578, 64508, 65439, 66370, 67300, 68231]]
    hit0 = 1
    data1 = [int(i*1.15) for i in [0, 2876, 3543, 4210, 4877, 5544, 6211, 6878, 7545, 8212, 8879, 9546, 10213, 10880, 11547, 12214, 12881, 13548, 14215, 14882, 15549, 16216, 16883, 17550, 18217, 18884, 19551, 20218, 20885, 21552, 22219, 22886, 23553, 24220, 24887, 25554, 26221, 26888, 27555, 28222, 28889, 29556, 30223, 30890, 31557, 32224, 32891, 33558, 34225, 34892, 35559, 36226, 36893, 37560, 38227, 38894, 39561, 40228, 40895, 41562, 42229, 42896, 43563, 44230, 44897, 45564, 46231, 46898, 47565, 48232, 48899]]
    hit1 = 12
    data2 = [int(i*1.15) for i in [0, 7224, 8899, 10575, 12250, 13925, 15600, 17276, 18951, 20626, 22301, 23977, 25652, 27327, 29002, 30678, 32353, 34028, 35703, 37379, 39054, 40729, 42404, 44080, 45755, 47430, 49105, 50781, 52456, 54131, 55806, 57482, 59157, 60832, 62507, 64183, 65858, 67533, 69208, 70884, 72559, 74234, 75909, 77585, 79260, 80935, 82610, 84286, 85961, 87636, 89311, 90987, 92662, 94337, 96012, 97688, 99363, 101038, 102713, 104389, 106064, 107739, 109414, 111090, 112765, 114440, 116115, 117791, 119466, 121141, 122816]]
    hit2 = 1
    data3 = [int(i*1.15) for i in [0, 17258, 21260, 25262, 29264, 33266, 37268, 41270, 45272, 49274, 53276, 57278, 61280, 65282, 69284, 73286, 77288, 81290, 85292, 89294, 93296, 97298, 101300, 105302, 109304, 113306, 117308, 121310, 125312, 129314, 133316, 137318, 141320, 145322, 149324, 153326, 157328, 161330, 165332, 169334, 173336, 177338, 181340, 185342, 189344, 193346, 197348, 201350, 205352, 209354, 213355, 217357, 221359, 225361, 229363, 233365, 237367, 241369, 245371, 249373, 253375, 257377, 261379, 265381, 269383, 273385, 277387, 281389, 285391, 289393, 293395]]
    hit3 = 2
    power3 = 1.35 #追加操作
    倍率 = 1.35
    CD = 180.0

    MP = [2500, 5000]
    无色消耗 = 10

    形态 = ["魔化", "常规"]

    def 形态变更(self, 形态, char:Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "魔化":
            self.倍率 = 1.35
        if 形态 == "常规":
            self.倍率 = 1.00


class 技能21(主动技能):
    名称 = '极恶洪流'
    备注 = '追加操作'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i*1.21) for i in [0, 8416, 9269, 10123, 10977, 11830, 12684, 13538, 14392, 15246, 16099, 16953, 17807, 18661, 19515, 20368, 21222, 22076, 22930, 23783, 24637, 25491, 26345, 27198, 28052, 28906, 29760, 30614, 31467, 32321, 33175, 34029, 34883, 35736, 36590, 37444, 38298, 39151, 40005, 40859, 41713, 42567, 43420, 44274, 45128, 45982, 46836, 47689, 48543, 49397, 50250, 51105, 51958, 52812, 53666, 54519, 55373, 56227, 57081, 57935, 58788, 59642, 60496, 61350, 62204, 63057, 63911, 64765, 65618, 66473, 67326]]
    hit0 = 3
    power0 = 1.2 #追加操作
    data1 = [int(i*1.21) for i in [0, 37871, 41713, 45554, 49397, 53239, 57081, 60923, 64765, 68607, 72449, 76291, 80133, 83975, 87817, 91659, 95501, 99343, 103185, 107027, 110869, 114711, 118553, 122395, 126237, 130079, 133921, 137763, 141605, 145448, 149289, 153131, 156973, 160816, 164657, 168499, 172341, 176183, 180025, 183867, 187710, 191551, 195393, 199235, 203078, 206919, 210761, 214603, 218446, 222287, 226129, 229972, 233814, 237655, 241497, 245340, 249182, 253023, 256865, 260708, 264550, 268391, 272234, 276076, 279917, 283759, 287602, 291444, 295285, 299127, 302970]]
    hit1 = 1
    power1 = 1.2 #追加操作
    倍率 = 1.3
    CD = 60.0

    MP = [800, 6000]
    无色消耗 = 7

    形态 = ["魔化", "常规"]

    def 形态变更(self, 形态, char:Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "魔化":
            self.倍率 = 1.30
        if 形态 == "常规":
            self.倍率 = 1.00


class 技能22(被动技能):
    名称 = '光之影'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能23(主动技能):
    名称 = '末日福音：毁灭之翼'
    所在等级 = 100
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i*1.246) for i in [0, 49219, 60632, 72046, 83459, 94872, 106285, 117699, 129112, 140525, 151938, 163352, 174765, 186178, 197591, 209005, 220418, 231831, 243244, 254658, 266071, 277484, 288897, 300311, 311724, 323137, 334550, 345964, 357377, 368790, 380203, 391617, 403030, 414443, 425856, 437270, 448683, 460096, 471509, 482923, 494336, 505749, 517162, 528576, 539989, 551402, 562816, 574229, 585642, 597055, 608469, 619882, 631295, 642708, 654122, 665535, 676948, 688361, 699775, 711188, 722601, 734014, 745428, 756841, 768254, 779667, 791081, 802494, 813907, 825320, 836734]]
    hit0 = 1
    data1 = [int(i*1.246) for i in [0, 24609, 30316, 36023, 41729, 47436, 53142, 58849, 64556, 70262, 75969, 81676, 87382, 93089, 98795, 104502, 110209, 115915, 121622, 127329, 133035, 138742, 144448, 150155, 155862, 161568, 167275, 172982, 178688, 184395, 190101, 195808, 201515, 207221, 212928, 218635, 224341, 230048, 235754, 241461, 247168, 252874, 258581, 264288, 269994, 275701, 281408, 287114, 292821, 298527, 304234, 309941, 315647, 321354, 327061, 332767, 338474, 344180, 349887, 355594, 361300, 367007, 372714, 378420, 384127, 389833, 395540, 401247, 406953, 412660, 418367]]
    hit1 = 1
    data2 = [int(i*1.246) for i in [0, 61524, 75791, 90057, 104324, 118590, 132857, 147123, 161390, 175657, 189923, 204190, 218456, 232723, 246989, 261256, 275523, 289789, 304056, 318322, 332589, 346855, 361122, 375388, 389655, 403922, 418188, 432455, 446721, 460988, 475254, 489521, 503788, 518054, 532321, 546587, 560854, 575120, 589387, 603654, 617920, 632187, 646453, 660720, 674986, 689253, 703519, 717786, 732053, 746319, 760586, 774852, 789119, 803385, 817652, 831919, 846185, 860452, 874718, 888985, 903251, 917518, 931785, 946051, 960318, 974584, 988851, 1003117, 1017384, 1031650, 1045917]]
    hit2 = 1
    data3 = [int(i*1.246) for i in [0, 110744, 136424, 162103, 187783, 213463, 239143, 264823, 290502, 316182, 341862, 367542, 393222, 418902, 444581, 470261, 495941, 521621, 547301, 572980, 598660, 624340, 650020, 675700, 701379, 727059, 752739, 778419, 804099, 829779, 855458, 881138, 906818, 932498, 958178, 983857, 1009537, 1035217, 1060897, 1086577, 1112257, 1137936, 1163616, 1189296, 1214976, 1240656, 1266335, 1292015, 1317695, 1343375, 1369055, 1394735, 1420414, 1446094, 1471774, 1497454, 1523134, 1548813, 1574493, 1600173, 1625853, 1651533, 1677213, 1702892, 1728572, 1754252, 1779932, 1805612, 1831291, 1856971, 1882651]]
    hit3 = 1
    倍率 = 1.4
    CD = 290.0

    MP = [4028, 8056]
    无色消耗 = 15

    形态 = ["魔化", "常规"]

    def 形态变更(self, 形态, char:Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "魔化":
            self.倍率 = 1.4
        if 形态 == "常规":
            self.倍率 = 1.0


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'avenger'
        self.名称 = '神启·复仇者'
        self.角色 = '圣职者(男)'
        self.角色类型 = '输出'
        self.职业 = '复仇者'
        # 用来筛CP武器的
        self.转职 = '复仇者'
        self.武器选项 = ['镰刀']
        self.输出类型选项 = ['魔法百分比']
        self.防具精通属性 = ['智力']
        self.类型 = '魔法百分比'
        self.武器类型 = '镰刀'
        self.防具类型 = '重甲'
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
        self.buff = 1.90

        super().__init__()

    def 职业特殊计算(self):
        # 审判等级绑定
        审判 =  self.get_skill_by_name('审判')
        审判.等级上限 = 50
        审判.等级 = self.get_skill_by_name('魔化：末日审判者').等级
