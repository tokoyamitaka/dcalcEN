
from core.baseClass.skill import 技能
from core.baseClass.character import Character
from core.baseClass.skill import 主动技能, 被动技能


class 技能0(被动技能):
    名称 = '长刀精通'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 0.95


class 技能1(主动技能):
    名称 = '掩护射击'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [21, 220]
    data0 = [int(i*1.111*1.085)for i in [0, 266, 293, 320, 347, 374, 402, 428, 455, 482, 509, 536, 563, 591, 617, 644, 671, 698, 725, 752, 780, 806, 833, 860, 887, 914, 941, 969, 995, 1022, 1049, 1077, 1103, 1130, 1158,
                                         1184, 1211, 1238, 1266, 1292, 1319, 1347, 1373, 1400, 1427, 1455, 1481, 1508, 1536, 1562, 1589, 1616, 1644, 1670, 1697, 1725, 1751, 1778, 1805, 1833, 1859, 1886, 1914, 1940, 1967, 1994, 2022, 2048, 2075, 2103, 2129]]
    hit0 = 10
    CD = 6
    TP成长 = 0.10
    TP上限 = 7


class 技能2(主动技能):
    名称 = '捷影步'
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [21, 220]
    data0 = [int(i*1.108*1.085) for i in [0, 476, 524, 573, 621, 669, 718, 766, 814, 863, 911, 959, 1007, 1056, 1104, 1152, 1201, 1249, 1297, 1346, 1394, 1442, 1490, 1539, 1587, 1635, 1684, 1732, 1780, 1829, 1877, 1925, 1973, 2022,
                                          2070, 2118, 2167, 2215, 2263, 2312, 2360, 2408, 2456, 2505, 2554, 2602, 2651, 2699, 2747, 2796, 2844, 2892, 2940, 2989, 3037, 3085, 3134, 3182, 3230, 3279, 3327, 3375, 3423, 3472, 3520, 3568, 3617, 3665, 3713, 3762, 3810]]
    hit0 = 5
    CD = 5
    TP成长 = 0.10
    TP上限 = 7


class 技能3(主动技能):
    名称 = '轮盘连射'
    所在等级 = 20
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [33, 346]
    data0 = [int(i*1.126*1.085) for i in [0, 1483, 1634, 1784, 1935, 2086, 2237, 2387, 2538, 2687, 2838, 2988, 3139, 3289, 3440, 3591, 3741, 3892, 4043, 4194, 4344, 4495, 4646, 4795, 4945, 5096, 5246, 5397, 5548, 5698, 5849, 6000, 6151,
                                          6301, 6452, 6603, 6752, 6902, 7053, 7203, 7354, 7505, 7655, 7806, 7957, 8108, 8258, 8409, 8560, 8710, 8859, 9010, 9160, 9311, 9462, 9612, 9763, 9914, 10065, 10215, 10366, 10517, 10667, 10816, 10967, 11117, 11268, 11419, 11569, 11720]]
    hit0 = 1
    data1 = [int(i*1.126*1.085) for i in [0, 1887, 2080, 2271, 2463, 2654, 2846, 3037, 3229, 3421, 3613, 3803, 3995, 4187, 4379, 4570, 4762, 4953, 5145, 5336, 5529, 5719, 5911, 6103, 6295, 6486, 6677, 6869, 7061, 7252, 7444, 7636, 7827, 8018, 8211,
                                          8402, 8594, 8784, 8977, 9168, 9360, 9552, 9743, 9934, 10126, 10318, 10510, 10700, 10892, 11084, 11276, 11467, 11659, 11850, 12042, 12233, 12426, 12618, 12808, 13000, 13192, 13383, 13575, 13766, 13958, 14149, 14342, 14534, 14724, 14915]]
    hit1 = 0
    data2 = [int(i*1.126*1.085) for i in [0, 222, 244, 267, 289, 313, 335, 358, 380, 403, 425, 448, 470, 493, 515, 539, 560, 584, 606, 629, 651, 673, 696, 718, 742, 763, 787, 808, 832, 853, 877, 900, 922, 945, 967,
                                          990, 1012, 1035, 1057, 1080, 1103, 1125, 1147, 1170, 1194, 1215, 1239, 1261, 1284, 1306, 1329, 1351, 1373, 1396, 1418, 1441, 1464, 1487, 1509, 1532, 1554, 1577, 1599, 1622, 1644, 1668, 1689, 1713, 1734, 1758]]
    hit2 = 3
    power2 = 3.72
    # 三觉被动变更
    CD = 8
    TP成长 = 0.10
    TP上限 = 7


class 技能4(主动技能):
    名称 = '剑刃突刺'
    所在等级 = 20
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [33, 346]
    data0 = [int(i*1.112*1.085) for i in [0, 330, 364, 397, 430, 464, 498, 531, 564, 598, 631, 665, 699, 733, 765, 799, 833, 866, 900, 933, 966, 1000, 1034, 1067, 1100, 1134, 1167, 1201, 1235, 1267, 1301, 1335, 1369, 1402, 1435,
                                          1469, 1502, 1536, 1570, 1602, 1636, 1670, 1703, 1737, 1771, 1803, 1837, 1871, 1905, 1938, 1971, 2005, 2038, 2072, 2106, 2138, 2172, 2206, 2239, 2273, 2307, 2339, 2373, 2407, 2441, 2473, 2507, 2541, 2574, 2608, 2642]]
    hit0 = 4
    data1 = [int(i*1.112*1.085) for i in [0, 998, 1098, 1200, 1301, 1402, 1503, 1605, 1705, 1807, 1908, 2009, 2110, 2212, 2312, 2414, 2516, 2616, 2718, 2819, 2919, 3021, 3123, 3223, 3325, 3426, 3527, 3628, 3730, 3830, 3932, 4033, 4134,
                                          4235, 4337, 4437, 4539, 4641, 4741, 4843, 4944, 5045, 5146, 5248, 5348, 5450, 5551, 5652, 5753, 5855, 5955, 6057, 6158, 6259, 6360, 6462, 6562, 6664, 6764, 6866, 6968, 7068, 7170, 7271, 7372, 7473, 7575, 7675, 7777, 7878, 7979]]
    hit1 = 1
    data2 = [int(i*1.112*1.085) for i in [0, 320, 353, 386, 419, 451, 484, 515, 548, 581, 613, 646, 679, 712, 744, 776, 808, 841, 874, 907, 939, 972, 1005, 1036, 1069, 1102, 1134, 1167, 1200, 1232, 1264, 1297, 1329, 1362, 1395,
                                          1427, 1460, 1493, 1524, 1557, 1590, 1622, 1655, 1688, 1720, 1753, 1785, 1817, 1850, 1883, 1915, 1948, 1981, 2012, 2045, 2078, 2110, 2143, 2176, 2208, 2241, 2273, 2305, 2338, 2371, 2403, 2436, 2469, 2501, 2533, 2566]]
    hit2 = 3
    CD = 6
    TP成长 = 0.10
    TP上限 = 7


class 技能5(主动技能):
    名称 = '潜行射击'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [47, 493]
    data0 = [int(i*1.113*1.085) for i in [0, 261, 287, 313, 340, 366, 393, 419, 445, 472, 498, 525, 552, 577, 604, 631, 657, 684, 709, 736, 763, 789, 816, 842, 868, 895, 922, 948, 974, 1000, 1027, 1054, 1080, 1106, 1133,
                                          1159, 1186, 1213, 1238, 1265, 1291, 1318, 1345, 1370, 1397, 1424, 1450, 1477, 1503, 1529, 1556, 1582, 1609, 1635, 1661, 1688, 1715, 1741, 1767, 1794, 1820, 1847, 1872, 1899, 1926, 1952, 1979, 2006, 2031, 2058, 2085]]
    hit0 = 15
    CD = 7
    TP成长 = 0.10
    TP上限 = 7


class 技能6(主动技能):
    名称 = '利刃旋斩'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [33, 346]
    data0 = [int(i*1.112*1.085) for i in [0, 515, 567, 620, 672, 724, 776, 829, 881, 933, 985, 1038, 1090, 1143, 1194, 1247, 1299, 1352, 1404, 1456, 1508, 1561, 1613, 1665, 1717, 1770, 1822, 1875, 1926, 1979, 2031, 2084, 2135, 2188,
                                          2240, 2293, 2345, 2397, 2449, 2502, 2554, 2607, 2658, 2711, 2763, 2816, 2867, 2919, 2972, 3024, 3077, 3128, 3181, 3233, 3286, 3337, 3390, 3442, 3495, 3547, 3599, 3651, 3704, 3756, 3809, 3860, 3913, 3965, 4018, 4069, 4122]]
    hit0 = 2
    data1 = [int(i*1.112*1.085) for i in [0, 288, 318, 347, 376, 406, 435, 465, 493, 522, 552, 581, 611, 640, 669, 699, 727, 756, 786, 815, 845, 874, 903, 933, 961, 991, 1020, 1049, 1079, 1108, 1138, 1167, 1196, 1225, 1254,
                                          1284, 1313, 1342, 1372, 1401, 1431, 1459, 1488, 1518, 1547, 1577, 1606, 1635, 1665, 1693, 1722, 1752, 1781, 1811, 1840, 1869, 1899, 1927, 1957, 1986, 2015, 2045, 2074, 2104, 2133, 2162, 2191, 2220, 2250, 2279, 2308]]
    hit1 = 5
    data2 = [int(i*1.112*1.085) for i in [0, 1649, 1816, 1983, 2151, 2318, 2485, 2653, 2820, 2987, 3155, 3322, 3489, 3656, 3824, 3990, 4157, 4325, 4492, 4659, 4827, 4994, 5161, 5328, 5496, 5663, 5830, 5998, 6165, 6332, 6500, 6667, 6834, 7002, 7169,
                                          7336, 7503, 7671, 7838, 8005, 8173, 8340, 8507, 8675, 8841, 9008, 9175, 9343, 9510, 9677, 9845, 10012, 10179, 10347, 10514, 10681, 10849, 11016, 11183, 11350, 11518, 11685, 11852, 12020, 12187, 12354, 12522, 12689, 12856, 13023, 13191]]
    hit2 = 1
    CD = 7
    TP成长 = 0.10
    TP上限 = 7


class 技能7(被动技能):
    名称 = '暗刃战略'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10

    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.02 * self.等级, 5)


class 技能8(主动技能):
    名称 = '游弹枪袭'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [62, 651]
    data0 = [int(i*1.118*1.085) for i in [0, 175, 192, 210, 227, 245, 262, 280, 297, 316, 334, 351, 369, 386, 404, 421, 439, 457, 475, 492, 510, 528, 545, 563, 581, 599, 616, 634, 651, 669, 686, 704, 723, 740, 758,
                                          775, 793, 810, 828, 845, 864, 882, 899, 917, 934, 952, 969, 987, 1005, 1023, 1041, 1058, 1076, 1093, 1111, 1128, 1147, 1164, 1182, 1199, 1217, 1234, 1252, 1270, 1288, 1306, 1323, 1341, 1358, 1376, 1393]]
    hit0 = 30
    CD = 8
    TP成长 = 0.10
    TP上限 = 7


class 技能9(主动技能):
    名称 = '全方位射击'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.122*1.085) for i in [0, 365, 403, 440, 476, 514, 550, 587, 624, 661, 699, 735, 772, 810, 846, 886, 922, 959, 996, 1033, 1070, 1106, 1145, 1181, 1218, 1256, 1293, 1329, 1367, 1404, 1440, 1478, 1515, 1552,
                                          1587, 1628, 1664, 1698, 1739, 1774, 1811, 1850, 1886, 1922, 1960, 1997, 2033, 2071, 2108, 2145, 2182, 2220, 2256, 2294, 2330, 2367, 2405, 2441, 2480, 2516, 2554, 2591, 2628, 2665, 2701, 2740, 2776, 2812, 2851, 2888, 2923]]
    hit0 = 15
    data1 = [int(i*1.122*1.085) for i in [0, 609, 671, 733, 793, 856, 918, 979, 1041, 1102, 1165, 1229, 1290, 1351, 1412, 1474, 1537, 1598, 1660, 1720, 1782, 1844, 1906, 1969, 2031, 2093, 2155, 2215, 2278, 2340, 2401, 2463, 2524,
                                          2586, 2649, 2709, 2771, 2834, 2895, 2958, 3021, 3082, 3144, 3204, 3266, 3329, 3390, 3452, 3513, 3575, 3635, 3699, 3761, 3823, 3885, 3947, 4008, 4071, 4133, 4193, 4255, 4316, 4378, 4442, 4503, 4565, 4625, 4688, 4751, 4812, 4874]]
    hit1 = 6
    CD = 15
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    技能施放时间 = 1

    MP = [131, 1100]
    无色消耗 = 1

    def 装备护石(self):
        self.hit0 = 20
        self.hit1 = 0
        self.power0 *= 1.4732
        self.CDR *= 0.95


class 技能10(主动技能):
    名称 = '回旋飞剑'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.117*1.085) for i in [0, 607, 670, 731, 793, 855, 916, 979, 1038, 1102, 1163, 1225, 1286, 1349, 1410, 1472, 1535, 1594, 1655, 1717, 1780, 1841, 1904, 1966, 2028, 2089, 2152, 2211, 2274, 2334, 2397, 2457, 2520,
                                          2583, 2643, 2707, 2766, 2828, 2891, 2952, 3014, 3076, 3137, 3200, 3260, 3322, 3382, 3445, 3508, 3569, 3631, 3693, 3755, 3817, 3879, 3939, 4001, 4062, 4124, 4185, 4248, 4310, 4372, 4433, 4494, 4555, 4618, 4679, 4741, 4804, 4864]]
    hit0 = 1
    data1 = [int(i*1.117*1.085) for i in [0, 489, 540, 587, 637, 687, 737, 786, 837, 885, 936, 985, 1035, 1085, 1135, 1182, 1234, 1284, 1332, 1381, 1433, 1481, 1531, 1580, 1629, 1680, 1730, 1777, 1830, 1879, 1926, 1976, 2028, 2076,
                                          2125, 2176, 2225, 2275, 2324, 2374, 2424, 2474, 2521, 2573, 2622, 2671, 2720, 2772, 2820, 2870, 2920, 2970, 3019, 3069, 3117, 3168, 3217, 3266, 3316, 3367, 3415, 3466, 3515, 3565, 3614, 3665, 3712, 3764, 3813, 3862, 3912]]
    hit1 = 8
    data2 = [int(i*1.117*1.085) for i in [0, 1306, 1438, 1572, 1704, 1837, 1970, 2103, 2235, 2370, 2500, 2633, 2765, 2899, 3030, 3163, 3296, 3429, 3560, 3694, 3826, 3959, 4090, 4224, 4356, 4489, 4623, 4754, 4886, 5021, 5153, 5286, 5416,
                                          5551, 5683, 5815, 5949, 6080, 6212, 6347, 6479, 6610, 6742, 6877, 7009, 7140, 7274, 7407, 7539, 7673, 7804, 7937, 8069, 8203, 8335, 8467, 8600, 8733, 8865, 8998, 9131, 9264, 9396, 9530, 9661, 9794, 9927, 10060, 10191, 10324, 10457]]
    hit2 = 5
    CD = 20
    TP成长 = 0.10
    TP上限 = 5

    MP = [62, 651]
    无色消耗 = 1


class 技能11(主动技能):
    名称 = '枪刃乱舞'
    所在等级 = 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.12*1.085) for i in [0, 418, 458, 504, 544, 587, 630, 671, 713, 756, 799, 842, 882, 927, 969, 1011, 1052, 1095, 1137, 1179, 1224, 1264, 1306, 1350, 1392, 1435, 1476, 1519, 1562, 1602, 1648, 1688, 1730, 1773,
                                         1815, 1858, 1900, 1942, 1986, 2028, 2069, 2112, 2155, 2195, 2239, 2282, 2325, 2365, 2408, 2451, 2493, 2535, 2579, 2622, 2663, 2706, 2748, 2791, 2832, 2874, 2918, 2958, 3001, 3045, 3087, 3130, 3172, 3213, 3256, 3298, 3341]]
    hit0 = 10
    data1 = [int(i*1.12*1.085) for i in [0, 288, 317, 347, 374, 406, 436, 463, 493, 523, 552, 581, 611, 639, 669, 699, 727, 756, 787, 816, 844, 874, 903, 933, 962, 990, 1021, 1048, 1079, 1109, 1137, 1166, 1197, 1226, 1253,
                                         1284, 1313, 1340, 1372, 1400, 1429, 1458, 1489, 1518, 1547, 1576, 1604, 1636, 1663, 1694, 1722, 1750, 1782, 1810, 1839, 1868, 1899, 1926, 1957, 1986, 2014, 2046, 2074, 2102, 2132, 2163, 2191, 2220, 2251, 2277, 2309]]
    hit1 = 15
    data2 = [int(i*1.12*1.085) for i in [0, 5450, 6002, 6557, 7110, 7662, 8215, 8770, 9321, 9873, 10426, 10979, 11533, 12086, 12640, 13191, 13746, 14298, 14852, 15406, 15958, 16510, 17063, 17617, 18171, 18722, 19276, 19829, 20381, 20934, 21487, 22041, 22593, 23147,
                                         23699, 24251, 24804, 25357, 25911, 26464, 27018, 27569, 28122, 28674, 29229, 29782, 30334, 30887, 31442, 31994, 32548, 33100, 33654, 34207, 34760, 35313, 35864, 36418, 36970, 37525, 38078, 38630, 39182, 39737, 40289, 40843, 41394, 41949, 42502, 43053, 43607]]
    hit2 = 1
    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    power1 = 1
    power2 = 1

    MP = [174, 1461]
    无色消耗 = 1

    def 装备护石(self):
        self.power0 *= 1.07
        self.power1 *= 1.07
        self.power2 *= 1.50
        self.CDR *= 0.80


class 技能12(主动技能):
    名称 = '血光斩'
    所在等级 = 45
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.125*1.085) for i in [0, 20826, 22939, 25051, 27164, 29278, 31390, 33503, 35615, 37728, 39841, 41954, 44067, 46179, 48292, 50405, 52517, 54631, 56744, 58856, 60969, 63081, 65195, 67308, 69420, 71533, 73645, 75758, 77872, 79984, 82097, 84209, 86322, 88435, 90548, 92661,
                                          94773, 96886, 98999, 101112, 103225, 105338, 107450, 109563, 111675, 113789, 115902, 118014, 120127, 122239, 124353, 126466, 128578, 130691, 132803, 134916, 137030, 139142, 141255, 143367, 145480, 147593, 149706, 151819, 153932, 156044, 158157, 160270, 162383, 164496, 166608]]
    hit0 = 1
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [305, 2562]
    无色消耗 = 2

    def 装备护石(self):
        self.倍率 *= 1.33


class 技能13(被动技能):
    名称 = 'BG枪刃改造'
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


class 技能14(主动技能):
    名称 = '电光飞掠'
    所在等级 = 50
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i*1.109*1.085) for i in [0, 1802, 2220, 2637, 3055, 3473, 3891, 4309, 4727, 5145, 5562, 5980, 6398, 6816, 7234, 7652, 8070, 8487, 8905, 9323, 9741, 10159, 10577, 10995, 11411, 11829, 12247, 12665, 13083, 13501, 13919, 14336, 14754, 15172, 15590,
                                          16008, 16426, 16844, 17261, 17679, 18097, 18515, 18933, 19351, 19769, 20186, 20604, 21022, 21440, 21858, 22276, 22694, 23111, 23529, 23947, 24365, 24783, 25201, 25619, 26036, 26454, 26872, 27290, 27708, 28126, 28544, 28960, 29378, 29796, 30214, 30632]]
    hit0 = 13
    data1 = [int(i*1.109*1.085) for i in [0, 2196, 2705, 3215, 3724, 4233, 4742, 5251, 5760, 6269, 6780, 7289, 7798, 8307, 8816, 9325, 9834, 10344, 10853, 11362, 11871, 12381, 12890, 13399, 13908, 14418, 14927, 15436, 15945, 16454, 16963, 17472, 17983, 18492, 19001,
                                          19510, 20019, 20528, 21037, 21547, 22056, 22566, 23075, 23584, 24093, 24602, 25111, 25621, 26130, 26639, 27148, 27657, 28167, 28676, 29186, 29695, 30204, 30713, 31222, 31731, 32240, 32751, 33260, 33769, 34278, 34787, 35296, 35805, 36314, 36824, 37333]]
    hit1 = 16
    CD = 145

    MP = [1018, 8551]
    无色消耗 = 5


class 技能15(主动技能):
    名称 = '近敌灭杀'
    所在等级 = 60
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.122*1.085) for i in [0, 7595, 8366, 9136, 9907, 10678, 11448, 12219, 12989, 13760, 14531, 15301, 16071, 16842, 17613, 18383, 19153, 19924, 20695, 21466, 22235, 23006, 23777, 24548, 25319, 26088, 26859, 27630, 28401, 29170, 29941, 30712, 31483, 32252,
                                          33023, 33794, 34565, 35335, 36105, 36876, 37647, 38418, 39188, 39958, 40729, 41500, 42270, 43041, 43811, 44582, 45352, 46123, 46893, 47664, 48435, 49205, 49976, 50746, 51517, 52287, 53058, 53829, 54599, 55369, 56140, 56911, 57681, 58451, 59222, 59993, 60764]]
    hit0 = 1
    data1 = [int(i*1.122*1.085) for i in [0, 569, 628, 685, 743, 801, 859, 916, 975, 1032, 1090, 1147, 1206, 1263, 1321, 1379, 1436, 1494, 1551, 1610, 1667, 1726, 1783, 1841, 1898, 1957, 2014, 2072, 2130, 2188, 2245, 2304, 2361, 2419,
                                          2476, 2535, 2592, 2650, 2708, 2766, 2823, 2882, 2939, 2997, 3055, 3112, 3170, 3227, 3286, 3343, 3401, 3459, 3517, 3574, 3633, 3690, 3748, 3806, 3864, 3921, 3980, 4037, 4095, 4152, 4211, 4268, 4326, 4384, 4442, 4499, 4558]]
    hit1 = 20
    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    power1 = 1

    MP = [340, 952]
    无色消耗 = 2

    def 装备护石(self):
        self.power1 *= 1.553
        self.CDR *= 0.85


class 技能16(主动技能):
    名称 = '大回旋坠斩'
    所在等级 = 70
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.113*1.085) for i in [0, 1223, 1347, 1471, 1596, 1719, 1843, 1967, 2091, 2214, 2339, 2463, 2587, 2711, 2835, 2957, 3083, 3207, 3331, 3455, 3577, 3703, 3828, 3952, 4076, 4200, 4325, 4448, 4572, 4696, 4820, 4943, 5068,
                                          5192, 5316, 5440, 5563, 5687, 5810, 5936, 6060, 6183, 6307, 6433, 6557, 6681, 6805, 6928, 7052, 7177, 7301, 7425, 7549, 7672, 7796, 7921, 8045, 8169, 8292, 8416, 8541, 8664, 8789, 8912, 9037, 9162, 9286, 9410, 9534, 9657, 9781]]
    hit0 = 10
    data1 = [int(i*1.113*1.085) for i in [0, 1171, 1287, 1406, 1527, 1645, 1763, 1882, 2001, 2120, 2239, 2357, 2475, 2594, 2712, 2831, 2951, 3069, 3188, 3306, 3425, 3543, 3661, 3780, 3901, 4017, 4137, 4256, 4376, 4494, 4613, 4729, 4849,
                                          4968, 5086, 5205, 5325, 5443, 5561, 5680, 5799, 5917, 6036, 6154, 6273, 6393, 6510, 6630, 6750, 6868, 6987, 7102, 7223, 7342, 7460, 7579, 7699, 7816, 7935, 8054, 8174, 8291, 8410, 8527, 8647, 8766, 8884, 9004, 9124, 9242, 9361]]
    hit1 = 10
    data2 = [int(i*1.113*1.085) for i in [0, 10134, 11161, 12189, 13217, 14243, 15274, 16300, 17328, 18357, 19384, 20412, 21441, 22468, 23497, 24525, 25552, 26582, 27610, 28636, 29665, 30691, 31722, 32749, 33776, 34805, 35832, 36859, 37889, 38917, 39945, 40973, 42001,
                                          43029, 44057, 45084, 46113, 47140, 48168, 49196, 50225, 51252, 52280, 53307, 54336, 55364, 56392, 57421, 58449, 59476, 60504, 61530, 62561, 63588, 64615, 65644, 66671, 67701, 68728, 69756, 70784, 71812, 72840, 73868, 74896, 75925, 76952, 77979, 79010, 80036, 81064]]
    hit2 = 1
    power2 = 1
    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [699, 1467]
    无色消耗 = 2

    # 暂时只录入了地面形态的护石数据
    # 空中形态段数001，power2 *= 3.9483

    形态 = ["地面", "空中"]

    def 形态变更(self, 形态, char: Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "空中" and '大回旋坠斩' in char.护石栏:
            self.hit0 = 0
            self.hit1 = 0
            self.hit2 = 1
            self.power2 = 3.9483
        else:
            形态 = "地面"
        if 形态 == "地面":
            self.hit0 = 10
            self.hit1 = 10
            self.hit2 = 1
            if '大回旋坠斩' in char.护石栏:
                self.hit0 += 1
                self.hit1 += 1

    def 装备护石(self):
        self.hit0 += 1
        self.hit1 += 1
        self.power0 = 1.23
        self.power1 = 1.23
        self.power2 = 1.23


class 技能17(主动技能):
    名称 = '致命焰火'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    # 此处为原地射击数据，向后射击数据为10 10 0
    data0 = [int(i*1.115*1.085) for i in [0, 2221, 2447, 2671, 2898, 3123, 3348, 3575, 3799, 4024, 4249, 4476, 4701, 4926, 5149, 5376, 5603, 5826, 6053, 6278, 6503, 6730, 6954, 7179, 7405, 7631, 7856, 8082, 8307, 8532, 8759, 8984, 9208, 9433, 9660, 9885,
                                          10110, 10334, 10560, 10786, 11011, 11237, 11462, 11687, 11914, 12139, 12364, 12590, 12813, 13041, 13266, 13490, 13715, 13941, 14167, 14392, 14617, 14843, 15069, 15294, 15520, 15745, 15969, 16197, 16422, 16646, 16870, 17098, 17322, 17547, 17772]]
    hit0 = 10
    data1 = [int(i*1.115*1.085) for i in [0, 2224, 2449, 2675, 2901, 3125, 3353, 3578, 3802, 4030, 4255, 4478, 4707, 4932, 5155, 5384, 5608, 5832, 6060, 6284, 6509, 6736, 6960, 7186, 7413, 7637, 7863, 8090, 8314, 8542, 8767, 8991, 9219, 9443, 9668, 9896,
                                          10120, 10345, 10573, 10797, 11022, 11248, 11474, 11699, 11924, 12151, 12376, 12601, 12828, 13054, 13278, 13504, 13731, 13955, 14181, 14408, 14632, 14858, 15084, 15309, 15535, 15761, 15986, 16212, 16437, 16663, 16889, 17114, 17341, 17565, 17791]]
    hit1 = 15
    data2 = [int(i*1.115*1.085) for i in [0, 3332, 3669, 4009, 4346, 4685, 5023, 5362, 5698, 6037, 6375, 6712, 7051, 7389, 7727, 8065, 8404, 8742, 9078, 9419, 9756, 10093, 10433, 10770, 11108, 11447, 11785, 12123, 12461, 12799, 13135, 13476, 13812, 14150, 14489,
                                          14826, 15165, 15502, 15842, 16179, 16516, 16856, 17192, 17531, 17869, 18208, 18545, 18885, 19222, 19561, 19899, 20237, 20574, 20914, 21251, 21588, 21928, 22265, 22603, 22941, 23278, 23617, 23954, 24294, 24630, 24968, 25307, 25645, 25983, 26322, 26660]]
    hit2 = 0
    CD = 40
    是否有护石 = 1

    MP = [579, 4487]
    无色消耗 = 3

    形态 = ["原地", "向后"]

    def 形态变更(self, 形态, char:Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "原地":
            self.hit0 = 10
            self.hit1 = 15
            self.hit2 = 0
        if 形态 == "向后":
            self.hit0 = 10
            self.hit1 = 0
            self.hit2 = 10

    def 装备护石(self):
        self.倍率 *= 1.3
        self.CDR *= 0.90


class 技能18(被动技能):
    名称 = 'BC精锐特训'
    所在等级 = 75

    等级上限 = 50
    等级精通 = 40
    学习间隔 = 3

    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


class 技能19(主动技能):
    名称 = '碧波瞬斩'
    所在等级 = 80
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.118*1.085) for i in [0, 21717, 23919, 26122, 28326, 30529, 32732, 34935, 37139, 39342, 41545, 43748, 45952, 48155, 50357, 52560, 54763, 56967, 59170, 61373, 63576, 65780, 67983, 70186, 72389, 74591, 76795, 78998, 81201, 83404, 85608, 87811, 90014, 92217, 94420, 96624,
                                          98826, 101029, 103232, 105436, 107639, 109842, 112045, 114249, 116452, 118655, 120858, 123060, 125264, 127467, 129670, 131873, 134077, 136280, 138483, 140686, 142889, 145093, 147296, 149498, 151701, 153905, 156108, 158311, 160514, 162718, 164921, 167124, 169327, 171530, 173733]]
    hit0 = 3
    CD = 50
    是否有护石 = 1

    MP = [839, 6292]
    无色消耗 = 5

    def 装备护石(self):
        self.hit0 = 1
        self.倍率 *= 4.11


class 技能20(主动技能):
    名称 = '集结·暮光之翼'
    所在等级 = 85

    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i*1.111*1.085) for i in [0, 10282, 12667, 15051, 17436, 19819, 22204, 24588, 26973, 29357, 31741, 34125, 36510, 38895, 41279, 43663, 46047, 48432, 50816, 53200, 55584, 57969, 60353, 62738, 65121, 67506, 69891, 72275, 74660, 77043, 79428, 81812, 84197, 86580, 88965, 91349,
                                          93734, 96119, 98502, 100887, 103271, 105656, 108040, 110424, 112808, 115193, 117577, 119962, 122345, 124730, 127115, 129499, 131883, 134267, 136652, 139036, 141421, 143804, 146189, 148573, 150958, 153342, 155726, 158111, 160495, 162880, 165263, 167648, 170032, 172417, 174801]]
    hit0 = 4
    data1 = [int(i*1.111*1.085) for i in [0, 2493, 3071, 3648, 4227, 4804, 5383, 5960, 6539, 7116, 7695, 8272, 8851, 9428, 10007, 10584, 11163, 11741, 12319, 12897, 13475, 14053, 14631, 15209, 15787, 16365, 16943, 17521, 18099, 18677, 19255, 19833, 20411, 20989,
                                          21567, 22145, 22724, 23301, 23880, 24457, 25036, 25613, 26192, 26769, 27348, 27925, 28504, 29081, 29660, 30237, 30816, 31393, 31972, 32549, 33128, 33705, 34284, 34862, 35440, 36018, 36596, 37174, 37752, 38330, 38908, 39486, 40064, 40642, 41220, 41798, 42376]]
    hit1 = 11
    data2 = [int(i*1.111*1.085) for i in [0, 2742, 3377, 4014, 4650, 5285, 5921, 6557, 7193, 7828, 8465, 9100, 9736, 10371, 11008, 11644, 12279, 12915, 13551, 14187, 14822, 15459, 16094, 16730, 17365, 18002, 18637, 19273, 19910, 20545, 21181, 21816, 22453, 23088,
                                          23724, 24359, 24996, 25631, 26267, 26904, 27539, 28175, 28810, 29447, 30082, 30718, 31353, 31990, 32625, 33261, 33898, 34533, 35169, 35804, 36441, 37076, 37712, 38348, 38984, 39619, 40255, 40892, 41527, 42163, 42798, 43435, 44070, 44706, 45342, 45978, 46613]]
    hit2 = 20
    data3 = [int(i*1.111*1.085) for i in [0, 13710, 16889, 20068, 23247, 26426, 29605, 32785, 35964, 39142, 42322, 45501, 48680, 51859, 55038, 58218, 61396, 64575, 67755, 70933, 74113, 77292, 80471, 83650, 86829, 90009, 93187, 96366, 99546, 102725, 105903, 109083, 112262, 115441, 118620,
                                          121799, 124979, 128157, 131337, 134516, 137694, 140874, 144053, 147233, 150411, 153590, 156770, 159949, 163127, 166307, 169486, 172665, 175844, 179023, 182203, 185381, 188561, 191740, 194918, 198098, 201277, 204456, 207635, 210814, 213994, 217172, 220351, 223531, 226710, 229889, 233068]]
    hit3 = 1
    CD = 180

    MP = [2500, 5000]
    无色消耗 = 10


class 技能21(主动技能):
    名称 = '燃情协战'
    所在等级 = 95

    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    # 此处为向前突进形态的数据，普通施放为0 0 0 10 6
    data0 = [int(i*1.112*1.085) for i in [0, 2224, 2450, 2676, 2902, 3127, 3353, 3579, 3805, 4030, 4256, 4482, 4708, 4932, 5158, 5384, 5610, 5835, 6061, 6287, 6513, 6738, 6964, 7190, 7416, 7641, 7867, 8093, 8319, 8544, 8769, 8995, 9221, 9446, 9672,
                                          9898, 10124, 10349, 10575, 10801, 11027, 11252, 11478, 11704, 11930, 12155, 12381, 12606, 12831, 13057, 13283, 13509, 13734, 13960, 14186, 14412, 14637, 14863, 15089, 15315, 15540, 15766, 15992, 16218, 16442, 16668, 16894, 17120, 17345, 17571]]
    hit0 = 10
    data1 = [int(i*1.112*1.085) for i in [0, 6674, 7350, 8028, 8705, 9382, 10059, 10737, 11413, 12090, 12767, 13445, 14122, 14798, 15475, 16153, 16830, 17507, 18184, 18861, 19538, 20215, 20892, 21570, 22246, 22923, 23600, 24278, 24955, 25632, 26308, 26985, 27663,
                                          28340, 29017, 29694, 30371, 31048, 31725, 32402, 33080, 33756, 34433, 35110, 35788, 36465, 37142, 37818, 38496, 39173, 39850, 40527, 41205, 41881, 42558, 43235, 43913, 44590, 45266, 45943, 46620, 47298, 47975, 48652, 49328, 50006, 50683, 51360, 52037, 52714]]
    hit1 = 5
    data2 = [int(i*1.112*1.085) for i in [0, 55616, 61259, 66900, 72543, 78185, 83827, 89469, 95112, 100753, 106396, 112038, 117680, 123322, 128965, 134606, 140249, 145891, 151533, 157175, 162818, 168459, 174102, 179744, 185386, 191028, 196671, 202312, 207955, 213597, 219239, 224881, 230524, 236165,
                                          241808, 247450, 253092, 258734, 264377, 270020, 275661, 281304, 286946, 292588, 298230, 303873, 309514, 315157, 320799, 326441, 332083, 337726, 343367, 349010, 354652, 360294, 365936, 371579, 377220, 382863, 388505, 394147, 399789, 405432, 411073, 416716, 422358, 428000, 433642, 439285]]
    hit2 = 1
    data3 = [int(i*1.112*1.085) for i in [0, 3894, 4289, 4683, 5078, 5473, 5868, 6264, 6659, 7053, 7448, 7843, 8238, 8634, 9028, 9423, 9818, 10213, 10609, 11003, 11398, 11793, 12188, 12583, 12978, 13373, 13768, 14163, 14558, 14952, 15348, 15743, 16138, 16533,
                                          16928, 17323, 17718, 18113, 18508, 18903, 19297, 19693, 20088, 20483, 20878, 21272, 21667, 22063, 22458, 22853, 23247, 23642, 24037, 24433, 24828, 25223, 25617, 26012, 26408, 26803, 27198, 27592, 27987, 28382, 28778, 29173, 29567, 29962, 30357, 30752]]
    hit3 = 0
    data4 = [int(i*1.112*1.085) for i in [0, 12051, 13274, 14496, 15719, 16941, 18163, 19387, 20609, 21832, 23054, 24276, 25500, 26722, 27944, 29167, 30390, 31612, 32835, 34057, 35279, 36503, 37725, 38947, 40170, 41393, 42616, 43838, 45060, 46283, 47506, 48728, 49951,
                                          51173, 52395, 53619, 54841, 56063, 57286, 58509, 59732, 60954, 62176, 63399, 64622, 65844, 67067, 68289, 69512, 70735, 71957, 73179, 74402, 75625, 76847, 78070, 79292, 80516, 81738, 82960, 84183, 85405, 86628, 87851, 89073, 90295, 91518, 92741, 93963, 95186]]
    hit4 = 0
    CD = 60

    MP = [1007, 7550]
    无色消耗 = 7


class 技能22(被动技能):
    名称 = '暮光战略'
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


class 技能23(主动技能):
    名称 = '暮光密令：黎明决战'
    所在等级 = 100
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i*1.0*1.085) for i in [0, 1401, 1726, 2051, 2377, 2701, 3026, 3351, 3675, 4000, 4326, 4651, 4976, 5301, 5625, 5950, 6276, 6601, 6925, 7250, 7575, 7899, 8226, 8551, 8875, 9200, 9525, 9849, 10174, 10500, 10825, 11149, 11474, 11800, 12124,
                                        12450, 12775, 13099, 13424, 13749, 14074, 14398, 14724, 15049, 15374, 15699, 16024, 16349, 16674, 16999, 17323, 17648, 17973, 18299, 18623, 18949, 19274, 19598, 19923, 20249, 20573, 20898, 21223, 21547, 21872, 22197, 22524, 22848, 23173, 23498, 23822]]
    hit0 = 22
    data1 = [int(i*1.0*1.085) for i in [0, 28902, 35605, 42307, 49008, 55709, 62413, 69114, 75815, 82519, 89220, 95921, 102624, 109326, 116029, 122730, 129432, 136135, 142836, 149537, 156241, 162942, 169643, 176347, 183048, 189750, 196451, 203154, 209856, 216557, 223260, 229962, 236663, 243365, 250068,
                                        256769, 263472, 270174, 276875, 283578, 290279, 296982, 303684, 310385, 317088, 323790, 330491, 337195, 343896, 350597, 357300, 364002, 370703, 377406, 384108, 390809, 397512, 404213, 410916, 417618, 424319, 431022, 437724, 444425, 451127, 457830, 464531, 471233, 477936, 484638, 491339]]
    hit1 = 2
    data2 = [int(i*1.0*1.085) for i in [0, 24085, 29670, 35256, 40841, 46424, 52010, 57595, 63180, 68765, 74350, 79935, 85521, 91106, 96690, 102274, 107860, 113445, 119029, 124615, 130200, 135785, 141371, 146955, 152540, 158125, 163710, 169294, 174879, 180465, 186050, 191635, 197220, 202805, 208390,
                                        213976, 219561, 225144, 230729, 236315, 241900, 247484, 253070, 258655, 264240, 269826, 275410, 280995, 286579, 292165, 297749, 303334, 308920, 314505, 320089, 325675, 331260, 336845, 342428, 348014, 353599, 359184, 364770, 370354, 375939, 381525, 387110, 392695, 398281, 403864, 409449]]
    hit2 = 4
    data3 = [int(i*1.0*1.085) for i in [0, 2890, 3560, 4230, 4901, 5571, 6242, 6912, 7581, 8251, 8922, 9592, 10262, 10933, 11603, 12272, 12943, 13613, 14283, 14954, 15624, 16295, 16965, 17634, 18304, 18975, 19645, 20315, 20986, 21656, 22325, 22996, 23666, 24336,
                                        25007, 25677, 26348, 27017, 27688, 28357, 29028, 29698, 30368, 31039, 31708, 32380, 33049, 33719, 34389, 35060, 35730, 36399, 37071, 37740, 38412, 39081, 39751, 40421, 41091, 41762, 42431, 43103, 43772, 44442, 45113, 45782, 46454, 47123, 47794, 48463, 49134]]
    hit3 = 16
    data4 = [int(i*1.0*1.085) for i in [0, 154145, 189889, 225634, 261377, 297121, 332865, 368609, 404354, 440097, 475841, 511585, 547329, 583074, 618817, 654561, 690305, 726047, 761792, 797536, 833280, 869024, 904767, 940512, 976256, 1012000, 1047744, 1083487, 1119232, 1154976, 1190720, 1226464, 1262207, 1297952, 1333695,
                                        1369439, 1405182, 1440927, 1476671, 1512415, 1548159, 1583902, 1619647, 1655391, 1691135, 1726879, 1762622, 1798367, 1834111, 1869855, 1905598, 1941342, 1977086, 2012830, 2048573, 2084317, 2120062, 2155806, 2191550, 2227293, 2263037, 2298781, 2334526, 2370270, 2406013, 2441757, 2477501, 2513246, 2548990, 2584733, 2620476]]
    hit4 = 1
    CD = 290

    MP = [4028, 8056]
    无色消耗 = 15


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'hitman'
        self.名称 = '苍暮·暗刃'
        self.角色 = '枪剑士'

        self.职业 = '暗刃'
        self.武器选项 = ['长刀']
        self.输出类型选项 = ['物理百分比']
        self.防具精通属性 = ['力量']
        self.类型 = '物理百分比'
        self.武器类型 = '长刀'
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
        self.buff = 1.85

        super().__init__()
