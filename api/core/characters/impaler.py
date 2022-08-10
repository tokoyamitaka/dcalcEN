from core.basic.skill import 技能
from core.basic.character import Character
from core.basic.skill import 主动技能, 被动技能


class 技能0(主动技能):
    名称 = '双重投射'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [30, 219]
    data0 = [(i) for i in [1340, 1477, 1612, 1749, 1885, 2020, 2157, 2293, 2428, 2565, 2701, 2837, 2973, 3109, 3245, 3381, 3516, 3653, 3789, 3926, 4061, 4197, 4333, 4469, 4606, 4741, 4877, 5014, 5149, 5285, 5422, 5557, 5694, 5830,
                           5965, 6102, 6238, 6373, 6510, 6646, 6782, 6918, 7054, 7190, 7326, 7462, 7598, 7734, 7871, 8006, 8142, 8279, 8414, 8551, 8687, 8822, 8959, 9094, 9230, 9367, 9502, 9639, 9775, 9910, 10047, 10183, 10318, 10455, 10591, 10727]]
    hit0 = 2
    CD = 6
    TP成长 = 0.1
    TP上限 = 7


class 技能1(主动技能):
    名称 = '侵蚀之矛'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [30, 219]
    data0 = [(i) for i in [0, 2638, 2906, 3174, 3441, 3709, 3977, 4245, 4511, 4779, 5047, 5314, 5582, 5850, 6117, 6385, 6653, 6921, 7188, 7456, 7724, 7991, 8259, 8527, 8794, 9062, 9330, 9598, 9865, 10133, 10401, 10668, 10936, 11204, 11471, 11739,
                           12007, 12275, 12542, 12810, 13078, 13344, 13612, 13880, 14148, 14415, 14683, 14951, 15218, 15486, 15754, 16021, 16289, 16557, 16825, 17092, 17360, 17628, 17895, 18163, 18431, 18698, 18966, 19234, 19502, 19769, 20037, 20305, 20572, 20840, 21108]]
    hit0 = 1
    CD = 5
    TP成长 = 0.1
    TP上限 = 7


class 技能2(被动技能):
    名称 = '暗蚀'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    关联技能 = ['所有']
    关联技能1 = ['双重投射', '暗矛投射', '暗矛贯穿', '绝望枪', '暗蚀螺旋枪', '连锁侵蚀',
             '坠蚀之雨', '暗蚀爆雷杀', '黑蚀酷刑', '冥夜裂空', '虚空碎灭']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.07 + 0.01 * self.等级, 5)

    def 加成倍率1(self, 武器类型):
        return 1.2


class 技能3(主动技能):
    名称 = '暗矛投射'
    所在等级 = 20
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [36, 262]
    data0 = [(i) for i in [0, 844, 930, 1014, 1100, 1186, 1272, 1357, 1443, 1529, 1614, 1700, 1786, 1872, 1957, 2043, 2129, 2214, 2300, 2386, 2471, 2556, 2642, 2728, 2813, 2899, 2985, 3071, 3156, 3242, 3328, 3413, 3499, 3585,
                           3671, 3756, 3841, 3927, 4012, 4098, 4184, 4269, 4355, 4441, 4527, 4612, 4698, 4784, 4869, 4955, 5041, 5127, 5211, 5297, 5383, 5468, 5554, 5640, 5726, 5811, 5897, 5983, 6068, 6154, 6240, 6326, 6411, 6497, 6582, 6667, 6753]]
    hit0 = 4
    CD = 7
    TP成长 = 0.1
    TP上限 = 7


class 技能4(被动技能):
    名称 = '暗矛精通'
    所在等级 = 20
    等级上限 = 30
    基础等级 = 20

    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 20:
            return round(1 + 0.01 * self.等级, 5)
        else:
            return round(0.8 + 0.02 * self.等级, 5)


class 技能5(主动技能):
    名称 = '黑暗枪雨'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [78, 708]
    data0 = [(i) for i in [0, 768, 846, 924, 1002, 1080, 1158, 1236, 1314, 1392, 1470, 1548, 1626, 1704, 1782, 1860, 1938, 2016, 2094, 2172, 2250, 2328, 2406, 2484, 2562, 2640, 2718, 2796, 2874, 2952, 3030, 3108, 3186, 3264,
                           3342, 3420, 3498, 3576, 3654, 3732, 3810, 3888, 3966, 4044, 4122, 4200, 4278, 4356, 4434, 4512, 4590, 4668, 4746, 4824, 4902, 4980, 5058, 5136, 5214, 5292, 5370, 5448, 5526, 5604, 5682, 5760, 5838, 5916, 5994, 6072, 6150]]
    hit0 = 8
    CD = 12
    TP成长 = 0.1
    TP上限 = 7


class 技能6(主动技能):
    名称 = '暗矛贯穿'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [78, 708]
    # 魔枪贯穿攻击力：<data0>%
    data0 = [(i) for i in [0, 1642, 1808, 1975, 2141, 2308, 2474, 2641, 2807, 2974, 3140, 3307, 3473, 3640, 3806, 3973, 4139, 4306, 4472, 4639, 4805, 4971, 5139, 5305, 5472, 5638, 5805, 5971, 6138, 6304, 6471, 6637, 6804, 6970, 7137, 7303,
                           7470, 7636, 7803, 7969, 8136, 8302, 8470, 8636, 8803, 8969, 9136, 9302, 9469, 9635, 9802, 9968, 10135, 10301, 10468, 10634, 10801, 10967, 11134, 11300, 11467, 11633, 11800, 11966, 12134, 12300, 12467, 12633, 12800, 12966, 13133]]
    hit0 = 1
    # 冲击波攻击力：<data1>%
    data1 = [(i) for i in [0, 2450, 2698, 2948, 3196, 3445, 3693, 3942, 4190, 4439, 4688, 4937, 5185, 5434, 5682, 5931, 6179, 6429, 6677, 6926, 7174, 7422, 7671, 7921, 8169, 8417, 8666, 8914, 9163, 9411, 9661, 9909, 10158, 10406, 10655, 10903, 11152,
                           11401, 11650, 11898, 12147, 12395, 12644, 12893, 13142, 13390, 13638, 13887, 14135, 14384, 14633, 14882, 15130, 15379, 15627, 15876, 16124, 16374, 16622, 16871, 17119, 17368, 17616, 17865, 18114, 18363, 18611, 18859, 19108, 19356, 19606]]
    hit1 = 1
    CD = 8
    TP成长 = 0.1
    TP上限 = 7


class 技能7(主动技能):
    名称 = '黑蚀葬礼'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [72, 650]
    # 黑暗之枪爆炸攻击力：<data0>%
    data0 = [(i) for i in [2220, 2446, 2670, 2896, 3122, 3346, 3572, 3796, 4022, 4248, 4472, 4698, 4923, 5148, 5374, 5599, 5824, 6050, 6275, 6500, 6725, 6951, 7176, 7401, 7626, 7851, 8077, 8302, 8527, 8753, 8978, 9203, 9429, 9653, 9879, 10105,
                           10329, 10555, 10781, 11005, 11231, 11455, 11681, 11907, 12131, 12357, 12582, 12807, 13033, 13258, 13483, 13709, 13934, 14159, 14384, 14610, 14835, 15060, 15285, 15511, 15736, 15961, 16186, 16412, 16637, 16862, 17088, 17312, 17538, 17764]]
    hit0 = 1
    # 黑雷枪爆炸攻击力：<data1>%
    data1 = [(i) for i in [3330, 3668, 4006, 4344, 4682, 5019, 5358, 5695, 6034, 6371, 6710, 7047, 7385, 7723, 8060, 8399, 8736, 9075, 9412, 9750, 10088, 10426, 10764, 11102, 11440, 11778, 12115, 12454, 12791, 13130, 13467, 13806, 14143, 14480, 14819,
                           15156, 15495, 15832, 16171, 16508, 16846, 17184, 17522, 17860, 18198, 18536, 18874, 19211, 19550, 19887, 20225, 20563, 20901, 21239, 21576, 21915, 22252, 22591, 22928, 23267, 23604, 23942, 24280, 24618, 24956, 25294, 25632, 25969, 26307, 26645]]
    hit1 = 1
    power1 = 1.2  # 黑雷系
    CD = 10
    TP成长 = 0.1
    TP上限 = 7


class 技能8(主动技能):
    名称 = '绝望枪'
    备注 = '暗源之蚀'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [71, 745]
    # 投掷魔枪攻击力：<data0>%
    data0 = [(i) for i in [0, 562, 620, 676, 733, 791, 847, 905, 962, 1019, 1076, 1134, 1190, 1248, 1304, 1362, 1419, 1476, 1533, 1591, 1647, 1705, 1761, 1818, 1876, 1932, 1990, 2047, 2104, 2161, 2218, 2275, 2333, 2389, 2447,
                           2504, 2561, 2618, 2675, 2732, 2790, 2846, 2903, 2961, 3017, 3075, 3131, 3189, 3246, 3303, 3360, 3418, 3474, 3532, 3588, 3646, 3703, 3760, 3817, 3875, 3931, 3988, 4045, 4102, 4160, 4216, 4274, 4331, 4388, 4445, 4502]]
    hit0 = 15
    power0 = 0.72
    CD = 8
    TP成长 = 0.1
    TP上限 = 7


class 技能9(被动技能):
    名称 = '暗枪突破'
    所在等级 = 30
    等级上限 = 11
    基础等级 = 1

    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.09 + 0.01 * self.等级, 5)


class 技能10(主动技能):
    名称 = '连锁侵蚀'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    # 浓缩黑雷攻击力：<data0>%
    data0 = [(i) for i in [0, 3378, 3720, 4063, 4405, 4748, 5091, 5434, 5777, 6119, 6461, 6804, 7147, 7490, 7833, 8175, 8518, 8860, 9203, 9546, 9889, 10232, 10574, 10916, 11259, 11602, 11945, 12288, 12630, 12973, 13315, 13658, 14001, 14344, 14687, 15029,
                           15372, 15714, 16057, 16400, 16743, 17085, 17428, 17770, 18113, 18456, 18799, 19142, 19484, 19827, 20169, 20512, 20855, 21198, 21541, 21883, 22225, 22568, 22911, 23254, 23597, 23939, 24282, 24624, 24967, 25310, 25653, 25996, 26338, 26680, 27023]]
    hit0 = 1
    # 持续伤害攻击力：<data1>%
    data1 = [(i) for i in [0, 844, 930, 1016, 1101, 1187, 1273, 1358, 1444, 1530, 1614, 1700, 1786, 1872, 1957, 2043, 2129, 2214, 2300, 2386, 2472, 2557, 2643, 2729, 2814, 2900, 2986, 3072, 3157, 3243, 3329, 3414, 3500, 3586,
                           3672, 3757, 3843, 3928, 4013, 4099, 4185, 4271, 4356, 4442, 4528, 4613, 4699, 4785, 4871, 4956, 5042, 5128, 5213, 5299, 5385, 5471, 5556, 5642, 5728, 5813, 5899, 5985, 6071, 6155, 6241, 6327, 6412, 6498, 6584, 6669, 6755]]
    hit1 = 6
    CD = 20
    TP成长 = 0.1
    TP上限 = 5

    MP = [194, 1600]
    无色消耗 = 1


class 技能11(主动技能):
    名称 = '暗蚀螺旋枪'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    # 多段攻击力：<data0>% x 20
    data0 = [(i) for i in [0, 295, 326, 355, 385, 416, 445, 475, 506, 535, 565, 596, 625, 655, 685, 715, 745, 775, 805, 835, 865, 895, 926, 955, 985, 1016, 1045, 1075, 1106, 1135, 1165, 1196, 1225, 1255, 1285, 1315,
                           1345, 1375, 1405, 1435, 1465, 1495, 1526, 1555, 1585, 1616, 1645, 1675, 1706, 1735, 1765, 1796, 1825, 1855, 1885, 1915, 1945, 1975, 2005, 2035, 2065, 2095, 2126, 2155, 2185, 2216, 2245, 2275, 2306, 2335, 2365]]
    hit0 = 20
    # 爆炸攻击力：<data1>%
    data1 = [(i) for i in [0, 3463, 3815, 4166, 4517, 4868, 5220, 5571, 5923, 6275, 6626, 6977, 7328, 7680, 8031, 8383, 8734, 9085, 9436, 9788, 10139, 10491, 10842, 11194, 11544, 11896, 12247, 12599, 12951, 13302, 13654, 14004, 14356, 14707, 15059, 15410,
                           15762, 16113, 16464, 16815, 17167, 17518, 17870, 18221, 18573, 18923, 19275, 19627, 19978, 20330, 20681, 21033, 21383, 21735, 22086, 22438, 22789, 23141, 23492, 23843, 24194, 24546, 24897, 25249, 25601, 25952, 26303, 26654, 27006, 27357, 27709]]
    hit1 = 1
    CD = 18
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    MP = [185, 1526]
    无色消耗 = 1

    def 装备护石(self):
        self.倍率 *= 1.34


class 技能12(主动技能):
    名称 = '坠蚀之雨'
    所在等级 = 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [(i) for i in [0, 564, 622, 679, 737, 794, 852, 909, 966, 1023, 1081, 1138, 1196, 1253, 1310, 1367, 1425, 1482, 1540, 1597, 1655, 1711, 1769, 1826, 1884, 1941, 1999, 2055, 2112, 2170, 2228, 2285, 2343, 2400, 2456,
                           2514, 2571, 2629, 2686, 2744, 2800, 2858, 2915, 2973, 3030, 3088, 3145, 3202, 3259, 3317, 3374, 3432, 3489, 3546, 3603, 3661, 3718, 3776, 3833, 3891, 3947, 4005, 4062, 4120, 4177, 4235, 4291, 4349, 4406, 4464, 4521]]
    hit0 = 20
    CD = 22
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    MP = [185, 1526]
    无色消耗 = 1

    def 装备护石(self):
        self.hit0 += 2+3.6
        self.倍率 = 1.09


class 技能13(主动技能):
    名称 = '暗蚀爆雷杀'
    所在等级 = 45
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    # 贯穿攻击力：<data0>%
    data0 = [(i) for i in [0, 7306, 8047, 8789, 9531, 10272, 11013, 11754, 12495, 13237, 13978, 14719, 15460, 16201, 16943, 17684, 18425, 19167, 19908, 20650, 21391, 22132, 22873, 23614, 24356, 25097, 25838, 26579, 27320, 28062, 28803, 29545, 30286, 31028, 31769,
                           32510, 33251, 33992, 34734, 35475, 36216, 36957, 37698, 38440, 39182, 39923, 40664, 41405, 42147, 42888, 43629, 44370, 45111, 45853, 46594, 47335, 48076, 48817, 49560, 50301, 51042, 51783, 52524, 53266, 54007, 54748, 55489, 56230, 56972, 57713, 58454]]
    hit0 = 1
    # 冲击波攻击力：<data1>%
    data1 = [(i) for i in [0, 5147, 5669, 6192, 6714, 7236, 7759, 8281, 8803, 9326, 9847, 10369, 10892, 11414, 11936, 12459, 12981, 13503, 14026, 14548, 15070, 15591, 16114, 16636, 17158, 17681, 18203, 18725, 19248, 19770, 20292, 20815, 21337, 21858, 22381,
                           22903, 23425, 23948, 24470, 24992, 25515, 26037, 26559, 27082, 27603, 28125, 28648, 29170, 29692, 30215, 30737, 31259, 31782, 32304, 32826, 33349, 33870, 34392, 34915, 35437, 35959, 36481, 37004, 37526, 38048, 38571, 39093, 39614, 40137, 40659, 41181]]
    hit1 = 1
    # 爆炸攻击力：<data2>%
    data2 = [(i) for i in [0, 7830, 8625, 9419, 10214, 11008, 11803, 12597, 13391, 14186, 14981, 15775, 16569, 17363, 18159, 18953, 19747, 20541, 21337, 22131, 22925, 23719, 24513, 25309, 26103, 26897, 27691, 28486, 29281, 30075, 30869, 31664, 32458, 33253, 34047,
                           34842, 35636, 36430, 37225, 38019, 38814, 39608, 40403, 41197, 41992, 42786, 43580, 44375, 45170, 45964, 46758, 47552, 48348, 49142, 49936, 50730, 51524, 52320, 53114, 53908, 54702, 55497, 56292, 57086, 57880, 58675, 59469, 60264, 61058, 61853, 62647]]
    hit2 = 1
    CD = 40
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    MP = [350, 3080]
    无色消耗 = 2

    def 装备护石(self):
        self.倍率 *= 1.32
        self.CDR *= 0.9


class 技能14(被动技能):
    名称 = '黑暗支配者'
    所在等级 = 48
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.105 + 0.015 * self.等级, 5)


class 技能15(主动技能):
    名称 = '无尽侵蚀：缚魂'
    所在等级 = 50
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    # 黑暗之枪攻击力：<data0>% x 15
    data0 = [(i) for i in [0, 1855, 2286, 2717, 3147, 3577, 4008, 4438, 4868, 5299, 5729, 6160, 6590, 7020, 7451, 7881, 8311, 8742, 9173, 9602, 10033, 10464, 10894, 11324, 11755, 12186, 12615, 13046, 13477, 13906, 14337, 14768, 15198, 15628, 16059, 16489,
                           16919, 17350, 17780, 18211, 18641, 19072, 19502, 19933, 20363, 20793, 21224, 21654, 22084, 22515, 22946, 23375, 23806, 24237, 24666, 25097, 25528, 25958, 26388, 26819, 27250, 27679, 28110, 28541, 28971, 29401, 29832, 30262, 30692, 31123, 31553]]
    hit0 = 15
    # 爆炸攻击力：<data1>% x 10 - 黑雷系
    data1 = [(i) for i in [0, 3403, 4191, 4980, 5770, 6559, 7348, 8136, 8926, 9715, 10504, 11293, 12083, 12871, 13660, 14449, 15239, 16028, 16816, 17605, 18395, 19184, 19973, 20761, 21551, 22340, 23129, 23918, 24708, 25496, 26285, 27074, 27864, 28653, 29441,
                           30230, 31020, 31809, 32598, 33387, 34176, 34965, 35754, 36543, 37333, 38121, 38910, 39699, 40489, 41278, 42067, 42855, 43645, 44434, 45223, 46012, 46801, 47590, 48379, 49168, 49958, 50747, 51535, 52324, 53114, 53903, 54692, 55480, 56270, 57059, 57848]]
    hit1 = 10
    power1 = 1.2  # 黑雷系
    CD = 145

    MP = [1200, 10080]
    无色消耗 = 5


class 技能16(主动技能):
    名称 = '暗影蚀魂'
    所在等级 = 60
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [(i) for i in [0, 21601, 23793, 25985, 28176, 30367, 32559, 34750, 36942, 39134, 41324, 43516, 45708, 47899, 50091, 52283, 54474, 56665, 58857, 61049, 63240, 65431, 67623, 69814, 72006, 74198, 76389, 78580, 80772, 82963, 85155, 87347, 89537, 91729, 93921, 96113, 98304,
                           100496, 102687, 104878, 107070, 109262, 111453, 113644, 115836, 118027, 120219, 122411, 124602, 126793, 128985, 131177, 133368, 135560, 137751, 139942, 142134, 144326, 146517, 148709, 150900, 153091, 155283, 157475, 159666, 161857, 164049, 166240, 168432, 170624, 172816]]
    hit0 = 1
    CD = 30
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    MP = [400, 1120]
    无色消耗 = 2

    def 装备护石(self):
        self.倍率 *= 1.36


class 技能17(主动技能):
    名称 = '黑蚀酷刑'
    所在等级 = 70
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    # 巨大魔枪攻击力：<data0>%
    data0 = [(i) for i in [0, 6729, 7412, 8094, 8777, 9460, 10143, 10825, 11508, 12190, 12874, 13556, 14238, 14921, 15603, 16287, 16969, 17652, 18334, 19017, 19700, 20383, 21065, 21748, 22430, 23114, 23796, 24479, 25161, 25845, 26527, 27210, 27892, 28575, 29258,
                           29941, 30623, 31306, 31988, 32672, 33354, 34036, 34719, 35401, 36085, 36767, 37450, 38132, 38815, 39498, 40181, 40863, 41546, 42229, 42912, 43594, 44277, 44959, 45643, 46325, 47008, 47690, 48373, 49056, 49739, 50421, 51104, 51786, 52470, 53152, 53834]]
    hit0 = 1
    # 小型魔枪攻击力：<data1>%
    data1 = [(i) for i in [0, 1682, 1852, 2024, 2194, 2364, 2536, 2706, 2876, 3047, 3218, 3388, 3559, 3730, 3901, 4071, 4242, 4413, 4583, 4753, 4925, 5095, 5266, 5437, 5607, 5778, 5949, 6119, 6290, 6461, 6632, 6802, 6972, 7144, 7314, 7484,
                           7656, 7826, 7996, 8168, 8338, 8509, 8679, 8850, 9021, 9191, 9362, 9533, 9703, 9875, 10045, 10215, 10386, 10557, 10727, 10898, 11069, 11240, 11410, 11581, 11752, 11922, 12092, 12264, 12434, 12604, 12776, 12946, 13117, 13288, 13458]]
    hit1 = 10
    # 爆炸攻击力：<data2>%
    data2 = [(i) for i in [0, 9461, 10421, 11381, 12341, 13301, 14260, 15220, 16181, 17141, 18100, 19060, 20020, 20980, 21940, 22900, 23859, 24819, 25780, 26739, 27699, 28659, 29618, 30579, 31539, 32499, 33458, 34418, 35379, 36338, 37298, 38258, 39217, 40178, 41138,
                           42097, 43057, 44017, 44977, 45937, 46897, 47857, 48816, 49777, 50737, 51696, 52656, 53616, 54576, 55536, 56496, 57455, 58415, 59376, 60335, 61295, 62255, 63215, 64174, 65135, 66095, 67054, 68014, 68975, 69934, 70894, 71854, 72813, 73773, 74734, 75694]]
    hit2 = 1
    CD = 45
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    MP = [800, 1650]
    无色消耗 = 2

    def 装备护石(self):
        self.hit1 = 0
        self.倍率 *= 2.58
        self.CDR *= 0.9


class 技能18(主动技能):
    名称 = '冥夜裂空'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [(i) for i in [0, 2680, 2951, 3224, 3495, 3767, 4038, 4311, 4583, 4854, 5127, 5398, 5670, 5941, 6214, 6486, 6757, 7030, 7301, 7573, 7846, 8117, 8389, 8660, 8933, 9204, 9476, 9749, 10020, 10292, 10564, 10836, 11108, 11379, 11652, 11923,
                           12195, 12467, 12739, 13011, 13283, 13555, 13826, 14098, 14371, 14642, 14914, 15186, 15458, 15729, 16002, 16274, 16545, 16818, 17089, 17361, 17632, 17905, 18177, 18448, 18721, 18992, 19264, 19537, 19808, 20080, 20351, 20624, 20895, 21167, 21440]]
    hit0 = 20
    CD = 40
    是否有护石 = 1

    MP = [580, 4500]
    无色消耗 = 3

    def 装备护石(self):
        self.倍率 *= 1.34


class 技能19(被动技能):
    名称 = '黑暗本源'
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


class 技能20(主动技能):
    名称 = '冥蚀脉冲'
    所在等级 = 80
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    # 黑暗气息攻击力：<data0>%
    data0 = [(i) for i in [0, 6135, 6756, 7379, 8002, 8624, 9246, 9868, 10491, 11114, 11735, 12358, 12980, 13603, 14225, 14847, 15470, 16093, 16714, 17337, 17959, 18582, 19205, 19826, 20449, 21071, 21693, 22316, 22938, 23561, 24182, 24805, 25428, 26050, 26673,
                           27295, 27917, 28540, 29162, 29784, 30407, 31029, 31652, 32273, 32896, 33519, 34141, 34763, 35386, 36008, 36631, 37252, 37875, 38498, 39120, 39742, 40364, 40987, 41610, 42231, 42854, 43477, 44099, 44722, 45343, 45966, 46589, 47211, 47833, 48455, 49078]]
    hit0 = 1
    # 地面射出的黑雷枪攻击力：<data1>% x 8
    data1 = [(i*1.085*1.0) for i in [0, 3220, 3547, 3873, 4200, 4528, 4854, 5181, 5507, 5834, 6161, 6487, 6815, 7141, 7468, 7795, 8121, 8448, 8774, 9102, 9429, 9755, 10082, 10408, 10735, 11062, 11389, 11716, 12042, 12369, 12696, 13022, 13350, 13676, 14003,
                                     14330, 14656, 14983, 15309, 15637, 15964, 16290, 16617, 16943, 17270, 17597, 17924, 18251, 18577, 18904, 19231, 19557, 19884, 20211, 20538, 20865, 21191, 21518, 21844, 22171, 22499, 22825, 23152, 23478, 23805, 24131, 24459, 24786, 25112, 25439, 25765]]
    hit1 = 8
    power1 = 1.2  # 黑雷系
    # 爆炸攻击力：<data2>%
    data2 = [(i) for i in [0, 29447, 32434, 35421, 38409, 41396, 44383, 47371, 50358, 53345, 56333, 59320, 62307, 65295, 68282, 71269, 74257, 77244, 80231, 83220, 86207, 89195, 92182, 95169, 98157, 101144, 104131, 107119, 110106, 113093, 116081, 119068, 122055, 125043, 128030, 131017,
                           134005, 136992, 139979, 142967, 145954, 148941, 151929, 154916, 157903, 160891, 163878, 166865, 169853, 172841, 175829, 178816, 181803, 184791, 187778, 190765, 193753, 196740, 199727, 202715, 205702, 208689, 211677, 214664, 217651, 220639, 223626, 226613, 229601, 232588, 235575]]
    hit2 = 1
    power2 = 1.2  # 黑雷系
    CD = 45
    是否有护石 = 1

    MP = [800, 6000]
    无色消耗 = 5

    def 装备护石(self):
        self.倍率 *= 1.32
        self.CDR *= 0.9


class 技能21(主动技能):
    名称 = '幽影暗蚀：寂灭'
    所在等级 = 85
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    # 黑暗气息攻击力：<data0>%
    data0 = [(i) for i in [0, 6330, 7798, 9266, 10734, 12202, 13670, 15137, 16605, 18073, 19541, 21009, 22477, 23945, 25413, 26881, 28349, 29817, 31285, 32752, 34220, 35688, 37156, 38624, 40092, 41560, 43028, 44496, 45964, 47432, 48900, 50367, 51835, 53303, 54771,
                           56239, 57707, 59175, 60643, 62111, 63579, 65047, 66515, 67982, 69450, 70918, 72386, 73854, 75322, 76790, 78258, 79726, 81194, 82662, 84130, 85597, 87065, 88533, 90001, 91469, 92937, 94405, 95873, 97341, 98809, 100277, 101745, 103212, 104680, 106148, 107616]]
    hit0 = 1
    # 爆炸攻击力：<data1>% 暗雷系
    data1 = [(i) for i in [0, 120277, 148168, 176058, 203947, 231838, 259728, 287619, 315509, 343399, 371290, 399180, 427071, 454961, 482851, 510742, 538632, 566523, 594413, 622304, 650194, 678084, 705975, 733865, 761756, 789646, 817536, 845427, 873317, 901208, 929097, 956987, 984878, 1012768, 1040659, 1068549, 1096440,
                           1124330, 1152220, 1180111, 1208001, 1235891, 1263782, 1291672, 1319563, 1347453, 1375344, 1403234, 1431125, 1459015, 1486905, 1514796, 1542686, 1570577, 1598466, 1626356, 1654247, 1682137, 1710028, 1737918, 1765809, 1793699, 1821589, 1849480, 1877370, 1905260, 1933151, 1961041, 1988932, 2016822, 2044712]]
    hit1 = 1
    power1 = 1.2
    CD = 180

    MP = [2500, 5000]
    无色消耗 = 10


class 技能22(主动技能):
    名称 = '虚空碎灭'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i) for i in [0, 35529, 39134, 42738, 46343, 49947, 53551, 57157, 60761, 64365, 67970, 71574, 75179, 78783, 82387, 85992, 89597, 93202, 96806, 100410, 104015, 107619, 111223, 114828, 118432, 122036, 125642, 129246, 132851, 136455, 140059, 143664, 147268, 150873, 154477, 158082,
                              161687, 165291, 168895, 172500, 176104, 179709, 183313, 186917, 190522, 194127, 197731, 201336, 204940, 208545, 212149, 215753, 219358, 222962, 226568, 230172, 233776, 237381, 240985, 244589, 248194, 251798, 255402, 259007, 262612, 266217, 269821, 273425, 277030, 280634, 284239]]
    hit0 = 1
    data1 = [int(i) for i in [0, 1014, 1118, 1221, 1324, 1427, 1530, 1633, 1736, 1838, 1941, 2044, 2147, 2250, 2353, 2456, 2560, 2663, 2766, 2869, 2972, 3074, 3177, 3280, 3383, 3486, 3589, 3692, 3795, 3898, 4001, 4105, 4208, 4310,
                              4413, 4516, 4619, 4722, 4825, 4928, 5031, 5134, 5237, 5340, 5443, 5545, 5649, 5752, 5855, 5958, 6061, 6164, 6267, 6370, 6473, 6576, 6679, 6781, 6884, 6987, 7090, 7194, 7297, 7400, 7503, 7606, 7709, 7812, 7915, 8017, 8120]]
    hit1 = 20
    data2 = [int(i) for i in [0, 45681, 50315, 54950, 59584, 64218, 68852, 73487, 78121, 82755, 87390, 92024, 96658, 101292, 105927, 110562, 115196, 119831, 124465, 129099, 133733, 138368, 143002, 147636, 152270, 156905, 161539, 166173, 170808, 175442, 180076, 184710, 189346, 193980, 198614,
                              203249, 207883, 212517, 217151, 221786, 226420, 231054, 235688, 240323, 244957, 249591, 254226, 258860, 263494, 268128, 272764, 277398, 282032, 286667, 291301, 295935, 300569, 305204, 309838, 314472, 319107, 323741, 328375, 333009, 337644, 342278, 346912, 351547, 356182, 360816, 365450]]
    hit2 = 1
    CD = 60.0

    MP = [960, 9600]
    无色消耗 = 7


class 技能23(被动技能):
    名称 = '暗源之蚀'
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


class 技能24(主动技能):
    名称 = '暗·渊灭禁绝'
    所在等级 = 100
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    # 暗蚀之枪
    data0 = [int(i) for i in [0, 12766, 15727, 18688, 21648, 24609, 27569, 30530, 33491, 36451, 39412, 42371, 45332, 48292, 51253, 54214, 57174, 60135, 63095, 66056, 69016, 71977, 74938, 77898, 80859, 83818, 86779, 89740, 92700, 95661, 98621, 101582, 104542, 107503, 110464, 113424,
                              116385, 119345, 122306, 125265, 128226, 131187, 134147, 137108, 140068, 143029, 145990, 148950, 151911, 154871, 157832, 160792, 163753, 166714, 169673, 172634, 175594, 178555, 181515, 184476, 187437, 190397, 193358, 196318, 199279, 202239, 205200, 208161, 211120, 214081, 217041]]
    hit0 = 12
    # 黑雷之枪
    data1 = [int(i) for i in [0, 28725, 35387, 42048, 48709, 55370, 62032, 68692, 75353, 82015, 88676, 95337, 101999, 108659, 115320, 121981, 128643, 135304, 141965, 148627, 155287, 161948, 168610, 175271, 181932, 188593, 195254, 201915, 208576, 215238, 221899, 228560, 235221, 241882, 248543,
                              255204, 261866, 268527, 275187, 281849, 288510, 295171, 301833, 308494, 315155, 321815, 328477, 335138, 341799, 348461, 355122, 361782, 368444, 375105, 381766, 388427, 395089, 401749, 408410, 415072, 421733, 428394, 435056, 441717, 448377, 455038, 461700, 468361, 475022, 481684, 488344]]
    hit1 = 8
    power1 = 1.2  # 黑雷系
    CD = 290.0

    MP = [4028, 8056]
    无色消耗 = 15


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'impaler'
        self.名称 = '千魂·暗枪士'
        self.角色 = '魔枪士'
        self.角色类型 = '输出'
        self.职业 = '暗枪士'
        self.武器选项 = ['暗矛']
        self.输出类型选项 = ['魔法百分比']
        self.防具精通属性 = ['智力']
        self.类型 = '魔法百分比'
        self.武器类型 = '暗矛'
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
        self.buff = 1.93

        super().__init__()