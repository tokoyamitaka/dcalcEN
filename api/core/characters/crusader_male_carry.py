from core.basic.skill import 技能
from core.basic.character import Character
from core.basic.skill import 主动技能, 被动技能
from math import *


class 技能0(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    学习间隔 = 1
    等级精通 = 110
    关联技能 = ['神罚之锤', '空斩打']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)


class 技能1(被动技能):
    名称 = '勇气恩赐'
    所在等级 = 15
    等级上限 = 25
    基础等级 = 15

    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        return (1.15 + (self.等级 - 15) * 0.02) if self.等级 >= 15 else (1 + self.等级 * 0.01)


class 技能2(主动技能):
    名称 = '光之复仇'
    所在等级 = 20
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [45, 469]
    data0 = [int(i*1.24) for i in [0, 191, 210, 229, 249, 268, 288, 308, 327, 345, 365, 384, 404, 424, 443, 462, 482, 501, 520, 541, 560, 579, 599, 617, 636, 656, 676, 695, 715, 734,
                                   753, 772, 793, 812, 831, 851, 869, 888, 908, 928, 947, 967, 986, 1005, 1025, 1045, 1064, 1084, 1103, 1121, 1141, 1160, 1180, 1200, 1219, 1238, 1258, 1277, 1297, 1316, 1336]]
    hit0 = 1
    CD = 0.2
    TP成长 = 0.10
    TP上限 = 7


class 技能3(主动技能):
    名称 = '纯白之刃'
    所在等级 = 20
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [27, 294]
    data0 = [int(i*1.243) for i in [0, 1106, 1218, 1330, 1443, 1555, 1667, 1779, 1892, 2004, 2116, 2228, 2341, 2453, 2565, 2677, 2790, 2902, 3014, 3126, 3239, 3351, 3463, 3575, 3688, 3800, 3912, 4024, 4137, 4249, 4361, 4473, 4586,
                                    4698, 4810, 4922, 5035, 5147, 5259, 5371, 5484, 5596, 5708, 5820, 5933, 6045, 6157, 6269, 6382, 6494, 6606, 6718, 6831, 6943, 7055, 7167, 7280, 7392, 7504, 7616, 7729, 7841, 7953, 8065, 8178, 8290, 8402, 8514, 8627, 8739, 8851]]
    hit0 = 1
    CD = 2.0
    TP成长 = 0.10
    TP上限 = 7


class 技能4(主动技能):
    名称 = '胜利之矛'
    所在等级 = 20
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [32, 343]
    data0 = [int(i*1.23) for i in [0, 978, 1077, 1176, 1276, 1375, 1475, 1574, 1673, 1773, 1872, 1971, 2070, 2170, 2269, 2368, 2467, 2566, 2666, 2765,
                                   2865, 2964, 3063, 3163, 3262, 3361, 3460, 3560, 3659, 3758, 3857, 3956, 4056, 4155, 4255, 4354, 4453, 4553, 4652,
                                   4751, 4850, 4949, 5049, 5148, 5247, 5346, 5446, 5545, 5645, 5744, 5843, 5943, 6042, 6141, 6240, 6339, 6439, 6538,
                                   6637, 6736, 6835, 6935, 7035, 7134, 7233, 7333, 7432, 7531, 7630, 7729, 7829]]
    hit0 = 1
    data1 = [int(i*1.23) for i in [0, 1525, 1681, 1835, 1990, 2145, 2300, 2455, 2610, 2765, 2919, 3075, 3229, 3384, 3539, 3694, 3848, 4004, 4158,
                                   4313, 4468, 4623, 4777, 4933, 5087, 5242, 5397, 5552, 5706, 5862, 6016, 6171, 6326, 6481, 6635, 6791, 6945, 7100,
                                   7255, 7410, 7565, 7720, 7875, 8029, 8185, 8339, 8494, 8649, 8804, 8958, 9114, 9268, 9423, 9578, 9733, 9887, 10043,
                                   10197, 10352, 10507, 10662, 10816, 10972, 11126, 11281, 11436, 11591, 11745, 11901, 12055, 12210]]
    hit1 = 1
    CD = 6.6
    TP成长 = 0.10
    TP上限 = 7


class 技能5(主动技能):
    名称 = '圣光十字'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [32, 343]
    data0 = [int(i*1.273) for i in [0, 1549, 1706, 1864, 2021, 2178, 2335, 2492, 2650, 2807, 2964, 3121, 3278, 3436, 3593, 3750, 3907, 4065, 4222, 4379, 4536, 4693, 4851, 5008, 5165, 5322, 5479, 5637, 5794, 5951, 6108, 6266, 6423, 6580, 6737,
                                    6894, 7052, 7209, 7366, 7523, 7680, 7838, 7995, 8152, 8309, 8467, 8624, 8781, 8938, 9095, 9253, 9410, 9567, 9724, 9881, 10039, 10196, 10353, 10510, 10667, 10825, 10982, 11139, 11296, 11454, 11611, 11768, 11925, 12082, 12240, 12397]]
    hit0 = 1
    data1 = [int(i*1.273) for i in [0, 2041, 2247, 2455, 2662, 2869, 3076, 3283, 3490, 3697, 3905, 4111, 4318, 4525, 4733, 4940, 5146, 5354, 5561, 5768, 5975, 6182, 6389, 6596, 6803, 7010, 7217, 7425, 7632, 7838, 8045, 8253, 8460, 8666, 8874, 9081,
                                    9288, 9495, 9702, 9909, 10116, 10324, 10530, 10737, 10945, 11152, 11359, 11565, 11773, 11980, 12187, 12394, 12601, 12808, 13015, 13222, 13429, 13636, 13844, 14051, 14257, 14465, 14672, 14879, 15085, 15293, 15500, 15707, 15915, 16121, 16328]]
    hit1 = 1
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 7
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1.2


class 技能6(主动技能):
    名称 = '圣光沁盾'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [91, 763]
    data0 = [int(i*1.3) for i in [0, 3881, 4275, 4669, 5062, 5456, 5850, 6244, 6637, 7031, 7425, 7819, 8213, 8606, 9000, 9394, 9788, 10181, 10575, 10969, 11363, 11757, 12150, 12544, 12938, 13332, 13725, 14119, 14513, 14907,
                                  15301, 15694, 16088, 16482, 16876, 17269, 17663, 18057, 18451, 18845, 19238, 19632, 20026, 20420, 20813, 21207, 21601, 21995, 22389, 22782, 23176, 23570, 23964, 24357, 24751, 25145, 25539, 25932, 26326, 26720, 27114]]
    hit0 = 1
    power0 = 1
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 7


class 技能7(被动技能):
    名称 = '坚定信念'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10

    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 >= 10:
            return (1.10 + (self.等级 - 10) * 0.015)
        else:
            return (1 + self.等级 * 0.01)


class 技能8(主动技能):
    名称 = '圣光球'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.247) for i in [0, 789, 869, 949, 1029, 1109, 1189, 1269, 1350, 1430, 1510, 1590, 1670, 1750, 1830, 1910, 1990, 2070, 2150, 2231,
                                    2311, 2391, 2471, 2551, 2631, 2711, 2791, 2871, 2951, 3031, 3112, 3192, 3272, 3352, 3432, 3512, 3592, 3672, 3752,
                                    3832, 3912, 3993, 4073, 4153, 4233, 4313, 4393, 4473, 4553, 4633, 4713, 4794, 4874, 4954, 5034, 5114, 5194, 5274,
                                    5354, 5434, 5514, 5594, 5675, 5755, 5835, 5915, 5995, 6075, 6155, 6235, 6315]]
    hit0 = 10
    data1 = [int(i*1.247) for i in [0, 1790, 1972, 2154, 2335, 2517, 2699, 2881, 3062, 3244, 3425, 3607, 3789, 3971, 4153, 4334, 4515, 4697, 4879,
                                    5061, 5243, 5425, 5605, 5787, 5969, 6151, 6333, 6515, 6696, 6877, 7059, 7241, 7423, 7605, 7786, 7968, 8149, 8331,
                                    8513, 8695, 8876, 9058, 9239, 9421, 9603, 9785, 9966, 10148, 10330, 10511, 10693, 10875, 11056, 11238, 11420,
                                    11602, 11783, 11965, 12146, 12328, 12510, 12692, 12874, 13055, 13236, 13418, 13600, 13782, 13964, 14145, 14326]]
    hit1 = 1
    CD = 14.4
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [150, 1260]
    无色消耗 = 1

    def TP加成(self):
        return 1
    # 理论下需要怪物可移动才能达成
    形态 = ["固定", "理论", "被动"]
    # 护石的部分还没写 护石的话理论和固定目标是hit0上限变为17，(ceil(5 / (0.5 - 0.10 * self.TP等级))/10)就是tp下的hit0；不到17按实际算；
    # 然后就是整体倍率*1.34

    def 形态变更(self, 形态, char: Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "理论":
            self.hit0 = ceil(10 / (1 - 0.10 * self.TP等级))
            self.hit1 = 1
            self.power1 = 1 + self.TP成长 * self.TP等级
            if '圣光球' in char.护石栏:
                self.hit0 = min(17, self.hit0)
        if 形态 == "固定":
            self.hit0 = ceil(8 / (1 - 0.10 * self.TP等级))
            self.hit1 = 1
            self.power1 = 1 + self.TP成长 * self.TP等级
            if '圣光球' in char.护石栏:
                self.hit0 = min(17, self.hit0)
        if 形态 == "被动":
            self.hit0 = 1*0.1
            self.hit1 = 1*0.5+5*1
            self.power0 = self.power1 = (1 + self.TP成长 * self.TP等级)

    def 装备护石(self):
        self.倍率 *= 1.34


class 技能9(主动技能):
    名称 = '圣光聚合'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [32, 343]
    data0 = [int(i*1.33) for i in [0, 422, 465, 507, 550, 593, 636, 679, 722, 764, 807, 850, 893, 936, 979, 1021, 1064, 1107, 1150, 1193, 1236, 1278, 1321, 1364, 1407, 1450, 1493, 1535, 1578, 1621,
                                   1664, 1707, 1750, 1792, 1835, 1878, 1921, 1964, 2006, 2049, 2092, 2135, 2178, 2221, 2263, 2306, 2349, 2392, 2435, 2478, 2520, 2563, 2606, 2649, 2692, 2735, 2777, 2820, 2863, 2906, 2949]]
    hit0 = 1
    data1 = [int(i*1.33) for i in [0, 844, 930, 1015, 1101, 1187, 1272, 1358, 1444, 1529, 1615, 1701, 1786, 1872, 1958, 2043, 2129, 2215, 2300, 2386, 2472, 2557, 2643, 2729, 2814, 2900, 2986, 3071, 3157,
                                   3243, 3328, 3414, 3500, 3585, 3671, 3756, 3842, 3928, 4013, 4099, 4185, 4270, 4356, 4442, 4527, 4613, 4699, 4784, 4870, 4956, 5041, 5127, 5213, 5298, 5384, 5470, 5555, 5641, 5727, 5812, 5898]]
    hit1 = 1
    data2 = [int(i*1.33) for i in [0, 3219, 3545, 3872, 4198, 4525, 4852, 5178, 5505, 5831, 6158, 6484, 6811, 7138, 7464, 7791, 8117, 8444, 8770, 9097, 9424, 9750, 10077, 10403, 10730, 11056, 11383, 11710, 12036, 12363,
                                   12689, 13016, 13343, 13669, 13996, 14322, 14649, 14975, 15302, 15629, 15955, 16282, 16608, 16935, 17261, 17588, 17915, 18241, 18568, 18894, 19221, 19548, 19874, 20201, 20527, 20854, 21180, 21507, 21834, 22160, 22487]]
    hit2 = 1
    CD = 10.0
    TP成长 = 0.10
    TP上限 = 5


class 技能10(主动技能):
    名称 = '忏悔之锤'
    所在等级 = 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.254) for i in [0, 4886, 5382, 5877, 6373, 6869, 7365, 7860, 8356, 8852, 9348, 9843, 10339, 10835, 11331, 11826, 12322, 12818, 13313, 13809, 14305, 14801, 15296, 15792, 16288, 16784, 17279, 17775, 18271, 18767, 19262, 19758, 20254, 20749, 21245,
                                    21741, 22237, 22732, 23228, 23724, 24220, 24715, 25211, 25707, 26202, 26698, 27194, 27690, 28185, 28681, 29177, 29673, 30168, 30664, 31160, 31656, 32151, 32647, 33143, 33638, 34134, 34630, 35126, 35621, 36117, 36613, 37109, 37604, 38100, 38596, 39092]]
    hit0 = 1
    data1 = [int(i*1.254) for i in [0, 2033, 2239, 2445, 2652, 2858, 3064, 3271, 3477, 3683, 3889, 4096, 4302, 4508, 4715, 4921, 5127, 5333, 5540, 5746, 5952, 6158, 6365, 6571, 6777, 6984, 7190, 7396, 7602, 7809, 8015, 8221, 8428, 8634, 8840, 9046,
                                    9253, 9459, 9665, 9872, 10078, 10284, 10490, 10697, 10903, 11109, 11316, 11522, 11728, 11934, 12141, 12347, 12553, 12760, 12966, 13172, 13378, 13585, 13791, 13997, 14203, 14410, 14616, 14822, 15029, 15235, 15441, 15647, 15854, 16060, 16266]]
    hit1 = 1
    CD = 14.4
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [160, 1344]
    无色消耗 = 1

    def 装备护石(self):
        self.倍率 *= 1.34
        self.CDR *= 0.9


class 技能11(主动技能):
    名称 = '正义审判'
    所在等级 = 45
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.251) for i in [0, 575, 633, 691, 750, 808, 866, 925, 983, 1041, 1100, 1158, 1216, 1275, 1333, 1391, 1450, 1508, 1566, 1625, 1683, 1742, 1800, 1858, 1917, 1975, 2033, 2092, 2150, 2208, 2267, 2325, 2383, 2442,
                                    2500, 2558, 2617, 2675, 2733, 2792, 2850, 2908, 2967, 3025, 3083, 3142, 3200, 3258, 3317, 3375, 3434, 3492, 3550, 3609, 3667, 3725, 3784, 3842, 3900, 3959, 4017, 4075, 4134, 4192, 4250, 4309, 4367, 4425, 4484, 4542, 4600]]
    hit0 = 16
    data1 = [int(i*1.251) for i in [0, 9201, 10135, 11068, 12002, 12935, 13869, 14802, 15736, 16670, 17603, 18537, 19470, 20404, 21337, 22271, 23204, 24138, 25071, 26005, 26938, 27872, 28805, 29739, 30672, 31606, 32539, 33473, 34406, 35340, 36273, 37207, 38141, 39074,
                                    40008, 40941, 41875, 42808, 43742, 44675, 45609, 46542, 47476, 48409, 49343, 50276, 51210, 52143, 53077, 54010, 54944, 55877, 56811, 57744, 58678, 59611, 60545, 61479, 62412, 63346, 64279, 65213, 66146, 67080, 68013, 68947, 69880, 70814, 71747, 72681, 73614]]
    hit1 = 1
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [350, 2940]
    无色消耗 = 2

    def 装备护石(self):
        self.hit0 = 8
        self.power1 = 2.16


class 技能12(被动技能):
    名称 = '信念光环'
    所在等级 = 48
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30

    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.015 + 0.02 * self.等级, 5)


class 技能13(主动技能):
    名称 = '天启之珠'
    所在等级 = 50
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i*1.244) for i in [0, 576, 710, 844, 978, 1111, 1245, 1379, 1512, 1646, 1780, 1914, 2047, 2181, 2315, 2449, 2582, 2716, 2850,
                                    2984, 3117, 3251, 3385, 3519, 3652, 3786, 3920, 4054, 4187, 4321, 4455, 4589, 4722, 4856, 4990, 5124, 5257, 5391, 5525, 5659, 5792]]
    hit0 = 29
    data1 = [int(i*1.244) for i in [0, 19873, 24482, 29090, 33699, 38307, 42916, 47524, 52133, 56741, 61350, 65958, 70567, 75175, 79784, 84392, 89000, 93609, 98217, 102826,
                                    107434, 112043, 116651, 121260, 125868, 130477, 135085, 139694, 144302, 148910, 153519, 158127, 162736, 167344, 171953, 176561, 181170, 185778, 190387, 194995, 199604]]
    hit1 = 1
    倍率 = 1.3  # 圣灵之槌
    CD = 145

    MP = [1200, 10080]
    无色消耗 = 5


class 技能14(主动技能):
    名称 = '圣光突袭'
    所在等级 = 60
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.242) for i in [0, 1650, 1818, 1985, 2153, 2320, 2488, 2655, 2823, 2990, 3158, 3325, 3493, 3660, 3828, 3995, 4163, 4330, 4498, 4665, 4832, 5000, 5167, 5335, 5502, 5670, 5837, 6005, 6172, 6340, 6507, 6675, 6842, 7010, 7177,
                                    7345, 7512, 7680, 7847, 8015, 8182, 8350, 8517, 8685, 8852, 9019, 9187, 9354, 9522, 9689, 9857, 10024, 10192, 10359, 10527, 10694, 10862, 11029, 11197, 11364, 11532, 11699, 11867, 12034, 12202, 12369, 12537, 12704, 12872, 13039, 13206]]
    hit0 = 3
    data1 = [int(i*1.242) for i in [0, 10985, 12099, 13214, 14328, 15443, 16557, 17672, 18786, 19901, 21015, 22129, 23244, 24358, 25473, 26587, 27702, 28816, 29931, 31045, 32160, 33274, 34388, 35503, 36617, 37732, 38846, 39961, 41075, 42190, 43304, 44419, 45533, 46647,
                                    47762, 48876, 49991, 51105, 52220, 53334, 54449, 55563, 56678, 57792, 58906, 60021, 61135, 62250, 63364, 64479, 65593, 66708, 67822, 68937, 70051, 71165, 72280, 73394, 74509, 75623, 76738, 77852, 78967, 80081, 81196, 82310, 83425, 84539, 85653, 86768, 87882]]
    hit1 = 1
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [400, 1000]
    无色消耗 = 1

    def 装备护石(self):
        self.power1 = 1.49
        self.CDR *= 0.9


class 技能15(主动技能):
    名称 = '神圣之矛'
    所在等级 = 70
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.242) for i in [0, 471, 519, 567, 615, 663, 711, 759, 806, 854, 902, 950, 998, 1046, 1094, 1142, 1189, 1237, 1285, 1333, 1381, 1429,
                                    1477, 1525, 1572, 1620, 1668, 1716, 1764, 1812, 1860, 1908, 1955, 2003, 2051, 2099, 2147, 2195, 2243, 2290, 2338, 2386, 2434, 2482, 2530, 2578, 2626]]
    hit0 = 1
    data1 = [int(i*1.242) for i in [0, 1962, 2161, 2360, 2560, 2759, 2958, 3157, 3356, 3555, 3754, 3953, 4153, 4352, 4551, 4750, 4949, 5148, 5347, 5546, 5745, 5945,
                                    6144, 6343, 6542, 6741, 6940, 7139, 7338, 7537, 7737, 7936, 8135, 8334, 8533, 8732, 8931, 9130, 9330, 9529, 9728, 9927, 10126, 10325, 10524, 10723, 10922]]
    hit1 = 1
    data2 = [int(i*1.242) for i in [0, 5546, 6108, 6671, 7234, 7796, 8359, 8922, 9484, 10047, 10610, 11172, 11735, 12298, 12860, 13423, 13986, 14548, 15111, 15674, 16236, 16799,
                                    17362, 17924, 18487, 19049, 19612, 20175, 20737, 21300, 21863, 22425, 22988, 23551, 24113, 24676, 25239, 25801, 26364, 26927, 27489, 28052, 28615, 29177, 29740, 30303, 30865]]
    hit2 = 3
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [860, 1500]
    无色消耗 = 2

    def 装备护石(self):
        self.倍率 *= 1.31


class 技能16(主动技能):
    名称 = '神圣之光'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40
    MP = [580, 4500]
    data0 = [int(i*1.241) for i in [0, 25717, 28326, 30935, 33544, 36153, 38763, 41372, 43981, 46590, 49199, 51808, 54417, 57026, 59635, 62244, 64853, 67462, 70071, 72680,
                                    75289, 77898, 80507, 83116, 85725, 88334, 90943, 93553, 96162, 98771, 101380, 103989, 106598, 109207, 111816, 114425, 117034, 119643, 122252, 124861, 127470]]
    hit0 = 1
    CD = 20.0
    是否有护石 = 1
    无色消耗 = 3

    # 破招下的技能本身额外加成和圣光十字的buff属于加算

    def 装备护石(self):
        self.倍率 *= 1.35
        self.无色消耗 -= 3


class 技能17(主动技能):
    名称 = '圣佑结界'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.245) for i in [0, 4322, 4761, 5200, 5638, 6077, 6515, 6954, 7392, 7831, 8270, 8708, 9147, 9585, 10024, 10462, 10901, 11340, 11778, 12217,
                                    12655, 13094, 13532, 13971, 14409, 14848, 15287, 15725, 16164, 16602, 17041, 17479, 17918, 18357, 18795, 19234, 19672, 20111, 20549, 20988, 21427]]
    hit0 = 2
    data1 = [int(i*1.245) for i in [0, 21614, 23807, 26000, 28193, 30386, 32579, 34771, 36964, 39157, 41350, 43543, 45736, 47928, 50121, 52314, 54507, 56700, 58893,
                                    61085, 63278, 65471, 67664, 69857, 72049, 74242, 76435, 78628, 80821, 83014, 85206, 87399, 89592, 91785, 93978, 96171, 98363, 100556, 102749, 104942, 107135]]
    hit1 = 1
    倍率 = 1.43  # 圣灵之槌
    CD = 40.0
    是否有护石 = 1

    MP = [580, 4500]
    无色消耗 = 3

    def 装备护石(self, x):
        self.hit0 = 0
        self.power1 = 1.78


# 神罚之锤下的空斩打和落凤锤问题比较多，暂时放置了
class 技能18(主动技能):
    名称 = '神罚之锤'
    备注 = '(一轮普通攻击，TP为基础精通)'
    所在等级 = 80
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    # 平x第一击+平x第二击+平x第三击+神圣冲击光柱+神圣冲击冲击波；不成长
    # 冲击波吃圣光十字双加成
    data0 = [0] + [181+219+282+349+244*1.2] * 50
    hit0 = 1
    CD = 2.0
    TP成长 = 0.10
    TP上限 = 5

    # 本身有无色消耗和蓝耗的，可以通过多次上buff来被无色套加成；但同时也可以吃到非无色技能+xx这种加成
    MP = [800, 6000]
    无色消耗 = 5

    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.24 + 0.02 * self.等级, 5)


class 技能19(主动技能):
    名称 = '神圣洗礼：信仰之翼'
    所在等级 = 85
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i*1.296) for i in [0, 2176, 2681, 3186, 3691, 4196, 4700, 5205, 5710, 6215, 6720, 7224, 7729, 8234, 8739, 9243, 9748, 10253, 10758, 11263,
                                    11767, 12272, 12777, 13282, 13787, 14291, 14796, 15301, 15806, 16311, 16815, 17320, 17825, 18330, 18834, 19339, 19844, 20349, 20854, 21358, 21863]]
    hit0 = 15
    data1 = [int(i*1.296) for i in [0, 91430, 112631, 133832, 155033, 176234, 197435, 218637, 239838, 261039, 282240, 303441, 324642, 345844, 367045, 388246, 409447, 430648, 451849,
                                    473051, 494252, 515453, 536654, 557855, 579056, 600258, 621459, 642660, 663861, 685062, 706263, 727465, 748666, 769867, 791068, 812269, 833470, 854672, 875873, 897074, 918275]]
    hit1 = 1
    CD = 180

    # 这里有个小问题，现在二觉把终结技信仰之翼 : 裁决单独拆解出来了，而这个技能等级是锁1的；也就是MP消耗锁2500。
    # 不过这版本影响不大，只有耳环对MP4000以上有要求，本体部分能够4000基本上终结技也够的
    MP = [2500, 5000]
    无色消耗 = 10


class 技能20(主动技能):
    名称 = '神罚之锤：天怒'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.244) for i in [0, 61029, 67221, 73412, 79604, 85795, 91987, 98178, 104369, 110561, 116752, 122944, 129135, 135327, 141518, 147710, 153901, 160092, 166284, 172475, 178667, 184858, 191050, 197241, 203433, 209624, 215815, 222007, 228198, 234390, 240581, 246773, 252964, 259155, 265347,
                                    271538, 277730, 283921, 290113, 296304, 302496, 308687, 314878, 321070, 327261, 333453, 339644, 345836, 352027, 358219, 364410, 370601, 376793, 382984, 389176, 395367, 401559, 407750, 413941, 420133, 426324, 432516, 438707, 444899, 451090, 457282, 463473, 469664, 475856, 482047, 488239]]
    hit0 = 1
    data1 = [int(i*1.244) for i in [0, 40686, 44814, 48941, 53069, 57197, 61324, 65452, 69579, 73707, 77835, 81962, 86090, 90218, 94345, 98473, 102601, 106728, 110856, 114983, 119111, 123239, 127366, 131494, 135622, 139749, 143877, 148004, 152132, 156260, 160387, 164515, 168643, 172770, 176898,
                                    181025, 185153, 189281, 193408, 197536, 201664, 205791, 209919, 214046, 218174, 222302, 226429, 230557, 234685, 238812, 242940, 247067, 251195, 255323, 259450, 263578, 267706, 271833, 275961, 280088, 284216, 288344, 292471, 296599, 300727, 304854, 308982, 313109, 317237, 321365, 325492]]
    hit1 = 1
    CD = 60.0

    MP = [1065, 8000]
    无色消耗 = 7


class 技能21(被动技能):
    名称 = '神之代行者'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    关联技能 = ['所有']

    非关联技能 = ['空斩打']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能22(主动技能):
    名称 = '生命礼赞：神威'
    所在等级 = 100
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i*1.241) for i in [0, 41386, 50983, 60579, 70176, 79773, 89370, 98967, 108563, 118160, 127757, 137354, 146951, 156547, 166144, 175741, 185338, 194935, 204531, 214128, 223725, 233322, 242919, 252516, 262112, 271709, 281306, 290903, 300500, 310096, 319693, 329290, 338887, 348484, 358080,
                                    367677, 377274, 386871, 396468, 406064, 415661, 425258, 434855, 444452, 454048, 463645, 473242, 482839, 492436, 502033, 511629, 521226, 530823, 540420, 550017, 559613, 569210, 578807, 588404, 598001, 607597, 617194, 626791, 636388, 645985, 655581, 665178, 674775, 684372, 693969, 703565]]
    hit0 = 8
    CD = 290

    MP = [4025, 8055]
    无色消耗 = 15


class 技能23(主动技能):
    名称 = '空斩打'
    所在等级 = 1
    等级上限 = 20
    学习间隔 = 3
    等级精通 = 10
    MP = [0, 0]
    data0 = [int(i*1.0) for i in [0, 95, 105, 115, 126, 136, 147, 158, 168, 179, 189, 200, 210, 220, 231, 241, 252, 263, 273, 284, 294, 305, 315, 325, 336, 346, 357, 368, 378, 389, 399, 410, 420,
                                  430, 441, 451, 462, 473, 483, 494, 504, 515, 525, 535, 546, 556, 567, 578, 588, 599, 609, 620, 630, 640, 651, 661, 672, 683, 693, 704, 714, 725, 735, 745, 756, 766, 777, 788, 798, 809, 819]]
    CD = 2.0

    # 冲击波吃圣光十字双加成
    data1 = [0] + [349+244*1.2]*20
    hit1 = 1
    power1 = 1

    TP成长 = 0.1
    TP上限 = 5


class 技能24(主动技能):
    名称 = '落凤锤'
    所在等级 = 80
    等级上限 = 1
    基础等级 = 1
    # 当装备[神罚之锤]时,[落凤锤] : 可发动[雷霆粉碎]
    data0 = [int(x*1.246) for x in [0, 2660, 2930, 3198, 3469, 3738, 4008, 4279, 4548, 4817, 5087, 5357, 5627, 5897, 6167, 6437, 6705, 6976, 7246,
                                    7516, 7786, 8056, 8324, 8594, 8865, 9134, 9404, 9675, 9944, 10213, 10484, 10753, 11023, 11293, 11563, 11832, 12101, 12372, 12642, 12911, 13182]]
    hit0 = 2
    CD = 6.0


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'crusader_male_carry'
        self.名称 = '战斗·神启·圣骑士'
        self.角色 = '圣职者(男)'
        self.角色类型 = '输出'
        self.职业 = '圣骑士'
        # 用来筛CP武器的
        self.转职 = '圣骑士(男)'
        self.武器选项 = ['镰刀', '念珠', '战斧', '十字架']
        self.输出类型选项 = ['魔法固伤']
        self.防具精通属性 = ['智力']
        self.类型 = '魔法固伤'
        self.武器类型 = '镰刀'
        self.防具类型 = '板甲'
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
        self.buff = 1.97

        super().__init__()

    def 职业特殊计算(self):
        神罚之锤 = self.get_skill_by_name('神罚之锤')
        空斩打 = self.get_skill_by_name('空斩打')
        落凤锤 = self.get_skill_by_name('落凤锤')

        空斩打.power0 *= 1+0.1*self.get_skill_by_name('神罚之锤').TP等级
        落凤锤.等级 = 神罚之锤.等级

        落凤锤.等级上限 = 神罚之锤.等级上限

    def 伤害指数计算(self):

        神之代行者 = self.get_skill_by_name('神之代行者')

        x = 神之代行者.加成倍率(self.武器类型)

        self.get_skill_by_name('空斩打').power1 *= x

        super().伤害指数计算()
