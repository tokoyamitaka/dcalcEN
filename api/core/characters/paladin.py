from core.baseClass.skill import 技能
from core.baseClass.character import Character
from core.baseClass.skill import 主动技能, 被动技能


class 技能0(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    等级精通 = 110
    关联技能 = ['基本攻击']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)


class 技能1(主动技能):
    名称 = '神光冲击'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [30, 300]
    data0 = [(i*1.073) for i in [0, 2450, 2698, 2947, 3195, 3444, 3692, 3941, 4189, 4438, 4686, 4935, 5183, 5433, 5681, 5930, 6178, 6426, 6675, 6923, 7172, 7420, 7669, 7917, 8166, 8415, 8664, 8912, 9161, 9409, 9658,
                                 9906, 10155, 10403, 10651, 10900, 11148, 11398, 11646, 11895, 12143, 12392, 12640, 12889, 13137, 13386, 13634, 13883, 14131, 14380, 14629, 14878, 15126, 15374, 15623, 15871, 16120, 16368, 16617, 16865, 17114]]
    hit0 = 1
    CD = 4
    TP成长 = 0.10
    TP上限 = 7


class 技能2(主动技能):
    名称 = '神光连斩'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [30, 300]
    # 第1击攻击力：<data0>%
    data0 = [(i*1.073) for i in [0, 1618, 1783, 1946, 2110, 2275, 2439, 2603, 2768, 2932, 3097, 3260, 3424, 3589, 3753, 3917, 4082, 4246, 4409, 4574, 4738, 4902, 5067, 5231, 5395, 5560, 5723, 5887, 6052, 6216, 6381, 6545, 6709, 6873, 7037,
                                 7201, 7366, 7530, 7694, 7859, 8022, 8186, 8351, 8515, 8679, 8844, 9008, 9172, 9336, 9500, 9665, 9829, 9993, 10158, 10322, 10485, 10650, 10814, 10978, 11143, 11307, 11471, 11636, 11799, 11963, 12128, 12292, 12456, 12621, 12785, 12949]]
    hit0 = 1
    # 第2击攻击力：<data1>%
    data1 = [(i*1.073) for i in [0, 1618, 1783, 1946, 2110, 2275, 2439, 2603, 2768, 2932, 3097, 3260, 3424, 3589, 3753, 3917, 4082, 4246, 4409, 4574, 4738, 4902, 5067, 5231, 5395, 5560, 5723, 5887, 6052, 6216, 6381, 6545, 6709, 6873, 7037,
                                 7201, 7366, 7530, 7694, 7859, 8022, 8186, 8351, 8515, 8679, 8844, 9008, 9172, 9336, 9500, 9665, 9829, 9993, 10158, 10322, 10485, 10650, 10814, 10978, 11143, 11307, 11471, 11636, 11799, 11963, 12128, 12292, 12456, 12621, 12785, 12949]]
    hit1 = 1
    CD = 5
    TP成长 = 0.10
    TP上限 = 7


class 技能3(被动技能):
    名称 = '天使光翼'
    所在等级 = 15
    等级上限 = 20
    学习间隔 = 2
    等级精通 = 10
    冷却关联技能 = ['所有']
    非冷却关联技能 = ['信仰聚合：神光惩戒', '神圣意志：大天使降临', '启示录：末日救赎']

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 <= 10:
            return round(1.00 + 0.01 * self.等级, 5)
        else:
            return round(0.90 + 0.02 * self.等级, 5)

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 0.95


class 技能4(被动技能):
    名称 = '天使降临'
    所在等级 = 15
    等级上限 = 20
    学习间隔 = 2
    等级精通 = 10

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 <= 10:
            return round(1.08 + 0.01 * self.等级, 5)
        else:
            return round(0.98 + 0.02 * self.等级, 5)


class 技能5(主动技能):
    名称 = '圣盾突击'
    所在等级 = 20
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [40, 400]
    # 攻击力：<data0>% X 4
    data0 = [(i*1.073) for i in [0, 1059, 1166, 1274, 1381, 1489, 1596, 1703, 1811, 1918, 2026, 2133, 2241, 2348, 2455, 2563, 2670, 2778, 2885, 2992, 3100, 3207, 3315, 3422, 3530, 3637, 3744, 3852, 3959,
                                 4067, 4174, 4281, 4390, 4497, 4605, 4712, 4820, 4927, 5034, 5142, 5249, 5357, 5464, 5571, 5679, 5786, 5894, 6001, 6109, 6216, 6323, 6431, 6538, 6646, 6753, 6860, 6968, 7075, 7183, 7290, 7398]]
    攻击次数 = 4
    CD = 6
    TP成长 = 0.10
    TP上限 = 7


class 技能6(主动技能):
    名称 = '神光喷涌'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [50, 500]
    # 锤击攻击力：<data0>%
    data0 = [(i*1.1) for i in [0, 1262, 1390, 1518, 1646, 1774, 1902, 2030, 2158, 2286, 2414, 2542, 2670, 2798, 2926, 3054, 3182, 3310, 3438, 3566, 3694, 3822, 3950, 4079, 4208, 4336, 4464, 4592, 4720, 4848, 4976, 5104, 5232, 5360,
                               5488, 5616, 5744, 5872, 6000, 6128, 6256, 6384, 6512, 6640, 6768, 6896, 7024, 7152, 7280, 7408, 7536, 7664, 7792, 7921, 8049, 8177, 8305, 8433, 8561, 8689, 8817, 8945, 9074, 9202, 9330, 9458, 9586, 9714, 9842, 9970, 10098]]
    hit0 = 1
    # 喷涌的神光攻击力：<data1>% X 4
    data1 = [(i*1.1) for i in [0, 1262, 1390, 1518, 1646, 1774, 1902, 2030, 2158, 2286, 2414, 2542, 2670, 2798, 2926, 3054, 3182, 3310, 3438, 3566, 3694, 3822, 3950, 4079, 4208, 4336, 4464, 4592, 4720, 4848, 4976, 5104, 5232, 5360,
                               5488, 5616, 5744, 5872, 6000, 6128, 6256, 6384, 6512, 6640, 6768, 6896, 7024, 7152, 7280, 7408, 7536, 7664, 7792, 7921, 8049, 8177, 8305, 8433, 8561, 8689, 8817, 8945, 9074, 9202, 9330, 9458, 9586, 9714, 9842, 9970, 10098]]
    hit1 = 4
    CD = 8
    TP成长 = 0.10
    TP上限 = 7

    def 小型喷涌神光攻击力(self):
        return int(self.data1[self.等级] * (1 + self.TP成长 * self.TP等级)*0.1 * self.倍率)


class 技能7(主动技能):
    名称 = '神光盾击'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [60, 600]
    # 第1击攻击力：<data0>% X 3
    data0 = [(i*1.1) for i in [0, 1239, 1365, 1491, 1616, 1741, 1867, 1993, 2119, 2245, 2371, 2497, 2622, 2747, 2873, 2999, 3125, 3251, 3377, 3502, 3628, 3754, 3879, 4005, 4131, 4256, 4382, 4508, 4634,
                               4760, 4885, 5011, 5136, 5262, 5388, 5514, 5640, 5766, 5892, 6016, 6142, 6268, 6394, 6520, 6646, 6771, 6897, 7023, 7148, 7274, 7400, 7526, 7651, 7777, 7903, 8029, 8155, 8280, 8405, 8531, 8657]]
    hit0 = 3
    # 第2击攻击力：<data1>% X 3
    data1 = [(i*1.1) for i in [0, 1271, 1400, 1529, 1658, 1787, 1915, 2044, 2173, 2302, 2431, 2561, 2690, 2818, 2947, 3076, 3205, 3334, 3463, 3592, 3720, 3850, 3979, 4108, 4237, 4366, 4495, 4623, 4752,
                               4881, 5011, 5140, 5269, 5398, 5526, 5655, 5784, 5913, 6042, 6171, 6301, 6429, 6558, 6687, 6816, 6945, 7074, 7203, 7331, 7460, 7590, 7719, 7848, 7977, 8106, 8234, 8363, 8492, 8621, 8751, 8880]]
    hit1 = 3
    CD = 8
    TP成长 = 0.10
    TP上限 = 7


class 技能8(主动技能):
    名称 = '烈光'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [60, 600]
    # 上挑攻击力：<data0>%
    data0 = [(i*1.071) for i in [0, 3800, 4186, 4571, 4957, 5343, 5728, 6114, 6499, 6885, 7271, 7656, 8042, 8427, 8812, 9199, 9584, 9970, 10355, 10740, 11127, 11512, 11897, 12283, 12668, 13055, 13440, 13825, 14211, 14597, 14982,
                                 15368, 15753, 16139, 16525, 16910, 17296, 17681, 18066, 18453, 18838, 19224, 19609, 19994, 20381, 20766, 21151, 21537, 21922, 22309, 22694, 23079, 23465, 23850, 24236, 24622, 25007, 25393, 25779, 26164, 26550, 26935]]
    hit0 = 1
    # 下砸攻击力：<data1>%
    data1 = [(i*1.071) for i in [0, 3812, 4199, 4585, 4971, 5359, 5745, 6132, 6519, 6906, 7292, 7680, 8066, 8453, 8839, 9226, 9613, 9999, 10387, 10773, 11160, 11547, 11934, 12320, 12708, 13094, 13480, 13867, 14254, 14641, 15027,
                                 15415, 15801, 16188, 16574, 16962, 17348, 17734, 18122, 18508, 18895, 19282, 19669, 20055, 20442, 20829, 21216, 21602, 21989, 22376, 22762, 23150, 23536, 23923, 24309, 24697, 25083, 25469, 25857, 26243, 26630, 27017]]
    hit1 = 1
    CD = 8
    TP成长 = 0.10
    TP上限 = 7


class 技能9(主动技能):
    名称 = '神光闪耀'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    # 多段攻击力：<data0>% X 10
    data0 = [(i*1.07) for i in [0, 921, 1014, 1108, 1201, 1295, 1389, 1482, 1575, 1669, 1762, 1856, 1950, 2043, 2136, 2230, 2323, 2417, 2511, 2604, 2697, 2791, 2885, 2978, 3072, 3165, 3258, 3352, 3446, 3539, 3633, 3726, 3819, 3913,
                                4007, 4100, 4194, 4287, 4380, 4473, 4568, 4661, 4754, 4848, 4941, 5034, 5129, 5222, 5315, 5409, 5502, 5595, 5690, 5783, 5876, 5970, 6063, 6157, 6251, 6344, 6437, 6531, 6624, 6718, 6812, 6905, 6998, 7092, 7185, 7279, 7373]]
    hit0 = 10
    # 最后一击攻击力：<data1>%
    data1 = [(i*1.07) for i in [0, 3949, 4350, 4750, 5152, 5552, 5952, 6354, 6754, 7154, 7556, 7956, 8357, 8758, 9158, 9559, 9959, 10361, 10761, 11161, 11563, 11963, 12364, 12765, 13165, 13566, 13967, 14368, 14768, 15168, 15570, 15970, 16370, 16772, 17172,
                                17573, 17974, 18374, 18775, 19176, 19577, 19977, 20377, 20779, 21179, 21580, 21981, 22381, 22782, 23183, 23584, 23984, 24385, 24786, 25186, 25586, 25988, 26388, 26789, 27190, 27590, 27991, 28392, 28793, 29193, 29594, 29995, 30395, 30796, 31197, 31597]]
    hit1 = 1
    CD = 16
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    技能施放时间 = 2

    MP = [70, 700]
    无色消耗 = 1

    def 装备护石(self):
        self.倍率 *= 1.33


class 技能10(主动技能):
    名称 = '神光闪影击'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [(i*1.072) for i in [0, 722, 794, 868, 941, 1014, 1087, 1161, 1234, 1307, 1380, 1454, 1527, 1600, 1673, 1747, 1820, 1893, 1966, 2040, 2112, 2186, 2259, 2333, 2405, 2479, 2552, 2626, 2698,
                                 2772, 2845, 2919, 2991, 3065, 3138, 3212, 3285, 3358, 3432, 3505, 3578, 3651, 3725, 3798, 3871, 3944, 4018, 4090, 4164, 4237, 4311, 4383, 4457, 4530, 4604, 4676, 4750, 4823, 4897, 4969, 5043]]
    hit0 = 15
    data1 = [(i*1.072) for i in [0, 4803, 5290, 5778, 6265, 6752, 7239, 7726, 8215, 8702, 9189, 9676, 10163, 10650, 11138, 11626, 12113, 12600, 13087, 13574, 14062, 14549, 15036, 15524, 16011, 16499, 16986, 17473, 17960, 18447,
                                 18935, 19423, 19910, 20397, 20884, 21371, 21858, 22346, 22834, 23321, 23808, 24295, 24782, 25270, 25757, 26244, 26732, 27219, 27707, 28194, 28681, 29168, 29655, 30143, 30631, 31118, 31605, 32092, 32579, 33066, 33554]]
    hit1 = 1
    CD = 20
    TP成长 = 0.10
    TP上限 = 5

    MP = [70, 700]
    无色消耗 = 1


class 技能11(主动技能):
    名称 = '神罚之锤'
    所在等级 = 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [(i*1.071) for i in [0, 17447, 19216, 20986, 22757, 24526, 26296, 28067, 29836, 31606, 33377, 35146, 36916, 38687, 40456, 42226, 43996, 45766, 47536, 49306, 51076, 52846, 54616, 56386, 58156, 59926, 61696, 63466, 65236, 67006,
                                 68776, 70546, 72316, 74086, 75856, 77626, 79396, 81166, 82936, 84706, 86476, 88246, 90016, 91786, 93555, 95326, 97096, 98865, 100636, 102406, 104175, 105946, 107716, 109485, 111256, 113026, 114795, 116566, 118336, 120105, 121876]]
    hit0 = 1
    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [80, 800]
    无色消耗 = 1

    def 装备护石(self):
        self.倍率 *= 1.36


class 技能12(主动技能):
    名称 = '神光之跃'
    所在等级 = 45
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [(i*1.073) for i in [0, 29375, 32356, 35336, 38316, 41296, 44277, 47256, 50237, 53217, 56196, 59177, 62157, 65138, 68117, 71098, 74078, 77058, 80038, 83019, 85998, 88979, 91959, 94939, 97919, 100900, 103880, 106859, 109840, 112820, 115800,
                                 118780, 121761, 124740, 127721, 130701, 133682, 136661, 139642, 142622, 145602, 148582, 151563, 154543, 157522, 160503, 163483, 166463, 169443, 172424, 175403, 178384, 181364, 184344, 187324, 190305, 193285, 196265, 199245, 202226, 205205]]
    hit0 = 1
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [90, 900]
    无色消耗 = 2

    def 装备护石(self):
        self.倍率 *= 1.32


class 技能13(被动技能):
    名称 = '荣耀之光'
    所在等级 = 48
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.105 + 0.015 * self.等级, 5)


class 技能14(主动技能):
    名称 = '信仰聚合：神光惩戒'
    所在等级 = 50
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [(i*1.06) for i in [0, 82965, 102203, 121441, 140679, 159917, 179155, 198393, 217631, 236870, 256108, 275346, 294584, 313822, 333060, 352298, 371537, 390775, 410013,
                                429251, 448489, 467727, 486965, 506203, 525442, 544680, 563918, 583156, 602394, 621632, 640870, 660109, 679347, 698585, 717823, 737061, 756299, 775537, 794776, 814014, 833252]]
    hit0 = 1
    CD = 145.0

    MP = [300, 3000]
    无色消耗 = 5


class 技能15(主动技能):
    名称 = '圣盾裁决'
    所在等级 = 60
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [(i*1.07) for i in [0, 22818, 25132, 27447, 29762, 32077, 34392, 36707, 39022, 41336, 43652, 45966, 48281, 50596, 52911, 55225, 57541, 59855, 62171, 64485,
                                66800, 69115, 71430, 73744, 76060, 78374, 80689, 83004, 85319, 87633, 89949, 92264, 94578, 96894, 99208, 101523, 103838, 106153, 108467, 110783, 113097]]
    hit0 = 1
    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [120, 1200]
    无色消耗 = 1

    def 装备护石(self):
        self.倍率 *= 1.33
        self.CDR *= 0.90


class 技能16(主动技能):
    名称 = '破晓之光'
    所在等级 = 70
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [(i*1.072) for i in [0, 44586, 49109, 53633, 58156, 62679, 67203, 71726, 76249, 80773, 85295, 89818, 94342, 98865, 103389, 107912, 112435, 116959, 121482, 126005,
                                 130529, 135052, 139575, 144098, 148621, 153144, 157668, 162191, 166715, 171238, 175761, 180285, 184808, 189331, 193855, 198378, 202900, 207424, 211947, 216471, 220994]]
    hit0 = 1
    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [140, 1400]
    无色消耗 = 2

    def 装备护石(self):
        self.倍率 *= 1.19
        self.CDR *= 0.90


class 技能17(主动技能):
    名称 = '神光回旋斩'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [(i*1.071) for i in [0, 67929, 74821, 81711, 88603, 95494, 102386, 109277, 116169, 123060, 129952, 136842, 143734, 150625, 157517, 164408, 171300, 178192, 185083, 191974,
                                 198865, 205757, 212648, 219540, 226431, 233323, 240214, 247105, 253996, 260888, 267779, 274671, 281562, 288454, 295345, 302237, 309127, 316019, 322910, 329802, 336693]]
    hit0 = 1
    CD = 40
    是否有护石 = 1

    MP = [450, 4500]
    无色消耗 = 5

    def 装备护石(self):
        self.倍率 *= 0.2*1.14*6


class 技能18(被动技能):
    名称 = '戒律'
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


class 技能19(主动技能):
    名称 = '神圣信约'
    所在等级 = 80
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [(i*1.071) for i in [0, 6994, 7704, 8413, 9123, 9832, 10542, 11251, 11961, 12671, 13380, 14090, 14799, 15509, 16219, 16928, 17638, 18347, 19057,
                                 19767, 20476, 21186, 21895, 22605, 23314, 24024, 24734, 25443, 26153, 26862, 27572, 28282, 28991, 29701, 30410, 31120, 31830, 32539, 33249, 33958, 34668]]
    hit0 = 11
    CD = 45
    是否有护石 = 1

    MP = [500, 5000]
    无色消耗 = 5

    形态 = ["蓄力", "非蓄"]

    def 装备护石(self):
        pass

    # 抄的刃影75写法，不知道最后还需不需要再覆盖
    def 形态变更(self, 形态, char: Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "非蓄" and '神圣信约' in char.护石栏:
            self.power0 = 1.32
        else:
            形态 = "蓄力"
        if 形态 == "蓄力":
            self.hit0 = 11
            if '神圣信约' in char.护石栏:
                self.hit0 = 1
                self.power0 = (11+0.23)*1.32


class 技能20(主动技能):
    名称 = '神圣意志：大天使降临'
    所在等级 = 85
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [(i*1.06) for i in [0, 191057, 235359, 279663, 323966, 368269, 412572, 456875, 501178, 545482, 589784, 634087, 678391, 722694, 766996, 811300, 855603, 899906, 944209, 988512, 1032815,
                                1077119, 1121421, 1165724, 1210028, 1254331, 1298633, 1342937, 1387240, 1431542, 1475846, 1520149, 1564452, 1608756, 1653058, 1697361, 1741665, 1785968, 1830271, 1874574, 1918877]]
    hit0 = 1
    CD = 180

    MP = [2000, 5000]
    无色消耗 = 10


class 技能21(被动技能):
    名称 = '超越之翼'
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


class 技能22(主动技能):
    名称 = '神光耀世'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.072) for i in [0, 13070, 14396, 15722, 17048, 18373, 19699, 21025, 22351, 23677, 25003, 26329, 27654, 28980, 30306, 31633, 32959, 34285, 35611,
                                    36937, 38263, 39588, 40914, 42240, 43566, 44892, 46218, 47544, 48869, 50195, 51522, 52848, 54174, 55500, 56826, 58152, 59478, 60803, 62129, 63455, 64781]]
    hit0 = 4
    data1 = [int(i*1.072) for i in [0, 17426, 19194, 20962, 22730, 24498, 26266, 28033, 29802, 31569, 33338, 35105, 36874, 38641, 40409, 42177, 43945, 45713, 47481,
                                    49249, 51017, 52784, 54553, 56320, 58089, 59856, 61625, 63392, 65160, 66928, 68696, 70464, 72232, 73999, 75768, 77535, 79304, 81071, 82840, 84607, 86375]]
    hit1 = 1
    data2 = [int(i*1.072) for i in [0, 17426, 19194, 20962, 22730, 24498, 26266, 28033, 29802, 31569, 33338, 35105, 36874, 38641, 40409, 42177, 43945, 45713, 47481,
                                    49249, 51017, 52784, 54553, 56320, 58089, 59856, 61625, 63392, 65160, 66928, 68696, 70464, 72232, 73999, 75768, 77535, 79304, 81071, 82840, 84607, 86375]]
    hit2 = 6
    CD = 60

    MP = [960, 7200]
    无色消耗 = 7


class 技能23(主动技能):
    名称 = '启示录：末日救赎'
    所在等级 = 100
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i*1.061) for i in [0, 49870, 61435, 72999, 84563, 96127, 107692, 119256, 130820, 142385, 153948, 165512, 177076, 188641, 200205, 211769, 223333, 234898, 246462,
                                    258026, 269591, 281155, 292719, 304283, 315848, 327412, 338976, 350540, 362105, 373669, 385233, 396798, 408361, 419925, 431489, 443054, 454618, 466182, 477746, 489311, 500875]]
    hit0 = 1
    data1 = [int(i*1.061) for i in [0, 14248, 17552, 20856, 24161, 27465, 30768, 34072, 37377, 40681, 43985, 47289, 50592, 53897, 57201, 60505, 63809, 67114, 70418, 73721,
                                    77025, 80329, 83634, 86938, 90242, 93545, 96850, 100154, 103458, 106762, 110066, 113371, 116674, 119978, 123282, 126587, 129891, 133195, 136498, 139802, 143107]]
    hit1 = 7
    data2 = [int(i*1.061) for i in [0, 199483, 245739, 291996, 338253, 384510, 430767, 477024, 523280, 569538, 615795, 662052, 708309, 754565, 800822, 847079, 893336, 939593, 985849, 1032107,
                                    1078364, 1124621, 1170878, 1217135, 1263391, 1309648, 1355905, 1402162, 1448419, 1494676, 1540933, 1587190, 1633447, 1679704, 1725960, 1772217, 1818474, 1864731, 1910988, 1957246, 2003502]]
    hit2 = 1
    data3 = [int(i*1.061) for i in [0, 21372, 26329, 31285, 36241, 41197, 46153, 51109, 56065, 61021, 65978, 70934, 75889, 80846, 85802, 90758, 95714, 100671, 105626, 110582,
                                    115538, 120495, 125451, 130407, 135362, 140319, 145275, 150231, 155188, 160144, 165099, 170055, 175012, 179968, 184924, 189880, 194836, 199792, 204748, 209704, 214661]]
    hit3 = 7
    CD = 290.0

    MP = [4025, 8055]
    无色消耗 = 15


class 技能24(主动技能):
    名称 = '基本攻击'
    备注 = '一轮'
    是否主动 = 0
    关联技能 = ['无']
    所在等级 = 1
    等级上限 = 1
    等级精通 = 1
    学习间隔 = 1
    CD = 1  # 也没有CD，不知道为什么原来有
    #163.0%+182.0%+446.0% 三段平x
    data0 = [0, 163.0+182.0+446.0]
    hit0 = 1
    TP成长 = 0.10
    TP上限 = 5
    # 以下部分是原有的
    # 三觉后平x组成为3段平x(三觉前4段总伤害不变)+最后一击的小型神光喷涌；小型神光喷涌的单段伤害是神光喷涌单段的10%；共5段
    hit1 = 5
    data0 = [0, 0]

    def 等效百分比(self, **argv):
        char: Character = argv.get('char', {})
        self.data1 = [0, char.get_skill_by_name(
            "神光喷涌").小型喷涌神光攻击力()/char.get_skill_by_name("基础精通").加成倍率('')]
        return super().等效百分比(**argv)


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'paladin'
        self.名称 = '皓曦·帕拉丁'
        self.角色 = '守护者'
        self.角色类型 = '输出'
        self.职业 = '帕拉丁'
        self.武器选项 = ['钝器']
        self.输出类型选项 = ['物理百分比']
        self.防具精通属性 = ['力量']
        self.类型 = '物理百分比'
        self.武器类型 = '钝器'
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
        self.buff = 1.89

        super().__init__()
