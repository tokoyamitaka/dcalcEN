from core.baseClass.skill import 技能
from core.baseClass.character import Character
from core.baseClass.skill import 主动技能, 被动技能


class 技能0(主动技能):
    名称 = '狂风冲刺'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [31, 185]
    # 打满9次 操作比较反人类
    data0 = [int(i) for i in [0, 335, 370, 405, 438, 473, 506, 541, 576, 611, 643, 678, 714, 746, 781, 814, 848, 881, 917, 952, 986, 1019, 1055, 1089, 1123, 1157, 1190, 1226, 1260, 1293, 1328, 1363, 1394, 1430, 1465, 1498,
                              1532, 1566, 1601, 1636, 1669, 1703, 1739, 1772, 1807, 1841, 1875, 1910, 1942, 1977, 2012, 2044, 2079, 2115, 2148, 2182, 2217, 2251, 2285, 2320, 2353, 2388, 2421, 2456, 2491, 2524, 2557, 2591, 2627, 2662, 2695]]
    hit0 = 9
    CD = 5
    TP成长 = 0.10
    TP上限 = 7

    CP武器 = False

    def 等效百分比(self, **argv):
        游离 = 0
        if self.CP武器:
            char = argv.get('char', {})
            游离 = char.get_skill_by_name("游离之风").等效百分比(**argv)*0.5
        return super().等效百分比(**argv) + 游离


class 技能1(主动技能):
    名称 = '回风斩'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [38, 227]
    # 风击物理攻击力：<data0>%
    data0 = [int(i) for i in [0, 749, 825, 901, 977, 1054, 1129, 1204, 1281, 1356, 1433, 1508, 1585, 1662, 1736, 1813, 1889, 1965, 2041, 2117, 2194, 2269, 2345, 2421, 2498, 2574, 2650, 2726, 2800, 2877, 2952, 3029, 3106, 3181,
                              3258, 3332, 3409, 3485, 3561, 3638, 3714, 3790, 3865, 3941, 4018, 4094, 4170, 4246, 4323, 4396, 4473, 4549, 4625, 4702, 4777, 4854, 4929, 5005, 5082, 5157, 5234, 5310, 5386, 5463, 5538, 5614, 5690, 5766, 5842, 5919, 5995]]
    hit0 = 4
    CD = 5.5
    TP成长 = 0.10
    TP上限 = 7


class 技能2(被动技能):
    名称 = '疾风之棍棒精通'
    所在等级 = 15
    等级上限 = 30
    基础等级 = 20
    冷却关联技能 = ['所有']
    非冷却关联技能 = ['万象风龙阵', '无限风域', '风之极·永坠']

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        if self.等级 <= 20:
            return round(1.00 + 0.01 * self.等级, 5)
        else:
            return round(0.80 + 0.02 * self.等级, 5)

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 0.9


class 技能3(主动技能):
    名称 = '朔风牵引'
    所在等级 = 20
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [45, 268]
    # 逆风物理攻击力：<data0>%
    data0 = [int(i) for i in [0, 475, 522, 573, 621, 669, 718, 767, 814, 861, 910, 959, 1007, 1055, 1105, 1152, 1201, 1249, 1298, 1345, 1394, 1441, 1492, 1540, 1588, 1635, 1683, 1732, 1779, 1829, 1877, 1926, 1974, 2024, 2071,
                              2119, 2167, 2217, 2264, 2311, 2361, 2410, 2459, 2505, 2553, 2602, 2651, 2698, 2746, 2796, 2844, 2893, 2940, 2989, 3037, 3086, 3135, 3183, 3231, 3280, 3329, 3374, 3423, 3471, 3521, 3569, 3617, 3665, 3715, 3763, 3811]]
    hit0 = 9
    CD = 10
    TP成长 = 0.10
    TP上限 = 7


class 技能4(主动技能):
    名称 = '风鸣冲击'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [61, 366]
    # 爆炸物理攻击力：<data0>%
    data0 = [int(i) for i in [0, 5677, 6255, 6829, 7406, 7982, 8556, 9132, 9710, 10286, 10862, 11437, 12014, 12589, 13166, 13743, 14318, 14894, 15470, 16046, 16621, 17198, 17773, 18351, 18927, 19501, 20077, 20654, 21230, 21805,
                              22381, 22959, 23534, 24111, 24686, 25262, 25838, 26415, 26989, 27568, 28143, 28719, 29295, 29872, 30445, 31022, 31598, 32175, 32750, 33326, 33903, 34478, 35055, 35630, 36206, 36783, 37360, 37934, 38511, 39087, 39663]]
    hit0 = 1
    CD = 8.5
    TP成长 = 0.10
    TP上限 = 7


class 技能5(主动技能):
    名称 = '游离之风'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [45, 268]
    # 旋风物理攻击力：<data0>%
    data0 = [int(i) for i in [0, 1049, 1156, 1262, 1368, 1475, 1581, 1687, 1796, 1900, 2008, 2112, 2221, 2327, 2434, 2541, 2646, 2754, 2859, 2966, 3072, 3179, 3285, 3392, 3498, 3604, 3711, 3817, 3926, 4030, 4138, 4245, 4351, 4457,
                              4564, 4670, 4776, 4883, 4990, 5095, 5203, 5308, 5415, 5522, 5628, 5735, 5841, 5949, 6053, 6162, 6266, 6374, 6481, 6587, 6693, 6800, 6907, 7012, 7120, 7225, 7332, 7439, 7545, 7651, 7758, 7864, 7970, 8077, 8185, 8289, 8398]]
    hit0 = 4
    CD = 6.7
    TP成长 = 0.10
    TP上限 = 7


class 技能6(主动技能):
    名称 = '双翼风刃'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [91, 545]
    # 旋风物理攻击力：<data0>%
    data0 = [int(i) for i in [0, 2104, 2318, 2531, 2744, 2958, 3171, 3384, 3599, 3813, 4025, 4239, 4453, 4666, 4879, 5093, 5307, 5520, 5734, 5947, 6161, 6374, 6587, 6801, 7016, 7228, 7442, 7656, 7868, 8082, 8295,
                              8509, 8723, 8937, 9150, 9364, 9577, 9790, 10004, 10216, 10431, 10645, 10859, 11071, 11285, 11498, 11711, 11925, 12140, 12353, 12566, 12779, 12993, 13207, 13419, 13633, 13848, 14062, 14274, 14488, 14701]]
    hit0 = 4
    CD = 14
    TP成长 = 0.10
    TP上限 = 7


class 技能7(被动技能):
    名称 = '风之意志'
    所在等级 = 30
    等级上限 = 15
    基础等级 = 5

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025+0.015*self.等级, 5)


class 技能8(主动技能):
    名称 = '刃风'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    # 第1击攻击力：<data0>%
    data0 = [int(i) for i in [0, 2050, 2258, 2466, 2673, 2882, 3090, 3297, 3506, 3714, 3921, 4131, 4339, 4546, 4754, 4963, 5170, 5378, 5587, 5794, 6002, 6209, 6418, 6626, 6833, 7042, 7251, 7457, 7667, 7875, 8082,
                              8290, 8499, 8706, 8914, 9123, 9330, 9538, 9747, 9954, 10162, 10372, 10579, 10787, 10995, 11203, 11411, 11618, 11827, 12035, 12242, 12450, 12659, 12866, 13074, 13284, 13490, 13699, 13908, 14115, 14323]]
    hit0 = 1
    # 第2击攻击力：<data1>%
    data1 = [int(i) for i in [0, 2527, 2782, 3038, 3295, 3551, 3807, 4064, 4320, 4575, 4833, 5089, 5346, 5602, 5858, 6115, 6371, 6626, 6883, 7139, 7396, 7653, 7909, 8166, 8422, 8677, 8934, 9190, 9447, 9703, 9959,
                              10216, 10471, 10727, 10985, 11241, 11498, 11754, 12010, 12267, 12522, 12778, 13035, 13291, 13548, 13804, 14061, 14318, 14573, 14829, 15086, 15342, 15598, 15855, 16111, 16366, 16623, 16879, 17136, 17393, 17649]]
    hit1 = 1
    # 空中切割攻击力：<data2>%
    data2 = [int(i) for i in [0, 1262, 1391, 1518, 1647, 1775, 1904, 2031, 2159, 2288, 2415, 2544, 2672, 2800, 2928, 3056, 3184, 3313, 3442, 3569, 3698, 3826, 3953, 4082, 4210, 4339, 4466, 4595, 4723,
                              4851, 4979, 5107, 5235, 5363, 5492, 5619, 5748, 5876, 6003, 6132, 6260, 6390, 6517, 6646, 6774, 6901, 7030, 7158, 7286, 7414, 7543, 7670, 7798, 7927, 8054, 8183, 8311, 8440, 8567, 8695, 8824]]
    hit2 = 1
    # 地上切割攻击力：<data3>%
    data3 = [int(i) for i in [0, 1894, 2086, 2279, 2471, 2664, 2856, 3048, 3240, 3432, 3624, 3817, 4009, 4201, 4393, 4585, 4777, 4969, 5162, 5354, 5547, 5739, 5931, 6123, 6317, 6509, 6701, 6893, 7085, 7277,
                              7469, 7662, 7854, 8046, 8238, 8430, 8622, 8816, 9008, 9200, 9392, 9584, 9776, 9968, 10161, 10353, 10545, 10737, 10929, 11121, 11313, 11506, 11698, 11891, 12083, 12275, 12467, 12661, 12853, 13045, 13237]]
    hit3 = 1
    # 凝缩爆炸攻击力：<data4>%
    data4 = [int(i) for i in [0, 4767, 5252, 5736, 6219, 6703, 7187, 7672, 8155, 8639, 9123, 9606, 10089, 10574, 11057, 11541, 12025, 12510, 12993, 13477, 13961, 14444, 14927, 15412, 15896, 16379, 16863, 17347, 17830, 18315,
                              18799, 19283, 19765, 20249, 20734, 21217, 21701, 22185, 22669, 23152, 23637, 24121, 24603, 25087, 25571, 26056, 26539, 27023, 27507, 27990, 28475, 28959, 29443, 29925, 30409, 30894, 31377, 31861, 32345, 32829, 33312]]
    hit4 = 1
    CD = 18
    TP成长 = 0.10
    TP上限 = 5

    MP = [132, 1108]
    无色消耗 = 1


class 技能9(主动技能):
    名称 = '风暴之眼'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    # 风暴物理攻击力：<data0>%
    data0 = [int(i) for i in [0, 8583, 9451, 10325, 11195, 12066, 12936, 13807, 14678, 15548, 16418, 17291, 18161, 19032, 19902, 20772, 21644, 22514, 23385, 24256, 25125, 25999, 26867, 27740, 28609, 29481, 30351, 31222, 32092,
                              32963, 33832, 34706, 35574, 36447, 37316, 38188, 39058, 39929, 40800, 41671, 42543, 43413, 44284, 45153, 46026, 46895, 47767, 48636, 49507, 50378, 51249, 52120, 52991, 53860, 54733, 55602, 56474, 57343, 58215, 59086, 59956]]
    hit0 = 1
    CD = 16
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [128, 766]
    无色消耗 = 1

    def 装备护石(self):
        self.倍率 *= 1.37
        self.CDR *= 0.90


class 技能10(主动技能):
    名称 = '真空旋风破'
    所在等级 = 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    # 龙卷风物理攻击力：<data0>%
    data0 = [int(i) for i in [0, 763, 841, 919, 997, 1074, 1152, 1229, 1307, 1384, 1463, 1541, 1617, 1696, 1773, 1850, 1927, 2005, 2082, 2161, 2239, 2316, 2394, 2469, 2548, 2625, 2704, 2782, 2859,
                              2936, 3013, 3092, 3169, 3247, 3323, 3401, 3480, 3557, 3635, 3712, 3791, 3868, 3946, 4022, 4099, 4177, 4254, 4333, 4411, 4489, 4565, 4643, 4720, 4799, 4877, 4954, 5031, 5107, 5186, 5263, 5341]]
    hit0 = 8
    # 爆炸物理攻击力：<data1>%
    data1 = [int(i) for i in [0, 6117, 6737, 7358, 7979, 8599, 9220, 9841, 10463, 11082, 11703, 12323, 12945, 13565, 14187, 14807, 15427, 16047, 16667, 17289, 17909, 18531, 19151, 19773, 20393, 21012, 21634, 22254, 22875, 23495,
                              24117, 24737, 25356, 25976, 26599, 27219, 27840, 28462, 29082, 29703, 30322, 30943, 31564, 32184, 32804, 33427, 34047, 34667, 35286, 35909, 36529, 37150, 37770, 38393, 39012, 39631, 40252, 40873, 41495, 42114, 42737]]
    hit1 = 1
    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [164, 983]
    无色消耗 = 1

    def 装备护石(self):
        self.power1 = 1.35
        self.CDR *= 0.8


class 技能11(主动技能):
    名称 = '风暴之拳'
    所在等级 = 45
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    # 重拳物理攻击力：<data0>%
    data0 = [int(i) for i in [0, 18906, 20823, 22739, 24659, 26577, 28494, 30413, 32330, 34248, 36167, 38084, 40002, 41919, 43838, 45756, 47674, 49590, 51511, 53426, 55345, 57264, 59179, 61101, 63018, 64935, 66852, 68772, 70689, 72607,
                              74524, 76443, 78362, 80278, 82196, 84112, 86032, 87952, 89867, 91787, 93705, 95623, 97540, 99458, 101376, 103294, 105211, 107130, 109046, 110965, 112883, 114801, 116719, 118637, 120554, 122473, 124390, 126309, 128227, 130145, 132063]]
    hit0 = 1
    # 风暴多段攻击力：<data1>%
    data1 = [int(i) for i in [0, 1620, 1784, 1949, 2114, 2277, 2442, 2606, 2770, 2934, 3100, 3264, 3426, 3592, 3757, 3922, 4085, 4250, 4414, 4580, 4745, 4906, 5072, 5236, 5402, 5565, 5730, 5894, 6060, 6224,
                              6386, 6551, 6716, 6880, 7045, 7210, 7374, 7537, 7701, 7867, 8031, 8194, 8360, 8524, 8690, 8854, 9017, 9181, 9347, 9511, 9674, 9840, 10004, 10170, 10330, 10497, 10661, 10827, 10992, 11154, 11319]]
    hit1 = 5
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [311, 1866]
    无色消耗 = 2

    def 装备护石(self):
        self.hit1 = 0
        self.power0 = 1.85


class 技能12(被动技能):
    名称 = '御风之力'
    所在等级 = 48
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)


class 技能13(主动技能):
    名称 = '万象风龙阵'
    所在等级 = 50
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    # 飓风物理攻击力：<data0>%
    data0 = [int(i) for i in [0, 538, 663, 788, 914, 1037, 1163, 1288, 1414, 1694, 1830, 1969, 2104, 2238, 2379, 2517, 2653, 2793, 2927,
                              3066, 3205, 3341, 3482, 3617, 3754, 3891, 4029, 4169, 4306, 4442, 4580, 4716, 4855, 4993, 5129, 5269, 5403, 5541, 5681, 5817, 5954]]
    hit0 = 56
    # 飓风爆炸攻击力：<data1>%
    data1 = [int(i) for i in [0, 9700, 11951, 14202, 16452, 18700, 20950, 23201, 25450, 30470, 32947, 35418, 37895, 40369, 42843, 45319, 47796, 50268, 52743, 55219,
                              57695, 60169, 62644, 65120, 67593, 70067, 72544, 75017, 77493, 79967, 82443, 84919, 87391, 89866, 92341, 94816, 97289, 99765, 102241, 104714, 107190]]
    hit1 = 4
    CD = 145

    MP = [600, 5040]
    无色消耗 = 5


class 技能14(主动技能):
    名称 = '疾风瞬影闪'
    所在等级 = 60
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    # 风之剑物理攻击力：<data0>%
    data0 = [int(i) for i in [0, 2806, 3091, 3375, 3662, 3945, 4228, 4515, 4799, 5085, 5369, 5654, 5939, 6222, 6508, 6792, 7079, 7363, 7647, 7931,
                              8217, 8502, 8785, 9071, 9355, 9641, 9926, 10209, 10494, 10779, 11065, 11349, 11632, 11920, 12203, 12487, 12773, 13057, 13341, 13627, 13911]]
    hit0 = 4
    data1 = [int(i) for i in [0, 2806, 3091, 3375, 3662, 3945, 4228, 4515, 4799, 5085, 5369, 5654, 5939, 6222, 6508, 6792, 7079, 7363, 7647, 7931,
                              8217, 8502, 8785, 9071, 9355, 9641, 9926, 10209, 10494, 10779, 11065, 11349, 11632, 11920, 12203, 12487, 12773, 13057, 13341, 13627, 13911]]
    hit1 = 4
    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [220, 1320]
    无色消耗 = 1

    def 装备护石(self):
        self.倍率 *= 1.27


class 技能15(主动技能):
    名称 = '风卷残云'
    所在等级 = 70
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    # 10+1
    # 风暴物理攻击力：<data0>%
    data0 = [int(i) for i in [0, 2602, 2867, 3130, 3394, 3659, 3922, 4186, 4451, 4714, 4978, 5243, 5506, 5770, 6035, 6298, 6563, 6827, 7090, 7355,
                              7619, 7883, 8147, 8411, 8675, 8939, 9203, 9467, 9731, 9995, 10259, 10523, 10788, 11051, 11315, 11580, 11843, 12108, 12372, 12635, 12900]]
    hit0 = 10
    # 爆炸物理攻击力：<data1>%
    data1 = [int(i) for i in [0, 8675, 9555, 10436, 11315, 12195, 13076, 13956, 14836, 15716, 16596, 17476, 18356, 19237, 20117, 20997, 21878, 22758, 23637,
                              24517, 25398, 26278, 27158, 28039, 28919, 29798, 30678, 31558, 32438, 33318, 34199, 35079, 35959, 36840, 37720, 38599, 39480, 40360, 41240, 42120, 43001]]
    hit1 = 1
    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [551, 3305]
    无色消耗 = 2

    def 装备护石(self):
        self.倍率 *= 1.30


class 技能16(主动技能):
    名称 = '游龙惊风破'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    # 12+1
    # 多段物理攻击力：<data0>%
    data0 = [int(i) for i in [0, 2255, 2484, 2713, 2941, 3169, 3398, 3628, 3856, 4085, 4313, 4543, 4772, 5001, 5229, 5456, 5686, 5915, 6144,
                              6372, 6602, 6830, 7059, 7288, 7516, 7746, 7974, 8204, 8433, 8660, 8889, 9117, 9347, 9576, 9805, 10033, 10262, 10491, 10720, 10949, 11177]]
    hit0 = 12
    # 爆炸物理攻击力：<data1>%
    data1 = [int(i) for i in [0, 37184, 40957, 44729, 48501, 52272, 56047, 59818, 63590, 67363, 71135, 74906, 78681, 82452, 86224, 89996, 93769, 97540, 101314, 105087, 108859,
                              112631, 116402, 120176, 123948, 127720, 131493, 135265, 139036, 142811, 146582, 150354, 154128, 157899, 161670, 165445, 169217, 172988, 176761, 180533, 184305]]
    hit1 = 1
    CD = 40
    是否有护石 = 1

    MP = [580, 4500]
    无色消耗 = 3

    def 装备护石(self):
        self.hit0 = 0
        self.power1 = 2.18


class 技能17(被动技能):
    名称 = '风神诀'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


class 技能18(主动技能):
    名称 = '九霄风雷'
    所在等级 = 80
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    # 14+1
    # 低于100攻速且立即落地时，存在丢hit情况，hit数11-13
    # 携带CP后不存在丢hit
    # 多段物理攻击力：<data0>%
    data0 = [int(i) for i in [0, 2195, 2416, 2642, 2863, 3087, 3309, 3532, 3755, 3979, 4200, 4424, 4646, 4868, 5092, 5313, 5537, 5760, 5982,
                              6205, 6429, 6650, 6873, 7097, 7318, 7542, 7764, 7987, 8210, 8432, 8655, 8879, 9101, 9324, 9547, 9768, 9992, 10214, 10438, 10661, 10883]]
    hit0 = 14
    # 爆炸物理攻击力：<data1>%
    data1 = [int(i) for i in [0, 46110, 50788, 55466, 60146, 64822, 69499, 74179, 78856, 83534, 88213, 92890, 97568, 102246, 106925, 111602, 116279, 120957, 125635, 130315,
                              134991, 139668, 144348, 149025, 153701, 158382, 163059, 167737, 172415, 177094, 181770, 186449, 191126, 195805, 200482, 205160, 209837, 214518, 219194, 223870, 228551]]
    hit1 = 1
    CD = 45
    是否有护石 = 1

    MP = [800, 6000]
    无色消耗 = 5

    def 装备护石(self):
        self.倍率 *= 1.27
        self.CDR *= 0.89


class 技能19(主动技能):
    名称 = '无限风域'
    所在等级 = 85
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    # 狂风物理攻击力：<data0>%
    data0 = [int(i) for i in [0, 15627, 19252, 22875, 26500, 30124, 33747, 37371, 40995, 44617, 48242, 51866, 55490, 59114, 62739, 66361, 69986, 73610, 77234, 80857,
                              84481, 88104, 91729, 95353, 98978, 102600, 106225, 109849, 113471, 117096, 120721, 124344, 127967, 131592, 135215, 138839, 142463, 146087, 149710, 153335, 156958]]
    hit0 = 1
    # 飞行攻击物理攻击力：<data1>%
    data1 = [int(i) for i in [0, 5861, 7217, 8577, 9939, 11295, 12653, 14013, 15373, 16731, 18091, 19449, 20807, 22169, 23527, 24884, 26245, 27605, 28963, 30322,
                              31680, 33037, 34399, 35757, 37116, 38475, 39833, 41193, 42553, 43911, 45271, 46629, 47988, 49348, 50706, 52064, 53425, 54783, 56141, 57501, 58859]]
    hit1 = 8
    # 最后刺击物理攻击力：<data2>%
    data2 = [int(i) for i in [0, 31255, 38502, 45752, 52998, 60246, 67494, 74741, 81991, 89239, 96485, 103731, 110980, 118228, 125477, 132724, 139972, 147219, 154467, 161715,
                              168963, 176211, 183458, 190706, 197954, 205201, 212450, 219697, 226946, 234193, 241440, 248689, 255936, 263184, 270433, 277679, 284926, 292175, 299423, 306670, 313919]]
    hit2 = 1
    # 最后爆炸物理攻击力：<data3>%
    data3 = [int(i) for i in [0, 62511, 77008, 91501, 105998, 120495, 134989, 149485, 163980, 178476, 192971, 207467, 221963, 236457, 250954, 265449, 279945, 294441, 308935, 323432,
                              337925, 352421, 366919, 381414, 395908, 410403, 424901, 439394, 453890, 468388, 482880, 497377, 511873, 526367, 540864, 555359, 569855, 584350, 598846, 613342, 627836]]
    hit3 = 1
    # 1+8+1+1
    CD = 180

    MP = [1500, 5000]
    无色消耗 = 10


class 技能20(主动技能):
    名称 = '怒风狂涌'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i) for i in [0, 4110, 4527, 4944, 5361, 5777, 6193, 6612, 7029, 7445, 7862, 8280, 8696, 9113, 9530, 9947, 10365, 10782, 11198, 11616,
                              12033, 12448, 12865, 13283, 13699, 14117, 14534, 14951, 15368, 15785, 16202, 16619, 17036, 17452, 17871, 18288, 18704, 19120, 19538, 19954, 20371]]
    hit0 = 6
    data1 = [int(i) for i in [0, 9247, 10186, 11125, 12062, 12999, 13939, 14876, 15814, 16752, 17691, 18629, 19568, 20505, 21445, 22382, 23320, 24257, 25197,
                              26134, 27073, 28010, 28949, 29887, 30826, 31763, 32703, 33640, 34578, 35516, 36455, 37393, 38331, 39268, 40208, 41145, 42083, 43024, 43961, 44898, 45837]]
    hit1 = 4
    data2 = [int(i) for i in [0, 61652, 67906, 74161, 80415, 86670, 92925, 99181, 105435, 111689, 117944, 124198, 130453, 136708, 142962, 149217, 155471, 161725, 167980, 174235,
                              180490, 186744, 192999, 199255, 205507, 211762, 218018, 224272, 230527, 236782, 243037, 249290, 255545, 261800, 268054, 274309, 280564, 286818, 293072, 299327, 305580]]
    hit2 = 1
    CD = 60

    MP = [773, 6000]
    无色消耗 = 7


class 技能21(被动技能):
    名称 = '初始之风'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能22(主动技能):
    名称 = '风之极·永坠'
    所在等级 = 100
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i) for i in [0, 46437, 57206, 67974, 78743, 89510, 100279, 111048, 121816, 132584, 143352, 154121, 164889, 175657, 186426, 197194, 207962, 218731, 229499, 240268,
                              251035, 261804, 272573, 283341, 294109, 304877, 315646, 326415, 337182, 347951, 358719, 369488, 380256, 391024, 401793, 412561, 423329, 434098, 444866, 455635, 466402]]
    hit0 = 1
    data1 = [int(i) for i in [0, 69657, 85809, 101962, 118115, 134267, 150420, 166571, 182725, 198877, 215030, 231182, 247334, 263487, 279640, 295792, 311944, 328096, 344249, 360402,
                              376554, 392707, 408858, 425012, 441164, 457317, 473469, 489623, 505774, 521927, 538079, 554232, 570385, 586537, 602689, 618843, 634994, 651148, 667299, 683451, 699605]]
    hit1 = 1
    data2 = [int(i) for i in [0, 13931, 17161, 20393, 23623, 26853, 30083, 33314, 36544, 39775, 43005, 46236, 49466, 52697, 55928, 59157, 62388, 65619, 68849, 72080,
                              75311, 78541, 81772, 85002, 88232, 91462, 94693, 97923, 101155, 104385, 107616, 110846, 114077, 117307, 120537, 123767, 126998, 130228, 133459, 136690, 139921]]
    hit2 = 25
    CD = 290

    MP = [4028, 8056]
    无色消耗 = 15


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'swift_master'
        self.名称 = '知源·逐风者'
        self.角色 = '魔法师(男)'
        self.角色类型 = '输出'
        self.职业 = '逐风者'
        # 用来筛CP武器的
        self.转职 = '逐风者'
        self.武器选项 = ['棍棒']
        self.输出类型选项 = ['物理百分比']
        self.防具精通属性 = ['力量']
        self.类型 = '物理百分比'
        self.武器类型 = '棍棒'
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
        self.buff = 2.11

        super().__init__()
