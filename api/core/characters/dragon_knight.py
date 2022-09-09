from core.basic.skill import 技能
from core.basic.character import Character
from core.basic.skill import 主动技能, 被动技能


class 技能0(被动技能):
    名称 = '基础精通'
    所在等级 = 1
    等级上限 = 200
    基础等级 = 110
    关联技能 = ['龙人剑术', '基本攻击']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(0.463 + 0.089 * self.等级, 5)


class 技能1(主动技能):
    名称 = '基本攻击'
    所在等级 = 1
    等级上限 = 1
    基础等级 = 1
    # 3击 242.9176+259.9278+310.9584
    data0 = [(i) for i in [0, 813.8037]]
    hit0 = 1
    CD = 1
    TP成长 = 0.10
    TP上限 = 5


class 技能2(主动技能):
    名称 = '龙人剑术'
    备注 = '(TP为基础精通)'
    所在等级 = 15
    等级上限 = 1
    学习间隔 = 2
    等级精通 = 1
    MP = [35, 35]
    data0 = [(i) for i in [0, 1473]]
    hit0 = 1
    CD = 3.0
    TP成长 = 0.10
    TP上限 = 5


class 技能3(主动技能):
    名称 = '火焰吐息'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [30, 252]
    data0 = [(i) for i in [0, 1060, 1166, 1275, 1382, 1490, 1597, 1704, 1813, 1920, 2027, 2134, 2243, 2350, 2458, 2565, 2673, 2781, 2887, 2995, 3104, 3210, 3318, 3426, 3532, 3641, 3749, 3855, 3963,
                           4070, 4178, 4286, 4392, 4501, 4609, 4715, 4823, 4932, 5038, 5146, 5254, 5362, 5469, 5576, 5683, 5792, 5899, 6006, 6114, 6221, 6330, 6437, 6544, 6651, 6760, 6867, 6974, 7081, 7190, 7298, 7404]]
    hit0 = 3
    CD = 5.0
    TP成长 = 0.10
    TP上限 = 7


class 技能4(主动技能):
    名称 = '龙翼突袭'
    所在等级 = 20
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [30, 252]
    data0 = [(i) for i in [0, 1869, 2059, 2249, 2439, 2628, 2818, 3008, 3198, 3388, 3578, 3767, 3957, 4147, 4337, 4527, 4715, 4905, 5095, 5285, 5475, 5664, 5854, 6044, 6234, 6424, 6613, 6803, 6993, 7183, 7373, 7563, 7751, 7941, 8131, 8321,
                           8511, 8700, 8890, 9080, 9270, 9460, 9649, 9839, 10028, 10218, 10408, 10598, 10787, 10977, 11167, 11357, 11547, 11736, 11926, 12116, 12306, 12496, 12684, 12874, 13064, 13254, 13444, 13633, 13823, 14013, 14203, 14393, 14583, 14772, 14962]]
    hit0 = 1
    data1 = [(i) for i in [0, 1693, 1865, 2036, 2208, 2380, 2552, 2724, 2896, 3067, 3239, 3411, 3583, 3755, 3926, 4098, 4270, 4442, 4614, 4786, 4957, 5129, 5301, 5473, 5645, 5816, 5988, 6160, 6332, 6504, 6676, 6847, 7019, 7191, 7363, 7535,
                           7706, 7878, 8050, 8222, 8394, 8566, 8737, 8909, 9081, 9253, 9425, 9597, 9768, 9940, 10112, 10284, 10456, 10627, 10799, 10971, 11143, 11315, 11487, 11658, 11830, 12002, 12174, 12346, 12517, 12689, 12861, 13033, 13205, 13377, 13548]]
    hit1 = 1
    CD = 4.0
    TP成长 = 0.10
    TP上限 = 7


class 技能5(主动技能):
    名称 = '龙语召唤：阿斯特拉'
    所在等级 = 20
    等级上限 = 30
    学习间隔 = 2
    等级精通 = 20
    MP = [126, 975]
    data0 = [(i) for i in [0, 3616, 4194, 4769, 5345, 5923, 6498, 7076, 7652, 8229, 8805, 9383, 9958, 10534, 11112,
                           11687, 12265, 12841, 13418, 13994, 14572, 15147, 15724, 16301, 16876, 17454, 18031, 18608, 19183, 19761, 20338]]
    hit0 = 1
    CD = 7.0

    关联技能 = ['所有']

    def 独立攻击力倍率进图(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 20:
            return round(1.05 + 0.005 * self.等级, 5)
        else:
            return round(0.75 + 0.02 * self.等级, 5)


class 技能6(主动技能):
    名称 = '爆破龙角'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [35, 300]
    data0 = [(i) for i in [0, 2072, 2281, 2491, 2702, 2911, 3121, 3330, 3542, 3752, 3961, 4172, 4383, 4592, 4803, 5013, 5222, 5434, 5644, 5853, 6064, 6273, 6483, 6695, 6904, 7114, 7325, 7534, 7744, 7956, 8165,
                           8375, 8586, 8795, 9006, 9216, 9426, 9636, 9845, 10057, 10267, 10476, 10687, 10896, 11106, 11318, 11527, 11737, 11948, 12157, 12368, 12579, 12788, 12998, 13209, 13418, 13629, 13839, 14049, 14259, 14469]]
    hit0 = 1
    data1 = [(i) for i in [0, 4833, 5322, 5814, 6303, 6795, 7284, 7775, 8265, 8756, 9246, 9736, 10227, 10717, 11207, 11698, 12188, 12679, 13168, 13658, 14149, 14639, 15130, 15619, 16111, 16600, 17091, 17581, 18072, 18562,
                           19053, 19543, 20033, 20523, 21014, 21504, 21995, 22485, 22975, 23465, 23956, 24446, 24937, 25427, 25918, 26407, 26899, 27388, 27879, 28369, 28859, 29350, 29840, 30330, 30821, 31311, 31802, 32291, 32783, 33272, 33764]]
    hit1 = 1
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 7


class 技能7(主动技能):
    名称 = '龙拳'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [180, 1512]
    # 地面
    data0 = [(i) for i in [0, 2434, 2681, 2927, 3175, 3421, 3669, 3915, 4163, 4410, 4656, 4905, 5151, 5398, 5644, 5893, 6139, 6386, 6632, 6880, 7127, 7374, 7621, 7868, 8114, 8362, 8609, 8856, 9102, 9349, 9597, 9844,
                           10090, 10338, 10584, 10832, 11078, 11326, 11572, 11819, 12066, 12314, 12560, 12807, 13053, 13302, 13548, 13795, 14041, 14290, 14537, 14783, 15031, 15277, 15525, 15771, 16019, 16265, 16512, 16758, 17007]]
    hit0 = 1
    data1 = [(i) for i in [0, 3652, 4022, 4392, 4764, 5133, 5503, 5873, 6245, 6615, 6985, 7357, 7727, 8097, 8468, 8839, 9208, 9578, 9949, 10320, 10690, 11061, 11432, 11802, 12173, 12542, 12913, 13284, 13654, 14024, 14396,
                           14766, 15136, 15506, 15878, 16248, 16617, 16989, 17359, 17729, 18099, 18471, 18841, 19212, 19582, 19953, 20324, 20693, 21063, 21434, 21805, 22175, 22546, 22917, 23287, 23657, 24029, 24398, 24768, 25138, 25510]]
    hit1 = 1
    # 空中
    data2 = [(i) for i in [0, 670, 739, 806, 875, 943, 1011, 1078, 1146, 1216, 1283, 1351, 1419, 1487, 1554, 1624, 1692, 1759, 1828, 1895, 1963, 2030, 2100, 2168, 2235, 2304, 2371, 2440, 2508, 2576,
                           2644, 2712, 2781, 2848, 2917, 2985, 3052, 3121, 3189, 3257, 3324, 3393, 3462, 3529, 3598, 3665, 3733, 3801, 3870, 3938, 4005, 4074, 4141, 4209, 4278, 4346, 4414, 4482, 4550, 4617, 4687]]
    hit2 = 0
    data3 = [(i) for i in [0, 6038, 6650, 7263, 7876, 8488, 9101, 9714, 10326, 10938, 11552, 12164, 12777, 13389, 14001, 14614, 15226, 15840, 16453, 17064, 17677, 18289, 18902, 19516, 20127, 20740, 21353, 21965, 22577, 23191,
                           23803, 24416, 25029, 25640, 26253, 26867, 27479, 28092, 28703, 29316, 29929, 30543, 31155, 31767, 32379, 32992, 33605, 34216, 34830, 35443, 36055, 36668, 37279, 37892, 38506, 39119, 39731, 40343, 40955, 41568, 42182]]
    hit3 = 0
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 7

    形态 = ['地面', '空中']

    def 形态变更(self, 形态, char):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "地面":
            self.hit0 = 1
            self.hit1 = 1
            self.hit2 = 0
            self.hit3 = 0
        if 形态 == "空中":
            self.hit0 = 0
            self.hit1 = 0
            self.hit2 = 1
            self.hit3 = 1


class 技能8(主动技能):
    名称 = '龙之撕咬'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [50, 420]
    data0 = [(i) for i in [0, 1124, 1239, 1354, 1468, 1583, 1696, 1810, 1925, 2040, 2153, 2267, 2382, 2495, 2610, 2725, 2838, 2952, 3067, 3181, 3296, 3411, 3523, 3638, 3753, 3866, 3981, 4095, 4209,
                           4323, 4438, 4552, 4666, 4780, 4894, 5009, 5124, 5236, 5351, 5466, 5580, 5694, 5808, 5922, 6037, 6151, 6265, 6380, 6494, 6607, 6722, 6837, 6951, 7064, 7179, 7293, 7408, 7522, 7635, 7750, 7865]]
    hit0 = 6
    CD = 10
    TP成长 = 0.10
    TP上限 = 7


class 技能9(主动技能):
    名称 = '龙翼穿刺'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [(i) for i in [144, 157, 172, 188, 202, 215, 230, 246, 260, 273, 289, 304, 318, 334, 347, 362, 376, 392, 405, 420, 436, 450, 463, 478, 494, 508, 522, 537,
                           552, 566, 580, 595, 610, 624, 640, 653, 668, 682, 698, 711, 726, 742, 756, 770, 784, 800, 814, 828, 843, 858, 872, 888, 901, 916, 930, 946, 960, 974, 990, 1004]]
    hit0 = 2
    data1 = [(i) for i in [8795, 9687, 10580, 11472, 12364, 13257, 14149, 15042, 15933, 16826, 17718, 18610, 19503, 20395, 21288, 22179, 23071, 23964, 24856, 25749, 26641, 27534, 28425, 29317, 30210, 31102, 31995, 32887, 33780,
                           34671, 35563, 36456, 37348, 38241, 39133, 40026, 40917, 41809, 42702, 43594, 44487, 45379, 46272, 47163, 48055, 48948, 49840, 50733, 51625, 52516, 53409, 54301, 55194, 56086, 56979, 57871, 58762, 59655, 60547, 61440]]
    hit1 = 1
    data1 = [(i) for i in [9634, 10604, 11585, 12565, 13542, 14514, 15493, 16474, 17452, 18423, 19402, 20382, 21363, 22341, 23313, 24292, 25272, 26252, 27221, 28201, 29182, 30162, 31132, 32110, 33091, 34070, 35042, 36019, 37001,
                           37979, 38950, 39930, 40909, 41889, 42869, 43841, 44820, 45799, 46779, 47749, 48729, 49709, 50688, 51659, 52637, 53619, 54596, 55568, 56547, 57527, 58507, 59486, 60456, 61437, 62417, 63397, 64367, 65346, 66326, 67306]]
    hit1 = 0
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 5

    MP = [200, 1820]
    无色消耗 = 1

    形态 = ['常规', '撕咬']

    def 形态变更(self, 形态, char):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "常规":
            self.hit0 = 2
            self.hit1 = 1
            self.hit2 = 0
        if 形态 == "撕咬":
            self.hit0 = 0
            self.hit1 = 0
            self.hit2 = 1


class 技能10(主动技能):
    名称 = '飞龙斩'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [(i) for i in [0, 2716, 2992, 3267, 3542, 3818, 4094, 4370, 4645, 4920, 5198, 5473, 5749, 6024, 6298, 6576, 6851, 7126, 7402, 7677, 7954, 8229, 8504, 8780, 9056, 9332, 9607, 9882, 10158, 10434, 10710,
                           10985, 11260, 11536, 11812, 12087, 12363, 12638, 12915, 13190, 13465, 13741, 14016, 14293, 14568, 14843, 15119, 15394, 15670, 15946, 16221, 16497, 16774, 17048, 17325, 17599, 17874, 18152, 18427, 18703, 18978]]
    hit0 = 2
    data1 = [(i) for i in [0, 7979, 8787, 9597, 10407, 11216, 12026, 12837, 13646, 14454, 15263, 16074, 16884, 17693, 18503, 19312, 20121, 20931, 21740, 22550, 23360, 24168, 24978, 25788, 26597, 27407, 28216, 29025, 29835, 30644,
                           31455, 32265, 33074, 33884, 34692, 35502, 36312, 37121, 37931, 38741, 39549, 40359, 41168, 41978, 42788, 43597, 44406, 45215, 46025, 46835, 47644, 48455, 49263, 50072, 50883, 51692, 52502, 53312, 54121, 54930, 55740]]
    hit1 = 1
    CD = 15
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [105, 882]
    无色消耗 = 1

    def 装备护石(self):
        self.hit0 += 1.7
        self.CDR *= 0.9


class 技能11(被动技能):
    名称 = '大胃王'
    所在等级 = 35
    等级上限 = 20
    学习间隔 = 2
    等级精通 = 10
    是否有伤害 = 0
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 <= 10:
            return round(1.0 + 0.01 * self.等级, 5)
        else:
            return round(0.9 + 0.02 * self.等级, 5)


class 技能12(主动技能):
    名称 = '龙刃无双'
    所在等级 = 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [(i) for i in [0, 17491, 19266, 21039, 22815, 24590, 26365, 28137, 29912, 31687, 33461, 35236, 37011, 38784, 40559, 42334, 44109, 45883, 47658, 49432, 51206, 52981, 54756, 56530, 58305, 60079, 61854, 63628, 65403, 67178,
                           68952, 70726, 72501, 74275, 76050, 77825, 79600, 81373, 83148, 84923, 86697, 88472, 90247, 92019, 93794, 95569, 97345, 99118, 100893, 102667, 104441, 106216, 107991, 109765, 111540, 113314, 115089, 116863, 118638, 120413, 122187]]
    hit0 = 0
    data1 = [(i) for i in [0, 18431, 20301, 22172, 24041, 25912, 27782, 29651, 31522, 33391, 35262, 37131, 39002, 40870, 42741, 44611, 46481, 48352, 50221, 52091, 53961, 55831, 57701, 59571, 61440, 63311, 65180, 67051, 68920, 70791, 72661,
                           74530, 76401, 78270, 80141, 82011, 83880, 85750, 87620, 89490, 91360, 93229, 95100, 96969, 98840, 100710, 102580, 104450, 106319, 108190, 110059, 111930, 113801, 115669, 117539, 119409, 121280, 123150, 125018, 126889, 128759]]
    hit1 = 1
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [188, 1579]
    无色消耗 = 1

    形态 = ['上挑', '平砍']

    def 形态变更(self, 形态, char):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "上挑":
            self.hit0 = 0
            self.hit1 = 1
        if 形态 == "平砍":
            self.hit0 = 1
            self.hit1 = 0

    def 装备护石(self):
        self.倍率 *= 1.37


class 技能13(主动技能):
    名称 = '魔龙之息'
    所在等级 = 45
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [(i) for i in [0, 2396, 2639, 2882, 3125, 3369, 3611, 3855, 4098, 4341, 4584, 4827, 5072, 5313, 5558, 5799, 6043, 6285, 6529, 6774, 7015, 7260, 7501, 7746, 7987, 8232, 8475, 8718, 8962, 9204, 9448,
                           9690, 9934, 10177, 10420, 10663, 10906, 11149, 11393, 11636, 11879, 12122, 12365, 12608, 12851, 13095, 13337, 13581, 13823, 14067, 14312, 14553, 14798, 15039, 15284, 15525, 15770, 16011, 16255, 16498, 16741]]
    hit0 = 13
    data1 = [(i) for i in [0, 1587, 1747, 1909, 2070, 2230, 2392, 2553, 2713, 2875, 3035, 3197, 3358, 3518, 3680, 3841, 4001, 4163, 4324, 4485, 4646, 4806, 4968, 5128, 5288, 5449, 5611, 5771, 5933, 6093,
                           6254, 6416, 6576, 6737, 6899, 7059, 7220, 7382, 7542, 7704, 7865, 8025, 8187, 8347, 8508, 8670, 8830, 8991, 9153, 9313, 9475, 9636, 9796, 9958, 10118, 10279, 10441, 10601, 10763, 10924, 11084]]
    hit1 = 0
    power1 = 1
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石CD缩减 = 0

    MP = [222, 2225]
    无色消耗 = 2

    形态 = ["脱手", "骑乘"]

    def 形态变更(self, 形态, char: Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "脱手":
            self.hit0 = 13
            self.hit1 = 0
        if 形态 == "骑乘":
            self.hit0 = 0
            self.hit1 = 23
            if '魔龙之息' in char.护石栏:
                self.hit1 = 25
                self.power1 = 1.07
                self.护石CD缩减 = 4

    def 等效CD(self, **argv):
        # 武器类型 输出类型 额外CDR 手搓收益 恢复
        武器类型 = argv.get('武器类型', '')
        输出类型 = argv.get('输出类型', '')
        额外CDR = argv.get('额外CDR', 1.0)
        # 手搓收益 = argv.get('手搓收益', 1.0)
        面板显示 = argv.get('面板显示', False)

        cdr = 1
        if self.手搓:
            if self.所在等级 >= 15 and self.所在等级 <= 30:
                cdr = 1 - 0.01 * self.手搓收益
            if self.所在等级 >= 35 and self.所在等级 <= 70:
                cdr = 1 - 0.02 * self.手搓收益
            if self.所在等级 >= 75 and self.所在等级 <= 100:
                cdr = 1 - 0.05 * self.手搓收益
            if self.所在等级 in [50, 85, 100]:
                cdr = 1 - 0.05 * self.手搓收益
        return round(max(self.CD * (cdr if not 面板显示 else 1) * self.CDR * 额外CDR / (self.恢复 if not 面板显示 else 1) * self.武器CD系数(武器类型, 输出类型) - self.护石CD缩减, self.CD * 0.3, 1), 1)

    def 装备护石(self):
        self.power0 *= 1.30
        self.CDR *= 0.9


class 技能14(主动技能):
    名称 = '魔龙之力'
    备注 = '(1次)'
    是否主动 = 0
    所在等级 = 48
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    data0 = [int(i*1.0) for i in [0, 935, 1084, 1233, 1383, 1532, 1681, 1830, 1979, 2128, 2278, 2427, 2576, 2725, 2874, 3023, 3172, 3322, 3471,
                                  3620, 3769, 3918, 4067, 4217, 4366, 4515, 4664, 4813, 4962, 5112, 5261, 5410, 5559, 5708, 5857, 6006, 6156, 6305, 6454, 6603, 6752]]
    hit0 = 1

    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.105 + 0.015 * self.等级, 5)


class 技能15(主动技能):
    名称 = '雷光嘶吼'
    所在等级 = 50
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [(i) for i in [0, 2998, 3692, 4389, 5083, 5779, 6473, 7169, 7863, 8560, 9255, 9950, 10645, 11340, 12037, 12731, 13427, 14121, 14818, 15511,
                           16208, 16902, 17598, 18292, 18989, 19683, 20379, 21073, 21769, 22464, 23160, 23855, 24550, 25246, 25940, 26637, 27331, 28027, 28721, 29417, 30111]]
    hit0 = 8
    data1 = [(i) for i in [0, 53306, 65667, 78029, 90388, 102750, 115111, 127473, 139833, 152195, 164556, 176917, 189277, 201639, 214000, 226360, 238722, 251083, 263444, 275804,
                           288166, 300527, 312888, 325249, 337611, 349972, 362332, 374693, 387054, 399415, 411776, 424138, 436499, 448859, 461220, 473582, 485942, 498304, 510665, 523027, 535386]]
    hit1 = 1
    CD = 145

    MP = [900, 7560]
    无色消耗 = 5

    def 等效百分比(self, **argv):
        if self.等级 > 8:
            return super().等效百分比(**argv)*1.1
        return super().等效百分比(**argv)


class 技能16(主动技能):
    名称 = '龙皇制裁'
    所在等级 = 60
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [(i) for i in [0, 27960, 30798, 33633, 36471, 39306, 42143, 44981, 47816, 50654, 53489, 56327, 59163, 61999, 64837, 67672, 70510, 73346, 76183, 79020, 81855, 84693, 87528, 90366, 93203, 96038, 98876, 101711, 104549, 107386, 110222,
                           113059, 115894, 118732, 121568, 124405, 127242, 130077, 132915, 135751, 138588, 141425, 144261, 147098, 149935, 152771, 155609, 158444, 161281, 164118, 166954, 169792, 172627, 175464, 178301, 181137, 183974, 186810, 189648, 192484, 195320]]
    hit0 = 1
    data1 = [(i) for i in [0, 4925, 5424, 5923, 6424, 6923, 7422, 7923, 8422, 8921, 9421, 9921, 10420, 10920, 11420, 11919, 12418, 12920, 13418, 13917, 14417, 14918, 15416, 15917, 16417, 16916, 17416, 17916, 18415, 18915,
                           19414, 19914, 20414, 20913, 21413, 21913, 22412, 22912, 23411, 23911, 24410, 24910, 25410, 25909, 26409, 26909, 27408, 27908, 28409, 28907, 29406, 29908, 30407, 30905, 31407, 31906, 32405, 32906, 33405, 33904, 34403]]
    hit1 = 0
    data2 = [(i) for i in [0, 3009, 3315, 3619, 3925, 4230, 4536, 4840, 5146, 5453, 5757, 6063, 6369, 6673, 6979, 7284, 7589, 7894, 8200, 8504, 8810, 9117, 9421, 9727, 10032, 10338, 10642, 10948, 11254, 11558, 11864,
                           12169, 12474, 12781, 13086, 13391, 13696, 14002, 14306, 14612, 14918, 15222, 15528, 15833, 16138, 16443, 16750, 17056, 17360, 17666, 17971, 18276, 18581, 18887, 19191, 19497, 19803, 20107, 20414, 20720, 21024]]
    hit2 = 0
    data3 = [(i) for i in [0, 3282, 3617, 3949, 4282, 4615, 4948, 5281, 5615, 5948, 6280, 6614, 6947, 7281, 7613, 7946, 8278, 8613, 8945, 9279, 9611, 9944, 10279, 10611, 10944, 11277, 11610, 11943, 12277, 12609, 12943,
                           13275, 13609, 13943, 14275, 14608, 14941, 15275, 15607, 15941, 16273, 16606, 16941, 17273, 17607, 17939, 18272, 18606, 18939, 19271, 19605, 19937, 20271, 20604, 20937, 21270, 21603, 21937, 22269, 22603, 22935]]
    hit3 = 0
    data4 = [(i) for i in [0, 5844, 6439, 7032, 7624, 8218, 8810, 9404, 9997, 10589, 11184, 11776, 12369, 12963, 13555, 14148, 14742, 15334, 15927, 16521, 17114, 17706, 18300, 18893, 19485, 20079, 20671, 21266, 21859, 22451,
                           23045, 23638, 24230, 24824, 25416, 26009, 26604, 27196, 27789, 28382, 28975, 29567, 30161, 30754, 31348, 31941, 32534, 33127, 33720, 34312, 34906, 35499, 36091, 36686, 37278, 37871, 38465, 39057, 39650, 40243, 40836]]
    hit4 = 0
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [280, 784]
    无色消耗 = 1

    形态 = ["非抓", "抓取"]

    def 形态变更(self, 形态, char: Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "非抓":
            self.hit0 = 1
            self.hit1 = 0
            self.hit2 = 0
            self.hit3 = 0
            self.hit4 = 0
            if '龙皇制裁' in char.护石栏:
                self.倍率 *= 1.32
        if 形态 == "抓取":
            self.hit0 = 0
            self.hit1 = 1
            self.hit2 = 6
            self.hit3 = 1
            self.hit4 = 1
            if '龙皇制裁' in char.护石栏:
                self.hit0 = 1
                self.hit1 = 0
                self.hit2 = 0
                self.hit3 = 0
                self.hit4 = 0
                self.倍率 *= 1.32

    def 装备护石(self):
        self.倍率 *= 1.32


class 技能17(主动技能):
    名称 = '魔龙天翔'
    所在等级 = 70
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [(i) for i in [0, 39651, 43673, 47695, 51717, 55742, 59764, 63786, 67810, 71832, 75854, 79879, 83901, 87923, 91945, 95968, 99990, 104013, 108036, 112058, 116080,
                           120104, 124126, 128148, 132170, 136193, 140216, 144238, 148261, 152283, 156305, 160330, 164352, 168374, 172396, 176420, 180443, 184465, 188489, 192511, 196533]]
    hit0 = 1
    data1 = [(i) for i in [0, 14572, 16051, 17530, 19007, 20487, 21965, 23442, 24922, 26400, 27878, 29357, 30836, 32313, 33793, 35270, 36747, 38228, 39704,
                           41182, 42663, 44139, 45618, 47097, 48574, 50053, 51533, 53010, 54488, 55968, 57445, 58923, 60403, 61880, 63359, 64838, 66316, 67794, 69274, 70751, 72229]]
    hit1 = 0
    power1 = 1
    data2 = [(i) for i in [0, 11334, 12483, 13633, 14784, 15934, 17083, 18232, 19383, 20533, 21683, 22832, 23982, 25132, 26281, 27432, 28581, 29731, 30881,
                           32031, 33180, 34331, 35481, 36632, 37781, 38930, 40081, 41230, 42381, 43530, 44680, 45830, 46980, 48130, 49279, 50429, 51578, 52730, 53879, 55029, 56178]]
    hit2 = 0
    power2 = 1
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [756, 1587]
    无色消耗 = 2

    形态 = ["脱手", "骑乘"]

    def 形态变更(self, 形态, char: Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "脱手":
            self.hit0 = 1
            self.hit1 = 0
            self.hit2 = 0
            if '魔龙天翔' in char.护石栏:
                self.power0 = 1.26
        if 形态 == "骑乘":
            self.hit0 = 0
            self.hit1 = 1
            self.hit2 = 3
            if '魔龙天翔' in char.护石栏:
                self.power1 = 1.31
                self.power2 = 1.31

    def 装备护石(self):
        pass


class 技能18(主动技能):
    名称 = '魔龙星落'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [(i) for i in [0, 5016, 5525, 6034, 6543, 7052, 7560, 8069, 8579, 9087, 9596, 10105, 10614, 11123, 11632, 12140, 12649, 13159, 13667, 14176, 14685, 15194, 15703, 16212, 16720, 17229, 17739, 18247, 18756, 19265,
                           19773, 20284, 20793, 21301, 21810, 22320, 22829, 23337, 23846, 24354, 24864, 25373, 25881, 26390, 26900, 27409, 27917, 28426, 28934, 29444, 29953, 30461, 30970, 31480, 31989, 32497, 33006, 33514, 34024, 34533, 35041]]
    hit0 = 9
    data1 = [(i) for i in [0, 30098, 33151, 36205, 39258, 42312, 45366, 48419, 51472, 54526, 57579, 60632, 63688, 66741, 69794, 72848, 75901, 78954, 82009, 85062, 88115, 91169, 94222, 97275, 100329, 103383, 106436, 109489, 112543, 115596, 118649,
                           121704, 124757, 127810, 130864, 133917, 136970, 140026, 143078, 146131, 149186, 152238, 155291, 158347, 161400, 164453, 167507, 170560, 173613, 176666, 179721, 182774, 185827, 188881, 191934, 194987, 198042, 201095, 204148, 207202, 210255]]
    hit1 = 1
    data2 = [(i) for i in [0, 3138, 3456, 3775, 4092, 4410, 4729, 5047, 5366, 5684, 6003, 6320, 6639, 6958, 7276, 7594, 7913, 8231, 8548, 8868, 9187, 9504, 9822, 10141, 10459, 10778, 11096, 11415, 11732, 12051, 12369,
                           12689, 13006, 13325, 13643, 13962, 14279, 14599, 14917, 15234, 15553, 15871, 16190, 16508, 16827, 17145, 17463, 17781, 18100, 18419, 18737, 19055, 19374, 19691, 20009, 20329, 20648, 20965, 21283, 21602, 21919]]
    hit2 = 0
    data3 = [(i) for i in [0, 7845, 8639, 9436, 10232, 11029, 11824, 12619, 13415, 14211, 15008, 15804, 16599, 17395, 18190, 18987, 19782, 20579, 21374, 22171, 22967, 23761, 24558, 25353, 26150, 26946, 27740, 28537, 29333, 30130,
                           30925, 31720, 32517, 33312, 34109, 34905, 35700, 36496, 37292, 38088, 38883, 39680, 40475, 41271, 42068, 42862, 43659, 44455, 45251, 46047, 46841, 47638, 48434, 49231, 50026, 50821, 51618, 52413, 53210, 54006, 54800]]
    hit3 = 0
    data4 = [(i) for i in [0, 23535, 25921, 28311, 30698, 33085, 35473, 37861, 40248, 42636, 45023, 47412, 49799, 52186, 54574, 56962, 59349, 61737, 64124, 66513, 68900, 71287, 73675, 76063, 78450, 80838, 83225, 85614, 88001, 90388, 92776,
                           95164, 97551, 99939, 102326, 104715, 107102, 109489, 111877, 114265, 116652, 119040, 121427, 123816, 126203, 128590, 130978, 133365, 135753, 138141, 140528, 142917, 145304, 147691, 150079, 152466, 154855, 157242, 159629, 162017, 164405]]
    hit4 = 0
    CD = 40.0
    是否有护石 = 1

    MP = [580, 4500]
    无色消耗 = 3

    形态 = ["单独", "共同"]

    def 形态变更(self, 形态, char: Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "单独":
            self.hit0 = 9
            self.hit1 = 1
            self.hit2 = 0
            self.hit3 = 0
            self.hit4 = 0

        if 形态 == "共同":
            self.hit0 = 0
            self.hit1 = 0
            self.hit2 = 15
            self.hit3 = 1
            self.hit4 = 1

    def 装备护石(self):
        self.倍率 *= 1.37


class 技能19(被动技能):
    名称 = '龙神血脉'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40
    关联技能 = ['所有']

    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.21 + 0.02 * self.等级, 5)


class 技能20(主动技能):
    名称 = '征战无双'
    所在等级 = 80
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [(i*1.0) for i in [0, 37322, 41107, 44894, 48680, 52468, 56253, 60040, 63827, 67613, 71400, 75185, 78972, 82757, 86544, 90330, 94117, 97902, 101692, 105477, 109264, 113049, 116836, 120622, 124409, 128194, 131981, 135766, 139553, 143339,
                               147127, 150913, 154699, 158485, 162272, 166057, 169844, 173630, 177416, 181203, 184989, 188777, 192562, 196349, 200135, 203922, 207707, 211494, 215279, 219066, 222852, 226639, 230424, 234211, 237996, 241785, 245570, 249357, 253143, 256929, 260715]]
    hit0 = 1
    data1 = [(i*1.0) for i in [0, 57557, 63396, 69236, 75075, 80914, 86754, 92592, 98432, 104270, 110110, 115950, 121788, 127628, 133467, 139306, 145146, 150985, 156824, 162663, 168503, 174341, 180180, 186021, 191859, 197697, 203539, 209377, 215215,
                               221056, 226895, 232733, 238574, 244412, 250251, 256092, 261930, 267768, 273610, 279448, 285286, 291126, 296966, 302804, 308644, 314483, 320322, 326161, 332001, 337839, 343679, 349517, 355357, 361197, 367035, 372875, 378715, 384553, 390393, 396232, 402071]]
    hit1 = 1
    power1 = 1
    data2 = [(i*1.0) for i in [0, 2878, 3169, 3461, 3753, 4046, 4336, 4629, 4921, 5212, 5506, 5796, 6089, 6381, 6672, 6965, 7256, 7549, 7841, 8132, 8425, 8716, 9008, 9301, 9592, 9884, 10176, 10468, 10759, 11053,
                               11344, 11635, 11928, 12219, 12513, 12804, 13095, 13388, 13679, 13971, 14264, 14556, 14848, 15139, 15431, 15724, 16016, 16307, 16599, 16891, 17182, 17476, 17767, 18060, 18351, 18642, 18936, 19227, 19519, 19811, 20102]]
    hit2 = 0
    power2 = 1
    CD = 50.0
    是否有护石 = 1

    MP = [800, 6000]
    无色消耗 = 5

    形态 = ["单独", "骑乘", "延长"]

    def 形态变更(self, 形态, char: Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "单独":
            self.hit0 = 1
            self.hit1 = 1
            self.hit2 = 0
            if '征战无双' in char.护石栏:
                self.power0 = 1.16
                self.power1 = 1.16*1.23
        if 形态 == "延长" and '征战无双' in char.护石栏:
            self.hit0 = 0
            self.hit1 = 1
            self.power1 = 1.16*0.9
            self.hit2 = 28
            self.power2 = 1.16
        else:
            形态 = "骑乘"
        if 形态 == "骑乘":
            self.hit0 = 0
            self.hit1 = 1
            self.hit2 = 20
            if '征战无双' in char.护石栏:
                self.power1 = 1.16*1.28
                self.power2 = 1.16

    def 装备护石(self):
        self.power0 = 1.16
        self.power1 = 1.16*1.23
        self.CDR *= 0.9


class 技能21(主动技能):
    名称 = '龙神裁决：终末之光'
    所在等级 = 85
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [(i) for i in [0, 211084, 260033, 308979, 357928, 406876, 455822, 504771, 553717, 602664, 651613, 700559, 749507, 798454, 847402, 896348, 945297, 994244, 1043190, 1092139, 1141085, 1190034, 1238982, 1287928, 1336877, 1385823, 1434770, 1483719, 1532665, 1581613, 1630560, 1679508, 1728455, 1777403, 1826350, 1875297,
                           1924245, 1973193, 2022139, 2071088, 2120034, 2168983, 2217930, 2266877, 2315825, 2364772, 2413719, 2462668, 2511614, 2560561, 2609509, 2658456, 2707403, 2756351, 2805299, 2854245, 2903194, 2952140, 3001089, 3050036, 3098983, 3147931, 3196878, 3245825, 3294774, 3343720, 3392668, 3441615, 3490563, 3539510, 3588458]]
    hit0 = 1
    CD = 180

    MP = [2500, 5000]
    无色消耗 = 10


class 技能22(主动技能):
    名称 = '龙哮雷鸣'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i) for i in [0, 13151, 14486, 15821, 17155, 18489, 19823, 21158, 22492, 23826, 25160, 26494, 27830, 29164, 30498, 31832, 33166, 34500, 35835, 37169, 38503, 39837, 41171, 42507, 43841, 45175, 46509, 47843, 49178,
                              50512, 51846, 53181, 54515, 55849, 57184, 58518, 59852, 61186, 62520, 63856, 65190, 66524, 67858, 69192, 70527, 71861, 73195, 74529, 75863, 77197, 78533, 79867, 81201, 82535, 83869, 85204, 86538, 87872, 89207, 90541, 91876]]
    hit0 = 5
    data1 = [int(i) for i in [0, 98642, 108649, 118657, 128664, 138672, 148678, 158685, 168693, 178700, 188708, 198714, 208721, 218729, 228736, 238744, 248751, 258757, 268765, 278772, 288780, 298787, 308793, 318801, 328808, 338816, 348823, 358830, 368838, 378844,
                              388852, 398859, 408866, 418874, 428880, 438888, 448895, 458903, 468910, 478917, 488925, 498931, 508939, 518946, 528953, 538961, 548967, 558975, 568982, 578989, 588997, 599004, 609011, 619018, 629025, 639033, 649040, 659048, 669054, 679061, 689069]]
    hit1 = 1
    CD = 60.0

    MP = [960, 7200]
    无色消耗 = 7


class 技能23(被动技能):
    名称 = '龙血誓约'
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
    名称 = '龙神君临·虚空烬灭'
    所在等级 = 100
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i) for i in [0, 54238, 66816, 79394, 91970, 104548, 117125, 129703, 142278, 154856, 167433, 180010, 192588, 205165, 217743, 230319, 242897, 255474, 268052, 280627, 293205, 305784, 318360, 330937, 343514, 356092, 368669, 381246, 393823, 406401, 418979, 431554, 444133, 456709, 469287,
                              481863, 494441, 507018, 519596, 532173, 544750, 557328, 569903, 582481, 595058, 607636, 620212, 632790, 645368, 657945, 670522, 683099, 695677, 708254, 720830, 733407, 745985, 758563, 771139, 783717, 796294, 808872, 821448, 834026, 846603, 859181, 871758, 884334, 896912, 909489, 922066]]
    hit0 = 1
    data1 = [int(i) for i in [0, 27120, 33407, 39696, 45986, 52273, 58561, 64851, 71139, 77427, 83716, 90005, 96294, 102582, 108871, 115160, 121448, 127736, 134026, 140314, 146603, 152892, 159180, 165469, 171756, 178045, 184334, 190622, 196911, 203200, 209488, 215777, 222066, 228354, 234643,
                              240931, 247221, 253509, 259797, 266087, 272375, 278663, 284952, 291241, 297529, 303818, 310105, 316396, 322683, 328971, 335262, 341549, 347837, 354126, 360415, 366704, 372992, 379281, 385570, 391858, 398146, 404436, 410724, 417013, 423301, 429590, 435879, 442167, 448456, 454745, 461032]]
    hit1 = 8
    data2 = [int(i) for i in [0, 162717, 200448, 238181, 275912, 313644, 351375, 389107, 426839, 464571, 502301, 540033, 577766, 615496, 653228, 690960, 728692, 766424, 804155, 841886, 879619, 917351, 955081, 992813, 1030545, 1068276, 1106008, 1143740, 1181470, 1219203, 1256935, 1294666, 1332398, 1370129, 1407861, 1445593,
                              1483325, 1521055, 1558788, 1596520, 1634250, 1671982, 1709715, 1747446, 1785177, 1822909, 1860640, 1898373, 1936104, 1973835, 2011567, 2049300, 2087030, 2124762, 2162494, 2200224, 2237957, 2275689, 2313420, 2351151, 2388884, 2426615, 2464347, 2502078, 2539809, 2577542, 2615274, 2653004, 2690736, 2728469, 2766201]]
    hit2 = 1
    data3 = [int(i) for i in [0, 27120, 33407, 39696, 45986, 52273, 58561, 64851, 71139, 77427, 83716, 90005, 96294, 102582, 108871, 115160, 121448, 127736, 134026, 140314, 146603, 152892, 159180, 165469, 171756, 178045, 184334, 190622, 196911, 203200, 209488, 215777, 222066, 228354, 234643,
                              240931, 247221, 253509, 259797, 266087, 272375, 278663, 284952, 291241, 297529, 303818, 310105, 316396, 322683, 328971, 335262, 341549, 347837, 354126, 360415, 366704, 372992, 379281, 385570, 391858, 398146, 404436, 410724, 417013, 423301, 429590, 435879, 442167, 448456, 454745, 461032]]
    hit3 = 4
    CD = 290.0

    MP = [4027, 8055]
    无色消耗 = 15


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'dragon_knight'
        self.名称 = '皓曦·龙骑士'
        self.角色 = '守护者'
        self.角色类型 = '输出'
        self.职业 = '龙骑士'
        # 用来筛CP武器的
        self.转职 = '龙骑士'
        self.武器选项 = ['太刀', '钝器', '巨剑', '短剑']
        self.输出类型选项 = ['物理固伤']
        self.防具精通属性 = ['力量']
        self.类型 = '物理固伤'
        self.武器类型 = '太刀'
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
        self.buff = 1.850

        super().__init__()
