from math import ceil
from core.basic.skill import 技能
from core.basic.character import Character
from core.basic.skill import 主动技能, 被动技能


# 仅录入大成功/成功/失败


class 技能0(主动技能):
    名称 = '改良魔法星弹'
    备注 = '大成功'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [35, 350]
    # 大成功
    data0 = [int(i) for i in [0, 1535, 1690, 1851, 2006, 2162, 2320, 2487, 2639, 2798, 2954, 3118, 3273, 3430, 3598, 3745, 3908, 4059, 4225, 4377, 4537, 4701, 4858, 5016, 5169, 5337, 5491, 5647, 5804, 5964, 6120, 6277, 6441, 6599, 6755,
                              6913, 7076, 7232, 7391, 7544, 7711, 7860, 8024, 8180, 8338, 8502, 8651, 8819, 8971, 9131, 9294, 9449, 9607, 9763, 9921, 10077, 10241, 10398, 10558, 10714, 10871, 11033, 11193, 11345, 11504, 11660, 11824, 11981, 12137, 12303, 12454]]
    hit0 = 2
    CD = 5.4
    TP成长 = 0.10
    TP上限 = 7


class 技能1(主动技能):
    名称 = '改良舒露露'
    备注 = '大成功'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [35, 350]
    # 大成功
    data0 = [int(i) for i in [0, 7758, 8545, 9332, 10120, 10905, 11693, 12480, 13267, 14056, 14843, 15627, 16416, 17202, 17991, 18778, 19563, 20351, 21138, 21926, 22713, 23500, 24286, 25073, 25860, 26648, 27435, 28222, 29010, 29797, 30585, 31372, 32160, 32944,
                              33730, 34518, 35305, 36093, 36879, 37667, 38455, 39243, 40032, 40818, 41600, 42390, 43177, 43964, 44752, 45537, 46326, 47113, 47899, 48689, 49476, 50260, 51047, 51834, 52623, 53410, 54197, 54984, 55771, 56559, 57346, 58132, 58919, 59706, 60494, 61281, 62068]]
    hit0 = 1
    CD = 16.0
    TP成长 = 0.10
    TP上限 = 7


class 技能2(被动技能):
    名称 = '亲和法米利尔'
    所在等级 = 15
    等级上限 = 15
    基础等级 = 5

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + 0.02 * self.等级, 5)


class 技能3(主动技能):
    名称 = '魔幻粉末'
    备注 = '附加伤害不含平x本身'
    所在等级 = 20
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [35, 259]
    data0 = [int(i) for i in [0, 200, 228, 260, 292, 326, 353, 385, 418, 447, 478, 513, 544, 574, 608, 640, 666, 700, 732, 765, 794, 826, 859, 886, 921, 950, 981, 1011, 1045, 1077, 1107, 1139, 1171, 1200, 1233, 1263,
                              1293, 1326, 1356, 1391, 1424, 1453, 1484, 1515, 1546, 1579, 1609, 1641, 1671, 1703, 1734, 1764, 1797, 1829, 1860, 1891, 1923, 1953, 1986, 2016, 2047, 2078, 2109, 2142, 2171, 2204, 2232, 2269, 2299, 2329]]
    hit0 = 1
    data1 = [int(i) for i in [0, 251, 288, 327, 367, 404, 444, 481, 526, 564, 600, 640, 679, 718, 756, 795, 840, 875, 912, 954, 993, 1032, 1072, 1110, 1148, 1189, 1226, 1269, 1306, 1345, 1382, 1426, 1463, 1501, 1542,
                              1580, 1619, 1658, 1699, 1738, 1777, 1814, 1856, 1892, 1932, 1973, 2012, 2048, 2091, 2131, 2168, 2209, 2245, 2285, 2325, 2364, 2401, 2443, 2482, 2518, 2562, 2599, 2638, 2677, 2717, 2755, 2795, 2831, 2875, 2913]]
    hit1 = 1
    data2 = [int(i) for i in [0, 350, 404, 460, 513, 564, 621, 675, 735, 790, 844, 897, 950, 1003, 1060, 1114, 1174, 1225, 1278, 1337, 1391, 1443, 1501, 1554, 1604, 1663, 1718, 1777, 1829, 1882, 1936, 1993, 2047, 2102,
                              2157, 2212, 2270, 2324, 2377, 2433, 2489, 2541, 2597, 2652, 2705, 2763, 2817, 2870, 2928, 2982, 3036, 3090, 3144, 3197, 3256, 3308, 3362, 3421, 3474, 3528, 3584, 3638, 3691, 3750, 3801, 3856, 3915, 3968, 4023, 4076]]
    hit2 = 1
    中毒data0 = [int(i) for i in [0, 10, 13, 16, 19, 23, 26, 29, 32, 35, 38, 42, 45, 48, 51, 54, 57, 61, 64, 67, 70, 73, 76, 79, 83, 86, 89, 92, 95, 98, 102, 105, 108, 111, 114, 117,
                                121, 124, 127, 130, 133, 136, 139, 143, 146, 149, 152, 155, 158, 162, 165, 168, 171, 174, 177, 181, 184, 187, 190, 193, 196, 200, 203, 206, 209, 212, 215, 218, 222, 225]]
    中毒hit0 = 3
    CD = 5.0  # buff冷却，平x本身无冷却

    形态 = ["中毒", "冰冻"]

    def 形态变更(self, 形态, char):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "中毒":
            self.中毒hit0 = 3
        if 形态 == "冰冻":
            self.中毒hit0 = 0


class 技能4(主动技能):
    名称 = '暗影斗篷'
    所在等级 = 20
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [35, 350]
    data0 = [int(i) for i in [0, 5208, 5736, 6265, 6792, 7321, 7851, 8378, 8909, 9436, 9965, 10492, 11021, 11548, 12078, 12604, 13135, 13662, 14191, 14719, 15248, 15775, 16305, 16831, 17361, 17889, 18416, 18946, 19473, 20003, 20531, 21059, 21589, 22116, 22643,
                              23173, 23701, 24229, 24756, 25286, 25816, 26342, 26873, 27400, 27929, 28456, 28986, 29513, 30042, 30568, 31099, 31626, 32155, 32686, 33212, 33740, 34270, 34799, 35326, 35854, 36382, 36912, 37438, 37969, 38497, 39024, 39554, 40082, 40610, 41140, 41668]]
    hit0 = 1
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 7


class 技能5(主动技能):
    名称 = '魔法秀'
    所在等级 = 20
    等级上限 = 15
    基础等级 = 10
    是否有伤害 = 0
    冷却关联技能 = ['改良魔法星弹', '改良舒露露', '熔岩药瓶', '魔道酸雨云', '旋转扫把', '电鳗碰撞机',
              '暴炎加热炉', '冰霜钻孔车', '反重力装置', '光电兔', '雪人刨冰', '糖果大作战捣蛋杰克']

    魔法秀数值 = [0, 22, 43, 65, 86, 108, 130, 151, 173, 194, 216,
             238, 259, 281, 302, 324, 346, 367, 389, 410, 432]

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 - 0.001*self.魔法秀数值[self.等级], 3)


class 技能6(主动技能):
    名称 = '变异苍蝇拍'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [30, 105]
    data0 = [int(i) for i in [0, 6934, 7635, 8342, 9044, 9748, 10452, 11156, 11857, 12562, 13266, 13971, 14673, 15377, 16080, 16785, 17486, 18187, 18891, 19596, 20301, 21003, 21708, 22410, 23114, 23818, 24523, 25225, 25930, 26632, 27335, 28039, 28743, 29446, 30151,
                              30854, 31557, 32260, 32963, 33667, 34370, 35076, 35777, 36481, 37186, 37889, 38591, 39296, 40000, 40704, 41408, 42111, 42813, 43517, 44220, 44922, 45628, 46329, 47033, 47737, 48443, 49143, 49848, 50552, 51258, 51958, 52662, 53365, 54069, 54772, 55477]]
    hit0 = 1
    CD = 6.4
    TP成长 = 0.1
    TP上限 = 7
    演出时间 = 0.1


class 技能7(主动技能):
    名称 = '魔道酸雨云'
    备注 = '成功'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 3
    等级精通 = 60
    MP = [200, 1960]
    data0 = [int(i) for i in [0, 1079, 1251, 1421, 1596, 1769, 1938, 2112, 2284, 2456, 2629, 2798, 2973, 3146, 3318, 3491, 3662, 3834, 4006, 4178, 4350, 4520, 4692, 4867, 5042, 5209, 5384, 5556, 5727, 5901, 6070, 6245, 6418, 6589, 6762,
                              6932, 7104, 7278, 7451, 7621, 7793, 7964, 8141, 8313, 8482, 8655, 8825, 8998, 9170, 9341, 9514, 9691, 9861, 10032, 10204, 10379, 10550, 10721, 10893, 11064, 11236, 11412, 11584, 11755, 11926, 12097, 12273, 12442, 12612, 12786, 12962]]
    hit0 = 6
    data1 = [int(i) for i in [0, 238, 275, 311, 351, 387, 424, 462, 500, 537, 575, 614, 651, 689, 727, 766, 803, 841, 879, 916, 953, 989, 1030, 1065, 1103, 1141, 1182, 1216, 1255, 1292, 1330, 1368, 1408, 1444, 1482, 1519,
                              1557, 1593, 1632, 1671, 1708, 1745, 1784, 1823, 1860, 1897, 1936, 1971, 2009, 2049, 2084, 2124, 2160, 2197, 2234, 2273, 2312, 2350, 2386, 2425, 2464, 2501, 2538, 2577, 2613, 2651, 2688, 2728, 2762, 2803, 2838]]
    hit1 = 36
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 7


class 技能8(主动技能):
    名称 = '熔岩药瓶'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 3
    等级精通 = 60
    MP = [200, 1960]
    data0 = [int(i) for i in [0, 2239, 2595, 2953, 3310, 3666, 4024, 4381, 4737, 5095, 5452, 5809, 6166, 6523, 6880, 7237, 7594, 7951, 8308, 8665, 9021, 9379, 9735, 10092, 10450, 10806, 11163, 11521, 11878, 12234, 12592, 12949, 13305, 13663, 14020, 14376,
                              14734, 15091, 15449, 15805, 16162, 16520, 16876, 17233, 17591, 17947, 18303, 18660, 19018, 19374, 19731, 20089, 20445, 20802, 21160, 21516, 21873, 22231, 22588, 22944, 23302, 23659, 24015, 24373, 24730, 25088, 25444, 25801, 26159, 26515, 26872]]
    hit0 = 0
    data1 = [int(i) for i in [0, 112, 130, 146, 165, 183, 200, 218, 237, 254, 271, 290, 308, 326, 343, 361, 379, 395, 414, 432, 450, 467, 484, 503, 522, 539, 556, 574, 592, 609, 627, 644, 663, 680, 699,
                              716, 735, 752, 769, 788, 805, 822, 841, 859, 876, 894, 912, 930, 947, 966, 983, 1000, 1019, 1036, 1055, 1072, 1090, 1108, 1126, 1144, 1161, 1179, 1198, 1214, 1233, 1251, 1268, 1286, 1304, 1322, 1338]]
    hit1 = 0
    data2 = [int(i) for i in [0, 8637, 10014, 11393, 12771, 14147, 15527, 16903, 18279, 19656, 21032, 22411, 23788, 25164, 26547, 27923, 29299, 30676, 32052, 33430, 34808, 36186, 37565, 38942, 40315, 41691, 43070, 44450, 45827, 47205, 48581, 49957, 51335, 52713, 54089,
                              55468, 56846, 58224, 59601, 60977, 62354, 63731, 65109, 66486, 67864, 69243, 70619, 71995, 73372, 74749, 76128, 77504, 78884, 80260, 81637, 83014, 84390, 85769, 87146, 88526, 89902, 91278, 92656, 94031, 95410, 96787, 98163, 99543, 100919, 102298, 103673]]
    hit2 = 1
    灼伤data0 = [int(i) for i in [0, 12, 14, 16, 18, 20, 22, 24, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 73, 75,
                                77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 144]]
    灼伤hit0 = 1  # 几率不稳定，此处按1次处理
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 7

    形态 = ["失败", "成功"]

    def 形态变更(self, 形态, char):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "失败":
            self.hit0 = 0
            self.hit1 = 0
            self.hit2 = 1
        if 形态 == "成功":
            self.hit0 = 6
            self.hit1 = 10
            self.hit2 = 0

    def 等效百分比(self, **argv):
        武器类型 = argv.get('武器类型', '')
        char: Character = argv.get('char', {})
        self.power2 = char.get_skill_by_name("魔道学助手").失败倍率() / \
            char.get_skill_by_name("贤者之石").加成倍率('')
        return super().等效百分比(**argv)


class 技能9(主动技能):
    名称 = '旋转扫把'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [100, 840]
    data0 = [int(i) for i in [0, 272, 300, 328, 355, 383, 411, 438, 467, 494, 521, 550, 577, 604, 633, 660, 687, 716, 743, 771, 799, 826, 854, 881, 909, 937, 964, 992, 1020, 1047, 1076, 1103, 1130, 1159, 1186, 1213,
                              1242, 1269, 1296, 1325, 1352, 1380, 1408, 1435, 1463, 1491, 1518, 1546, 1573, 1602, 1629, 1656, 1685, 1712, 1739, 1768, 1795, 1822, 1851, 1878, 1906, 1934, 1961, 1989, 2017, 2044, 2072, 2100, 2127, 2155, 2183]]
    hit0 = 8
    data1 = [int(i) for i in [0, 1671, 1842, 2012, 2183, 2351, 2521, 2690, 2861, 3031, 3200, 3370, 3539, 3709, 3880, 4048, 4219, 4387, 4558, 4728, 4897, 5067, 5237, 5406, 5577, 5745, 5916, 6085, 6256, 6425, 6596, 6766, 6934, 7105, 7274, 7445,
                              7614, 7783, 7953, 8124, 8293, 8463, 8632, 8802, 8972, 9143, 9311, 9482, 9650, 9821, 9991, 10160, 10330, 10499, 10669, 10840, 11008, 11179, 11347, 11518, 11688, 11857, 12027, 12197, 12366, 12537, 12707, 12876, 13045, 13215, 13385]]
    hit1 = 1
    data2 = [int(i) for i in [0, 751, 828, 905, 980, 1057, 1133, 1210, 1286, 1362, 1439, 1515, 1591, 1668, 1744, 1820, 1897, 1973, 2049, 2126, 2202, 2278, 2355, 2431, 2507, 2584, 2660, 2736, 2813, 2888, 2965, 3042, 3117, 3194,
                              3271, 3346, 3423, 3500, 3575, 3652, 3729, 3804, 3881, 3958, 4033, 4110, 4187, 4262, 4339, 4416, 4491, 4568, 4644, 4720, 4797, 4873, 4949, 5026, 5102, 5178, 5255, 5331, 5408, 5484, 5560, 5637, 5713, 5789, 5866, 5942, 6018]]
    hit2 = 0
    data3 = [int(i) for i in [0, 7060, 7776, 8493, 9208, 9925, 10642, 11357, 12074, 12790, 13506, 14222, 14939, 15656, 16371, 17088, 17803, 18520, 19237, 19953, 20669, 21385, 22102, 22817, 23534, 24251, 24966, 25683, 26399, 27116, 27831, 28548, 29265, 29980, 30697,
                              31413, 32129, 32846, 33562, 34279, 34994, 35711, 36426, 37143, 37860, 38576, 39292, 40008, 40725, 41442, 42157, 42874, 43589, 44306, 45022, 45739, 46455, 47171, 47888, 48603, 49320, 50037, 50752, 51469, 52185, 52902, 53617, 54334, 55051, 55766, 56483]]
    hit3 = 1
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 5

    形态 = ["地面", "空中"]

    def 形态变更(self, 形态, char):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "地面":
            self.hit0 = 8
            self.hit1 = 1
            self.hit2 = 0
            self.hit3 = 1
        if 形态 == "空中":
            self.hit0 = 0
            self.hit1 = 0
            self.hit2 = 3
            self.hit3 = 1


class 技能10(主动技能):
    名称 = '电鳗碰撞机'
    备注 = '成功'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i) for i in [0, 944, 1041, 1137, 1233, 1330, 1426, 1521, 1617, 1712, 1808, 1905, 2001, 2097, 2192, 2288, 2383, 2481, 2576, 2672, 2769, 2864, 2960, 3054, 3153, 3248, 3344, 3439, 3536, 3630, 3728, 3824, 3920, 4015,
                              4112, 4208, 4303, 4400, 4496, 4592, 4686, 4784, 4878, 4976, 5070, 5168, 5262, 5359, 5454, 5551, 5646, 5743, 5839, 5935, 6030, 6126, 6224, 6318, 6415, 6510, 6607, 6701, 6799, 6894, 6991, 7086, 7183, 7278, 7373, 7471, 7567]]
    hit0 = 14
    data1 = [int(i) for i in [0, 1486, 1637, 1788, 1939, 2092, 2243, 2392, 2544, 2695, 2846, 2997, 3148, 3298, 3449, 3600, 3751, 3902, 4054, 4203, 4354, 4506, 4657, 4807, 4957, 5109, 5261, 5412, 5563, 5714, 5864, 6016, 6166, 6317, 6468,
                              6617, 6768, 6920, 7072, 7223, 7373, 7524, 7675, 7826, 7977, 8128, 8279, 8430, 8582, 8731, 8882, 9034, 9183, 9334, 9486, 9637, 9787, 9939, 10091, 10241, 10392, 10543, 10694, 10845, 10996, 11146, 11297, 11449, 11600, 11752, 11904]]
    hit1 = 1
    感电data0 = [int(i) for i in [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 12, 12, 12, 13, 13, 14, 14, 14, 15, 15, 16,
                                16, 16, 17, 17, 18, 18, 18, 19, 19, 20, 20, 20, 21, 21, 22, 22, 22, 23, 23, 24, 24, 25, 25, 25, 26, 26, 27, 27, 27, 28, 28, 29, 29, 29, 30, 30, 31, 31, 31]]
    感电hit0 = 1  # 几率不稳定，此处按1次处理
    CD = 25.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 4.8

    MP = [360, 3024]
    无色消耗 = 2

    形态 = ["装置", "骑乘"]

    def 形态变更(self, 形态, char):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "装置":
            self.hit0 = 14
            self.hit1 = 1
            self.hit2 = 1
        if 形态 == "骑乘":
            self.hit0 = 22
            self.hit1 = 1
            self.hit2 = 1

    def 装备护石(self):
        self.倍率 *= 1.36


class 技能11(主动技能):
    名称 = '反重力装置'
    备注 = '成功'
    所在等级 = 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i) for i in [0, 14817, 16320, 17823, 19326, 20829, 22331, 23833, 25338, 26841, 28345, 29847, 31350, 32853, 34356, 35860, 37364, 38866, 40369, 41872, 43375, 44878, 46380, 47885, 49388, 50892, 52393, 53897, 55399, 56902, 58407, 59910, 61414, 62915, 64419,
                              65921, 67425, 68927, 70432, 71935, 73435, 74940, 76443, 77947, 79450, 80955, 82459, 83960, 85463, 86966, 88468, 89972, 91474, 92979, 94481, 95984, 97488, 98991, 100494, 101998, 103502, 105003, 106507, 108009, 109513, 111015, 112520, 114023, 115525, 117028, 118531]]
    hit0 = 1
    data1 = [int(i) for i in [0, 2053, 2270, 2480, 2694, 2905, 3116, 3331, 3540, 3755, 3966, 4178, 4389, 4605, 4818, 5026, 5243, 5453, 5667, 5883, 6089, 6303, 6514, 6731, 6943, 7153, 7367, 7578, 7791, 8001, 8216, 8432, 8641, 8857, 9066, 9279, 9492,
                              9704, 9917, 10126, 10343, 10552, 10764, 10979, 11191, 11404, 11615, 11830, 12045, 12252, 12464, 12678, 12890, 13106, 13317, 13527, 13739, 13953, 14164, 14377, 14593, 14806, 15017, 15229, 15437, 15654, 15866, 16080, 16290, 16504, 16712]]
    hit1 = 0
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 0.1

    MP = [160, 1344]
    无色消耗 = 1

    形态 = ["非浮", "浮空"]

    def 形态变更(self, 形态, char):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "非浮":
            self.hit0 = 1
            self.hit1 = 0
        if 形态 == "浮空":
            self.hit0 = 1
            self.hit1 = 1


class 技能12(主动技能):
    名称 = '暴炎加热炉'
    所在等级 = 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i) for i in [0, 476, 524, 576, 620, 671, 719, 766, 821, 866, 914, 966, 1015, 1067, 1112, 1162, 1215, 1258, 1309, 1360, 1405, 1459, 1507, 1554, 1606, 1653, 1701, 1753, 1801, 1852, 1899, 1947, 1996, 2045, 2099,
                              2147, 2194, 2242, 2292, 2341, 2391, 2439, 2489, 2535, 2586, 2638, 2686, 2731, 2784, 2832, 2882, 2932, 2978, 3028, 3078, 3127, 3175, 3223, 3276, 3323, 3373, 3423, 3472, 3518, 3569, 3620, 3667, 3714, 3765, 3815, 3862]]
    hit0 = 0
    data1 = [int(i) for i in [0, 2005, 2209, 2420, 2627, 2840, 3044, 3244, 3461, 3663, 3865, 4080, 4283, 4500, 4702, 4903, 5118, 5322, 5525, 5738, 5944, 6157, 6360, 6561, 6779, 6981, 7183, 7397, 7600, 7818, 8016, 8222, 8436, 8639, 8853, 9055,
                              9260, 9473, 9676, 9881, 10092, 10299, 10510, 10715, 10921, 11134, 11335, 11537, 11755, 11956, 12170, 12374, 12577, 12790, 12992, 13196, 13413, 13612, 13828, 14033, 14234, 14452, 14651, 14868, 15072, 15270, 15489, 15690, 15893, 16108, 16310]]
    hit1 = 0
    data2 = [int(i) for i in [0, 1096, 1206, 1320, 1431, 1541, 1654, 1766, 1876, 1988, 2101, 2211, 2321, 2432, 2545, 2654, 2767, 2878, 2992, 3101, 3213, 3323, 3434, 3546, 3658, 3770, 3879, 3993, 4104, 4214, 4327, 4439, 4548, 4658,
                              4772, 4883, 4992, 5104, 5215, 5329, 5439, 5550, 5661, 5774, 5885, 5996, 6109, 6218, 6330, 6442, 6555, 6665, 6776, 6885, 6997, 7109, 7220, 7332, 7441, 7555, 7667, 7778, 7888, 8000, 8111, 8223, 8333, 8446, 8558, 8667, 8781]]
    hit2 = 13
    CD = 25.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 2.0
    是否有护石 = 1

    MP = [180, 1512]
    无色消耗 = 1

    形态 = ["失败", "成功"]

    def 形态变更(self, 形态, char):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "失败":
            self.hit0 = 0
            self.hit1 = 0
            self.hit2 = 13
            if '暴炎加热炉' in char.护石栏:
                self.power0 = self.power1 = self.power2 = 1.14*1.19
        else:
            形态 == "成功"
            self.hit0 = 4*11
            self.hit1 = 1
            self.hit2 = 0
            if '暴炎加热炉' in char.护石栏:
                self.power0 = self.power1 = self.power2 = 1.31

    def 装备护石(self):
        pass

    def 等效百分比(self, **argv):
        武器类型 = argv.get('武器类型', '')
        char: Character = argv.get('char', {})
        self.power2 = char.get_skill_by_name(
            "魔道学助手").失败倍率()/char.get_skill_by_name("贤者之石").加成倍率('')
        return super().等效百分比(**argv)


class 技能13(主动技能):
    名称 = '冰霜钻孔车'
    所在等级 = 45
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    # 成功(连按)
    data0 = [int(i) for i in [0, 808, 890, 973, 1058, 1145, 1220, 1305, 1393, 1471, 1562, 1643, 1729, 1807, 1891, 1978, 2059, 2143, 2228, 2308, 2387, 2476, 2557, 2639, 2731, 2804, 2888, 2975, 3052, 3142, 3226, 3315, 3390, 3477,
                              3562, 3641, 3727, 3808, 3892, 3975, 4057, 4142, 4225, 4314, 4387, 4480, 4561, 4637, 4730, 4810, 4898, 4978, 5061, 5145, 5228, 5310, 5389, 5478, 5555, 5642, 5725, 5805, 5897, 5980, 6062, 6142, 6229, 6310, 6395, 6479, 6557]]
    持续时间 = 5.5
    攻击间隔 = 0.115  # 测试计算结果
    hit0 = 0
    data1 = [int(i) for i in [0, 1615, 1781, 1945, 2111, 2287, 2443, 2611, 2785, 2940, 3117, 3282, 3457, 3612, 3781, 3956, 4110, 4285, 4451, 4608, 4782, 4949, 5114, 5280, 5454, 5612, 5772, 5952, 6108, 6285, 6454, 6624, 6780, 6942, 7118,
                              7278, 7454, 7620, 7784, 7948, 8117, 8281, 8447, 8622, 8775, 8957, 9119, 9277, 9448, 9617, 9792, 9945, 10110, 10288, 10456, 10621, 10787, 10951, 11119, 11285, 11449, 11614, 11789, 11957, 12121, 12290, 12453, 12618, 12785, 12948, 13113]]
    hit1 = 0
    # 失败
    data2 = [int(i) for i in [0, 1000, 1102, 1203, 1305, 1407, 1509, 1609, 1711, 1814, 1915, 2016, 2118, 2220, 2322, 2423, 2525, 2627, 2728, 2830, 2932, 3033, 3135, 3237, 3337, 3439, 3541, 3643, 3744, 3845, 3948, 4050, 4150, 4252,
                              4354, 4455, 4556, 4658, 4760, 4862, 4962, 5065, 5167, 5268, 5369, 5471, 5574, 5675, 5775, 5877, 5979, 6080, 6183, 6284, 6385, 6487, 6589, 6691, 6792, 6894, 6996, 7097, 7199, 7301, 7403, 7503, 7605, 7707, 7810, 7909, 8011]]
    hit2 = 9
    data3 = [int(i) for i in [0, 9012, 9928, 10841, 11757, 12670, 13585, 14499, 15415, 16329, 17242, 18157, 19072, 19986, 20900, 21816, 22727, 23643, 24558, 25473, 26387, 27301, 28215, 29130, 30045, 30958, 31874, 32788, 33701, 34616, 35532, 36446, 37360, 38274,
                              39188, 40103, 41017, 41932, 42846, 43760, 44675, 45590, 46505, 47419, 48332, 49247, 50163, 51075, 51991, 52907, 53818, 54733, 55649, 56563, 57477, 58391, 59305, 60221, 61134, 62049, 62965, 63878, 64791, 65707, 66622, 67535, 68449, 69364, 70279, 71192, 72108]]
    hit3 = 1

    power0 = 1
    power1 = 1
    power2 = 1
    power3 = 1

    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 2.0
    是否有护石 = 1

    MP = [360, 3024]
    无色消耗 = 2

    形态 = ["失败", "成功"]

    def 形态变更(self, 形态, char):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "失败":
            self.hit0 = 0
            self.hit1 = 0
            self.hit2 = 9
            self.hit3 = 1
            if '冰霜钻孔车' in char.护石栏:
                self.power0 = self.power1 = self.power2 = self.power3 = 1.32
        else:
            if 形态 == "成功":
                self.hit1 = 3
                self.hit2 = 0
                self.hit3 = 0
                if '冰霜钻孔车' in char.护石栏:
                    self.持续时间 = 6.0
                    self.power0 = self.power1 = self.power2 = self.power3 = 1.25
                self.hit0 = ceil(self.持续时间/self.攻击间隔)  # 贤者之石减攻击间隔在特殊计算部分

    def 装备护石(self):
        pass

    def 等效百分比(self, **argv):
        武器类型 = argv.get('武器类型', '')
        char: Character = argv.get('char', {})
        self.power2 *= char.get_skill_by_name("魔道学助手").失败倍率()
        self.power3 *= char.get_skill_by_name("魔道学助手").失败倍率()
        return super().等效百分比(**argv)


class 技能14(被动技能):
    名称 = '成功预感'
    所在等级 = 48
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 16:
            return 1 + round(6 + 0.7 * self.等级, 1) / 100
        else:
            return 1 + round(16 + 1.5 * (self.等级 - 16), 1) / 100


class 技能15(主动技能):
    名称 = '技艺融合'
    所在等级 = 50
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i) for i in [2089, 2575, 3060, 3547, 4030, 4517, 5001, 5487, 5971, 6456, 6939, 7427, 7910, 8397, 8880, 9366, 9849, 10336, 10820, 11305, 11791, 12275, 12761, 13246, 13729, 14216, 14702, 15183, 15671, 16156, 16639, 17123, 17611, 18093, 18580,
                              19065, 19548, 20035, 20520, 21003, 21490, 21974, 22461, 22946, 23431, 23913, 24401, 24884, 25368, 25855, 26339, 26824, 27310, 27795, 28279, 28764, 29250, 29733, 30220, 30703, 31188, 31676, 32158, 32645, 33129, 33615, 34098, 34584, 35069, 35554]]
    hit0 = 22
    data1 = [int(i) for i in [56785, 69951, 83120, 96287, 109453, 122622, 135790, 148958, 162124, 175291, 188460, 201628, 214793, 227963, 241130, 254297, 267464, 280632, 293800, 306966, 320136, 333303, 346469, 359638, 372804, 385973, 399139, 412306, 425477, 438644, 451810, 464977, 478145, 491313,
                              504479, 517649, 530816, 543982, 557150, 570318, 583485, 596652, 609821, 622989, 636156, 649322, 662489, 675659, 688826, 701995, 715161, 728328, 741497, 754664, 767831, 780998, 794165, 807336, 820502, 833670, 846835, 860003, 873171, 886337, 899509, 912675, 925841, 939008, 952176, 965344]]
    hit1 = 1
    CD = 145.0

    MP = [1000, 8400]
    无色消耗 = 5


class 技能16(主动技能):
    名称 = '超级苍蝇拍'
    所在等级 = 60
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i) for i in [0, 29719, 32736, 35749, 38763, 41777, 44793, 47808, 50824, 53839, 56854, 59868, 62884, 65900, 68915, 71929, 74945, 77959, 80975, 83991, 87006, 90020, 93037, 96050, 99065, 102079, 105095, 108109, 111125, 114141, 117156, 120170, 123185, 126201, 129216, 132231,
                              135247, 138262, 141277, 144292, 147307, 150322, 153334, 156349, 159365, 162379, 165395, 168410, 171426, 174440, 177456, 180470, 183485, 186501, 189516, 192531, 195545, 198563, 201577, 204592, 207607, 210622, 213635, 216651, 219667, 222681, 225696, 228711, 231728, 234742, 237756]]
    hit0 = 1
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 0.1
    是否有护石 = 1

    MP = [400, 1120]
    无色消耗 = 2

    def 装备护石(self):
        self.倍率 = 1.25
        self.CDR *= 0.9


class 技能17(主动技能):
    名称 = '光电兔'
    备注 = '大成功'
    所在等级 = 70
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i) for i in [0, 11417, 12576, 13735, 14892, 16050, 17208, 18368, 19524, 20683, 21842, 23000, 24159, 25317, 26476, 27635, 28793, 29950, 31108, 32267, 33426, 34585, 35741, 36899, 38059, 39217, 40376, 41534, 42692, 43851, 45010, 46167, 47325, 48484,
                              49642, 50802, 51958, 53116, 54276, 55434, 56592, 57748, 58910, 60068, 61227, 62382, 63541, 64700, 65858, 67016, 68174, 69333, 70491, 71652, 72808, 73967, 75124, 76282, 77440, 78599, 79758, 80917, 82074, 83232, 84391, 85550, 86709, 87866, 89025, 90182, 91341]]
    hit0 = 4
    data1 = [int(i) for i in [0, 7435, 8188, 8942, 9697, 10452, 11205, 11960, 12714, 13469, 14222, 14978, 15732, 16484, 17239, 17993, 18748, 19502, 20257, 21011, 21766, 22519, 23272, 24029, 24783, 25536, 26292, 27046, 27799, 28555, 29308, 30062, 30815, 31569, 32324,
                              33078, 33833, 34586, 35342, 36096, 36850, 37604, 38359, 39113, 39868, 40622, 41377, 42130, 42883, 43638, 44392, 45147, 45901, 46655, 47410, 48165, 48918, 49674, 50428, 51180, 51934, 52689, 53444, 54197, 54953, 55708, 56460, 57217, 57969, 58723, 59479]]
    hit1 = 1
    感电data0 = [int(i) for i in [0, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000,
                                3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000]]
    感电hit0 = 4
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 4
    是否有护石 = 1

    MP = [800, 1680]
    无色消耗 = 2

    def 装备护石(self):
        self.倍率 = 1.23


class 技能18(主动技能):
    名称 = '雪人刨冰'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i) for i in [0, 2579, 2840, 3101, 3362, 3625, 3888, 4149, 4410, 4670, 4934, 5196, 5456, 5718, 5981, 6241, 6505, 6765, 7029, 7287, 7551, 7814, 8073, 8340, 8599, 8860,
                              9124, 9384, 9647, 9908, 10169, 10431, 10693, 10956, 11216, 11479, 11739, 12000, 12264, 12525, 12786, 13048, 13310, 13572, 13832, 14095, 14356, 14618, 14879, 15142, 15404]]
    hit0 = 18
    data1 = [int(i) for i in [0, 1589, 1751, 1914, 2074, 2236, 2395, 2556, 2722, 2883, 3043, 3203, 3365, 3526, 3689, 3850, 4012, 4171, 4333, 4494, 4658, 4819, 4980, 5140,
                              5301, 5464, 5625, 5787, 5948, 6111, 6272, 6434, 6595, 6754, 6917, 7077, 7239, 7400, 7563, 7725, 7886, 8045, 8207, 8367, 8531, 8693, 8853, 9013, 9174, 9336, 9497]]
    hit1 = 13
    data2 = [int(i) for i in [0, 21877, 24094, 26313, 28533, 30751, 32972, 35191, 37410, 39629, 41849, 44068, 46286, 48504, 50725, 52942, 55165, 57383, 59604, 61822, 64040, 66263, 68480, 70699, 72921,
                              75136, 77356, 79577, 81796, 84015, 86234, 88452, 90672, 92890, 95112, 97328, 99549, 101769, 103987, 106206, 108427, 110645, 112866, 115084, 117303, 119525, 121744, 123961, 126181, 128399, 130620]]
    hit2 = 1
    CD = 40.0
    演出时间 = 4
    是否有护石 = 1

    MP = [800, 1680]
    无色消耗 = 2

    def 装备护石(self):
        self.倍率 = 1.3


class 技能19(被动技能):
    名称 = '贤者之石'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40
    关联技能 = ['魔道酸雨云', '电鳗碰撞机', '反重力装置', '熔岩药瓶', '暴炎加热炉']

    data0 = [0, 123, 147, 171, 194, 206, 219, 231, 242, 254, 265, 275, 286, 296, 306, 315, 324, 333, 342, 351,
             360, 360, 360, 360, 360, 360, 360, 360, 360, 360, 360, 360, 360, 360, 360, 360, 360, 360, 360, 360, 360, 360]

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)

    def 攻击间隔减少率(self):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.data0[self.等级]/1000, 5)


class 技能20(被动技能):
    名称 = '魔道学助手'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40
    关联技能 = ['变异苍蝇拍', '超级苍蝇拍', '改良舒露露', '改良魔法星弹', '暗影斗篷', '技艺融合',
            '超级棒棒糖', '光电兔', '雪人刨冰', '乌洛波洛斯之环', '糖果大作战精怪乐园', '糖果大作战捣蛋杰克']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.17 + 0.02 * self.等级, 5)

    def 失败倍率(self):  # 有0.50是苦涩棒棒糖的；这里一起算入了
        if self.等级 == 0:
            return 1.0
        else:
            return round(0.50+0.38 + 0.02 * self.等级, 5)


class 技能21(主动技能):
    名称 = '超级棒棒糖'
    所在等级 = 80
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    # 普通怪物110，其他101
    data0 = [int(i) for i in [0, 64048, 70544, 77044, 83538, 90037, 96534, 103034, 109531, 116030, 122525, 129024, 135521, 142019, 148516, 155014, 161510, 168013, 174506, 181006, 187503, 194001, 200497, 206996, 213493, 219991, 226489, 232986, 239483, 245981, 252477, 258977, 265474, 271973, 278471,
                              284969, 291463, 297962, 304459, 310958, 317456, 323955, 330449, 336947, 343444, 349945, 356441, 362939, 369437, 375934, 382433, 388929, 395429, 401924, 408422, 414919, 421420, 427916, 434415, 440910, 447407, 453906, 460404, 466902, 473401, 479896, 486393, 492893, 499390, 505886, 512386]]
    hit0 = 1
    data1 = [int(i) for i in [0, 17436, 19205, 20973, 22744, 24516, 26285, 28055, 29821, 31595, 33364, 35130, 36901, 38668, 40442, 42208, 43979, 45750, 47516, 49287, 51059, 52826, 54595, 56362, 58137, 59902, 61671, 63442, 65210, 66984, 68751, 70522, 72287, 74058, 75830, 77596,
                              79368, 81135, 82907, 84677, 86446, 88216, 89983, 91751, 93526, 95294, 97059, 98833, 100600, 102375, 104139, 105911, 107677, 109448, 111218, 112988, 114753, 116524, 118294, 120065, 121835, 123603, 125373, 127141, 128913, 130683, 132453, 134217, 135990, 137760, 139527]]
    hit1 = 1
    data2 = [int(i) for i in [0, 40949, 45104, 49257, 53412, 57565, 61721, 65874, 70027, 74181, 78336, 82489, 86645, 90796, 94953, 99104, 103260, 107414, 111568, 115727, 119879, 124034, 128188, 132343, 136494, 140652, 144803, 148958, 153112, 157266, 161418, 165574, 169727, 173884, 178035,
                              182191, 186345, 190499, 194655, 198808, 202965, 207116, 211272, 215427, 219580, 223734, 227890, 232043, 236198, 240351, 244506, 248659, 252813, 256969, 261122, 265274, 269430, 273585, 277739, 281894, 286046, 290203, 294356, 298513, 302665, 306821, 310973, 315128, 319283, 323438, 327589]]
    hit2 = 0
    CD = 45.0
    演出时间 = 0.5
    是否有护石 = 1

    MP = [800, 6000]
    无色消耗 = 5

    def 装备护石(self):
        self.倍率 *= 1.32
        self.CDR *= 0.9


class 技能22(主动技能):
    名称 = '乌洛波洛斯之环'
    备注 = '满'
    所在等级 = 85
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i) for i in [0, 3547, 4370, 5193, 6016, 6839, 7661, 8486, 9308, 10130, 10953, 11777, 12599, 13422, 14243, 15068, 15889, 16711, 17537, 18358, 19182, 20004, 20827, 21649, 22472, 23295, 24118, 24941, 25763, 26588, 27410, 28232, 29055, 29879, 30701,
                              31522, 32347, 33170, 33992, 34814, 35639, 36461, 37284, 38105, 38930, 39751, 40574, 41397, 42219, 43043, 43864, 44689, 45513, 46334, 47159, 47981, 48802, 49626, 50447, 51272, 52095, 52915, 53742, 54563, 55386, 56208, 57029, 57855, 58676, 59499, 60322]]
    hit0 = 21
    data1 = [int(i) for i in [0, 2884, 3552, 4220, 4891, 5557, 6225, 6896, 7564, 8232, 8902, 9569, 10237, 10907, 11577, 12245, 12913, 13584, 14252, 14918, 15589, 16258, 16925, 17594, 18264, 18933, 19601, 20269, 20939, 21606, 22275, 22944, 23611, 24280, 24951,
                              25620, 26288, 26957, 27625, 28294, 28962, 29631, 30302, 30968, 31635, 32305, 32975, 33644, 34313, 34982, 35650, 36318, 36987, 37655, 38324, 38995, 39661, 40328, 40998, 41669, 42337, 43006, 43675, 44344, 45010, 45679, 46349, 47017, 47685, 48354, 49026]]
    hit1 = 20
    data2 = [int(i) for i in [0, 89856, 110695, 131532, 152370, 173206, 194041, 214877, 235715, 256552, 277390, 298225, 319062, 339900, 360737, 381574, 402411, 423249, 444083, 464921, 485757, 506595, 527429, 548267, 569104, 589941, 610778, 631616, 652452, 673288, 694124, 714962, 735797, 756635, 777472, 798309,
                              819144, 839983, 860819, 881657, 902493, 923330, 944167, 965003, 985839, 1006677, 1027513, 1048351, 1069187, 1090024, 1110860, 1131698, 1152535, 1173369, 1194206, 1215045, 1235882, 1256718, 1277554, 1298391, 1319228, 1340065, 1360904, 1381740, 1402575, 1423412, 1444250, 1465087, 1485923, 1506759, 1527597]]
    hit2 = 1
    CD = 180.0

    MP = [2500, 8000]
    无色消耗 = 10


class 技能23(主动技能):
    名称 = '糖果大作战捣蛋杰克'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i) for i in [0, 6704, 7384, 8064, 8743, 9424, 10103, 10784, 11464, 12145, 12824, 13505, 14184, 14864, 15544, 16225, 16905, 17585, 18266, 18946, 19626, 20305, 20986, 21665, 22346,
                              23026, 23707, 24386, 25067, 25747, 26426, 27106, 27787, 28467, 29147, 29827, 30508, 31186, 31867, 32549, 33228, 33908, 34588, 35269, 35948, 36629, 37309, 37990, 38668, 39349, 40029]]
    hit0 = 25
    CD = 60.0

    MP = [773, 6000]
    无色消耗 = 7


class 技能24(被动技能):
    名称 = '粉红糖果'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能25(主动技能):
    名称 = '糖果大作战精怪乐园'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2

    data0 = [int(i) for i in [0, 15248, 18784, 22320, 25857, 29392, 32927, 36464, 39999, 43536, 47071, 50608, 54143, 57679, 61215, 64750, 68287, 71823, 75359, 78894, 82430, 85967, 89501, 93038, 96574, 100110,
                              103645, 107181, 110718, 114254, 117789, 121325, 124861, 128398, 131932, 135469, 139005, 142542, 146076, 149612, 153149, 156684, 160221, 163756, 167291, 170828, 174364, 177900, 181435, 184972, 188508]]
    hit0 = 8
    data1 = [int(i) for i in [0, 91492, 112706, 133923, 155137, 176353, 197568, 218784, 239998, 261215, 282429, 303646, 324861, 346076, 367293, 388507, 409724, 430938, 452154, 473368, 494585, 515799, 537016, 558230, 579446,
                              600662, 621877, 643094, 664308, 685524, 706738, 727955, 749169, 770386, 791600, 812816, 834030, 855247, 876462, 897678, 918893, 940108, 961325, 982539, 1003756, 1024970, 1046186, 1067401, 1088617, 1109831, 1131048]]
    hit1 = 1
    data2 = [int(i) for i in [0, 99116, 122099, 145082, 168065, 191050, 214033, 237016, 259999, 282982, 305966, 328949, 351932, 374916, 397900, 420883, 443866, 466850, 489834, 512815, 535800, 558783, 581766, 604749, 627734,
                              650717, 673700, 696683, 719667, 742651, 765634, 788616, 811601, 834584, 857567, 880550, 903535, 926518, 949501, 972484, 995467, 1018452, 1041434, 1064417, 1087401, 1110385, 1133368, 1156351, 1179335, 1202319, 1225302]]
    hit2 = 4
    CD = 290.0

    MP = [4028, 8056]
    无色消耗 = 15


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'witch'
        self.名称 = '知源·魔道学者'
        self.角色 = '魔法师(女)'
        self.角色类型 = '输出'
        self.职业 = '魔道学者'
        self.武器选项 = ['魔杖', '法杖', '棍棒', '矛', '扫把']
        self.输出类型选项 = ['魔法固伤']
        self.防具精通属性 = ['智力']
        self.类型 = '魔法固伤'
        self.武器类型 = '扫把'
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
        self.buff = 1.92

        super().__init__()

    def 职业特殊计算(self):
        魔道学助手 = self.get_skill_by_name('魔道学助手')
        贤者之石 = self.get_skill_by_name('贤者之石')
        冰霜钻孔车 = self.get_skill_by_name('冰霜钻孔车')
        魔道学助手.等级 = 贤者之石.等级
        冰霜钻孔车.hit0 = ceil(冰霜钻孔车.持续时间/(冰霜钻孔车.攻击间隔*(1-贤者之石.攻击间隔减少率())))
