from core.basic.skill import 技能
from core.basic.character import Character
from core.basic.skill import 主动技能, 被动技能

class 技能0(主动技能):
    名称 = '魔球连射'
    所在等级 = 5
    等级上限 = 11
    基础等级 = 1
    data0 = [0+(108+2*i) for i in range(1,11)]
    hit0 = 5
    CD = 2.4
    MP = [22,183]

class 技能1(被动技能):
    名称 = '元素融合'
    所在等级 = 15
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.095+0.005*self.等级, 5)

class 技能2(主动技能):
    名称 = '元素炮'
    所在等级 = 15
    等级上限 = 11
    等级精通 = 1
    data0 = [0,500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110, 1120, 1130, 1140, 1150, 1160, 1170, 1180, 1190]
    hit0 = 1
    CD = 5.0

class 技能3(主动技能):
    名称 = '属性变换'
    所在等级 = 15

    等级上限 = 70
    学习间隔 = 5
    等级精通 = 60

    MP = [31,259]

    data0 = [int(i*1.22)for i in [0, 254, 312, 371, 430, 489, 548, 606, 665, 724, 783, 842, 900, 959, 1018, 1077, 1136, 1194, 1253, 1312, 1371, 1430, 1488, 1547, 1606, 1665, 1724, 1782, 1841, 1900, 1959, 2018, 2077, 2135, 2194, 2253,
          2312, 2371, 2429, 2488, 2547, 2606, 2665, 2723, 2782, 2841, 2900, 2959, 3017, 3076, 3135, 3194, 3253, 3312, 3370, 3429, 3488, 3547, 3606, 3664, 3723, 3782, 3841, 3900, 3958, 4017, 4076, 4135, 4194, 4252, 4311]]
    hit0 = 1
    TP成长 = 0.1
    TP上限 = 7
    CD = 5.0

    关联技能 = ['元素炮', '魔球连射']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round((self.data0[self.等级]*0.01) * (1+self.TP成长 * self.TP等级), 5)


class 技能4(被动技能):
    名称 = '元素之力'
    所在等级 = 20
    等级上限 = 11
    基础等级 = 1
    每层加成 = [0, 7, 8, 10, 11, 13, 14, 15, 17, 18, 20, 21, 22, 24, 25, 27, 28, 29, 31, 32, 34, 35, 36, 38, 39, 41, 42, 43, 45, 46, 48, 49, 50, 52, 53,
            55, 56, 57, 59, 60, 62, 63, 64, 66, 67, 69, 70, 71, 73, 74, 76, 77, 78, 80, 81, 83, 84, 85, 87, 88, 90, 91, 92, 94, 95, 97, 98, 99, 101, 102, 104]
    关联技能 = ['元素炮']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1+0.01*self.每层加成[self.等级]*5, 5)

class 技能5(主动技能):
    名称 = '冰晶坠'
    所在等级 = 20
    等级上限 = 70
    等级精通 = 60
    学习间隔 = 2
    data0 = [int(i*1.173)for i in [0, 470, 517, 565, 613, 661, 708, 756, 804, 852, 900, 946, 994, 1042, 1090, 1138, 1185, 1233, 1281, 1329, 1376, 1424, 1472, 1519, 1567, 1614, 1662, 1710, 1758, 1805, 1853, 1901, 1949, 1997, 2044, 2091,
          2139, 2187, 2235, 2282, 2330, 2378, 2426, 2473, 2521, 2569, 2617, 2664, 2711, 2759, 2807, 2855, 2903, 2950, 2998, 3046, 3094, 3141, 3189, 3236, 3284, 3332, 3379, 3427, 3475, 3523, 3570, 3618, 3666, 3714, 3762]]
    hit0 = 7
    CD = 8
    TP成长 = 0.10
    TP上限 = 7
    MP = [60,616]


class 技能6(主动技能):
    名称 = '元素环绕'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0

    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.03+0.005*self.等级, 5)

class 技能7(被动技能):
    名称 = '元素禁断'
    所在等级 = 25
    基础等级 = 5
    等级上限 = 5

    关联技能 = ['无']

    冷却关联技能 = ['所有']
    非冷却关联技能 = ['幻魔四重奏','末日湮灭','启源·微观宇宙']

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 0.8


class 技能8(主动技能):
    名称 = '地炎'
    所在等级 = 25
    等级上限 = 70
    等级精通 = 60
    学习间隔 = 2

    data0 = [int(i*1.258)for i in [0, 268, 295, 322, 349, 377, 404, 432, 459, 486, 513, 540, 568, 596, 622, 650, 676, 704, 732, 759, 786, 814, 840, 867, 895, 922, 950, 976, 1004, 1031, 1059, 1086, 1113, 1140, 1168, 1195, 1223, 1249, 1277, 1304, 1331, 1359, 1386, 1413, 1441, 1467, 1494, 1522, 1549, 1577, 1603, 1631, 1658, 1686, 1713, 1740, 1767, 1795, 1822, 1850, 1877, 1904, 1931, 1958, 1985, 2014, 2040, 2068, 2094, 2121, 2149]]
    hit0 = 12
    CD = 5
    TP成长 = 0.1
    TP上限 = 7

    MP = [45,476]

    形态 = ["x12","x9","x6"]

    def 形态变更(self, 形态, char):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == 'x12':
            self.hit0 = 12
        if 形态 == 'x9':
            self.hit0 = 9
        if 形态 == 'x6':
            self.hit0 = 6

class 技能9(主动技能):
    名称 = '雷光链'
    所在等级 = 30
    等级上限 = 70
    等级精通 = 60
    学习间隔 = 2
    data0 =  [int(i*1.226)for i in [0, 1141, 1257, 1373, 1487, 1604, 1720, 1835, 1951, 2067, 2183, 2298, 2415, 2531, 2647, 2762, 2878, 2994, 3109, 3226, 3341, 3456, 3573, 3689, 3805, 3920, 4036, 4152, 4268, 4384, 4499, 4615, 4731, 4847, 4963, 5078, 5194, 5310, 5426, 5541, 5658, 5773, 5889, 6005, 6121, 6237, 6353, 6468, 6584, 6700, 6816, 6931, 7047, 7164, 7279, 7395, 7511, 7626, 7742, 7858, 7975, 8089, 8205, 8321, 8438, 8553, 8669, 8785, 8900, 9016, 9132]]
    hit0 = 4
    CD = 12
    TP成长 = 0.20
    TP上限 = 7
    MP = [100,1050]

class 技能10(主动技能):
    名称 = '暗域扩张'
    所在等级 = 30
    等级上限 = 70
    等级精通 = 60
    学习间隔 = 2
    data0 =  [int(i*1.217)for i in [0, 6475, 7133, 7789, 8446, 9104, 9761, 10418, 11074, 11732, 12389, 13046, 13703, 14360, 15017, 15675, 16330, 16988, 17646, 18301, 18959, 19616, 20273, 20930, 21587, 22244, 22902, 23558, 24215, 24872, 25529, 26186, 26843, 27501, 28157, 28814, 29472, 30127, 30785, 31443, 32099, 32756, 33413, 34070, 34728, 35384, 36042, 36699, 37356, 38013, 38669, 39327, 39985, 40640, 41298, 41955, 42611, 43269, 43926, 44583, 45240, 45897, 46554, 47210, 47868, 48525, 49182, 49839, 50496, 51153, 51811]]
    hit0 = 1
    CD = 15.0
    TP成长 = 0.10
    TP上限 = 7
    MP = [80,980]


class 技能11(被动技能):
    名称 = '元素循环'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10

    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.02 * self.等级, 5)


class 技能12(主动技能):
    名称 = '冰晶之浴'
    所在等级 = 35
    等级上限 = 70
    等级精通 = 60
    学习间隔 = 2
    data0 = [int(i*1.241)for i in [0, 477, 525, 574, 622, 671, 719, 768, 816, 864, 914, 961, 1010, 1059, 1106, 1156, 1204, 1252, 1301, 1349, 1398, 1446, 1494, 1543, 1592, 1640, 1689, 1738, 1785, 1834, 1883, 1931, 1980, 2028, 2076, 2125, 2173, 2222, 2271, 2318, 2367, 2416, 2464, 2513, 2561, 2610, 2658, 2706, 2755, 2803, 2852, 2900, 2950, 2997, 3045, 3094, 3142, 3192, 3239, 3289, 3337, 3384, 3434, 3482, 3531, 3579, 3627, 3676, 3724, 3773, 3821]]
    hit0 = 14
    CD = 12
    TP成长 = 0
    TP上限 = 1

    def 等效CD(self, **argv):
        if self.TP等级 >0:
            self.CD = self.CD - 3
        return super().等效CD(**argv)

class 技能13(主动技能):
    名称 = '旋炎破'
    所在等级 = 35
    等级上限 = 70
    等级精通 = 60
    学习间隔 = 2
    data0 = [int(i*1.2408)for i in [0, 759, 836, 913, 990, 1067, 1144, 1221, 1298, 1375, 1453, 1529, 1607, 1683, 1761, 1837, 1915, 1991, 2069, 2145, 2223, 2299, 2377, 2454, 2531, 2608, 2685, 2762, 2839, 2916, 2993, 3071, 3147, 3225, 3301, 3379, 3455, 3533, 3609, 3687, 3764, 3841, 3918, 3995, 4072, 4149, 4226, 4303, 4380, 4457, 4534, 4611, 4688, 4765, 4842, 4919, 4996, 5074, 5150, 5228, 5304, 5382, 5458, 5536, 5612, 5690, 5766, 5844, 5920, 5998, 6075]]
    hit0 = 6
    data1 = [int(i*1.2408)for i in [0, 3037, 3345, 3654, 3962, 4270, 4578, 4886, 5195, 5503, 5811, 6119, 6427, 6735, 7043, 7352, 7660, 7968, 8276, 8584, 8892, 9200, 9508, 9817, 10125, 10433, 10741, 11049, 11357, 11665, 11974, 12283, 12591, 12899, 13207, 13515, 13823, 14131, 14439, 14748, 15056, 15364, 15672, 15980, 16288, 16596, 16905, 17213, 17521, 17829, 18137, 18445, 18753, 19061, 19371, 19679, 19987, 20295, 20604, 20912, 21220, 21528, 21836, 22145, 22453, 22761, 23069, 23377, 23685, 23993, 24302]]
    hit1 = 1
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    无色消耗 = 1

    def 装备护石(self):
        self.power0 = 1.30
        self.power1 = 1.34

class 技能14(主动技能):
    名称 = '雷光屏障'
    所在等级 = 40
    等级上限 = 70
    等级精通 = 60
    学习间隔 = 2
    data0 = [int(i*1.239)for i in [0, 8424, 9279, 10134, 10990, 11844, 12699, 13554, 14408, 15263, 16118, 16973, 17826, 18681, 19536, 20391, 21246, 22101, 22955, 23810, 24665, 25520, 26374, 27229, 28084, 28938, 29793, 30648, 31502, 32358, 33213, 34068, 34922, 35777, 36632, 37486, 38341, 39196, 40051, 40905, 41760, 42615, 43470, 44325, 45180, 46035, 46889, 47744, 48598, 49452, 50307, 51162, 52016, 52872, 53727, 54582, 55436, 56291, 57146, 58000, 58855, 59710, 60564, 61419, 62274, 63129, 63984, 64839, 65694, 66548, 67403]]
    hit0 = 1
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    无色消耗 = 1

    def 装备护石(self):
        self.power0 = (4 + 0.4) * (1 - 0.72)

class 技能15(主动技能):
    名称 = '黑暗禁域'
    所在等级 = 40
    等级上限 = 70
    等级精通 = 60
    学习间隔 = 2
    data0 = [int(i*1.22)for i in [0, 7957, 8764, 9571, 10379, 11185, 11993, 12800, 13608, 14415, 15222, 16030, 16837, 17645, 18451, 19258, 20066, 20873, 21681, 22488, 23295, 24103, 24910, 25718, 26524, 27331, 28139, 28946, 29753, 30561, 31368, 32176, 32983, 33789, 34598, 35404, 36212, 37019, 37826, 38634, 39441, 40249, 41055, 41863, 42670, 43478, 44284, 45092, 45899, 46707, 47514, 48320, 49129, 49935, 50744, 51550, 52358, 53165, 53972, 54780, 55586, 56394, 57201, 58009, 58815, 59624, 60430, 61238, 62045, 62852, 63660]]
    hit0 = 1
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    无色消耗 = 1

class 技能16(主动技能):
    名称 = '元素轰炸'
    所在等级 = 45
    等级上限 = 70
    等级精通 = 60
    学习间隔 = 2
    data0 = [int(i*1.241)for i in [0, 2783, 3065, 3347, 3630, 3912, 4194, 4477, 4759, 5041, 5324, 5606, 5888, 6171, 6453, 6735, 7019, 7300, 7583, 7866, 8147, 8430, 8713, 8994, 9277, 9560, 9841, 10124, 10407, 10688, 10971, 11254, 11535, 11818, 12101, 12383, 12666, 12948, 13230, 13513, 13795, 14077, 14360, 14642, 14924, 15207, 15489, 15771, 16054, 16336, 16618, 16900, 17183, 17465, 17748, 18031, 18313, 18595, 18878, 19160, 19442, 19725, 20006, 20289, 20572, 20853, 21136, 21419, 21700, 21983, 22266]]
    hit0 = 1
    data1 = [int(i*1.241)for i in [0, 5566, 6131, 6695, 7260, 7824, 8389, 8955, 9519, 10084, 10649, 11213, 11777, 12343, 12907, 13471, 14037, 14602, 15166, 15731, 16296, 16860, 17425, 17990, 18554, 19119, 19684, 20249, 20814, 21378, 21943, 22508, 23072, 23637, 24202, 24767, 25331, 25897, 26461, 27025, 27591, 28155, 28719, 29284, 29849, 30415, 30979, 31544, 32109, 32673, 33237, 33803, 34367, 34931, 35498, 36062, 36626, 37191, 37756, 38320, 38885, 39450, 40014, 40579, 41144, 41709, 42274, 42838, 43403, 43968, 44532]]
    hit1 = 1
    data2 = [int(i*1.241)for i in [0, 255, 281, 308, 334, 359, 386, 411, 437, 464, 489, 515, 541, 567, 594, 620, 645, 671, 697, 723, 750, 775, 801, 827, 853, 880, 905, 931, 957, 984, 1009, 1036, 1061, 1087, 1113, 1139, 1166, 1191, 1217, 1243, 1270, 1295, 1322, 1347, 1372, 1400, 1425, 1452, 1477, 1503, 1529, 1555, 1581, 1607, 1633, 1658, 1686, 1711, 1738, 1763, 1789, 1816, 1841, 1867, 1893, 1919, 1945, 1972, 1997, 2022, 2049]]
    hit2 = 45
    CD = 40
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    无色消耗 = 2

    MP = [360,3150]

    def 装备护石(self):
        self.hit0 += 2.26 + 0.27
        self.hit1 += 1.45 + 0.46
        self.hit2 = 0

class 技能17(被动技能):
    名称 = '元素爆发'
    所在等级 = 48
    等级上限 = 60
    等级精通 = 50
    学习间隔 = 3

    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级 <= 16:
                return round(1.015 + 0.015 * self.等级, 5)
            else:
                return round(1.255 + 0.020 * (self.等级 - 16), 5)

class 技能18(主动技能):
    名称 = '幻魔四重奏'
    所在等级 = 50
    等级上限 = 50
    等级精通 = 40
    学习间隔 = 5
    data0 = [int(i*1.24)for i in [0, 2031, 2501, 2973, 3444, 3914, 4385, 4857, 5328, 5799, 6271, 6741, 7212, 7684, 8155, 8626, 9097, 9568, 10039, 10510, 10981, 11452, 11922, 12394, 12865, 13336, 13808, 14279, 14749, 15221, 15692, 16163, 16634, 17106, 17576, 18047, 18518, 18989, 19460, 19932, 20402, 20873, 21345, 21816, 22287, 22757, 23229, 23700, 24171, 24643, 25114, 25584, 26056, 26526, 26997, 27469, 27940, 28410, 28882, 29353, 29824, 30295, 30767, 31237, 31708, 32180, 32651, 33122, 33594, 34064, 34534]]
    hit0 = 30
    CD = 145.0
    无色消耗 = 5
    MP = [600,5040]

class 技能19(主动技能):
    名称 = '元素浓缩球'
    所在等级 = 60
    等级上限 = 50
    等级精通 = 40
    学习间隔 = 2
    data0 = [int(i*1.197)for i in [0, 5113, 5632, 6151, 6670, 7189, 7707, 8226, 8745, 9264, 9783, 10302, 10820, 11339, 11859, 12377, 12896, 13414, 13933, 14452, 14971, 15490, 16009, 16527, 17046, 17566, 18084, 18603, 19122, 19640, 20160, 20679, 21197, 21716, 22234, 22753, 23273, 23791, 24310, 24829, 25347, 25867, 26386, 26904, 27423, 27942, 28460, 28980, 29498, 30018, 30536, 31054, 31574, 32093, 32611, 33130, 33649, 34168, 34687, 35206, 35725, 36243, 36761, 37281, 37800, 38318, 38837, 39356, 39875, 40394, 40913]]
    hit0 = 1
    data1 = [int(i*1.197)for i in [0, 11932, 13143, 14353, 15565, 16775, 17986, 19195, 20406, 21617, 22828, 24039, 25249, 26459, 27670, 28881, 30092, 31302, 32513, 33722, 34934, 36144, 37355, 38566, 39776, 40988, 42197, 43408, 44619, 45829, 47041, 48251, 49461, 50671, 51882, 53093, 54304, 55515, 56724, 57935, 59146, 60357, 61568, 62778, 63988, 65199, 66410, 67620, 68831, 70042, 71253, 72463, 73673, 74884, 76095, 77306, 78517, 79726, 80937, 82147, 83358, 84569, 85780, 86990, 88200, 89411, 90622, 91833, 93044, 94253, 95464]]
    hit1 = 1
    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    无色消耗 = 1

    def 装备护石(self):
        self.hit0 *= 1.60
        self.hit1 *= 1 + 0.1 * 2

class 技能20(主动技能):
    名称 = '元素幻灭'
    所在等级 = 70
    等级上限 = 50
    等级精通 = 40
    学习间隔 = 2
    data0 = [int(i*1.238)for i in [0, 25649, 28251, 30853, 33456, 36059, 38660, 41262, 43864, 46467, 49069, 51671, 54272, 56875, 59478, 62080, 64682, 67283, 69886, 72488, 75091, 77693, 80294, 82897, 85499, 88102, 90703, 93305, 95907, 98510, 101113, 103714, 106317, 108918, 111521, 114123, 116725, 119328, 121929, 124532, 127133, 129736, 132338, 134941, 137542, 140144, 142747, 145349, 147952, 150553, 153155, 155757, 158360, 160963, 163564, 166166, 168768, 171371, 173973, 176576, 179176, 181779, 184382, 186984, 189586, 192187, 194790, 197392, 199995, 202596, 205199]]
    hit0 = 1
    data1 = [int(i*1.238)for i in [0, 1349, 1486, 1623, 1761, 1897, 2033, 2171, 2308, 2445, 2581, 2719, 2856, 2993, 3129, 3267, 3403, 3540, 3678, 3814, 3951, 4088, 4226, 4362, 4499, 4636, 4774, 4910, 5046, 5184, 5321, 5458, 5595, 5732, 5869, 6006, 6143, 6279, 6416, 6553, 6691, 6827, 6964, 7101, 7239, 7375, 7511, 7649, 7786, 7923, 8060, 8197, 8334, 8471, 8608, 8745, 8882, 9018, 9156, 9293, 9429, 9566, 9704, 9840, 9977, 10114, 10252, 10388, 10525, 10662, 10799]]
    hit1 = 1
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    无色消耗 = 2

    MP = [935,1960]

    def 装备护石(self):
        self.power0 = 1.1
        self.power1 = 5.4

class 技能21(主动技能):
    名称 = '元素禁域'
    所在等级 = 75
    等级上限 = 50
    等级精通 = 40
    学习间隔 = 2
    MP = [800,6000]
    data0 = [int(i*1.197)for i in [0, 43828, 48275, 52720, 57168, 61615, 66060, 70507, 74954, 79399, 83846, 88293, 92739, 97186, 101633, 106078, 110525, 114972, 119418, 123865, 128310, 132757, 137204, 141649, 146097, 150544, 154989, 159436, 163883, 168328, 172775, 177223, 181668, 186115, 190561, 195007, 199454, 203900, 208347, 212794, 217240, 221686, 226133, 230579, 235026, 239473, 243918, 248365, 252811, 257257, 261704, 266151, 270597, 275044, 279490, 283936, 288383, 292829, 297276, 301722, 306169, 310615, 315061, 319508, 323954, 328401, 332848, 337294, 341740, 346187, 350632]]
    hit0 = 1
    CD = 40.0
    是否有护石 = 1
    护石CD缩减 = 0
    无色消耗 = 3

    def 装备护石(self, x):
        self.倍率 *= 1.24

class 技能22(被动技能):
    名称 = '黑瞳'
    所在等级 = 75
    等级上限 = 50
    等级精通 = 40
    学习间隔 = 3

    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.23 + 0.02 * self.等级, 5)

class 技能23(主动技能):
    名称 = '聚能魔炮'
    所在等级 = 80
    等级上限 = 50
    等级精通 = 40
    学习间隔 = 2
    data0 = [int(i*1.197)for i in [0, 55032, 60615, 66199, 71782, 77365, 82949, 88532, 94114, 99697, 105280, 110863, 116446, 122030, 127613, 133196, 138779, 144362, 149945, 155528, 161111, 166694, 172278, 177861, 183443, 189027, 194610, 200193, 205776, 211359, 216942, 222525, 228109, 233691, 239274, 244858, 250441, 256024, 261607, 267190, 272773, 278356, 283939, 289522, 295105, 300689, 306272, 311855, 317438, 323020, 328603, 334187, 339770, 345353, 350937, 356520, 362103, 367687, 373268, 378851, 384434, 390018, 395601, 401184, 406768, 412351, 417934, 423517, 429100, 434682, 440266]]
    hit0 =1

    MP = [580,4500]
    无色消耗 = 5

    CD = 45.0
    演出时间 = 1.5
    是否有护石 = 1
    # 攻击倍率 = 1.083


    def 装备护石(self):
        self.倍率 *= 1.33


class 技能24(主动技能):
    名称 = '末日湮灭'
    所在等级 = 85

    等级上限 = 50
    等级精通 = 40
    学习间隔 = 5

    MP = [2500,5000]
    无色消耗 = 10

    data0 = [int(i*1.197)for i in [0, 6872, 8466, 10060, 11654, 13248, 14842, 16436, 18029, 19624, 21217, 22810, 24404, 25999, 27592, 29186, 30780, 32374, 33968, 35561, 37155, 38748, 40343, 41937, 43530, 45125, 46718, 48312, 49907, 51499, 53093, 54688, 56281, 57875, 59469, 61063, 62657, 64251, 65844, 67437, 69032, 70626, 72219, 73814, 75407, 77001, 78595, 80188, 81782, 83376, 84970, 86564, 88158, 89752, 91346, 92939, 94534, 96126, 97720, 99315, 100908, 102502, 104096, 105690, 107284, 108878, 110471, 112065, 113659, 115253, 116846]]
    hit0 = 1
    data1 = [int(i*1.197)for i in [0, 573, 705, 838, 971, 1103, 1236, 1368, 1502, 1634, 1767, 1900, 2032, 2165, 2299, 2432, 2565, 2697, 2830, 2963, 3095, 3228, 3361, 3494, 3627, 3759, 3892, 4026, 4158, 4291, 4424, 4557, 4690, 4822, 4955, 5087, 5220, 5353, 5486, 5619, 5751, 5885, 6018, 6150, 6283, 6416, 6549, 6682, 6814, 6947, 7080, 7212, 7345, 7478, 7612, 7745, 7877, 8010, 8143, 8275, 8409, 8541, 8674, 8807, 8939, 9072, 9204, 9339, 9471, 9604, 9737]]
    hit1 = 11
    data2 = [int(i*1.197)for i in [0, 123720, 152409, 181098, 209787, 238476, 267164, 295853, 324542, 353232, 381921, 410610, 439298, 467987, 496676, 525365, 554054, 582743, 611431, 640120, 668809, 697499, 726188, 754877, 783565, 812254, 840943, 869632, 898321, 927010, 955698, 984387, 1013076, 1041766, 1070455, 1099144, 1127833, 1156521, 1185210, 1213899, 1242588, 1271277, 1299966, 1328654, 1357343, 1386033, 1414722, 1443411, 1472100, 1500788, 1529477, 1558166, 1586855, 1615544, 1644233, 1672921, 1701610, 1730300, 1758989, 1787678, 1816367, 1845055, 1873743, 1902432, 1931121, 1959810, 1988499, 2017188, 2045877, 2074565, 2103255]]
    hit2 = 1

    CD = 180.0


class 技能25(被动技能):
    名称 = '异瞳'
    所在等级 = 95

    等级上限 = 50
    等级精通 = 40
    学习间隔 = 3

    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能26(主动技能):
    名称 = '聚魔轰击'
    所在等级 = 95

    等级上限 = 50
    等级精通 = 40
    学习间隔 = 2

    MP = [800,6667]
    无色消耗 = 7

    data0 = [int(i*1.196)for i in [0, 5434, 5985, 6537, 7088, 7639, 8191, 8742, 9293, 9845, 10396, 10947, 11499, 12050, 12601, 13153, 13704, 14255, 14807, 15358, 15909, 16461, 17012, 17563, 18115, 18666, 19217, 19769, 20320, 20871, 21423, 21974, 22525, 23077, 23628, 24180, 24731, 25282, 25834, 26385, 26936]]
    hit0 = 20
    CD = 60


class 技能27(主动技能):
    名称 = '启源·微观宇宙'
    所在等级 = 100

    等级上限 = 50
    等级精通 = 40
    学习间隔 = 5
    data0 = [int(i*1.197)for i in [0, 39550, 48721, 57892, 67063, 76234, 85405, 94576, 103747, 112918, 122089, 131260, 140431, 149602, 158773, 167944, 177115, 186286, 195457, 204628, 213799, 222970, 232141, 241312, 250483, 259654, 268825, 277996, 287167, 296339, 305510, 314681, 323852, 333023, 342194, 351365, 360536, 369707, 378878, 388049, 397220, 406391, 415562, 424733, 433904, 443075, 452246, 461417, 470588, 479759, 488930, 498101, 507272, 516443, 525614, 534785, 543956, 553127, 562298, 571469, 580641]]
    hit0 = 1
    data1 = [int(i*1.197)for i in [0, 6591, 8120, 9648, 11177, 12705, 14234, 15762, 17291, 18819, 20348, 21876, 23405, 24933, 26462, 27990, 29519, 31047, 32576, 34104, 35633, 37161, 38690, 40218, 41747, 43275, 44804, 46332, 47861, 49389, 50918, 52446, 53975, 55503, 57032, 58560, 60089, 61617, 63146, 64674, 66203, 67731, 69260, 70788, 72317, 73845, 75374, 76902, 78431, 79959, 81488, 83016, 84545, 86073, 87602, 89130, 90659, 92187, 93716, 95245, 96773]]
    hit1 = 12
    data2 = [int(i*1.197)for i in [0, 276850, 341047, 405244, 469442, 533639, 597836, 662033, 726231, 790428, 854625, 918822, 983020, 1047217, 1111414, 1175611, 1239808, 1304006, 1368203, 1432400, 1496597, 1560795, 1624992, 1689189, 1753386, 1817584, 1881781, 1945978, 2010175, 2074372, 2138570, 2202767, 2266964, 2331161, 2395359, 2459556, 2523753, 2587950, 2652148, 2716345, 2780542, 2844739, 2908936, 2973134, 3037331, 3101528, 3165725, 3229923, 3294120, 3358317, 3422514, 3486711, 3550909, 3615106, 3679303, 3743500, 3807698, 3871895, 3936092, 4000289, 4064487]]
    hit2 = 1
    CD = 290

    无色消耗 = 15
    MP = [4028,8056]

class classChange(Character):
    def __init__(self):
        self.实际名称 = 'elemental_bomber'
        self.名称 = '知源·元素爆破师'
        self.角色 = '魔法师(男)'

        self.职业 = '元素爆破师'
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
        self.buff = 2.07

        super().__init__()
