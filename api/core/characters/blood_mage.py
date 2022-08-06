from core.baseClass.skill import 技能
from core.baseClass.character import Character
from core.baseClass.skill import 主动技能, 被动技能


class 技能0(主动技能):
    名称 = '血蝠之袭'
    所在等级= 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [24, 240]
    data0 = [ int(i) for i in [0, 272, 299, 328, 355, 383, 410, 438, 465, 494, 521, 549, 576, 604, 631, 660, 687, 715, 742, 770, 797, 826, 853, 881, 908, 936, 963, 992, 1019, 1047, 1074, 1102, 1129, 1158, 1185, 1213, 1240, 1268, 1295, 1324, 1351, 1379, 1406, 1434, 1461, 1490, 1517, 1545, 1572, 1600, 1628, 1656, 1683, 1711, 1738, 1766, 1794, 1822, 1849, 1877, 1904, 1932, 1960, 1988, 2015, 2043, 2070, 2098, 2126, 2154, 2181]]
    hit0 = 15
    CD = 5
    TP成长 = 0.10
    TP上限 = 7

class 技能1(主动技能):
    名称 = '血翼突击'
    所在等级= 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [0, 0]
    data0 = [ int(i) for i in [0, 3356, 3696, 4036, 4377, 4718, 5057, 5398, 5739, 6079, 6420, 6760, 7100, 7441, 7782, 8122, 8462, 8803, 9143, 9484, 9824, 10164, 10505, 10846, 11186, 11526, 11867, 12207, 12548, 12889, 13228, 13569, 13910, 14250, 14591, 14931, 15271, 15612, 15953, 16292, 16633, 16974, 17314, 17655, 17995, 18335, 18676, 19017, 19357, 19697, 20038, 20378, 20719, 21059, 21399, 21740, 22081, 22422, 22761, 23102, 23443, 23783, 24124, 24463, 24804, 25145, 25486, 25825, 26166, 26507, 26847]]
    hit0 = 1
    CD = 5
    TP成长 = 0.10
    TP上限 = 7


class 技能2(被动技能):
    名称 = '鲜血融合'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    
    def 物理攻击力倍率进图(self, 武器类型):
        if self.等级<= 10:
            return round(1.00 + 0.01 * self.等级, 5)
        else:
            return round(0.90 + 0.02 *self.等级 , 5)


class 技能3(主动技能):
    名称 = '鲜血长枪'
    所在等级= 20
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [0, 0]
    data0 = [ int(i) for i in [0, 2157, 2375, 2594, 2813, 3031, 3251, 3470, 3688, 3907, 4126, 4344, 4564, 4783, 5002, 5220, 5439, 5658, 5876, 6096, 6315, 6533, 6752, 6971, 7189, 7408, 7628, 7846, 8065, 8284, 8503, 8721, 8940, 9160, 9378, 9597, 9816, 10034, 10253, 10472, 10691, 10910, 11129, 11347, 11566, 11785, 12004, 12223, 12442, 12661, 12879, 13098, 13317, 13535, 13755, 13974, 14192, 14411, 14630, 14848, 15067, 15287, 15506, 15724, 15943, 16162, 16380, 16599, 16819, 17037, 17256]]
    hit0 = 2
    CD = 6
    TP成长 = 0.10
    TP上限 = 7


class 技能4(被动技能):
    名称 = '血之共鸣'
    所在等级 = 20
    等级上限 = 11
    基础等级 = 1
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.08 + 0.02 * self.等级, 5)


class 技能5(主动技能):
    名称 = '血蝠之舞'
    所在等级 =25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [80, 800]
    data0 = [ int(i) for i in [0, 173, 190, 207, 225, 242, 259, 278, 295, 312, 330, 347, 365, 382, 400, 418, 435, 452, 470, 487, 505, 523, 540, 558, 575, 592, 610, 628, 646, 663, 680, 698, 715, 732, 751, 768, 786, 803, 820, 838, 855, 873, 891, 908, 926, 943, 960, 978, 996, 1013, 1031, 1048, 1065, 1083, 1101, 1119, 1136, 1153, 1171, 1188, 1205, 1224, 1241, 1259, 1276, 1293, 1311, 1328, 1346, 1364, 1381]]
    hit0 = 29 #原作者段数为30
    CD = 6
    TP成长 = 0.10
    TP上限 = 7


class 技能6(主动技能):
    名称 = '血腥狩猎'
    所在等级 =25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [0, 0]
    data0 = [ int(i) for i in [0, 1125, 1239, 1354, 1468, 1582, 1696, 1811, 1925, 2039, 2153, 2268, 2382, 2496, 2609, 2724, 2838, 2952, 3066, 3181, 3295, 3409, 3523, 3638, 3752, 3866, 3981, 4095, 4209, 4323, 4438, 4552, 4666, 4779, 4894, 5008, 5122, 5236, 5351, 5465, 5579, 5693, 5808, 5922, 6036, 6150, 6265, 6379, 6493, 6607, 6722, 6836, 6949, 7064, 7178, 7292, 7406, 7521, 7635, 7749, 7863, 7978, 8092, 8206, 8320, 8435, 8549, 8663, 8777, 8892, 9006]]
    hit0 = 5
    CD = 8
    TP成长 = 0.10
    TP上限 = 7


class 技能7(主动技能):
    名称 = '狱血之犬'
    所在等级= 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [112, 1120]
    #咬住敌人时物理攻击力：<data0>%
    data0 = [ int(i) for i in [0, 429, 472, 515, 559, 602, 646, 689, 732, 776, 819, 863, 906, 949, 993, 1037, 1081, 1124, 1167, 1211, 1254, 1298, 1341, 1384, 1428, 1471, 1515, 1558, 1603, 1646, 1689, 1733, 1776, 1820, 1863, 1906, 1950, 1993, 2037, 2080, 2123, 2167, 2211, 2255, 2298, 2341, 2385, 2428, 2472, 2515, 2558, 2602, 2645, 2689, 2732, 2777, 2820, 2863, 2907, 2950, 2994, 3037, 3080, 3124, 3167, 3211, 3254, 3297, 3341, 3385, 3429]]
    hit0 = 1
    #撕咬多段攻击物理攻击力：<data1>%
    data1 = [ int(i) for i in [0, 429, 472, 515, 559, 602, 646, 689, 732, 776, 819, 863, 906, 949, 993, 1037, 1081, 1124, 1167, 1211, 1254, 1298, 1341, 1384, 1428, 1471, 1515, 1558, 1603, 1646, 1689, 1733, 1776, 1820, 1863, 1906, 1950, 1993, 2037, 2080, 2123, 2167, 2211, 2255, 2298, 2341, 2385, 2428, 2472, 2515, 2558, 2602, 2645, 2689, 2732, 2777, 2820, 2863, 2907, 2950, 2994, 3037, 3080, 3124, 3167, 3211, 3254, 3297, 3341, 3385, 3429]]
    hit1 = 13
    CD = 10
    TP成长 = 0.10
    TP上限 = 7


class 技能8(主动技能):
    名称 = '狱血之牙'
    所在等级= 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [0, 0]
    data0 = [ int(i) for i in [0, 7654, 8430, 9207, 9983, 10760, 11537, 12313, 13089, 13866, 14642, 15419, 16196, 16972, 17748, 18525, 19302, 20078, 20855, 21632, 22407, 23184, 23961, 24737, 25514, 26291, 27066, 27843, 28620, 29396, 30173, 30950, 31726, 32502, 33279, 34056, 34832, 35609, 36385, 37161, 37938, 38715, 39491, 40268, 41044, 41821, 42597, 43374, 44151, 44927, 45703, 46480, 47256, 48033, 48810, 49586, 50362, 51139, 51916, 52692, 53469, 54246, 55021, 55798, 56575, 57351, 58128, 58905, 59680, 60457, 61234]]
    hit0 = 1
    CD = 12
    TP成长 = 0.10
    TP上限 = 7


class 技能9(主动技能):
    名称 = '血腥炼狱'
    所在等级= 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [ int(i) for i in [0, 1318, 1452, 1585, 1720, 1853, 1987, 2120, 2255, 2388, 2522, 2656, 2790, 2923, 3058, 3191, 3324, 3458, 3592, 3726, 3859, 3994, 4127, 4261, 4394, 4529, 4662, 4796, 4930, 5064, 5197, 5331, 5465, 5599, 5732, 5867, 6000, 6134, 6267, 6402, 6535, 6668, 6803, 6936, 7070, 7203, 7338, 7471, 7605, 7739, 7873, 8006, 8140, 8274, 8408, 8541, 8676, 8809, 8943, 9076, 9211, 9344, 9477, 9612, 9745, 9879, 10012, 10147, 10280, 10414, 10548]]
    hit0 = 10
    CD =18
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [0, 0]
    无色消耗 = 1

    def 装备护石(self):
        self.倍率 *= 1.29
        self.CDR *= 0.9


class 技能10(主动技能):
    名称 = '噬魂囚笼'
    所在等级= 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [ int(i) for i in [0, 707, 779, 851, 923, 995, 1067, 1138, 1210, 1282, 1354, 1426, 1497, 1569, 1642, 1713, 1785, 1856, 1928, 2001, 2072, 2144, 2216, 2287, 2360, 2431, 2503, 2575, 2646, 2719, 2791, 2862, 2934, 3005, 3078, 3150, 3221, 3293, 3365, 3437, 3509, 3581, 3652, 3724, 3796, 3868, 3940, 4011, 4083, 4156, 4227, 4299, 4370, 4442, 4515, 4586, 4658, 4730, 4801, 4874, 4945, 5017, 5089, 5160, 5233, 5305, 5376, 5448, 5519, 5592, 5664]]
    hit0 = 24 #原作者段数为30
    CD =20
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [192, 1920]
    无色消耗 = 1

    def 装备护石(self):
        self.倍率 *= 1.29
        self.CDR *= 0.82


class 技能11(主动技能):
    名称 = '狱血之噬'
    所在等级= 45
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    #吸血物理攻击力：<data0>%
    data0 = [ int(i) for i in [0, 33416, 36805, 40196, 43586, 46975, 50366, 53755, 57146, 60535, 63926, 67316, 70706, 74096, 77486, 80876, 84265, 87656, 91046, 94436, 97826, 101216, 104606, 107997, 111386, 114777, 118166, 121556, 124946, 128336, 131727, 135116, 138507, 141896, 145287, 148676, 152067, 155457, 158846, 162237, 165626, 169017, 172407, 175797, 179187, 182577, 185967, 189356, 192747, 196137, 199527, 202917, 206307, 209697, 213087, 216477, 219868, 223257, 226647, 230037, 233427, 236818, 240207, 243598, 246987, 250378, 253767, 257158, 260548, 263937, 267328]]
    hit0 = 1
    CD =40
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [0, 0]
    无色消耗 = 2

    def 装备护石(self):
        self.倍率 *= 1.28


class 技能12(被动技能):
    名称 = '血狱之力'
    所在等级 = 48
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.105 + 0.015 * self.等级, 5)


class 技能13(主动技能):
    名称 = '伯爵之歌'
    所在等级= 50
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    #多段物理攻击力：<data0>%
    data0 = [ int(i) for i in [0, 4030, 4964, 5898, 6833, 7768, 8702, 9637, 10571, 11505, 12441, 13375, 14309, 15244, 16178, 17113, 18047, 18982, 19916, 20850, 21786, 22720, 23654, 24589, 25524, 26458, 27392, 28327, 29261, 30196, 31131, 32065, 32999, 33934, 34869, 35803, 36738, 37672, 38606, 39541, 40476, 41410, 42344, 43280, 44214, 45148, 46083, 47017, 47952, 48886, 49821, 50755, 51689, 52625, 53559, 54493, 55428, 56362, 57297, 58232, 59166, 60100, 61035, 61970, 62904, 63838, 64773, 65708, 66642, 67577, 68511]]
    hit0 = 14
    #最终一击物理攻击力：<data1>%
    data1 = [ int(i) for i in [0, 24180, 29788, 35394, 41001, 46608, 52216, 57823, 63430, 69036, 74644, 80251, 85858, 91466, 97073, 102679, 108286, 113894, 119501, 125108, 130714, 136322, 141929, 147536, 153143, 158751, 164357, 169964, 175571, 181179, 186786, 192393, 197999, 203607, 209214, 214821, 220429, 226036, 231642, 237249, 242857, 248464, 254071, 259677, 265285, 270892, 276499, 282107, 287714, 293320, 298927, 304535, 310142, 315749, 321356, 326963, 332570, 338177, 343784, 349392, 354999, 360605, 366212, 371820, 377427, 383034, 388642, 394248, 399855, 405462, 411070]]
    hit1 = 1
    CD = 145

    MP = [0, 0]
    无色消耗 = 5


class 技能14(主动技能):
    名称 = '魔仆召唤：狱犬'
    所在等级= 60
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    #多段物理攻击力：<data0>%
    data0 = [ int(i) for i in [0, 1505, 1657, 1810, 1963, 2116, 2268, 2421, 2574, 2726, 2879, 3031, 3184, 3336, 3489, 3642, 3794, 3947, 4100, 4253, 4405, 4558, 4711, 4863, 5016, 5169, 5322, 5474, 5627, 5780, 5933, 6085, 6238, 6391, 6543, 6696, 6849, 7002, 7153, 7306, 7459, 7611, 7764, 7917, 8070, 8222, 8375, 8528, 8681, 8833, 8986, 9139, 9291, 9444, 9597, 9750, 9902, 10055, 10208, 10360, 10513, 10666, 10819, 10970, 11123, 11276, 11429, 11581, 11734, 11887, 12039]]
    hit0 = 17
    CD =25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [640, 1920]
    无色消耗 = 1

    def 装备护石(self):
        self.倍率 *= 1.22
        self.CDR *= 0.8


class 技能15(主动技能):
    名称 = '血翼绽放'
    所在等级= 70
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    #蝙蝠群冲击波攻击力：<data0>%
    data0 = [ int(i) for i in [0, 15430, 16995, 18561, 20126, 21691, 23257, 24823, 26388, 27953, 29519, 31084, 32650, 34214, 35780, 37346, 38911, 40476, 42042, 43607, 45173, 46739, 48303, 49869, 51434, 53000, 54565, 56130, 57696, 59262, 60826, 62392, 63957, 65523, 67089, 68653, 70219, 71785, 73350, 74915, 76481]]
    hit0 = 1
    #血气之翼物理攻击力：<data1>%
    data1 = [ int(i) for i in [0, 23145, 25493, 27841, 30189, 32538, 34886, 37234, 39582, 41930, 44278, 46626, 48975, 51323, 53671, 56019, 58366, 60714, 63063, 65411, 67759, 70107, 72455, 74803, 77152, 79500, 81848, 84196, 86544, 88892, 91240, 93589, 95937, 98285, 100633, 102981, 105329, 107678, 110026, 112373, 114721]]
    hit1 = 1
    CD =50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [0, 0]
    无色消耗 = 2

    def 装备护石(self):
        self.倍率 *= 1.33


class 技能16(主动技能):
    名称 = '地狱冥犬'
    所在等级= 75
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    #撕咬攻击力：<data0>%
    data0 = [ int(i) for i in [0, 1197, 1388, 1580, 1770, 1958, 2152, 2343, 2532, 2724, 2915, 3105, 3297, 3487, 3677, 3870, 4060, 4251, 4442, 4632, 4825, 5015, 5206, 5398, 5589, 5779, 5970, 6160, 6351, 6544, 6732, 6923, 7114, 7305, 7495, 7687, 7878, 8068, 8261, 8450, 8641, 8833, 9023, 9215, 9405, 9596, 9788, 9978, 10169, 10360, 10551, 10740, 10932, 11123, 11313, 11505, 11695, 11886, 12078, 12268, 12459, 12650, 12841, 13033, 13223, 13414, 13605, 13796, 13986, 14178, 14369]]
    hit0 = 20
    #冲向地面攻击力：<data1>%
    data1 = [ int(i) for i in [0, 23948, 27765, 31583, 35402, 39221, 43038, 46857, 50675, 54493, 58310, 62127, 65944, 69763, 73581, 77400, 81218, 85036, 88854, 92673, 96490, 100307, 104124, 107942, 111760, 115580, 119397, 123215, 127034, 130852, 134669, 138488, 142305, 146121, 149940, 153759, 157576, 161395, 165213, 169031, 172849, 176666, 180485, 184302, 188121, 191939, 195756, 199574, 203392, 207211, 211028, 214846, 218664, 222481, 226300, 230119, 233937, 237754, 241572, 245390, 249207, 253025, 256844, 260663, 264480, 268298, 272116, 275933, 279752, 283570, 287387]]
    hit1 = 1
    CD =30
    是否有护石 = 1

    MP = [1066, 2133]
    无色消耗 = 3

    def 装备护石(self):
        self.倍率 *= 1.29
        self.CDR *= 0.9


class 技能17(被动技能):
    名称 = '鲜血之殇'
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
    名称 = '死亡之握'
    所在等级= 80
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [ int(i) for i in [0, 89863, 98979, 108096, 117213, 126329, 135446, 144562, 153678, 162796, 171912, 181029, 190145, 199261, 208379, 217495, 226611, 235728, 244844, 253962, 263078, 272194, 281311, 290427, 299544, 308661, 317777, 326894, 336010, 345127, 354244, 363360, 372476, 381593, 390710, 399827, 408943, 418059, 427176, 436293, 445409]]
    hit0 = 1
    CD =50
    是否有护石 = 1

    MP = [0, 0]
    无色消耗 = 5

    def 装备护石(self):
        self.倍率 *= 1.34


class 技能19(主动技能):
    名称 = '血界彼岸'
    所在等级= 85
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    #多段攻击力：<data0>%
    data0 = [ int(i) for i in [0, 2722, 3354, 3985, 4617, 5248, 5880, 6511, 7141, 7773, 8404, 9036, 9667, 10299, 10930, 11562, 12193, 12825, 13456, 14088, 14719, 15349, 15981, 16612, 17244, 17875, 18507, 19138, 19770, 20401, 21033, 21664, 22296, 22927, 23558, 24189, 24820, 25452, 26083, 26715, 27346]]
    hit0 = 34 #原作者写的35段
    #最终一击攻击力：<data1>%
    data1 = [ int(i) for i in [0, 92577, 114043, 135510, 156978, 178445, 199911, 221379, 242846, 264313, 285780, 307247, 328714, 350182, 371648, 393115, 414582, 436050, 457516, 478983, 500451, 521918, 543384, 564852, 586319, 607786, 629253, 650720, 672187, 693655, 715121, 736588, 758056, 779523, 800989, 822457, 843924, 865391, 886858, 908325, 929792]]
    hit1 = 1
    CD = 180

    MP = [0, 0]
    无色消耗 = 10


class 技能20(主动技能):
    名称 = '血翼蔽空'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [ int(i) for i in [0, 149276, 164421, 179565, 194709, 209853, 224998, 240141, 255285, 270430, 285574, 300718, 315862, 331006, 346150, 361294, 376439, 391582, 406726, 421871, 437014, 452159, 467303, 482446, 497591, 512735, 527880, 543023, 558167, 573312, 588455, 603600, 618744, 633887, 649032, 664176, 679320, 694464, 709608, 724752, 739896, 755041, 770184, 785328, 800473, 815616, 830761, 845905, 861049, 876193, 891337, 906482, 921625, 936769, 951914, 967057, 982202, 997346, 1012489, 1027634, 1042778, 1057922, 1073066, 1088211, 1103355, 1118498, 1133643, 1148787, 1163930, 1179075, 1194219]]
    hit0 = 1
    CD = 60.0

    MP = [0, 0]
    无色消耗 = 7


class 技能21(被动技能):
    名称 = '血源之眼'
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
    名称 = '血域帷幕·陨灭'
    所在等级 = 100
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [ int(i) for i in [0, 52232, 64344, 76456, 88566, 100678, 112790, 124902, 137014, 149126, 161238, 173349, 185461, 197573, 209685, 221797, 233909, 246020, 258132, 270244, 282355, 294467, 306579, 318691, 330802, 342914, 355026, 367138, 379250, 391362, 403474, 415585, 427697, 439809, 451921, 464033, 476144, 488255, 500367, 512479, 524591, 536703, 548815, 560927, 573038, 585150, 597262, 609374, 621486, 633598, 645710, 657821, 669933, 682044, 694156, 706268, 718380, 730491, 742603, 754715, 766827, 778939, 791051, 803163, 815274, 827386, 839498, 851609, 863721, 875833, 887944]]
    hit0 = 1
    data1 = [ int(i) for i in [0, 5223, 6434, 7645, 8856, 10068, 11279, 12489, 13701, 14912, 16123, 17334, 18546, 19757, 20968, 22180, 23390, 24601, 25813, 27024, 28235, 29446, 30658, 31869, 33079, 34291, 35502, 36713, 37924, 39136, 40347, 41558, 42770, 43980, 45191, 46403, 47614, 48825, 50036, 51248, 52459, 53670, 54881, 56092, 57303, 58514, 59726, 60937, 62148, 63360, 64571, 65781, 66992, 68204, 69415, 70626, 71838, 73049, 74260, 75472, 76682, 77893, 79104, 80316, 81527, 82738, 83950, 85161, 86371, 87582, 88794]]
    hit1 = 20
    data2 = [ int(i) for i in [0, 365624, 450406, 535189, 619971, 704754, 789536, 874319, 959101, 1043884, 1128667, 1213449, 1298232, 1383014, 1467797, 1552579, 1637362, 1722143, 1806926, 1891709, 1976491, 2061274, 2146056, 2230839, 2315621, 2400404, 2485187, 2569969, 2654752, 2739534, 2824317, 2909099, 2993882, 3078664, 3163447, 3248230, 3333012, 3417794, 3502576, 3587359, 3672141, 3756924, 3841707, 3926489, 4011271, 4096054, 4180837, 4265619, 4350402, 4435184, 4519967, 4604750, 4689532, 4774315, 4859097, 4943878, 5028661, 5113444, 5198226, 5283009, 5367792, 5452574, 5537357, 5622139, 5706921, 5791704, 5876487, 5961270, 6046052, 6130834, 6215617]]
    hit2 = 1
    CD = 290.0

    MP = [0, 0]
    无色消耗 = 15


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'blood_mage'
        self.名称 = '知源·血法师'
        self.角色 = '魔法师(男)'
        self.角色类型 = '输出'
        self.职业 = '血法师'
        # 用来筛CP武器的
        self.转职 = '血法师'
        self.武器选项 = ['矛']
        self.输出类型选项 = ['物理百分比']
        self.防具精通属性 = ['力量']
        self.类型 = '物理百分比'
        self.武器类型 = '矛'
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
        self.buff = 1.97

        super().__init__()