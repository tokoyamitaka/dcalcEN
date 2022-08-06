
from core.baseClass.skill import 技能
from core.baseClass.character import Character
from core.baseClass.skill import 主动技能, 被动技能


class 技能0(主动技能):
    名称 = '连续射击'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [40, 292]
    data0 = [int(i) for i in [0, 932, 1028, 1122, 1217, 1313, 1407, 1502, 1596, 1692, 1786, 1880, 1975, 2070, 2164, 2259, 2354, 2449, 2543, 2639, 2733, 2828, 2923, 3017, 3111, 3206, 3301, 3396, 3490, 3586, 3680, 3775, 3870, 3965,
                              4058, 4153, 4248, 4343, 4437, 4533, 4627, 4722, 4816, 4912, 5006, 5100, 5195, 5290, 5384, 5480, 5574, 5669, 5763, 5859, 5954, 6048, 6144, 6237, 6332, 6426, 6522, 6616, 6711, 6806, 6901, 6995, 7091, 7185, 7279, 7373, 7469]]
    hit0 = 2
    data1 = [int(i) for i in [0, 1244, 1370, 1497, 1623, 1749, 1875, 2002, 2128, 2254, 2381, 2507, 2633, 2759, 2886, 3012, 3138, 3264, 3392, 3519, 3644, 3771, 3897, 4023, 4149, 4276, 4402, 4528, 4654, 4781, 4908, 5033, 5160, 5286,
                              5412, 5538, 5665, 5791, 5917, 6044, 6170, 6297, 6422, 6549, 6675, 6801, 6927, 7054, 7180, 7306, 7433, 7559, 7686, 7811, 7938, 8064, 8190, 8316, 8443, 8569, 8695, 8822, 8948, 9075, 9200, 9327, 9453, 9579, 9705, 9832, 9959]]
    hit1 = 1
    CD = 6
    TP成长 = 0.10
    TP上限 = 7


class 技能1(主动技能):
    名称 = '迅步突袭'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [12, 500]
    data0 = [int(i) for i in [0, 2952, 3252, 3551, 3851, 4150, 4450, 4749, 5049, 5348, 5648, 5947, 6247, 6546, 6846, 7145, 7445, 7744, 8044, 8343, 8643, 8943, 9242, 9542, 9841, 10141, 10440, 10740, 11039, 11339, 11638, 11938, 12237, 12537, 12836, 13136,
                              13435, 13735, 14034, 14334, 14634, 14933, 15233, 15532, 15832, 16131, 16431, 16730, 17030, 17329, 17629, 17928, 18228, 18527, 18827, 19126, 19426, 19725, 20025, 20325, 20624, 20924, 21223, 21523, 21822, 22122, 22421, 22721, 23020, 23320, 23619]]
    hit0 = 1
    CD = 5
    TP成长 = 0.10
    TP上限 = 7


class 技能2(被动技能):
    名称 = '特工秘技'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10


def 加成倍率(self, 武器类型):
    if self.等级 == 0:
        return 1.0
    else:
        return round(1.1 + 0.02 * self.等级, 5)


class 技能3(主动技能):
    名称 = '双弦斩'
    所在等级 = 20
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [40, 292]
    data0 = [int(i) for i in [0, 1246, 1372, 1498, 1625, 1751, 1877, 2004, 2132, 2256, 2384, 2511, 2638, 2763, 2890, 3017, 3143, 3269, 3396, 3522, 3648, 3775, 3901, 4028, 4154, 4281, 4407, 4534, 4660, 4786, 4913, 5040, 5165, 5292,
                              5419, 5544, 5671, 5798, 5924, 6050, 6177, 6304, 6430, 6556, 6683, 6809, 6936, 7062, 7188, 7315, 7442, 7567, 7694, 7821, 7946, 8073, 8201, 8328, 8453, 8580, 8707, 8833, 8959, 9086, 9212, 9339, 9465, 9591, 9718, 9844, 9970]]
    hit0 = 1
    data1 = [int(i) for i in [0, 1869, 2058, 2248, 2438, 2627, 2817, 3006, 3196, 3386, 3576, 3766, 3955, 4145, 4335, 4524, 4715, 4904, 5094, 5284, 5473, 5663, 5852, 6042, 6232, 6421, 6611, 6800, 6990, 7180, 7369, 7559, 7748, 7938, 8128, 8317,
                              8507, 8696, 8886, 9076, 9265, 9456, 9645, 9835, 10025, 10214, 10404, 10593, 10784, 10974, 11163, 11353, 11542, 11732, 11922, 12111, 12301, 12490, 12680, 12870, 13059, 13249, 13438, 13628, 13818, 14007, 14197, 14386, 14576, 14766, 14955]]
    hit1 = 1
    CD = 6
    TP成长 = 0.10
    TP上限 = 7


class 技能4(被动技能):
    名称 = '小太刀精通'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 <= 10:
            return round(1.040 + 0.01 * self.等级, 5)
        if self.等级 > 10:
            return round(1.150 + 0.02 * (self.等级 - 10), 5)


class 技能5(主动技能):
    名称 = '月光挥斩'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [15, 300]
    data0 = [int(i) for i in [0, 2143, 2360, 2578, 2795, 3013, 3230, 3448, 3665, 3883, 4100, 4318, 4535, 4752, 4970, 5187, 5405, 5622, 5840, 6057, 6275, 6492, 6710, 6927, 7144, 7362, 7579, 7797, 8014, 8232, 8449, 8667, 8884, 9102, 9319, 9536, 9754,
                              9971, 10189, 10406, 10624, 10841, 11059, 11276, 11493, 11711, 11928, 12146, 12363, 12581, 12798, 13016, 13233, 13451, 13668, 13885, 14103, 14320, 14538, 14755, 14973, 15190, 15408, 15625, 15843, 16060, 16277, 16495, 16712, 16930, 17147]]
    hit0 = 2
    CD = 7
    TP成长 = 0.10
    TP上限 = 7


class 技能6(主动技能):
    名称 = '精准射击'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [30, 500]
    data0 = [int(i) for i in [0, 6218, 6848, 7479, 8110, 8741, 9372, 10003, 10633, 11264, 11895, 12526, 13157, 13788, 14418, 15049, 15680, 16311, 16942, 17572, 18203, 18834, 19465, 20096, 20727, 21357, 21988, 22619, 23250, 23881, 24512, 25142, 25773, 26404, 27035,
                              27666, 28296, 28927, 29558, 30189, 30820, 31451, 32081, 32712, 33343, 33974, 34605, 35236, 35866, 36497, 37128, 37759, 38390, 39020, 39651, 40282, 40913, 41544, 42175, 42805, 43436, 44067, 44698, 45329, 45960, 46590, 47221, 47852, 48483, 49114, 49744]]
    hit0 = 1
    CD = 8
    TP成长 = 0.10
    TP上限 = 7


class 技能7(主动技能):
    名称 = '满月斩'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i) for i in [0, 1332, 1467, 1602, 1737, 1872, 2007, 2143, 2278, 2413, 2548, 2683, 2818, 2954, 3089, 3224, 3359, 3494, 3629, 3764, 3900, 4035, 4170, 4305, 4440, 4575, 4710, 4846, 4981, 5116, 5251, 5386, 5521, 5657,
                              5792, 5927, 6062, 6197, 6332, 6467, 6603, 6738, 6873, 7008, 7143, 7278, 7414, 7549, 7684, 7819, 7954, 8089, 8224, 8360, 8495, 8630, 8765, 8900, 9035, 9170, 9306, 9441, 9576, 9711, 9846, 9981, 10117, 10252, 10387, 10522, 10657]]
    hit0 = 3
    data1 = [int(i) for i in [0, 4884, 5380, 5875, 6371, 6866, 7362, 7858, 8353, 8849, 9344, 9840, 10335, 10831, 11326, 11822, 12318, 12813, 13309, 13804, 14300, 14795, 15291, 15786, 16282, 16778, 17273, 17769, 18264, 18760, 19255, 19751, 20246, 20742, 21238,
                              21733, 22229, 22724, 23220, 23715, 24211, 24706, 25202, 25698, 26193, 26689, 27184, 27680, 28175, 28671, 29166, 29662, 30158, 30653, 31149, 31644, 32140, 32635, 33131, 33626, 34122, 34618, 35113, 35609, 36104, 36600, 37095, 37591, 38086, 38582, 39078]]
    hit1 = 1
    CD = 15
    TP成长 = 0.10
    TP上限 = 5

    MP = [100, 850]
    无色消耗 = 1


class 技能8(主动技能):
    名称 = '月影秘步'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i) for i in [0, 837, 922, 1007, 1091, 1176, 1261, 1346, 1431, 1516, 1601, 1686, 1771, 1856, 1941, 2026, 2111, 2196, 2281, 2365, 2450, 2535, 2620, 2705, 2790, 2875, 2960, 3045, 3130, 3215, 3300, 3385, 3470, 3554,
                              3639, 3724, 3809, 3894, 3979, 4064, 4149, 4234, 4319, 4404, 4489, 4574, 4659, 4744, 4828, 4913, 4998, 5083, 5168, 5253, 5338, 5423, 5508, 5593, 5678, 5763, 5848, 5933, 6017, 6102, 6187, 6272, 6357, 6442, 6527, 6612, 6697]]
    hit0 = 18
    CD = 20
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [60, 850]
    无色消耗 = 1

    def 装备护石(self):
        self.倍率 *= 1.27
        self.CDR *= 0.85


class 技能9(主动技能):
    名称 = '锁定射击'
    所在等级 = 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i) for i in [0, 1430, 1575, 1721, 1866, 2011, 2156, 2301, 2446, 2591, 2737, 2882, 3027, 3172, 3317, 3462, 3608, 3753, 3898, 4043, 4188, 4333, 4478, 4624, 4769, 4914, 5059, 5204, 5349, 5495, 5640, 5785, 5930, 6075, 6220,
                              6365, 6511, 6656, 6801, 6946, 7091, 7236, 7382, 7527, 7672, 7817, 7962, 8107, 8252, 8398, 8543, 8688, 8833, 8978, 9123, 9268, 9414, 9559, 9704, 9849, 9994, 10139, 10285, 10430, 10575, 10720, 10865, 11010, 11155, 11301, 11446]]
    hit0 = 12
    CD = 20
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [150, 1260]
    无色消耗 = 1

    def 装备护石(self):
        self.倍率 *= 1.14


class 技能10(主动技能):
    名称 = '枪刃旋杀'
    所在等级 = 45
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i) for i in [0, 1343, 1479, 1616, 1752, 1888, 2024, 2161, 2297, 2433, 2570, 2706, 2842, 2978, 3115, 3251, 3387, 3524, 3660, 3796, 3933, 4069, 4205, 4341, 4478, 4614, 4750, 4887, 5023, 5159, 5295, 5432, 5568, 5704,
                              5841, 5977, 6113, 6249, 6386, 6522, 6658, 6795, 6931, 7067, 7204, 7340, 7476, 7612, 7749, 7885, 8021, 8158, 8294, 8430, 8566, 8703, 8839, 8975, 9112, 9248, 9384, 9521, 9657, 9793, 9929, 10066, 10202, 10338, 10475, 10611, 10747]]
    hit0 = 1
    data1 = [int(i) for i in [0, 1151, 1268, 1385, 1501, 1618, 1735, 1852, 1969, 2086, 2202, 2319, 2436, 2553, 2670, 2787, 2903, 3020, 3137, 3254, 3371, 3487, 3604, 3721, 3838, 3955, 4072, 4188, 4305, 4422, 4539, 4656, 4773, 4889,
                              5006, 5123, 5240, 5357, 5473, 5590, 5707, 5824, 5941, 6058, 6174, 6291, 6408, 6525, 6642, 6758, 6875, 6992, 7109, 7226, 7343, 7459, 7576, 7693, 7810, 7927, 8044, 8160, 8277, 8394, 8511, 8628, 8744, 8861, 8978, 9095, 9212]]
    hit1 = 17
    data2 = [int(i) for i in [0, 5924, 6525, 7126, 7727, 8329, 8930, 9531, 10132, 10733, 11334, 11935, 12536, 13137, 13738, 14339, 14940, 15541, 16142, 16743, 17345, 17946, 18547, 19148, 19749, 20350, 20951, 21552, 22153, 22754, 23355, 23956, 24557, 25158, 25759,
                              26361, 26962, 27563, 28164, 28765, 29366, 29967, 30568, 31169, 31770, 32371, 32972, 33573, 34174, 34775, 35377, 35978, 36579, 37180, 37781, 38382, 38983, 39584, 40185, 40786, 41387, 41988, 42589, 43190, 43791, 44393, 44994, 45595, 46196, 46797, 47398]]
    hit2 = 2
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [250, 2500]
    无色消耗 = 2

    def 装备护石(self):
        self.power1 = 2.07
        self.hit2 = 0


class 技能11(被动技能):
    名称 = '使命觉悟'
    所在等级 = 48
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)


class 技能12(主动技能):
    名称 = '噬血绝杀'
    所在等级 = 50
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i) for i in [0, 30810, 37955, 45100, 52244, 59389, 66533, 73678, 80823, 87967, 95112, 102256, 109401, 116545, 123690, 130835, 137979, 145124, 152268, 159413,
                              166557, 173702, 180847, 187991, 195136, 202280, 209425, 216569, 223714, 230859, 238003, 245148, 252292, 259437, 266581, 273726, 280871, 288015, 295160, 302304, 309449]]
    hit0 = 2
    CD = 145

    MP = [881, 7403]
    无色消耗 = 5

    def 等效百分比(self, 武器类型):
        if self.等级 >= 9:
            self.power0 = 1.1
        return super().等效百分比(武器类型)


class 技能13(主动技能):
    名称 = '终极锁定'
    所在等级 = 60
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i) for i in [0, 6121, 6742, 7363, 7984, 8605, 9226, 9847, 10468, 11089, 11710, 12331, 12952, 13573, 14194, 14815, 15436, 16056, 16677, 17298,
                              17919, 18540, 19161, 19782, 20403, 21024, 21645, 22266, 22887, 23508, 24129, 24750, 25371, 25992, 26613, 27234, 27855, 28476, 29097, 29718, 30339]]
    hit0 = 4
    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [400, 1620]
    无色消耗 = 2

    def 装备护石(self):
        self.hit0 = 4.6
        self.倍率 *= 1.16
        self.CDR *= 0.90


class 技能14(主动技能):
    名称 = '月相轮舞'
    所在等级 = 70
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i) for i in [0, 5638, 6210, 6782, 7354, 7926, 8498, 9070, 9641, 10213, 10785, 11357, 11929, 12501, 13073, 13645, 14217, 14789, 15361, 15933, 16505, 17077, 17649, 18221, 18793, 19365, 19937, 20509, 21081, 21653, 22225, 22797, 23369, 23941, 24513,
                              25085, 25657, 26229, 26801, 27373, 27945, 28517, 29089, 29661, 30233, 30805, 31377, 31949, 32521, 33093, 33665, 34237, 34809, 35381, 35953, 36525, 37097, 37669, 38241, 38813, 39385, 39957, 40529, 41101, 41673, 42245, 42816, 43388, 43960, 44532, 45104]]
    hit0 = 2
    data1 = [int(i) for i in [0, 6374, 7021, 7668, 8314, 8961, 9608, 10254, 10901, 11548, 12195, 12841, 13488, 14135, 14781, 15428, 16075, 16721, 17368, 18015, 18662, 19308, 19955, 20602, 21248, 21895, 22542, 23188, 23835, 24482, 25129, 25775, 26422, 27069, 27715,
                              28362, 29009, 29656, 30302, 30949, 31596, 32242, 32889, 33536, 34182, 34829, 35476, 36123, 36769, 37416, 38063, 38709, 39356, 40003, 40650, 41296, 41943, 42590, 43236, 43883, 44530, 45176, 45823, 46470, 47117, 47763, 48410, 49057, 49703, 50350, 50997]]
    hit1 = 2
    data2 = [int(i) for i in [0, 7968, 8776, 9585, 10393, 11201, 12010, 12818, 13626, 14435, 15243, 16052, 16860, 17668, 18477, 19285, 20094, 20902, 21710, 22519, 23327, 24135, 24944, 25752, 26561, 27369, 28177, 28986, 29794, 30603, 31411, 32219, 33028, 33836,
                              34644, 35453, 36261, 37070, 37878, 38686, 39495, 40303, 41111, 41920, 42728, 43537, 44345, 45153, 45962, 46770, 47579, 48387, 49195, 50004, 50812, 51620, 52429, 53237, 54046, 54854, 55662, 56471, 57279, 58087, 58896, 59704, 60513, 61321, 62129, 62938, 63746]]
    hit2 = 2
    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [800, 1680]
    无色消耗 = 2

    def 装备护石(self):
        self.倍率 *= 1.28
        self.CDR *= 0.90


class 技能15(主动技能):
    名称 = '月光镇魂曲'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i) for i in [0, 5081, 5597, 6112, 6628, 7143, 7659, 8174, 8690, 9206, 9721, 10237, 10752, 11268, 11783, 12299, 12814, 13330, 13845, 14361,
                              14876, 15392, 15908, 16423, 16939, 17454, 17970, 18485, 19001, 19516, 20032, 20547, 21063, 21578, 22094, 22610, 23125, 23641, 24156, 24672, 25187]]
    hit0 = 9
    data1 = [int(i) for i in [0, 19600, 21589, 23577, 25566, 27554, 29543, 31531, 33520, 35508, 37497, 39486, 41474, 43463, 45451, 47440, 49428, 51417, 53405,
                              55394, 57382, 59371, 61359, 63348, 65336, 67325, 69313, 71302, 73290, 75279, 77267, 79256, 81244, 83233, 85221, 87210, 89198, 91187, 93175, 95164, 97152]]
    hit1 = 1
    CD = 40
    是否有护石 = 1

    MP = [580, 4500]
    无色消耗 = 3

    def 装备护石(self):
        self.hit0 = 6
        self.power0 = 1.64
        self.power1 = 1.75


class 技能16(被动技能):
    名称 = '冷酷杀意'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


class 技能17(主动技能):
    名称 = '毁灭狂欢'
    所在等级 = 80
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i) for i in [0, 5513, 6073, 6632, 7192, 7751, 8310, 8870, 9429, 9989, 10548, 11107, 11667, 12226, 12785, 13345, 13904, 14464, 15023, 15582, 16142, 16701, 17261, 17820, 18379, 18939, 19498, 20058, 20617, 21176, 21736, 22295, 22854, 23414, 23973,
                              24533, 25092, 25651, 26211, 26770, 27330, 27889, 28448, 29008, 29567, 30126, 30686, 31245, 31805, 32364, 32923, 33483, 34042, 34602, 35161, 35720, 36280, 36839, 37399, 37958, 38517, 39077, 39636, 40195, 40755, 41314, 41874, 42433, 42992, 43552, 44111]]
    hit0 = 11
    data1 = [int(i) for i in [0, 10703, 11789, 12875, 13961, 15047, 16132, 17218, 18304, 19390, 20476, 21562, 22648, 23733, 24819, 25905, 26991, 28077, 29163, 30249, 31335, 32420, 33506, 34592, 35678, 36764, 37850, 38936, 40022, 41107, 42193, 43279, 44365, 45451,
                              46537, 47623, 48708, 49794, 50880, 51966, 53052, 54138, 55224, 56310, 57395, 58481, 59567, 60653, 61739, 62825, 63911, 64996, 66082, 67168, 68254, 69340, 70426, 71512, 72598, 73683, 74769, 75855, 76941, 78027, 79113, 80199, 81285, 82370, 83456, 84542, 85628]]
    hit1 = 1
    CD = 45
    是否有护石 = 1

    MP = [600, 5000]
    无色消耗 = 5

    def 装备护石(self):
        self.倍率 *= 1.33


class 技能18(主动技能):
    名称 = '月相天陨'
    所在等级 = 85
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i) for i in [0, 4402, 5423, 6444, 7465, 8486, 9507, 10528, 11549, 12569, 13590, 14611, 15632, 16653, 17674, 18695, 19716, 20737, 21758, 22778, 23799, 24820, 25841, 26862, 27883, 28904, 29925, 30946, 31967, 32988, 34008, 35029, 36050, 37071, 38092,
                              39113, 40134, 41155, 42176, 43197, 44218, 45238, 46259, 47280, 48301, 49322, 50343, 51364, 52385, 53406, 54427, 55447, 56468, 57489, 58510, 59531, 60552, 61573, 62594, 63615, 64636, 65657, 66677, 67698, 68719, 69740, 70761, 71782, 72803, 73824, 74845]]
    hit0 = 21
    data1 = [int(i) for i in [0, 49783, 61328, 72872, 84416, 95960, 107504, 119048, 130592, 142136, 153680, 165224, 176769, 188313, 199857, 211401, 222945, 234489, 246033, 257577, 269121, 280665, 292210, 303754, 315298, 326842, 338386, 349930, 361474, 373018, 384562, 396106, 407651, 419195, 430739,
                              442283, 453827, 465371, 476915, 488459, 500003, 511547, 523092, 534636, 546180, 557724, 569268, 580812, 592356, 603900, 615444, 626988, 638532, 650077, 661621, 673165, 684709, 696253, 707797, 719341, 730885, 742429, 753973, 765518, 777062, 788606, 800150, 811694, 823238, 834782, 846326]]
    hit1 = 1
    CD = 180

    MP = [2500, 5000]
    无色消耗 = 10


class 技能19(主动技能):
    名称 = '夜影迷踪'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i) for i in [0, 36327, 40012, 43697, 47383, 51068, 54754, 58439, 62124, 65810, 69495, 73180, 76866, 80551, 84237, 87922, 91607, 95293, 98978, 102663, 106349, 110034, 113720, 117405, 121090, 124776, 128461, 132146, 135832, 139517, 143203, 146888, 150573, 154259, 157944, 161629,
                              165315, 169000, 172686, 176371, 180056, 183742, 187427, 191112, 194798, 198483, 202169, 205854, 209539, 213225, 216910, 220595, 224281, 227966, 231652, 235337, 239022, 242708, 246393, 250078, 253764, 257449, 261135, 264820, 268505, 272191, 275876, 279561, 283247, 286932, 290618]]
    hit0 = 1
    data1 = [int(i) for i in [0, 38749, 42680, 46611, 50542, 54473, 58404, 62335, 66266, 70197, 74128, 78059, 81990, 85921, 89852, 93783, 97715, 101646, 105577, 109508, 113439, 117370, 121301, 125232, 129163, 133094, 137025, 140956, 144887, 148818, 152749, 156681, 160612, 164543, 168474,
                              172405, 176336, 180267, 184198, 188129, 192060, 195991, 199922, 203853, 207784, 211715, 215647, 219578, 223509, 227440, 231371, 235302, 239233, 243164, 247095, 251026, 254957, 258888, 262819, 266750, 270681, 274612, 278544, 282475, 286406, 290337, 294268, 298199, 302130, 306061, 309992]]
    hit1 = 1
    data2 = [int(i) for i in [0, 46014, 50682, 55350, 60018, 64687, 69355, 74023, 78691, 83359, 88027, 92695, 97364, 102032, 106700, 111368, 116036, 120704, 125372, 130041, 134709, 139377, 144045, 148713, 153381, 158049, 162718, 167386, 172054, 176722, 181390, 186058, 190726, 195394, 200063,
                              204731, 209399, 214067, 218735, 223403, 228071, 232740, 237408, 242076, 246744, 251412, 256080, 260748, 265417, 270085, 274753, 279421, 284089, 288757, 293425, 298094, 302762, 307430, 312098, 316766, 321434, 326102, 330771, 335439, 340107, 344775, 349443, 354111, 358779, 363448, 368116]]
    hit2 = 1
    CD = 60

    MP = [960, 7200]
    无色消耗 = 7


class 技能20(被动技能):
    名称 = '无暇'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能21(主动技能):
    名称 = '月夜：终极行动'
    所在等级 = 100
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i) for i in [0, 26331, 32437, 38543, 44649, 50754, 56860, 62966, 69072, 75178, 81284, 87390, 93496, 99601, 105707, 111813, 117919, 124025, 130131, 136237, 142342, 148448, 154554, 160660, 166766, 172872, 178978, 185084, 191189, 197295, 203401, 209507, 215613, 221719, 227825,
                              233930, 240036, 246142, 252248, 258354, 264460, 270566, 276671, 282777, 288883, 294989, 301095, 307201, 313307, 319413, 325518, 331624, 337730, 343836, 349942, 356048, 362154, 368259, 374365, 380471, 386577, 392683, 398789, 404895, 411000, 417106, 423212, 429318, 435424, 441530, 447636]]
    hit0 = 11
    data1 = [int(i) for i in [0, 124134, 152919, 181703, 210488, 239273, 268058, 296843, 325627, 354412, 383197, 411982, 440767, 469551, 498336, 527121, 555906, 584691, 613475, 642260, 671045, 699830, 728614, 757399, 786184, 814969, 843754, 872538, 901323, 930108, 958893, 987678, 1016462, 1045247, 1074032, 1102817,
                              1131602, 1160386, 1189171, 1217956, 1246741, 1275526, 1304310, 1333095, 1361880, 1390665, 1419450, 1448234, 1477019, 1505804, 1534589, 1563374, 1592158, 1620943, 1649728, 1678513, 1707298, 1736082, 1764867, 1793652, 1822436, 1851221, 1880006, 1908791, 1937576, 1966360, 1995145, 2023930, 2052715, 2081500, 2110285]]
    hit1 = 1
    CD = 290

    MP = [4028, 8056]
    无色消耗 = 15


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'agent'
        self.名称 = '苍暮·特工'
        self.角色 = '枪剑士'

        self.职业 = '特工'
        self.武器选项 = ['小太刀']
        self.输出类型选项 = ['物理百分比']
        self.防具精通属性 = ['力量']
        self.类型 = '物理百分比'
        self.武器类型 = '小太刀'
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
        self.buff = 2.00

        super().__init__()

    def 结果计算(self):
        装备锁定护石 = 0
        毁灭狂欢次数 = 0
        锁定射击次数 = 0
        加成倍率 = 0
        for item in self.护石栏:
            if item == '锁定射击':
                装备锁定护石 = 1
        for skill in self.技能队列:
            if skill['名称'] == '毁灭狂欢':
                毁灭狂欢次数 += 1
            if skill['名称'] == '锁定射击':
                锁定射击次数 += 1
        if 装备锁定护石 == 1 and 锁定射击次数 != 0:
            加成倍率 = 1+毁灭狂欢次数*0.5/锁定射击次数
            for skill in self.技能队列:
                if skill['名称'] == '锁定射击':
                    skill['倍率'] *= 加成倍率*1.14
        return self.伤害计算()
