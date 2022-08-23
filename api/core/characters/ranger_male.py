from core.basic.skill import 技能
from core.basic.character import Character
from core.basic.skill import 主动技能, 被动技能


class 技能0(主动技能):
    名称 = '回旋踢'
    所在等级 = 10
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [18, 196]
    data0 = [int(i) for i in [0, 1005, 1107, 1209, 1312, 1414, 1516, 1618, 1720, 1822, 1924, 2027, 2129, 2231, 2333, 2434, 2536, 2638, 2740, 2843, 2945, 3047, 3149, 3251, 3353, 3455, 3558, 3660, 3762, 3864, 3966, 4068, 4170, 4273, 4375, 4477, 4579, 4681, 4783, 4884, 4986, 5088, 5191, 5293, 5395, 5497, 5599, 5701, 5803, 5906, 6008, 6110, 6212, 6314, 6416, 6518, 6621, 6723, 6825, 6927, 7029]]
    hit0 = 2
    CD = 4.0
    TP成长 = 0.1
    TP上限 = 7


class 技能1(主动技能):
    名称 = '烟尘弹'
    所在等级 = 10
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [300, 322]
    data0 = [int(i) for i in [0, 462, 509, 556, 603, 650, 696, 744, 790, 837, 885, 931, 978, 1025, 1071, 1119, 1166, 1212, 1260, 1307, 1353, 1400, 1448, 1494, 1541, 1587, 1635, 1682, 1728, 1776, 1823, 1869, 1916, 1964, 2010, 2057, 2105, 2151, 2198, 2245, 2292, 2339, 2385, 2432, 2480, 2526, 2573, 2621, 2667, 2714, 2761, 2807, 2855, 2902, 2948, 2996, 3042, 3089, 3136, 3183, 3230]]
    hit0 = 6
    CD = 6
    TP成长 = 0.10
    TP上限 = 7


class 技能2(主动技能):
    名称 = '致命射击'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [60, 560]
    data0 = [int(i) for i in [0, 1479, 1629, 1779, 1929, 2079, 2229, 2381, 2531, 2681, 2831, 2981, 3131, 3281, 3431, 3581, 3732, 3882, 4032, 4182, 4332, 4482, 4632, 4782, 4932, 5084, 5234, 5384, 5534, 5684, 5834, 5984, 6134, 6284, 6435, 6585, 6735, 6885, 7035, 7185, 7335, 7485, 7635, 7785, 7937, 8087, 8237, 8387, 8537, 8687, 8837, 8987, 9138, 9288, 9438, 9588, 9738, 9888, 10038, 10188, 10338]]
    hit0 = 2
    CD = 6.9
    TP成长 = 0.1
    TP上限 = 7


class 技能3(被动技能):
    名称 = '左轮奥义'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        if self.等级 <= 10:
            return round(1.1 + 0.01 * self.等级, 5)
        else:
            return round(1.2 + 0.02 * (self.等级 - 10), 5)


class 技能4(被动技能):
    名称 = '花式枪术'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级 <= 10:
                return round(1 + 0.01 * self.等级, 5)
            else:
                return round(1.1 + 0.02 * (self.等级 - 10), 5)


class 技能5(主动技能):
    名称 = '复仇反击'
    所在等级 = 25
    等级上限 = 1
    基础等级 = 1
    MP = [252, 252]
    data0 = [int(i) for i in [0,0]]
    hit0 = 1
    CD = 4.0
    # 自身有TP，相关数据的致命射击也有TP
    TP成长 = 0.1
    TP上限 = 7

    def 等效百分比(self, **argv):
        char: Character = argv.get('char', {})
        self.data1 = [0, char.get_skill_by_name("致命射击").data0()]
        self.hit1 = [0, char.get_skill_by_name("致命射击").hit0()]
        self.power1 = [0, 1+char.get_skill_by_name("致命射击").TP等级()*char.get_skill_by_name("致命射击").TP成长()]
        return super().等效百分比(**argv)


class 技能6(主动技能):
    名称 = '浮空劫击'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [50, 420]
    data0 = [int(i) for i in [0, 1893, 2085, 2277, 2469, 2661, 2853, 3046, 3238, 3430, 3622, 3814, 4006, 4198, 4390, 4583, 4775, 4967, 5159, 5350, 5542, 5734, 5926, 6118, 6311, 6503, 6695, 6887, 7079, 7271, 7463, 7655, 7848, 8040, 8232, 8424, 8616, 8808, 9000, 9192, 9385, 9577, 9769, 9961, 10153, 10345, 10537, 10729, 10922, 11114, 11306, 11498, 11690, 11882, 12074, 12267, 12459, 12651, 12843, 13035, 13227]]
    hit0 = 2
    CD = 4.2
    TP成长 = 0.1
    TP上限 = 7


class 技能7(主动技能):
    名称 = '致命回射'
    所在等级 = 30
    等级上限 = 1
    基础等级 = 1
    MP = [150, 150]
    data0 = [int(i) for i in [0,0]]
    hit0 = 1
    倍率 = 1.5
    CD = 8.3
    #自身无TP，TP就是致命射击
    TP成长 = 0.1
    TP上限 = 7

    def TP加成(self):
        return 1.0

    def 等效百分比(self, **argv):
        char: Character = argv.get('char', {})
        self.data1 = [0, char.get_skill_by_name("致命射击").data0()]
        self.hit1 = [0, char.get_skill_by_name("致命射击").hit0()]
        self.power1 = [0, 1+char.get_skill_by_name("致命射击").TP等级()*char.get_skill_by_name("致命射击").TP成长()]
        return super().等效百分比(**argv)


class 技能8(主动技能):
    名称 = '三连发'
    备注 = '卓尔不群'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [50, 420]
    data0 = [int(i) for i in [0, 608, 670, 732, 793, 855, 917, 979, 1040, 1102, 1164, 1227, 1288, 1350, 1412, 1474, 1535, 1597, 1659, 1721, 1782, 1844, 1906, 1968, 2029, 2091, 2153, 2214, 2277, 2339, 2401, 2462, 2524, 2586, 2648, 2709, 2771, 2833, 2895, 2956, 3018, 3080, 3142, 3203, 3266, 3328, 3390, 3451, 3513, 3575, 3637, 3698, 3760, 3822, 3884, 3945, 4007, 4069, 4130, 4192, 4255]]
    hit0 = 1
    data1 = [int(i) for i in [0, 2740, 3018, 3297, 3574, 3853, 4130, 4409, 4687, 4965, 5244, 5522, 5799, 6078, 6356, 6634, 6912, 7190, 7468, 7747, 8024, 8303, 8581, 8859, 9136, 9416, 9693, 9970, 10249, 10527, 10806, 11083, 11362, 11640, 11918, 12195, 12475, 12752, 13030, 13308, 13587, 13864, 14143, 14421, 14699, 14977, 15255, 15534, 15812, 16089, 16369, 16646, 16924, 17202, 17481, 17758, 18036, 18314, 18592, 18871, 19148]]
    hit1 = 2
    CD = 8.0
    TP成长 = 0.1
    TP上限 = 7


class 技能9(主动技能):
    名称 = '移动射击'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i) for i in [0, 552, 608, 665, 721, 776, 833, 889, 944, 1001, 1057, 1114, 1169, 1225, 1282, 1338, 1393, 1450, 1506, 1563, 1618, 1674, 1731, 1786, 1842, 1899, 1955, 2011, 2067, 2123, 2180, 2235, 2292, 2348, 2404, 2460, 2516, 2573, 2628, 2684, 2741, 2797, 2852, 2909, 2965, 3022, 3077, 3133, 3190, 3246, 3301, 3358, 3414, 3471, 3526, 3582, 3639, 3694, 3750, 3807, 3863]]
    hit0 = 20
    CD = 24.3
    TP成长 = 0.10
    TP上限 = 5

    MP = [200, 1680]
    无色消耗 = 1


class 技能10(主动技能):
    名称 = '乱射'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i) for i in [0, 608, 670, 732, 793, 855, 917, 979, 1040, 1102, 1164, 1227, 1288, 1350, 1412, 1474, 1535, 1597, 1659, 1721, 1782, 1844, 1906, 1968, 2029, 2091, 2153, 2214, 2277, 2339, 2401, 2462, 2524, 2586, 2648, 2709, 2771, 2833, 2895, 2956, 3018, 3080, 3142, 3203, 3266, 3328, 3390, 3451, 3513, 3575, 3637, 3698, 3760, 3822, 3884, 3945, 4007, 4069, 4130, 4192, 4255]]
    hit0 = 20
    CD = 17.6
    TP成长 = 0.10 #每点TP加2hit，效果和常规TP是一样的
    TP上限 = 5
    是否有护石 = 1

    MP = [150, 1260]
    无色消耗 = 1

    def 装备护石(self):
        self.倍率 *= 1.22*1.1


class 技能11(主动技能):
    名称 = '多重射击'
    所在等级 = 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i) for i in [0, 2743, 3021, 3300, 3579, 3857, 4136, 4414, 4692, 4970, 5249, 5527, 5806, 6085, 6363, 6642, 6919, 7198, 7476, 7755, 8033, 8312, 8591, 8868, 9147, 9425, 9704, 9982, 10261, 10540, 10818, 11095, 11374, 11653, 11931, 12210, 12488, 12767, 13044, 13323, 13601, 13880, 14159, 14437, 14716, 14994, 15272, 15550, 15829, 16107, 16386, 16665, 16943, 17222, 17499, 17778, 18056, 18335, 18614, 18892, 19171]]
    hit0 = 5
    CD = 19.8
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [150, 1260]
    无色消耗 = 1

    def 装备护石(self):
        self.hit0 = 1
        self.倍率 *= 6.55


class 技能12(主动技能):
    名称 = '双鹰回旋'
    备注 = '(20/24/37 & 34/54)'
    所在等级 = 45
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.0) for i in [0, 513, 565, 618, 670, 722, 774, 826, 878, 930, 982, 1035, 1087, 1139, 1191, 1243, 1295, 1347, 1399, 1452, 1504, 1556, 1608, 1660, 1712, 1764, 1816, 1869, 1921, 1973, 2025, 2077, 2129, 2181, 2233, 2286, 2338, 2390, 2442, 2494, 2546, 2598, 2651, 2703, 2755, 2807, 2859, 2911, 2963, 3015, 3068, 3120, 3172, 3224, 3276, 3328, 3380, 3432, 3485, 3537, 3589, 3641, 3693, 3745, 3797, 3849, 3902, 3954, 4006, 4058, 4110]]
    hit0 = 16
    data1 = [int(i*1.0) for i in [0, 531, 585, 639, 693, 747, 800, 854, 908, 962, 1016, 1070, 1124, 1178, 1232, 1286, 1340, 1393, 1447, 1501, 1555, 1609, 1663, 1717, 1771, 1825, 1879, 1933, 1986, 2040, 2094, 2148, 2202, 2256, 2310, 2364, 2418, 2472, 2526, 2579, 2633, 2687, 2741, 2795, 2849, 2903, 2957, 3011, 3065, 3119, 3172, 3226, 3280, 3334, 3388, 3442, 3496, 3550, 3604, 3658, 3712, 3765, 3819, 3873, 3927, 3981, 4035, 4089, 4143, 4197, 4251]]
    hit1 = 18
    data2 = [int(i*1.0) for i in [0, 558, 614, 671, 728, 784, 841, 898, 954, 1011, 1067, 1124, 1181, 1237, 1294, 1351, 1407, 1464, 1520, 1577, 1634, 1690, 1747, 1804, 1860, 1917, 1974, 2030, 2087, 2143, 2200, 2257, 2313, 2370, 2427, 2483, 2540, 2596, 2653, 2710, 2766, 2823, 2880, 2936, 2993, 3050, 3106, 3163, 3219, 3276, 3333, 3389, 3446, 3503, 3559, 3616, 3672, 3729, 3786, 3842, 3899, 3956, 4012, 4069, 4126, 4182, 4239, 4295, 4352, 4409, 4465]]
    hit2 = 29
    攻击间隔 = 1
    CD = 44.6
    TP成长 = 0.05
    TP上限 = 5
    是否有护石 = 1

    MP = [360, 3024]
    无色消耗 = 2

    形态 = ["满", "常规(原地)"]

    def 形态变更(self, 形态, char:Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
            if 形态 == "满":
                self.hit0 = 16
                self.hit1 = 18
                self.hit2 = 29
                if '双鹰回旋' in char.护石栏:
                    self.hit0 = 0
                    self.hit1 = 28 #护石+10
                    self.power1 = 1.08
                    self.hit2 = 46 #护石+17
                    self.power2 = 1.15                 
            if 形态 == "常规(原地)":
                self.hit0 = 16
                self.hit1 = 18
                self.hit2 = 22
                if '双鹰回旋' in char.护石栏:
                    self.hit0 = 0
                    self.hit1 = 28 #护石+10
                    self.power1 = 1.08
                    self.hit2 = 37 #护石+15
                    self.power2 = 1.15  

    def 等效百分比(self, 武器类型):
        
        self.hit0 += int(((4 / 5) * self.TP等级) / self.攻击间隔)
        self.hit1 += int(((6 / 5) * self.TP等级) / self.攻击间隔)
        self.hit2 += int(((8 / 5) * self.TP等级) / self.攻击间隔)

        return super().等效百分比(武器类型)

    def 装备护石(self):
        self.hit0 = 0
        self.power1 = 1.08
        self.power2 = 1.15  


class 技能13(被动技能):
    名称 = '死亡印记'
    所在等级 = 48
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.065 + 0.02 * self.等级, 5)


class 技能14(主动技能):
    名称 = '疯狂屠戮'
    所在等级 = 50
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i*1.0) for i in [0, 676, 832, 990, 1147, 1304, 1461, 1617, 1775, 1932, 2089, 2245, 2403, 2560, 2717, 2873, 3031, 3188, 3345, 3502, 3658, 3816, 3973, 4130, 4286, 4444, 4601, 4758, 4915, 5071, 5229, 5386, 5543, 5699, 5857, 6014, 6171, 6327, 6484, 6642, 6799]]
    hit0 = 70
    data1 = [int(i*1.0) for i in [0, 1195, 1473, 1749, 2027, 2305, 2582, 2859, 3136, 3414, 3692, 3968, 4246, 4523, 4801, 5077, 5355, 5633, 5910, 6188, 6464, 6742, 7020, 7297, 7574, 7851, 8129, 8407, 8683, 8961, 9238, 9516, 9793, 10070, 10348, 10625, 10903, 11180, 11457, 11735, 12012]]
    hit1 = 25
    data2 = [int(i*1.0) for i in [0, 825, 1016, 1209, 1400, 1591, 1783, 1975, 2166, 2358, 2549, 2741, 2933, 3124, 3315, 3508, 3699, 3890, 4082, 4274, 4465, 4657, 4848, 5040, 5232, 5423, 5614, 5807, 5998, 6189, 6381, 6573, 6764, 6956, 7147, 7339, 7531, 7722, 7914, 8106, 8297]]
    hit2 = 3
    CD = 145

    MP = [1000, 8400]
    无色消耗 = 5


class 技能15(主动技能):
    名称 = '死亡突袭'
    所在等级 = 60
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.0) for i in [0, 8189, 9020, 9851, 10682, 11512, 12344, 13175, 14005, 14836, 15667, 16498, 17328, 18160, 18991, 19822, 20652, 21483, 22314, 23146, 23976, 24807, 25638, 26468, 27299, 28130, 28962, 29792, 30623, 31454, 32285, 33115, 33946, 34778, 35609, 36439, 37270, 38101, 38933, 39763, 40594]]
    hit0 = 3
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [400, 1620]
    无色消耗 = 2

    def 装备护石(self):
        self.倍率 *= 1.31
        self.CDR *= 0.90


class 技能16(主动技能):
    名称 = '压制射击'
    所在等级 = 70
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.0) for i in [0, 1854, 2043, 2231, 2420, 2607, 2796, 2985, 3172, 3361, 3548, 3737, 3925, 4114, 4302, 4490, 4679, 4866, 5055, 5244, 5431, 5620, 5808, 5996, 6184, 6373, 6561, 6749, 6938, 7125, 7314, 7503, 7690, 7879, 8067, 8255, 8443, 8632, 8820, 9008, 9197]]
    hit0 = 20
    data1 = [int(i*1.0) for i in [0, 4122, 4541, 4959, 5378, 5795, 6214, 6633, 7051, 7469, 7887, 8306, 8725, 9142, 9561, 9980, 10398, 10816, 11234, 11653, 12070, 12489, 12908, 13326, 13744, 14163, 14581, 15000, 15417, 15836, 16255, 16673, 17091, 17509, 17928, 18347, 18764, 19183, 19602, 20019, 20438]]
    hit1 = 1
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [800, 1680]
    无色消耗 = 3

    def 装备护石(self):
        self.hit0 = 24
        self.power1 = 2.42


class 技能17(主动技能):
    名称 = '疾风骤雨'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.0) for i in [0, 2876, 3168, 3459, 3751, 4043, 4335, 4627, 4918, 5211, 5502, 5794, 6086, 6377, 6670, 6961, 7253, 7546, 7837, 8129, 8420, 8712, 9005, 9296, 9588, 9879, 10172, 10464, 10755, 11047, 11339, 11631, 11923, 12214, 12507, 12799, 13090, 13382, 13674, 13966, 14258]]
    hit0 = 24
    CD = 40.0
    是否有护石 = 1

    MP = [580, 4500]
    无色消耗 = 3

    def 装备护石(self):
        self.倍率 *= 0.5*(1.15)+0.5*(1.15*1.37)


class 技能18(被动技能):
    名称 = '射击掌握'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40
    关联技能2 = ['致命射击']
    冷却关联技能 = ['致命回射']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round((1.305 + 0.045 * self.等级)/(1.22 + 0.02 * self.等级), 5)

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 - 0.235 - 0.015 * self.等级, 3)


class 技能19(主动技能):
    名称 = '抹杀'
    所在等级 = 80
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.0) for i in [0, 9314, 10259, 11204, 12150, 13095, 14039, 14984, 15929, 16875, 17820, 18764, 19709, 20655, 21600, 22545, 23489, 24434, 25380, 26325, 27270, 28215, 29159, 30105, 31050, 31995, 32940, 33886, 34830, 35775, 36720, 37665, 38611, 39555, 40500, 41445, 42390, 43336, 44281, 45225, 46170]]
    hit0 = 7
    CD = 45.0
    是否有护石 = 1

    MP = [800, 8000]
    无色消耗 = 5

    def 装备护石(self):
        self.hit0 = 14
        self.power0 = 0.5*1.17*(1+0.14)


class 技能20(主动技能):
    名称 = '第七翼动'
    所在等级 = 85
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i*1.0) for i in [0, 8321, 10250, 12180, 14110, 16040, 17968, 19898, 21828, 23757, 25687, 27617, 29546, 31476, 33406, 35336, 37265, 39195, 41125, 43053, 44983, 46913, 48842, 50772, 52702, 54632, 56561, 58491, 60421, 62350, 64280, 66210, 68138, 70068, 71998, 73928, 75857, 77787, 79717, 81646, 83576]]
    hit0 = 13
    data1 = [int(i*1.0) for i in [0, 46362, 57112, 67863, 78615, 89365, 100116, 110866, 121617, 132368, 143118, 153870, 164621, 175371, 186122, 196872, 207623, 218375, 229125, 239876, 250626, 261377, 272128, 282878, 293630, 304381, 315131, 325882, 336632, 347383, 358135, 368885, 379636, 390387, 401137, 411888, 422638, 433390, 444141, 454891, 465642]]
    hit1 = 1
    CD = 180

    MP = [2500, 8000]
    无色消耗 = 10


class 技能21(主动技能):
    名称 = '爆燃突击'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.0) for i in [0, 12610, 13889, 15170, 16449, 17729, 19008, 20288, 21567, 22846, 24126, 25405, 26685, 27964, 29243, 30523, 31802, 33082, 34361, 35640, 36920, 38199, 39478, 40758, 42037, 43317, 44596, 45875, 47155, 48435, 49715, 50994, 52274, 53553, 54832, 56112, 57391, 58671, 59950, 61229, 62509]]
    hit0 = 6
    data1 = [int(i*1.0) for i in [0, 50445, 55563, 60681, 65799, 70917, 76034, 81152, 86269, 91388, 96506, 101623, 106741, 111858, 116976, 122094, 127212, 132330, 137448, 142565, 147683, 152800, 157919, 163037, 168154, 173272, 178389, 183507, 188625, 193743, 198861, 203979, 209096, 214214, 219331, 224450, 229568, 234685, 239803, 244920, 250038]]
    hit1 = 1
    CD = 60

    MP = [1064, 7980]
    无色消耗 = 7


class 技能22(被动技能):
    名称 = '卓尔不群'
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
    名称 = '鹰眸·致命危机'
    所在等级 = 100
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i*1.0) for i in [0, 2484, 3060, 3636, 4213, 4789, 5365, 5941, 6517, 7093, 7671, 8247, 8823, 9399, 9974, 10552, 11128, 11704, 12280, 12856, 13432, 14009, 14585, 15161, 15737, 16313, 16889, 17466, 18042, 18618, 19194, 19770, 20346, 20923, 21499, 22075, 22651, 23227, 23803, 24380, 24956]]
    hit0 = 60
    data1 = [int(i*1.0) for i in [0, 12779, 15742, 18705, 21669, 24632, 27595, 30558, 33521, 36484, 39449, 42412, 45375, 48338, 51301, 54264, 57229, 60192, 63155, 66118, 69081, 72044, 75008, 77971, 80935, 83898, 86861, 89824, 92788, 95751, 98714, 101677, 104640, 107604, 110568, 113531, 116494, 119457, 122420, 125383, 128348]]
    hit1 = 6
    data2 = [int(i*1.0) for i in [0, 12779, 15742, 18705, 21669, 24632, 27595, 30558, 33521, 36484, 39449, 42412, 45375, 48338, 51301, 54264, 57229, 60192, 63155, 66118, 69081, 72044, 75008, 77971, 80935, 83898, 86861, 89824, 92788, 95751, 98714, 101677, 104640, 107604, 110568, 113531, 116494, 119457, 122420, 125383, 128348]]
    hit2 = 4
    data3 = [int(i*1.0) for i in [0, 42596, 52475, 62352, 72230, 82107, 91986, 101863, 111740, 121618, 131495, 141374, 151251, 161128, 171006, 180884, 190762, 200639, 210517, 220394, 230273, 240150, 250027, 259905, 269782, 279661, 289538, 299415, 309293, 319171, 329049, 338926, 348804, 358681, 368560, 378437, 388314, 398192, 408069, 417948, 427825]]
    hit3 = 1
    data4 = [int(i*1.0) for i in [0, 63896, 78713, 93528, 108345, 123161, 137978, 152795, 167610, 182427, 197244, 212060, 226877, 241694, 256509, 271326, 286142, 300959, 315776, 330591, 345408, 360225, 375041, 389858, 404675, 419490, 434307, 449123, 463940, 478757, 493574, 508389, 523206, 538022, 552839, 567656, 582472, 597288, 612105, 626921, 641738]]
    hit4 = 1
    data5 = [int(i*1.0) for i in [0, 4259, 5247, 6234, 7222, 8210, 9198, 10185, 11173, 12162, 13150, 14137, 15125, 16113, 17100, 18088, 19076, 20064, 21051, 22039, 23027, 24014, 25002, 25990, 26978, 27965, 28953, 29941, 30929, 31916, 32904, 33893, 34879, 35868, 36856, 37844, 38831, 39819, 40807, 41794, 42782]]
    hit5 = 10
    CD = 290

    MP = [4028, 8056]
    无色消耗 = 15


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'ranger_male'
        self.名称 = '重霄·漫游枪手'
        self.角色 = '神枪手(男)'

        self.职业 = '漫游枪手'
        # 用来筛CP武器的
        self.转职 = '漫游枪手(男)'
        self.武器选项 = ['左轮枪']
        self.输出类型选项 = ['物理百分比']
        self.防具精通属性 = ['力量']
        self.类型 = '物理百分比'
        self.武器类型 = '左轮枪'
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
        self.buff = 2.25

        super().__init__()