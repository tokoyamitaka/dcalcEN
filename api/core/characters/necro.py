from core.baseClass.skill import 技能
from core.baseClass.character import Character
from core.baseClass.skill import 主动技能, 被动技能


class 技能0(主动技能):
    名称 = '暗魂波'
    所在等级 = 5
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [15, 161]
    # 三觉后技能数据有轻微变化
    data0 = [int(i*1.0) for i in [0, 244, 268, 293, 318, 343, 369, 393, 417, 443, 468, 492, 515, 539, 566, 590, 616, 639, 665, 690, 714, 739, 765, 787, 813, 838, 862, 888, 913, 936, 962, 986, 1012, 1037, 1061, 1085, 1110, 1136, 1160, 1185, 1210, 1234, 1259, 1284, 1309, 1334, 1356, 1382, 1409, 1434, 1456, 1481, 1506, 1532, 1556, 1580, 1605, 1631, 1654, 1679, 1704, 1728, 1754, 1779, 1804, 1828, 1854, 1877, 1902, 1928, 1953]]
    hit0 = 4
    # 蓄力增伤35%
    倍率 = 1.35
    CD = 3.5
    TP成长 = 0.10
    TP上限 = 7


class 技能1(主动技能):
    名称 = '诅咒之箭'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [22, 235]
    data0 = [int(i*1.197) for i in [0, 424, 466, 509, 552, 596, 638, 682, 724, 767, 811, 855, 897, 941, 983, 1026, 1069, 1113, 1155, 1199, 1241, 1285, 1327, 1372, 1414, 1457, 1500, 1543, 1586, 1628, 1672, 1715, 1758, 1801, 1844,
                                   1886, 1931, 1974, 2017, 2060, 2103, 2145, 2188, 2232, 2274, 2318, 2360, 2404, 2446, 2490, 2533, 2577, 2619, 2663, 2705, 2748, 2791, 2835, 2877, 2921, 2963, 3005, 3050, 3094, 3136, 3179, 3222, 3264, 3308, 3351, 3394]]
    hit0 = 5
    CD = 10
    TP成长 = 0.1
    TP上限 = 7


class 技能2(主动技能):
    名称 = '降临 : 尼古拉斯(蜘蛛团/黑蜘蛛)'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [30, 420]
    data0 = [int(i*1.0) for i in [0, 105, 114, 126, 135, 147, 158, 169, 179, 191, 200, 213, 222, 234, 243, 255, 263, 274, 285, 297, 306, 318, 327, 340, 349, 361, 371, 382, 393, 405, 414, 425, 435,
                                  447, 457, 468, 479, 489, 501, 511, 522, 533, 543, 555, 565, 575, 586, 596, 607, 618, 629, 640, 650, 661, 672, 683, 694, 704, 715, 726, 736, 748, 757, 769, 779, 791, 800, 812, 822, 834, 844]]
    hit0 = 4
    # CD为测试数据
    CD = 2
    TP成长 = 0.1
    TP上限 = 7

    def 等效百分比(self, **argv):
        if self.TP等级 > 0:
            # 变更形态后数组
            # 黑蜘蛛相当于默认原蜘蛛团打6段的总伤害，再拆分成4段,在不计入TP影响时，该形态变更所带来的倍率为1.5
            self.power0 *= 1.5
        return super().等效百分比(**argv)


class 技能3(主动技能):
    名称 = '降临 : 尼古拉斯(艾克洛索/艾克尼亚)'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [30, 420]
    data0 = [int(i*1.0) for i in [0, 208, 229, 251, 272, 294, 316, 337, 359, 379, 400, 423, 444, 466, 487, 508, 528, 549, 572, 593, 614, 636, 657, 678, 700, 721, 743, 764, 786, 808, 829, 851, 872, 894, 916, 937, 959, 980,
                                  1001, 1023, 1044, 1065, 1087, 1109, 1131, 1151, 1172, 1194, 1215, 1238, 1259, 1280, 1299, 1321, 1343, 1365, 1386, 1407, 1429, 1451, 1473, 1494, 1515, 1537, 1559, 1581, 1602, 1622, 1644, 1666, 1687]]
    hit0 = 1
    data1 = [int(i*1.0) for i in [0, 623, 687, 753, 814, 880, 943, 1008, 1073, 1136, 1201, 1266, 1331, 1396, 1459, 1524, 1586, 1652, 1715, 1780, 1844, 1909, 1974, 2037, 2103, 2167, 2231, 2295, 2358, 2423, 2487, 2553, 2617, 2681,
                                  2746, 2809, 2874, 2939, 3003, 3067, 3132, 3197, 3261, 3325, 3390, 3454, 3518, 3582, 3647, 3711, 3777, 3841, 3904, 3969, 4033, 4097, 4161, 4225, 4290, 4355, 4420, 4484, 4548, 4612, 4676, 4740, 4805, 4868, 4933, 4998, 5063]]
    hit1 = 1
    # CD为测试数据
    CD = 6
    TP成长 = 0.1
    TP上限 = 7
    # TP变更形态后
    # 艾克尼亚相当于默认艾克洛索本体+冲击波打满的总伤害，再拆分为3段，在不计入TP影响时，形态变更不会导致总伤害变化
    # 故此处不必专门再写


class 技能4(主动技能):
    名称 = '驱使僵尸'
    所在等级 = 20
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [30, 420]
    # 僵尸自爆(不可抓取)
    data0 = [int(i*1.0) for i in [0, 668, 733, 800, 868, 937, 1004, 1071, 1140, 1206, 1276, 1340, 1408, 1476, 1546, 1614, 1680, 1747, 1814, 1885, 1950, 2019, 2086, 2154, 2221, 2288, 2356, 2421, 2490, 2555, 2627, 2692, 2761, 2829, 2895, 2964, 3030, 3101, 3168, 3236, 3300, 3369, 3438, 3506, 3572, 3642, 3705, 3774, 3843, 3908, 3977, 4044, 4109, 4180, 4248, 4318, 4382, 4451, 4520, 4588, 4653, 4719, 4788, 4856, 4925, 4993, 5057, 5123, 5191, 5260, 5328]]
    hit0 = 5
    # 僵尸撕咬(可抓取--对单)
    data1 = [int(i*1.0) for i in [0, 57, 60, 67, 70, 74, 82, 86, 92, 97, 102, 110, 115, 119, 127, 131, 138, 143, 144, 153, 157, 162, 169, 174, 179, 186, 190, 198, 202, 209, 214, 218, 226, 227, 233, 239, 246, 250, 257, 260, 269, 272, 279, 285, 289, 296, 299, 305, 309, 315, 320, 327, 333, 338, 343, 347, 355, 358, 365, 371, 376, 382, 388, 392, 398, 404, 410, 414, 422, 426, 430]]
    hit1 = 0
    data2 = [int(i*1.0) for i in [0, 106, 118, 130, 142, 154, 163, 175, 183, 194, 205, 217, 228, 240, 251, 260, 270, 283, 295, 305, 318, 328, 336, 346, 356, 370, 382, 394, 404, 411, 426, 436, 446, 458, 469, 482, 494, 499, 510, 523, 535, 542, 557, 567, 579, 589, 600, 613, 622, 637, 642, 654, 664, 676, 688, 698, 710, 720, 731, 743, 754, 766, 776, 783, 795, 808, 818, 830, 840, 852, 862]]
    hit2 = 0  
    data3 = [int(i*1.0) for i in [0, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 145, 147, 149, 151, 153, 155]]
    hit3 = 0
    CD = 8
    TP成长 = 0.10
    TP上限 = 7

    形态 = ["不可抓取", "可抓取"]

    def 形态变更(self, 形态, char):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "不可抓取":
            self.hit0 = 5
            self.hit1 = 0
            self.hit2 = 0
            self.hit3 = 0
        if 形态 == "可抓取":
            self.hit0 = 5
            self.hit1 = 2
            self.hit2 = 1
            self.hit3 = 1


class 技能5(主动技能):
    名称 = '服从'
    所在等级 = 20
    等级上限 = 20
    学习间隔 = 2
    等级精通 = 10
    是否有伤害 = 0
    # 本来还应该有个近战模式 降临 : 尼古拉斯(蜘蛛斩) 伤害和原尼古拉斯TP无关，只和服从等级相关
    # 不过用的太少而且很弱 就忽略掉了
    关联技能 = ['降临 : 尼古拉斯(蜘蛛团/黑蜘蛛)', '降临 : 尼古拉斯(艾克洛索/艾克尼亚)']
    # 蜘蛛斩
    # data0 = [int(i*1.0) for i in [0， 777, 957, 1138, 1318, 1498, 1679, 1859, 2039, 2220, 2400, 2580, 2761, 2941, 3121, 3302, 3482, 3662, 3843, 4023, 4203]]
    # hit0 = 1
    # CD = 2
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.0 + 0.04 * self.等级, 5)


class 技能6(被动技能):
    名称 = '黑暗之环'
    所在等级 = 20
    等级上限 = 20
    学习间隔 = 2
    等级精通 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.1 + 0.01 * self.等级, 5)

            
class 技能7(主动技能):
    名称 = '暗影蛛丝阵'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [95, 952]
    data0 = [int(i*1.197) for i in [0, 338, 373, 406, 439, 475, 509, 542, 577, 610, 646, 680, 713, 748, 782, 816, 851, 884, 920, 953, 987, 1022, 1056, 1089, 1125, 1159, 1191, 1226, 1260, 1295, 1328, 1362, 1398, 1432, 1465,
                                   1501, 1533, 1569, 1603, 1636, 1671, 1704, 1740, 1774, 1808, 1843, 1877, 1909, 1945, 1979, 2012, 2048, 2080, 2117, 2150, 2183, 2218, 2252, 2287, 2321, 2355, 2390, 2423, 2457, 2492, 2527, 2561, 2594, 2629, 2663, 2697]]
    hit0 = 19
    CD = 20
    TP成长 = 0.07
    TP上限 = 7          


class 技能8(主动技能):
    名称 = '死亡之爪'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [24, 259]
    data0 = [int(i*1.216) for i in [0, 2565, 2825, 3086, 3346, 3606, 3866, 4127, 4387, 4647, 4907, 5168, 5428, 5688, 5949, 6209, 6469, 6729, 6990, 7250, 7510, 7770, 8031, 8291, 8551, 8811, 9072, 9332, 9592, 9853, 10113, 10373, 10633, 10894, 11154, 11414,
                                   11674, 11935, 12195, 12455, 12716, 12976, 13236, 13496, 13757, 14017, 14277, 14537, 14798, 15058, 15318, 15578, 15839, 16099, 16359, 16620, 16880, 17140, 17400, 17661, 17921, 18181, 18441, 18702, 18962, 19222, 19483, 19743, 20003, 20263, 20524]]
    hit0 = 1
    CD = 7
    TP成长 = 0.10
    TP上限 = 7


class 技能9(主动技能):
    名称 = '死灵之怨'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [32, 336]
    data0 = [int(i*1.196) for i in [0, 316, 348, 379, 412, 444, 476, 508, 540, 572, 604, 637, 669, 700, 732, 765, 797, 829, 861, 893, 925, 958, 990, 1021, 1053, 1086, 1118, 1150, 1182, 1214, 1246, 1278, 1312, 1342, 1374,
                                   1407, 1439, 1471, 1503, 1535, 1567, 1599, 1633, 1665, 1695, 1727, 1761, 1793, 1824, 1856, 1888, 1920, 1954, 1986, 2016, 2048, 2082, 2114, 2146, 2178, 2210, 2242, 2274, 2307, 2337, 2369, 2403, 2435, 2467, 2497, 2531]]
    hit0 = 13
    CD = 10
    TP成长 = 0.10
    TP上限 = 7

    
class 技能10(主动技能):
    名称 = '百鬼夜行'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [65, 700]
    data0 = [int(i*1.205) for i in [0, 275, 302, 330, 359, 386, 414, 443, 470, 498, 527, 552, 580, 607, 636, 664, 691, 720, 748, 775, 804, 832, 859, 888, 916, 943, 972, 1000, 1027, 1056, 1082, 1109, 1136, 1166, 1193, 1220,
                                   1250, 1277, 1304, 1334, 1361, 1388, 1418, 1445, 1472, 1502, 1529, 1556, 1581, 1611, 1638, 1667, 1695, 1722, 1751, 1779, 1806, 1835, 1863, 1890, 1919, 1947, 1974, 2003, 2031, 2058, 2083, 2113, 2140, 2167, 2197]]
    hit0 = 14
    CD = 10
    TP成长 = 0
    TP上限 = 7
    # 增加持续时间，hit0变化依次为 15 17 18 20 21 23 24
    TP倍率 = [1, 15/14, 17/14, 18/14, 20/14, 21/14, 23/14, 24/14]

    形态 = ["自爆", "引爆"]

    def 形态变更(self, 形态, char):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "自爆":
            self.倍率 = 1.2
        if 形态 == "引爆":
            self.倍率 = 1.0


class 技能11(被动技能):
    名称 = '黑魔法书 : 亡者之魂'
    所在等级 = 30
    等级上限 = 10
    学习间隔 = 2
    等级精通 = 1
    关联技能 = ['暗魂波', '诅咒之箭', '驱使僵尸', '暗影蛛丝阵', '死亡之爪', '死灵之怨', '百鬼夜行', '降临 : 暴君巴拉克(平x)', '降临 : 暴君巴拉克(暗击拳)', '降临 : 暴君巴拉克(巴拉克强击)',
            '降临 : 暴君巴拉克(杀戮乱舞)', '吸魂暗劲波', '巴拉克的野心', '降临 : 僵尸莱迪娅', '巴拉克的愤怒', '千魂祭', '死灵之缚', '怨噬之沼', '暗黑蛛丝引', '暴君极刑斩', '亡者君临 : 巴拉克之戮', '亡者之茧', '命运殇痕·摩罗斯之咒']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.21 + 0.015 * self.等级, 5)


class 技能12(主动技能):
    名称 = '降临 : 暴君巴拉克(平x)'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [338, 3702]
    data0 = [int(i*1.0) for i in [0, 509, 523, 541, 557, 574, 592, 611, 630, 649, 669, 689, 711, 733, 756, 780, 803, 828, 853, 879, 905, 935, 964, 993, 1024, 1056, 1089, 1119, 1152, 1182, 1214, 1245, 1273, 1309, 1338, 1371, 1401, 1433, 1464, 1497, 1527, 1558, 1590, 1621, 1654, 1684, 1713, 1745, 1779, 1811, 1839, 1872, 1904, 1934, 1965, 1998, 2029, 2059, 2092, 2124, 2155, 2187, 2218, 2250, 2279, 2311, 2342, 2373, 2406, 2438, 2469]]  # 1
    hit0 = 1
    data1 = [int(i*1.187) for i in [0, 475, 489, 505, 521, 538, 554, 571, 588, 606, 626, 644, 665, 685, 706, 728, 751, 774, 798, 823, 848, 875, 902, 930, 958, 988, 1018, 1048, 1079, 1107, 1135, 1166, 1194, 1225, 1255, 1283,
                                    1312, 1341, 1373, 1401, 1429, 1459, 1488, 1519, 1549, 1578, 1606, 1635, 1665, 1694, 1726, 1753, 1782, 1811, 1841, 1871, 1900, 1930, 1959, 1988, 2016, 2046, 2076, 2106, 2134, 2164, 2194, 2224, 2253, 2282, 2310]]  # 2
    hit1 = 1
    data2 = [int(i*1.187) for i in [0, 250, 257, 266, 274, 283, 291, 299, 309, 319, 329, 339, 349, 360, 371, 383, 396, 406, 419, 433, 446, 460, 474, 488, 503, 519, 536, 550, 566, 582, 598, 612, 629, 644,
                                    659, 674, 689, 706, 721, 735, 753, 766, 782, 798, 813, 830, 844, 859, 876, 890, 903, 921, 937, 953, 968, 983, 999, 1014, 1030, 1044, 1060, 1076, 1091, 1107, 1122, 1138, 1153, 1169, 1181, 1197, 1213]]
    hit2 = 5
    data3 = [int(i*1.187) for i in [0, 571, 589, 608, 626, 646, 665, 686, 707, 728, 751, 775, 799, 824, 849, 875, 903, 930, 959, 988, 1019, 1051, 1083, 1116, 1152, 1187, 1224, 1257, 1294, 1329, 1363, 1398, 1436, 1468, 1503,
                                    1540, 1575, 1610, 1646, 1681, 1716, 1751, 1788, 1823, 1858, 1891, 1927, 1963, 1999, 2032, 2069, 2104, 2139, 2176, 2209, 2244, 2280, 2316, 2350, 2385, 2422, 2457, 2493, 2526, 2563, 2598, 2633, 2669, 2703, 2738, 2774]]  # 4
    hit3 = 1
    CD = 1 #非实际CD
    TP成长 = 0.1
    TP上限 = 5

    形态 = ["4x", "3x"]

    def 形态变更(self, 形态, char):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "4x":
            self.hit0 = 1
            self.hit1 = 1
            self.hit2 = 5
            self.hit3 = 1
        if 形态 == "3x":
            self.hit0 = 1
            self.hit1 = 1
            self.hit2 = 5
            self.hit3 = 0


class 技能13(主动技能):
    名称 = '降临 : 暴君巴拉克(暗击拳)'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [338, 3702]
    data0 = [int(i*1.0) for i in [0, 1182, 1219, 1255, 1295, 1334, 1375, 1419, 1461, 1508, 1553, 1602, 1651, 1702, 1754, 1810, 1865, 1923, 1983, 2043, 2106, 2171, 2240, 2309, 2379, 2454, 2529, 2602, 2673, 2748, 2818, 2893, 2965, 3037, 3111, 3185, 3258, 3330, 3404, 3474, 3549, 3623, 3694, 3767, 3837, 3915, 3988, 4059, 4133, 4205, 4278, 4350, 4424, 4498, 4568, 4643, 4716, 4789, 4862, 4934, 5009, 5080, 5155, 5225, 5299, 5372, 5445, 5518, 5590, 5665, 5736]]
    hit0 = 1
    data1 = [int(i*1.0) for i in [0, 1508, 1553, 1602, 1651, 1700, 1754, 1807, 1864, 1922, 1980, 2042, 2105, 2171, 2238, 2309, 2380, 2452, 2527, 2608, 2688, 2768, 2857, 2946, 3035, 3128, 3226, 3315, 3413, 3502, 3591, 3689, 3778, 3875, 3964, 4058, 4157, 4246, 4343, 4432, 4521, 4615, 4708, 4806, 4895, 4993, 5082, 5175, 5273, 5362, 5460, 5545, 5638, 5731, 5825, 5919, 6011, 6105, 6199, 6293, 6382, 6474, 6568, 6662, 6755, 6848, 6942, 7035, 7129, 7222, 7311]]
    hit1 = 0
    CD = 3.0
    TP成长 = 0.1
    TP上限 = 5

    形态 = ["不可抓取", "可抓取"]

    def 形态变更(self, 形态, char):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "不可抓取":
            self.hit0 = 1
            self.hit1 = 0
        if 形态 == "可抓取":
            self.hit0 = 1
            self.hit1 = 1


class 技能14(主动技能):
    名称 = '降临 : 暴君巴拉克(巴拉克强击)'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [338, 3702]
    data0 = [int(i*1.0) for i in [0, 2177, 2244, 2313, 2385, 2457, 2536, 2615, 2695, 2780, 2863, 2952, 3041, 3137, 3235, 3334, 3439, 3546, 3655, 3766, 3884, 4004, 4129, 4256, 4386, 4522, 4661, 4797, 4930, 5066, 5198, 5333, 5465, 5600, 5736, 5870, 6007, 6138, 6275, 6406, 6542, 6677, 6810, 6945, 7079, 7216, 7352, 7484, 7620, 7753, 7889, 8020, 8156, 8292, 8424, 8559, 8695, 8829, 8965, 9096, 9233, 9367, 9503, 9634, 9770, 9903, 10039, 10174, 10308, 10441, 10577]]
    hit0 = 1
    CD = 2.0
    TP成长 = 0.1
    TP上限 = 5


class 技能15(主动技能):
    名称 = '降临 : 暴君巴拉克(杀戮乱舞)'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [338, 3702]
    data0 = [int(i*1.0) for i in [0, 997, 1026, 1057, 1090, 1125, 1160, 1197, 1233, 1272, 1310, 1350, 1392, 1435, 1481, 1525, 1573, 1623, 1672, 1724, 1778, 1832, 1890, 1947, 2007, 2069, 2132, 2196, 2257, 2317, 2380, 2440, 2501, 2563, 2625, 2685, 2748, 2807, 2870, 2932, 2994, 3054, 3117, 3178, 3241, 3302, 3364, 3426, 3487, 3548, 3611, 3671, 3731, 3795, 3855, 3917, 3980, 4040, 4103, 4164, 4225, 4287, 4349, 4409, 4472, 4532, 4593, 4656, 4718, 4777, 4841]]
    hit0 = 3
    CD = 7.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.hit0 += 2
        self.倍率 *= 1.2862


class 技能16(主动技能):
    名称 = '吸魂暗劲波'
    所在等级 = 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.228) for i in [0, 1327, 1461, 1596, 1731, 1865, 2000, 2134, 2269, 2404, 2538, 2673, 2808, 2942, 3077, 3212, 3346, 3481, 3615, 3750, 3885, 4019, 4154, 4289, 4423, 4558, 4693, 4827, 4962, 5096, 5231, 5366, 5500, 5635, 5770, 5904,
                                    6039, 6174, 6308, 6443, 6577, 6712, 6847, 6981, 7116, 7251, 7385, 7520, 7655, 7789, 7924, 8058, 8193, 8328, 8462, 8597, 8732, 8866, 9001, 9136, 9270, 9405, 9539, 9674, 9809, 9943, 10078, 10213, 10347, 10482, 10617]]
    hit0 = 2
    data1 = [int(i*1.228) for i in [0, 5977, 6583, 7190, 7796, 8403, 9009, 9615, 10222, 10828, 11435, 12041, 12647, 13254, 13860, 14467, 15073, 15679, 16286, 16892, 17499, 18105, 18712, 19318, 19924, 20531, 21137, 21744, 22350, 22956, 23563, 24169, 24776, 25382, 25988, 26595,
                                    27201, 27808, 28414, 29020, 29627, 30233, 30840, 31446, 32053, 32659, 33265, 33872, 34478, 35085, 35691, 36297, 36904, 37510, 38117, 38723, 39329, 39936, 40542, 41149, 41755, 42361, 42968, 43574, 44181, 44787, 45394, 46000, 46606, 47213, 47819]]
    hit1 = 1
    CD = 35
    TP成长 = 0.1
    TP上限 = 5

    MP = [164, 1376]
    无色消耗 = 1


class 技能17(主动技能):
    名称 = '巴拉克的野心'
    所在等级 = 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.0) for i in [0, 2197, 2419, 2643, 2867, 3088, 3311, 3535, 3758, 3980, 4203, 4428, 4650, 4872, 5095, 5317, 5542, 5765, 5986, 6210, 6434, 6656, 6878, 7102, 7325, 7548, 7770, 7993, 8216, 8440, 8661, 8885, 9108, 9331, 9554, 9777, 9999, 10223, 10447, 10668, 10891, 11116, 11338, 11560, 11783, 12007, 12230, 12452, 12675, 12898, 13122, 13345, 13566, 13790, 14014, 14235, 14459, 14682, 14904, 15128, 15351, 15573, 15796, 16021, 16242, 16465, 16688, 16912, 17134, 17357, 17579]]
    hit0 = 1
    data1 = [int(i*1.0) for i in [0, 9865, 10866, 11866, 12868, 13868, 14869, 15871, 16871, 17872, 18872, 19874, 20875, 21875, 22877, 23878, 24878, 25879, 26881, 27881, 28882, 29883, 30884, 31885, 32885, 33887, 34886, 35887, 36889, 37889, 38890, 39890, 40892, 41893, 42893, 43895, 44895, 45896, 46897, 47898, 48899, 49900, 50901, 51902, 52902, 53903, 54905, 55905, 56906, 57908, 58908, 59909, 60910, 61911, 62910, 63911, 64913, 65913, 66914, 67916, 68916, 69917, 70917, 71919, 72920, 73920, 74922, 75923, 76923, 77924, 78925]]
    hit1 = 1
    CD = 25
    TP成长 = 0.1
    TP上限 = 5

    MP = [164, 1376]
    无色消耗 = 1

    def 装备护石(self):
        self.倍率 *= 1.18 * 1.18
        self.CDR *= 0.94


class 技能18(被动技能):
    名称 = '巴拉克的盟约'
    所在等级 = 40
    等级上限 = 20
    学习间隔 = 2
    等级精通 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.38 + 0.02 * self.等级, 5)   


class 技能19(主动技能):
    名称 = '降临 : 僵尸莱迪娅'
    所在等级 = 45
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data = [int(i*1.0) for i in [0, 579, 637, 696, 754, 811, 870, 931, 989, 1045, 1106, 1164, 1223, 1281, 1342, 1399, 1457, 1516, 1575, 1633, 1691, 1750, 1808, 1868, 1926, 1986, 2043, 2102, 2161, 2219, 2277, 2337, 2395, 2453, 2512, 2570, 2631, 2689, 2745, 2808, 2864, 2925, 2981, 3042, 3096, 3157, 3217, 3277, 3336, 3390, 3452, 3508, 3569, 3627, 3684, 3743, 3803, 3863, 3919, 3979, 4037, 4096, 4153, 4213, 4272, 4331, 4389, 4446, 4508, 4564, 4625]]
    攻击次数 = 30
    倍率 = 1.3
    CD = 45
    TP成长 = 0.1
    TP上限 = 5

    MP = [380, 3192]
    无色消耗 = 2

    形态 = ["蓄力", "不蓄力"]

    def 形态变更(self, 形态, char):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "蓄力":
            self.倍率 = 1.3
        if 形态 == "不蓄力":
            self.倍率 = 1.0


class 技能20(主动技能):
    名称 = '巴拉克的愤怒'
    所在等级 = 45
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.0) for i in [0, 1076, 1186, 1296, 1404, 1513, 1624, 1731, 1841, 1951, 2059, 2169, 2278, 2386, 2497, 2606, 2715, 2825, 2934, 3043, 3152, 3263, 3371, 3479, 3589, 3698, 3807, 3917, 4026, 4136, 4245, 4354, 4463, 4573, 4683, 4792, 4901, 5011, 5118, 5227, 5337, 5446, 5557, 5666, 5774, 5884, 5993, 6101, 6211, 6322, 6431, 6540, 6649, 6758, 6866, 6975, 7084, 7195, 7305, 7413, 7522, 7632, 7741, 7849, 7960, 8070, 8179, 8288, 8397, 8505, 8614]]
    hit0 = 1
    data1 = [int(i*1.0) for i in [0, 1080, 1190, 1299, 1409, 1519, 1629, 1739, 1848, 1958, 2067, 2178, 2287, 2397, 2507, 2616, 2726, 2835, 2946, 3055, 3166, 3275, 3384, 3494, 3604, 3714, 3823, 3934, 4043, 4152, 4263, 4372, 4482, 4590, 4702, 4810, 4919, 5030, 5139, 5249, 5358, 5469, 5578, 5689, 5798, 5907, 6017, 6126, 6237, 6347, 6457, 6566, 6675, 6785, 6895, 7005, 7115, 7225, 7334, 7443, 7553, 7663, 7774, 7883, 7993, 8102, 8211, 8321, 8432, 8542, 8651]]
    hit1 = 1
    data2 = [int(i*1.0) for i in [0, 915, 1007, 1101, 1192, 1286, 1378, 1472, 1563, 1658, 1749, 1843, 1935, 2028, 2121, 2214, 2306, 2400, 2492, 2585, 2680, 2771, 2864, 2957, 3050, 3142, 3235, 3327, 3419, 3512, 3606, 3698, 3792, 3883, 3978, 4069, 4163, 4255, 4348, 4440, 4534, 4626, 4719, 4812, 4905, 4996, 5091, 5182, 5277, 5368, 5462, 5556, 5648, 5740, 5833, 5927, 6018, 6113, 6204, 6298, 6390, 6484, 6576, 6670, 6761, 6855, 6947, 7040, 7133, 7226, 7317]]
    hit2 = 4
    data3 = [int(i*1.0) for i in [0, 3886, 4281, 4676, 5071, 5465, 5860, 6256, 6649, 7045, 7438, 7834, 8227, 8622, 9017, 9411, 9806, 10201, 10593, 10988, 11383, 11778, 12172, 12567, 12961, 13356, 13749, 14145, 14538, 14934, 15328, 15724, 16117, 16513, 16906, 17300, 17695, 18089, 18483, 18878, 19273, 19666, 20061, 20456, 20851, 21245, 21639, 22035, 22427, 22824, 23217, 23613, 24006, 24402, 24796, 25191, 25583, 25979, 26373, 26767, 27163, 27556, 27952, 28346, 28742, 29134, 29530, 29924, 30320, 30713, 31108]]
    hit3 = 1
    data4 = [int(i*1.0) for i in [0, 9736, 10724, 11713, 12700, 13689, 14677, 15664, 16652, 17640, 18628, 19616, 20605, 21590, 22580, 23567, 24554, 25542, 26531, 27518, 28506, 29495, 30482, 31471, 32459, 33445, 34434, 35422, 36410, 37397, 38387, 39372, 40360, 41349, 42337, 43325, 44313, 45302, 46288, 47275, 48265, 49252, 50240, 51229, 52216, 53202, 54193, 55179, 56166, 57156, 58142, 59131, 60119, 61107, 62095, 63083, 64070, 65058, 66047, 67034, 68023, 69008, 69996, 70985, 71972, 72961, 73949, 74937, 75925, 76912, 77900]]
    hit4 = 1
    CD = 45
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    MP = [380, 3192]
    无色消耗 = 2

    def 装备护石(self):
        self.倍率 *= 1.12 * 1.13
        self.CDR *= 0.89


class 技能21(被动技能):
    名称 = '屠戮之惧'
    所在等级 = 48
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.075 + 0.015 * self.等级, 5)


class 技能22(主动技能):
    名称 = '千魂祭'
    所在等级 = 50
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i*1.0) for i in [0, 677, 834, 990, 1148, 1305, 1464, 1618, 1776, 1934, 2090, 2247, 2405, 2562, 2719, 2877, 3033, 3190, 3348, 3504, 3662, 3818, 3976, 4132, 4290, 4447, 4605, 4762, 4918, 5076, 5232, 5389, 5546, 5704, 5862, 6017, 6175, 6333, 6489, 6645, 6803]]
    hit0 = 9
    data1 = [int(i*1.0) for i in [0, 2348, 2892, 3436, 3983, 4527, 5074, 5618, 6162, 6707, 7253, 7797, 8343, 8886, 9430, 9975, 10519, 11064, 11610, 12154, 12699, 13244, 13788, 14332, 14878, 15422, 15967, 16513, 17057, 17602, 18145, 18690, 19235, 19779, 20326, 20871, 21415, 21960, 22505, 23049, 23593]]
    hit1 = 13
    data2 = [int(i*1.0) for i in [0, 15281, 18824, 22369, 25911, 29455, 32998, 36542, 40085, 43630, 47173, 50718, 54260, 57803, 61347, 64890, 68434, 71978, 75522, 79063, 82608, 86151, 89696, 93239, 96783, 100327, 103869, 107412, 110957, 114500, 118044, 121588, 125129, 128674, 132217, 135761, 139305, 142849, 146392, 149936, 153478]]
    hit2 = 1
    CD = 145

    MP = [881, 7403]
    无色消耗 = 5

    #
    def 技能描述(self, 武器类型):
        temp = ''
        temp += '降临 : 尼古拉斯(蜘蛛团/黑蜘蛛), 降临 : 尼古拉斯(艾克洛索/艾克尼亚) Lv+5<br>'
        temp += '降临 : 暴君巴拉克(平x), 降临 : 暴君巴拉克(暗击拳), 降临 : 暴君巴拉克(巴拉克强击),降临 : 暴君巴拉克(杀戮乱舞)Lv+4'
        return temp


class 技能23(主动技能):
    名称 = '死灵之缚'
    所在等级 = 60
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.0) for i in [0, 790, 869, 949, 1029, 1108, 1190, 1270, 1348, 1428, 1508, 1588, 1668, 1749, 1827, 1908, 1990, 2069, 2149, 2230, 2308, 2388, 2470, 2549, 2629, 2707, 2787, 2868, 2948, 3031, 3110, 3189, 3268,
                                         3349, 3429, 3510, 3589, 3668, 3748, 3829, 3909, 3988, 4069, 4148, 4227, 4310, 4390, 4470, 4548, 4629, 4709, 4788, 4869, 4950, 5028, 5108, 5188, 5268, 5350, 5430, 5508, 5590, 5670, 5749, 5829, 5909, 5988, 6068, 6148, 6229, 6309]]
    hit0 = 20
    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [400, 1120]
    无色消耗 = 2

    def 装备护石(self):
        # 实际情况是先是一个4hit+1hit组成；4hit部分占原伤害的30%，1hit部分为原伤害的1.21*0.88
        self.倍率 *= 0.3+1.21*0.88


class 技能24(主动技能):
    名称 = '怨噬之沼'
    所在等级 = 70
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.0) for i in [0, 6445, 7101, 7755, 8408, 9064, 9717, 10371, 11024, 11680, 12334, 12987, 13640, 14296, 14950, 15604, 16258, 16912, 17566, 18220, 18874, 19528, 20182, 20836, 21490, 22144, 22798, 23452, 24106, 24760, 25414,
             26068, 26722, 27376, 28030, 28684, 29338, 29992, 30646, 31300, 31954, 32608, 33262, 33916, 34570, 35224, 35878, 36532, 37186, 37840, 38494, 39148, 39802, 40456, 41110, 41764, 42418, 43072, 43726, 44380, 45034]]
    hit0 = 1
    data1 = [int(i*1.0) for i in [0, 3221, 3551, 3877, 4204, 4531, 4857, 5184, 5511, 5840, 6167, 6493, 6820, 7147, 7474, 7801, 8128, 8455, 8782, 9109, 9436, 9763, 10090, 10417, 10744, 11071, 11398, 11725, 12052, 12379, 12706, 13033,
             13360, 13687, 14014, 14341, 14668, 14995, 15322, 15649, 15976, 16303, 16630, 16957, 17284, 17611, 17938, 18265, 18592, 18919, 19246, 19573, 19900, 20227, 20554, 20881, 21208, 21535, 21862, 22189, 22516]]
    hit1 = 3
    data2 = [int(i*1.0) for i in [0, 2148, 2367, 2584, 2801, 3020, 3237, 3457, 3674, 3893, 4110, 4327, 4547, 4764, 4983, 5201, 5419, 5637, 5855, 6073, 6291, 6509, 6727, 6945, 7163, 7381, 7599, 7817, 8035, 8253, 8471, 8689,
             8907, 9125, 9343, 9561, 9779, 9997, 10215, 10433, 10651, 10869, 11087, 11305, 11523, 11741, 11959, 12177, 12395, 12613, 12831, 13049, 13267, 13485, 13703, 13921, 14139, 14357, 14575, 14793, 15011]]
    hit2 = 3
    data3 = [int(i*1.0) for i in [0, 9669, 10652, 11632, 12615, 13595, 14575, 15558, 16538, 17520, 18500, 19483, 20463, 21443, 22426, 23407, 24388, 25369, 26350, 27331, 28312, 29293, 30274, 31255, 32236, 33217, 34198, 35179, 36160, 37141,
             38122, 39103, 40084, 41065, 42046, 43027, 44008, 44989, 45970, 46951, 47932, 48913, 49894, 50875, 51856, 52837, 53818, 54799, 55780, 56761, 57742, 58723, 59704, 60685, 61666, 62647, 63628, 64609, 65590, 66571, 67552]]
    hit3 = 1
    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [800, 1680]
    无色消耗 = 1

    def 装备护石(self):
        self.倍率 *= 1.3

class 技能25(主动技能):
    名称 = '暗黑蛛丝引'  # 一部分伤害统计时分给尼古拉斯了，约2.32765倍
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.0) for i in [0, 6946, 7653, 8356, 9058, 9765, 10468, 11177, 11877, 12584, 13290, 13992, 14699, 15401, 16108, 16810, 17517, 18221, 18926, 19632, 20334, 21041, 21745, 22451, 23154, 23861, 24563, 25270, 25973, 26676, 27384, 28085, 28793, 29496, 30203, 30906, 31609, 32316, 33021, 33725, 34428]]
    hit0 = 1
    data1 = [int(i*1.0) for i in [0, 9261, 10204, 11140, 12078, 13020, 13959, 14901, 15839, 16780, 17719, 18654, 19597, 20536, 21480, 22414, 23356, 24294, 25237, 26176, 27112, 28054, 28990, 29935, 30870, 31814, 32752, 33695, 34630, 35569, 36512, 37449, 38391, 39327, 40270, 41208, 42145, 43088, 44026, 44967, 45906]]
    hit1 = 1
    data2 = [int(i*1.0) for i in [0, 1158, 1275, 1393, 1511, 1627, 1746, 1862, 1980, 2096, 2216, 2334, 2450, 2567, 2684, 2802, 2918, 3037, 3153, 3271, 3390, 3507, 3625, 3741, 3859, 3976, 4094, 4210, 4329, 4447, 4562, 4682, 4799, 4916, 5032, 5151, 5269, 5385, 5504, 5621, 5738]]
    hit2 = 6
    CD = 20
    是否有护石 = 1

    MP = [580, 4500]
    无色消耗 = 3

    def 装备护石(self):
        self.hit0 = 0
        self.hit1 = 0
        self.power2 = 4.53
        self.CDR *= 0.9


class 技能26(被动技能):
    名称 = '亡魂之息'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40
    关联技能 = ['降临 : 尼古拉斯(蜘蛛团/黑蜘蛛)', '降临 : 尼古拉斯(艾克洛索/艾克尼亚)', '驱使僵尸', '暗影蛛丝阵', '死亡之爪', '死灵之怨', '百鬼夜行',
            '降临 : 暴君巴拉克(平x)', '降临 : 暴君巴拉克(暗击拳)', '降临 : 暴君巴拉克(巴拉克强击)',
            '降临 : 暴君巴拉克(杀戮乱舞)', '吸魂暗劲波', '巴拉克的野心', '降临 : 僵尸莱迪娅',
            '巴拉克的愤怒', '千魂祭', '死灵之缚', '怨噬之沼', '暗黑蛛丝引', '暴君极刑斩', '亡者君临 : 巴拉克之戮', '亡者之茧', '命运殇痕·摩罗斯之咒']
    关联技能2 = ['暗魂波', '诅咒之箭']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.16 + 0.02 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.31 + 0.02 * self.等级, 5)


class 技能27(主动技能):
    名称 = '暴君极刑斩'
    所在等级 = 80
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.0) for i in [0, 53403, 58821, 64238, 69656, 75073, 80491, 85909, 91327, 96745, 102162, 107580, 112998, 118415, 123833, 129251, 134668, 140087, 145503, 150922, 156338, 161757, 167175, 172592, 178011, 183427, 188846, 194262, 199681, 205097, 210516, 215933, 221351, 226769, 232186, 237605, 243022, 248440, 253857, 259275, 264693]]
    hit0 = 1
    CD = 45
    是否有护石 = 1

    MP = [800, 6000]
    无色消耗 = 5

    def 装备护石(self):
        self.倍率 *= 1.31


class 技能28(主动技能):
    名称 = '亡者君临 : 巴拉克之戮'
    所在等级 = 85
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30

    data0 = [int(i*1.0) for i in [0, 23469, 28913, 34353, 39797, 45241, 50682, 56126, 61567, 67010, 72451, 77895, 83339, 88780, 94223, 99664, 105107, 110550, 115990, 121435, 126878, 132319, 137763, 143204, 148647, 154088, 159533, 164975, 170417, 175861, 181301, 186745, 192187, 197630, 203072, 208515, 213956, 219400, 224842, 230284, 235725]]
    hit0 = 1
    data1 = [int(i*1.0) for i in [0, 3199, 3941, 4682, 5424, 6166, 6908, 7651, 8393, 9135, 9877, 10617, 11359, 12102, 12844, 13585, 14327, 15069, 15811, 16553, 17295, 18036, 18778, 19520, 20262, 21005, 21748, 22489, 23231, 23972, 24714, 25456, 26196, 26938, 27680, 28422, 29164, 29906, 30647, 31390, 32132]]
    hit1 = 11
    data2 = [int(i*1.0) for i in [0, 58676, 72284, 85890, 99497, 113104, 126708, 140315, 153922, 167528, 181135, 194741, 208347, 221953, 235560, 249167, 262773, 276380, 289987, 303593, 317198, 330805, 344411, 358018, 371625, 385232, 398839, 412442, 426049, 439656, 453262, 466870, 480477, 494083, 507690, 521293, 534900, 548509, 562114, 575721, 589328]]
    hit2 = 1
    CD = 180

    MP = [1500, 5000]
    无色消耗 = 10


class 技能29(被动技能):
    名称 = '冥河之钥'
    所在等级 = 95
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能30(主动技能):
    名称 = '亡者之茧'
    所在等级 = 95
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30

    data0 = [int(i*1.196*1.075) for i in [0, 4803, 5290, 5777, 6264, 6752, 7239, 7726, 8213, 8701, 9188, 9675, 10162, 10650, 11137, 11624, 12111, 12599, 13086, 13573, 14060, 14547, 15035, 15522, 16009, 16496, 16984, 17471, 17958, 18445, 18933, 19420, 19907, 20394, 20881,
                                          21369, 21856, 22343, 22830, 23318, 23805, 24292, 24779, 25267, 25754, 26241, 26728, 27216, 27703, 28190, 28677, 29164, 29652, 30139, 30626, 31113, 31601, 32088, 32575, 33062, 33550, 34037, 34524, 35011, 35499, 35986, 36473, 36960, 37447, 37935, 38422]]
    hit0 = 5
    data1 = [int(i*1.196*1.075) for i in [0, 56032, 61716, 67400, 73084, 78769, 84454, 90138, 95822, 101507, 107191, 112875, 118559, 124245, 129929, 135613, 141297, 146983, 152667, 158351, 164035, 169720, 175404, 181088, 186772, 192458, 198142, 203826, 209510, 215194, 220880, 226564, 232248, 237932, 243617,
                                          249302, 254986, 260670, 266355, 272039, 277723, 283407, 289093, 294777, 300461, 306145, 311831, 317515, 323199, 328883, 334568, 340252, 345936, 351621, 357306, 362990, 368674, 374358, 380042, 385728, 391412, 397096, 402780, 408465, 414150, 419834, 425518, 431203, 436887, 442571, 448255]]
    hit1 = 1
    CD = 60.0

    MP = [1066, 8000]
    无色消耗 = 7


class 技能31(主动技能):
    名称 = '命运殇痕·摩罗斯之咒'
    所在等级 = 100
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30

    data0 = [int(i*1.0) for i in [0, 339829, 418634, 497435, 576236, 655038, 733839, 812642, 891444, 970245, 1049046, 1127847, 1206651, 1285452, 1364253, 1443055, 1521856, 1600660, 1679462, 1758263, 1837063, 1915864, 1994669, 2073470, 2152271, 2231073, 2309874, 2388677, 2467479, 2546280, 2625081, 2703882, 2782686, 2861487, 2940288, 3019090, 3097891, 3176694, 3255496, 3334297, 3413098, 3491899, 3570704, 3649505, 3728305, 3807108, 3885908, 3964712, 4043514, 4122315, 4201116, 4279917, 4358721, 4437522, 4516323, 4595125, 4673926, 4752729, 4831531, 4910332, 4989133, 5067934, 5146739, 5225539, 5304340, 5383142, 5461943, 5540747, 5619549, 5698350, 5777151]]
    hit0 = 1
    CD = 290.0

    MP = [4027, 12888]
    无色消耗 = 15


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'necro'
        self.名称 = '隐夜·死灵术士'
        self.角色 = '暗夜使者'
        self.角色类型 = '输出'
        self.职业 = '死灵术士'
        self.武器选项 = ['手杖']
        self.输出类型选项 = ['魔法百分比']
        self.防具精通属性 = ['智力']
        self.类型 = '魔法百分比'
        self.武器类型 = '手杖'
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
        self.buff = 2.14

        super().__init__()