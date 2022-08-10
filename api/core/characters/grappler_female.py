from core.basic.skill import 技能
from core.basic.character import Character
from core.basic.skill import 主动技能, 被动技能


# class 技能0(被动技能):
# 名称 = '基础精通'
# 所在等级 = 1
# 等级上限 = 200
# 基础等级 = 100
# 关联技能 = ['普通攻击']

# def 加成倍率(self, 武器类型):
#     if self.等级 == 0:
#         return 1.0
#     else:
#         return round(0.463 + 0.089 * self.等级, 5)


# class 技能1(主动技能):
# 名称 = '普通攻击'
# 所在等级 = 1
# 等级上限 = 1
# 基础等级 = 1
# #3击 243.3735+307.4934*2
# data0 = [(i) for i in [0, 858.3604]]
# hit0 = 1
# CD = 1
# TP成长 = 0.10
# TP上限 = 5


class 技能0(主动技能):
    名称 = '背摔'
    所在等级 = 5
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [20, 168]
    data0 = [int(i*1.054) for i in [0, 2334, 2576, 2811, 3043, 3280, 3520, 3756, 3990, 4229, 4467, 4702, 4936, 5175, 5412, 5654, 5889, 6122, 6359, 6599, 6837, 7068, 7309, 7545, 7785, 8018, 8255, 8491, 8732, 8969, 9200, 9441, 9677, 9915, 10147, 10388,
                                    10624, 10865, 11096, 11333, 11570, 11810, 12042, 12280, 12520, 12757, 12996, 13229, 13466, 13701, 13943, 14176, 14410, 14652, 14889, 15119, 15357, 15597, 15834, 16076, 16308, 16544, 16780, 17020, 17255, 17490, 17731, 17968, 18200, 18441, 18676]]
    hit0 = 1
    CD = 5.0
    TP成长 = 0.10
    TP上限 = 7


class 技能1(主动技能):
    名称 = '抛投'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [30, 336]
    data0 = [int(i*1.055) for i in [0, 5294, 5834, 6370, 6906, 7444, 7982, 8519, 9058, 9591, 10132, 10668, 11207, 11743, 12279, 12818, 13353, 13892, 14428, 14966, 15504, 16041, 16578, 17116, 17653, 18190, 18726, 19265, 19800, 20339, 20875, 21414, 21951, 22487,
                                    23028, 23562, 24098, 24638, 25174, 25712, 26249, 26784, 27325, 27860, 28400, 28936, 29475, 30010, 30548, 31085, 31622, 32159, 32698, 33232, 33772, 34308, 34847, 35384, 35919, 36458, 36994, 37533, 38068, 38606, 39144, 39682, 40218, 40756, 41294, 41831, 42366]]
    hit0 = 1
    CD = 8.5
    TP成长 = 0.1
    TP上限 = 7


class 技能2(被动技能):
    名称 = '摔技强化'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10

    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级 <= 10:
                return round(1 + 0.01 * self.等级, 5)
            else:
                return round(1.1 + 0.02 * (self.等级 - 10), 5)


class 技能3(主动技能):
    名称 = '折颈'
    所在等级 = 20
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [30, 336]
    data0 = [int(i*1.054) for i in [0, 5589, 6155, 6724, 7289, 7854, 8423, 8989, 9557, 10123, 10692, 11257, 11825, 12392, 12960, 13527, 14094, 14662, 15226, 15793, 16361, 16928, 17495, 18063, 18629, 19198, 19763, 20331, 20898, 21466, 22032, 22599, 23164, 23731,
                                    24299, 24866, 25432, 26001, 26567, 27136, 27701, 28269, 28836, 29404, 29970, 30535, 31103, 31669, 32238, 32804, 33372, 33939, 34506, 35074, 35641, 36206, 36775, 37341, 37907, 38475, 39042, 39609, 40175, 40742, 41310, 41877, 42444, 43012, 43579, 44144, 44714]]
    hit0 = 1
    CD = 7.7
    TP成长 = 0.1
    TP上限 = 7


class 技能4(被动技能):
    名称 = '强力抱摔'
    所在等级 = 20
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能5(主动技能):
    名称 = '野蛮冲撞'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [50, 420]
    data0 = [int(i*1.050) for i in [0, 6897, 7598, 8297, 8998, 9699, 10398, 11097, 11797, 12498, 13197, 13898, 14597, 15296, 15996, 16696, 17396, 18095, 18795, 19495, 20195, 20894, 21595, 22295, 22993, 23694, 24393, 25093, 25793, 26494, 27192, 27892, 28592, 29292,
                                    29992, 30691, 31391, 32090, 32794, 33494, 34193, 34894, 35593, 36292, 36992, 37692, 38392, 39090, 39792, 40491, 41191, 41890, 42591, 43290, 43989, 44690, 45389, 46089, 46790, 47489, 48188, 48888, 49589, 50288, 50987, 51687, 52387, 53086, 53788, 54487, 55186]]
    hit0 = 1
    CD = 8.0
    TP成长 = 0.1
    TP上限 = 7


class 技能6(主动技能):
    名称 = '霹雳肘击'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [50, 420]
    data0 = [int(i*1.052) for i in [0, 8913, 9818, 10720, 11626, 12528, 13436, 14338, 15243, 16145, 17051, 17955, 18859, 19763, 20668, 21574, 22478, 23382, 24286, 25190, 26093, 27000, 27902, 28808, 29711, 30615, 31520, 32425, 33329, 34232, 35136, 36042, 36944, 37850,
                                    38752, 39659, 40562, 41468, 42370, 43275, 44180, 45084, 45990, 46892, 47798, 48700, 49607, 50510, 51415, 52318, 53221, 54127, 55031, 55935, 56840, 57742, 58650, 59551, 60457, 61360, 62266, 63168, 64074, 64980, 65881, 66787, 67690, 68597, 69500, 70406, 71307]]
    hit0 = 1
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 7


class 技能7(主动技能):
    名称 = '空绞锤'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [50, 420]
    data0 = [int(i*1.052) for i in [0, 6519, 7183, 7852, 8538, 9212, 9880, 10552, 11231, 11909, 12581, 13245, 13926, 14595, 15274, 15945, 16623, 17292, 17972, 18642, 19324, 19987, 20657, 21337, 22015, 22693, 23361, 24029, 24714, 25387, 26049, 26721, 27396, 28084,
                                    28753, 29423, 30091, 30773, 31455, 32116, 32787, 33465, 34136, 34815, 35484, 36165, 36835, 37515, 38181, 38858, 39530, 40204, 40876, 41553, 42227, 42903, 43578, 44242, 44921, 45595, 46264, 46947, 47615, 48296, 48966, 49641, 50307, 50988, 51658, 52339, 53008]]
    hit0 = 1
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 7


class 技能8(主动技能):
    名称 = '霹雳冲击'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.050) for i in [0, 4466, 4919, 5373, 5826, 6280, 6730, 7185, 7637, 8092, 8543, 8998, 9450, 9905, 10354, 10810, 11261, 11717, 12167, 12622, 13074, 13529, 13982, 14435, 14887, 15341, 15794, 16246, 16699, 17153, 17606, 18062, 18511, 18966, 19418,
                                    19873, 20324, 20779, 21231, 21686, 22136, 22590, 23042, 23497, 23949, 24403, 24856, 25310, 25763, 26216, 26668, 27122, 27576, 28030, 28481, 28935, 29388, 29842, 30294, 30747, 31200, 31654, 32108, 32560, 33014, 33466, 33921, 34372, 34825, 35278, 35732]]
    hit0 = 1
    data1 = [int(i*1.050) for i in [0, 10182, 11216, 12250, 13283, 14315, 15348, 16382, 17415, 18449, 19482, 20515, 21548, 22582, 23615, 24648, 25681, 26713, 27749, 28782, 29816, 30849, 31881, 32911, 33945, 34979, 36013, 37046, 38079, 39113, 40147, 41180, 42214, 43246,
                                    44277, 45311, 46346, 47378, 48412, 49445, 50477, 51514, 52544, 53577, 54611, 55644, 56676, 57710, 58744, 59778, 60810, 61843, 62876, 63911, 64944, 65978, 67011, 68041, 69074, 70108, 71141, 72175, 73208, 74241, 75276, 76309, 77342, 78376, 79406, 80439, 81475]]
    hit1 = 1
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5

    MP = [150, 1260]
    无色消耗 = 1


class 技能9(主动技能):
    名称 = '螺旋彗星落'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.050) for i in [0, 15212, 16756, 18300, 19844, 21386, 22931, 24474, 26018, 27562, 29105, 30650, 32191, 33735, 35280, 36824, 38367, 39911, 41455, 42997, 44541, 46086, 47628, 49172, 50713, 52258, 53802, 55346, 56889, 58433, 59977, 61522, 63063, 64607, 66152,
                                    67693, 69237, 70781, 72324, 73868, 75412, 76955, 78499, 80043, 81587, 83129, 84671, 86215, 87758, 89302, 90847, 92389, 93933, 95478, 97022, 98564, 100109, 101649, 103193, 104738, 106281, 107824, 109369, 110912, 112458, 114001, 115545, 117089, 118630, 120175, 121716]]
    hit0 = 1
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    无色消耗 = 1
    MP = [150, 1260]

    def 装备护石(self):
        self.倍率 *= 1.29
        self.CDR *= 0.88


class 技能10(主动技能):
    名称 = '地狱摇篮'
    所在等级 = 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.051) for i in [0, 23605, 26000, 28397, 30789, 33187, 35577, 37975, 40371, 42764, 45159, 47553, 49948, 52344, 54737, 57132, 59527, 61923, 64319, 66712, 69108, 71502, 73896, 76292, 78685, 81082, 83480, 85870, 88268, 90663, 93057, 95453, 97846, 100241, 102636, 105031,
                                    107428, 109820, 112216, 114609, 117005, 119401, 121795, 124190, 126585, 128979, 131376, 133769, 136165, 138558, 140953, 143349, 145743, 148139, 150534, 152927, 155323, 157717, 160111, 162508, 164902, 167297, 169692, 172088, 174482, 176876, 179271, 181665, 184060, 186456, 188849]]
    hit0 = 1
    data1 = [int(i*1.051) for i in [0, 3275, 3607, 3941, 4274, 4606, 4937, 5270, 5602, 5936, 6267, 6600, 6931, 7264, 7595, 7929, 8263, 8594, 8926, 9257, 9591, 9921, 10257, 10590, 10921, 11254, 11585, 11918, 12251, 12584, 12915, 13247, 13580, 13912, 14246,
                                    14578, 14910, 15242, 15572, 15906, 16240, 16573, 16904, 17235, 17568, 17900, 18235, 18567, 18899, 19232, 19563, 19896, 20228, 20561, 20893, 21226, 21557, 21890, 22221, 22555, 22888, 23220, 23552, 23883, 24217, 24551, 24882, 25215, 25546, 25879, 26210]]
    hit1 = 0
    data2 = [int(i*1.051) for i in [0, 7223, 7955, 8688, 9420, 10155, 10888, 11618, 12352, 13085, 13816, 14551, 15283, 16016, 16748, 17482, 18217, 18946, 19680, 20414, 21148, 21880, 22609, 23345, 24078, 24811, 25544, 26275, 27009, 27741, 28475, 29208, 29938, 30672,
                                    31405, 32140, 32872, 33604, 34337, 35068, 35803, 36537, 37268, 38001, 38735, 39468, 40200, 40932, 41666, 42399, 43132, 43864, 44596, 45329, 46063, 46795, 47528, 48261, 48992, 49726, 50461, 51195, 51924, 52657, 53392, 54123, 54858, 55590, 56322, 57055, 57788]]
    hit2 = 0
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [220, 1988]
    无色消耗 = 1

    形态 = ["非抓", "抓取"]

    def 形态变更(self, 形态, char: Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "非抓":
            self.hit0 = 1
            self.hit1 = 0
            self.hit2 = 0
            if '地狱摇篮' in char.护石栏:
                self.power0 = 1.32
        if 形态 == "抓取":
            self.hit0 = 0
            self.hit1 = 5
            self.hit2 = 1
            if '地狱摇篮' in char.护石栏:
                self.hit1 = 10
                self.power1 = 0.6
                self.power2 = 1.59

    def 装备护石(self):
        self.power0 *= 1.32
        self.CDR *= 0.9


class 技能11(主动技能):
    名称 = '裂石破天'
    所在等级 = 45
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.050) for i in [0, 16784, 18486, 20192, 21892, 23598, 25299, 26999, 28705, 30409, 32109, 33815, 35516, 37217, 38922, 40622, 42327, 44033, 45734, 47439, 49139, 50840, 52545, 54250, 55951, 57654, 59356, 61057, 62763, 64465, 66169, 67872, 69575, 71275, 72980,
                                    74684, 76384, 78089, 79792, 81495, 83196, 84897, 86603, 88307, 90011, 91713, 93414, 95113, 96819, 98523, 100229, 101930, 103629, 105335, 107037, 108742, 110444, 112146, 113851, 115553, 117254, 118959, 120661, 122363, 124068, 125769, 127472, 129175, 130876, 132580, 134286]]
    hit0 = 1
    # 摔技强化固定65%加成，别的技能已经直接加成在了面板上；仅裂石破天和死亡摇篮的非抓下需要额外65%加成
    power0 = 1.65
    data1 = [int(i*1.050) for i in [0, 4324, 4760, 5198, 5638, 6077, 6514, 6954, 7390, 7833, 8269, 8707, 9145, 9586, 10024, 10463, 10903, 11338, 11780, 12216, 12659, 13095, 13533, 13972, 14410, 14847, 15289, 15725, 16169, 16603, 17042, 17480, 17919, 18356, 18799,
                                    19234, 19678, 20112, 20552, 20990, 21430, 21865, 22308, 22745, 23182, 23622, 24060, 24499, 24939, 25376, 25816, 26252, 26691, 27130, 27569, 28008, 28448, 28885, 29325, 29760, 30200, 30639, 31078, 31515, 31957, 32394, 32833, 33269, 33708, 34148, 34587]]
    hit1 = 0
    data2 = [int(i*1.050) for i in [0, 1438, 1585, 1731, 1877, 2021, 2169, 2315, 2460, 2605, 2754, 2897, 3043, 3190, 3336, 3481, 3628, 3773, 3919, 4065, 4212, 4355, 4506, 4650, 4798, 4942, 5089, 5234, 5382, 5527, 5672, 5818, 5964, 6110,
                                    6258, 6402, 6548, 6692, 6840, 6987, 7133, 7280, 7424, 7571, 7718, 7862, 8006, 8155, 8299, 8446, 8592, 8740, 8883, 9030, 9175, 9321, 9468, 9614, 9761, 9908, 10053, 10200, 10344, 10491, 10636, 10784, 10928, 11075, 11220, 11366, 11512]]
    hit2 = 0
    data3 = [int(i*1.050) for i in [0, 5727, 6308, 6890, 7470, 8050, 8631, 9215, 9796, 10376, 10956, 11537, 12118, 12700, 13281, 13862, 14441, 15022, 15604, 16187, 16768, 17348, 17930, 18511, 19092, 19672, 20255, 20837, 21416, 21995, 22580, 23158, 23740, 24320,
                                    24903, 25480, 26066, 26645, 27229, 27806, 28389, 28970, 29550, 30130, 30715, 31296, 31875, 32458, 33039, 33621, 34199, 34780, 35361, 35942, 36525, 37107, 37687, 38266, 38848, 39431, 40012, 40592, 41171, 41754, 42335, 42917, 43498, 44079, 44658, 45238, 45823]]
    hit3 = 0
    data4 = [int(i*1.050) for i in [0, 15448, 17015, 18582, 20150, 21716, 23283, 24852, 26416, 27984, 29553, 31119, 32686, 34255, 35822, 37388, 38956, 40520, 42087, 43656, 45224, 46792, 48357, 49923, 51494, 53061, 54628, 56195, 57761, 59329, 60898, 62462, 64030, 65599, 67165,
                                    68731, 70300, 71868, 73434, 75001, 76566, 78135, 79702, 81269, 82836, 84403, 85969, 87540, 89107, 90673, 92241, 93807, 95375, 96944, 98508, 100075, 101644, 103211, 104777, 106346, 107911, 109480, 111046, 112612, 114181, 115748, 117313, 118882, 120449, 122015, 123586]]
    hit4 = 0
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [360, 3024]
    无色消耗 = 2

    形态 = ["应变", "抓取", "非抓"]

    def 形态变更(self, 形态, char: Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "应变":
            self.hit0 = 1
            self.hit1 = 0
            self.hit2 = 0
            self.hit3 = 0
            self.hit4 = 0
            if '裂石破天' in char.护石栏:
                self.power0 = 1.31
        if 形态 == "抓取":
            self.hit0 = 0
            self.hit1 = 1
            self.hit2 = 0
            self.hit3 = 1
            self.hit4 = 1
            if '裂石破天' in char.护石栏:
                self.power3 = 1.28
                self.power4 = 1.28
        if 形态 == "非抓":
            self.hit0 = 0
            self.hit1 = 1
            self.hit2 = 3
            self.hit3 = 1
            self.hit4 = 1
            if '裂石破天' in char.护石栏:
                self.hit2 += 2
                self.power3 = 1.28
                self.power4 = 1.28

    def 装备护石(self):
        pass


class 技能12(被动技能):
    名称 = '抓取奥义'
    所在等级 = 48
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.09 + 0.015 * self.等级, 5)


class 技能13(主动技能):
    名称 = '末日风暴'
    所在等级 = 50
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i) for i in [0, 2568, 3164, 3757, 4352, 4950, 5545, 6140, 6735, 7332, 7926, 8522, 9117, 9712, 10311, 10903, 11499, 12096, 12690, 13284, 13883, 14477, 15071, 15666, 16262, 16860, 17453, 18049, 18644, 19241, 19837, 20431, 21026, 21622, 22216,
                              22811, 23409, 24003, 24598, 25195, 25789, 26387, 26980, 27576, 28172, 28769, 29362, 29958, 30554, 31151, 31745, 32338, 32936, 33531, 34129, 34722, 35318, 35915, 36509, 37103, 37699, 38295, 38890, 39485, 40081, 40679, 41271, 41868, 42463, 43056, 43656]]
    hit0 = 1
    data1 = [int(i) for i in [0, 39987, 49258, 58527, 67804, 77076, 86346, 95619, 104889, 114164, 123435, 132707, 141978, 151252, 160525, 169796, 179069, 188342, 197613, 206885, 216157, 225428, 234702, 243973, 253246, 262518, 271789, 281065, 290335, 299608, 308878, 318152, 327423, 336696, 345967,
                              355241, 364513, 373784, 383055, 392329, 401603, 410873, 420147, 429418, 438692, 447964, 457235, 466507, 475779, 485053, 494324, 503595, 512868, 522139, 531413, 540685, 549957, 559230, 568502, 577772, 587045, 596318, 605591, 614862, 624133, 633405, 642680, 651952, 661224, 670495, 679768]]
    hit1 = 1
    CD = 140.0

    MP = [900, 7560]
    无色消耗 = 5

    形态 = ["秒C", "满"]

    def 形态变更(self, 形态, char: Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "秒C":
            self.hit0 = 1
            self.hit1 = 1
        if 形态 == "满":
            self.hit0 = 13
            self.hit1 = 1

    def 等效百分比(self, **argv):
        if self.等级 > 8:
            self.power1 = 1.1
        return super().等效百分比(**argv)


class 技能14(主动技能):
    名称 = '空绞连锤'
    所在等级 = 60
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.052) for i in [0, 2086, 2297, 2507, 2721, 2934, 3143, 3355, 3570, 3780, 3991, 4204, 4415, 4625, 4838, 5049, 5262, 5473, 5685, 5896, 6109, 6319, 6531, 6743, 6952, 7168, 7378, 7588, 7802, 8015, 8224, 8435, 8650, 8859, 9071, 9283,
                                    9495, 9706, 9919, 10130, 10340, 10553, 10768, 10977, 11187, 11401, 11612, 11823, 12033, 12249, 12459, 12668, 12881, 13094, 13304, 13517, 13730, 13941, 14152, 14363, 14577, 14787, 15000, 15212, 15421, 15634, 15845, 16057, 16267, 16482, 16693]]
    hit0 = 3
    data1 = [int(i*1.052) for i in [0, 25054, 27596, 30140, 32680, 35222, 37763, 40306, 42849, 45390, 47934, 50474, 53016, 55559, 58101, 60641, 63183, 65724, 68268, 70809, 73350, 75891, 78434, 80979, 83520, 86062, 88603, 91144, 93686, 96229, 98772, 101311, 103854, 106397, 108938, 111479,
                                    114020, 116563, 119107, 121649, 124190, 126732, 129273, 131816, 134357, 136900, 139441, 141982, 144523, 147067, 149608, 152150, 154691, 157235, 159777, 162318, 164859, 167401, 169944, 172487, 175029, 177570, 180111, 182652, 185195, 187738, 190278, 192821, 195360, 197906, 200447]]
    hit1 = 1
    data2 = [int(i*1.052) for i in [0, 9399, 10350, 11305, 12255, 13210, 14165, 15118, 16071, 17026, 17976, 18931, 19884, 20840, 21792, 22745, 23700, 24650, 25605, 26558, 27511, 28466, 29420, 30371, 31325, 32278, 33234, 34186, 35138, 36091, 37045, 37998, 38953, 39906,
                                    40861, 41813, 42766, 43719, 44673, 45628, 46581, 47533, 48486, 49441, 50393, 51349, 52304, 53253, 54208, 55159, 56114, 57066, 58023, 58975, 59927, 60880, 61835, 62788, 63744, 64695, 65648, 66603, 67554, 68509, 69465, 70415, 71370, 72321, 73275, 74229, 75181]]
    hit2 = 0
    data3 = [int(i*1.052) for i in [0, 15657, 17245, 18835, 20423, 22009, 23598, 25186, 26775, 28364, 29955, 31542, 33132, 34719, 36308, 37897, 39484, 41074, 42661, 44251, 45839, 47425, 49016, 50604, 52193, 53781, 55371, 56958, 58544, 60133, 61722, 63311, 64898, 66488, 68077,
                                    69664, 71255, 72844, 74431, 76021, 77609, 79198, 80787, 82373, 83963, 85552, 87139, 88728, 90318, 91906, 93492, 95080, 96670, 98258, 99846, 101434, 103025, 104611, 106200, 107789, 109377, 110965, 112557, 114144, 115734, 117322, 118911, 120500, 122086, 123676, 125264]]
    hit3 = 0
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [450, 1260]
    无色消耗 = 1

    形态 = ["非抓", "抓取"]

    def 形态变更(self, 形态, char: Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "非抓":
            self.hit0 = 3
            self.hit1 = 1
            self.hit2 = 0
            self.hit3 = 0
        if 形态 == "抓取":
            self.hit0 = 3
            self.hit1 = 0
            self.hit2 = 1
            self.hit3 = 1

    def 装备护石(self):
        self.倍率 *= 1.21


class 技能15(主动技能):
    名称 = '死亡摇篮'
    所在等级 = 70
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.052) for i in [0, 26861, 29585, 32310, 35038, 37760, 40487, 43213, 45935, 48660, 51389, 54111, 56837, 59563, 62287, 65012, 67740, 70464, 73189, 75914, 78635, 81363, 84091, 86814, 89539, 92264, 94988, 97714, 100440, 103166, 105891, 108616, 111339, 114064, 116790, 119515,
                                    122239, 124966, 127690, 130415, 133141, 135865, 138589, 141318, 144042, 146764, 149492, 152217, 154940, 157669, 160392, 163116, 165841, 168567, 171289, 174019, 176744, 179466, 182192, 184918, 187641, 190368, 193094, 195818, 198543, 201269, 203991, 206716, 209446, 212167, 214894]]
    hit0 = 1
    # 摔技强化固定65%加成，别的技能已经直接加成在了面板上；仅裂石破天和死亡摇篮的非抓下需要额外65%加成
    power0 = 1.65
    data1 = [int(i*1.052) for i in [0, 2252, 2484, 2713, 2939, 3169, 3398, 3625, 3857, 4085, 4311, 4542, 4771, 4999, 5228, 5456, 5684, 5914, 6143, 6369, 6601, 6829, 7056, 7287, 7515, 7744, 7974, 8203, 8430, 8658, 8888, 9116, 9345, 9573, 9804, 10032,
                                    10260, 10490, 10718, 10947, 11176, 11406, 11633, 11861, 12091, 12319, 12548, 12776, 13005, 13234, 13463, 13694, 13921, 14149, 14380, 14606, 14835, 15066, 15294, 15522, 15752, 15979, 16208, 16438, 16665, 16893, 17125, 17352, 17580, 17810, 18038]]
    hit1 = 0
    data2 = [int(i*1.052) for i in [0, 45019, 49583, 54152, 58719, 63285, 67852, 72420, 76987, 81553, 86120, 90690, 95256, 99822, 104389, 108958, 113525, 118090, 122657, 127226, 131793, 136358, 140925, 145494, 150061, 154627, 159193, 163764, 168331, 172897, 177464, 182032, 186597, 191164, 195731,
                                    200301, 204866, 209433, 214000, 218568, 223134, 227700, 232267, 236838, 241404, 245971, 250537, 255105, 259671, 264238, 268804, 273374, 277940, 282507, 287074, 291640, 296207, 300776, 305343, 309909, 314477, 319044, 323611, 328177, 332746, 337312, 341879, 346445, 351013, 355581, 360145]]
    hit2 = 0
    data3 = [int(i*1.052) for i in [0, 47272, 52070, 56865, 61661, 66456, 71252, 76045, 80843, 85640, 90435, 95233, 100026, 104822, 109619, 114413, 119211, 124005, 128803, 133598, 138394, 143190, 147984, 152782, 157578, 162372, 167169, 171963, 176762, 181556, 186353, 191148, 195942, 200740, 205535,
                                    210333, 215128, 219924, 224720, 229513, 234312, 239107, 243904, 248698, 253492, 258291, 263088, 267882, 272678, 277474, 282269, 287067, 291862, 296659, 301452, 306249, 311046, 315841, 320637, 325432, 330228, 335024, 339820, 344617, 349410, 354209, 359003, 363799, 368596, 373391, 378188]]
    hit3 = 0
    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [840, 1764]
    无色消耗 = 2

    形态 = ["应变", "抓取", "非抓"]

    def 形态变更(self, 形态, char: Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "应变":
            self.hit0 = 1
            self.hit1 = 0
            self.hit2 = 0
            self.hit3 = 0
            if '死亡摇篮' in char.护石栏:
                self.power0 = 1.31
        if 形态 == "抓取":
            self.hit0 = 0
            self.hit1 = 1
            self.hit2 = 1
            self.hit3 = 0
            if '死亡摇篮' in char.护石栏:
                self.hit0 = 0
                self.hit1 = 0
                self.hit2 = 0
                self.hit3 = 1
                self.power3 = 1.23
        if 形态 == "非抓":
            self.hit0 = 0
            self.hit1 = 0
            self.hit2 = 0
            self.hit3 = 1
            if '死亡摇篮' in char.护石栏:
                self.power3 = 1.23

    def 装备护石(self):
        pass


class 技能16(主动技能):
    名称 = '末日摇篮'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.051) for i in [0, 13280, 14626, 15974, 17322, 18671, 20016, 21365, 22712, 24058, 25405, 26754, 28100, 29448, 30797, 32142, 33490, 34838, 36184, 37532, 38880, 40229, 41574, 42920, 44270, 45616, 46964, 48312, 49658, 51006, 52353, 53700, 55047, 56396,
                                    57743, 59090, 60437, 61784, 63132, 64478, 65828, 67173, 68522, 69870, 71215, 72564, 73911, 75259, 76605, 77953, 79300, 80647, 81995, 83342, 84690, 86037, 87386, 88731, 90079, 91428, 92774, 94122, 95470, 96817, 98163, 99509, 100858, 102205, 103553, 104900, 106248]]
    hit0 = 1
    data1 = [int(i*1.051) for i in [0, 53124, 58510, 63899, 69292, 74679, 80068, 85460, 90848, 96235, 101624, 107017, 112406, 117792, 123185, 128576, 133961, 139355, 144741, 150131, 155524, 160910, 166299, 171686, 177080, 182468, 187856, 193249, 198637, 204024, 209417, 214803, 220192, 225587, 230975,
                                    236361, 241749, 247142, 252533, 257918, 263312, 268700, 274086, 279480, 284867, 290255, 295648, 301037, 306425, 311811, 317205, 322595, 327980, 333374, 338763, 344150, 349543, 354931, 360318, 365712, 371098, 376488, 381880, 387268, 392656, 398043, 403438, 408826, 414211, 419605, 424993]]
    hit1 = 1
    data2 = [int(i*1.051) for i in [0, 9109, 10032, 10954, 11877, 12802, 13726, 14649, 15573, 16497, 17424, 18347, 19270, 20196, 21118, 22041, 22965, 23891, 24816, 25739, 26662, 27585, 28511, 29433, 30356, 31281, 32205, 33130, 34054, 34977, 35903, 36826, 37749, 38674,
                                    39597, 40524, 41446, 42369, 43294, 44218, 45140, 46064, 46988, 47915, 48838, 49761, 50684, 51610, 52532, 53456, 54379, 55306, 56231, 57153, 58077, 59002, 59925, 60848, 61771, 62696, 63620, 64547, 65469, 66392, 67317, 68241, 69163, 70088, 71011, 71938, 72861]]
    hit2 = 0
    data3 = [int(i*1.051) for i in [0, 13974, 15391, 16808, 18226, 19644, 21060, 22479, 23897, 25313, 26731, 28149, 29567, 30984, 32402, 33818, 35235, 36656, 38072, 39491, 40907, 42325, 43744, 45159, 46578, 47996, 49414, 50831, 52248, 53667, 55083, 56499, 57922, 59336,
                                    60755, 62171, 63590, 65009, 66424, 67843, 69260, 70677, 72095, 73513, 74933, 76347, 77766, 79187, 80602, 82019, 83435, 84855, 86272, 87689, 89107, 90525, 91942, 93360, 94778, 96194, 97612, 99032, 100450, 101864, 103284, 104700, 106117, 107537, 108954, 110372, 111788]]
    hit3 = 0
    data4 = [int(i*1.051) for i in [0, 59544, 65585, 71626, 77666, 83710, 89750, 95789, 101831, 107872, 113913, 119955, 125995, 132035, 138076, 144118, 150157, 156200, 162241, 168280, 174324, 180363, 186404, 192445, 198488, 204526, 210567, 216608, 222650, 228692, 234733, 240771, 246813, 252854, 258896,
                                    264937, 270977, 277017, 283058, 289100, 295142, 301182, 307222, 313262, 319305, 325345, 331386, 337428, 343468, 349508, 355549, 361591, 367632, 373674, 379714, 385754, 391795, 397837, 403878, 409920, 415959, 422000, 428040, 434084, 440124, 446164, 452203, 458245, 464287, 470329, 476368]]
    hit4 = 0
    CD = 40.0
    是否有护石 = 1

    MP = [580, 4500]
    无色消耗 = 3

    形态 = ["应变", "抓取", "非抓"]

    def 形态变更(self, 形态, char: Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "应变":
            self.hit0 = 1
            self.hit1 = 1
            self.hit2 = 0
            self.hit3 = 0
            self.hit4 = 0
        if 形态 == "抓取":
            self.hit0 = 0
            self.hit1 = 0
            self.hit2 = 6
            self.hit3 = 1
            self.hit4 = 0
        if 形态 == "非抓":
            self.hit0 = 0
            self.hit1 = 0
            self.hit2 = 1
            self.hit3 = 0
            self.hit4 = 1

    def 装备护石(self):
        self.倍率 *= 1.3225
        self.CDR *= 0.9
    # 攻击力+15% ；生成总攻击力15%伤害的旋风（多段，15次攻击，每次1%）


class 技能17(被动技能):
    名称 = '极手奥义'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能18(主动技能):
    名称 = '风暴之舞'
    所在等级 = 80
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.051) for i in [0, 9192, 10127, 11056, 11991, 12922, 13854, 14787, 15722, 16655, 17586, 18520, 19448, 20385, 21314, 22247, 23179, 24112, 25046, 25976, 26909, 27842, 28776, 29706, 30639, 31575, 32503, 33440, 34370, 35304, 36235, 37169, 38101, 39034,
                                    39968, 40896, 41833, 42762, 43695, 44627, 45562, 46493, 47425, 48360, 49288, 50225, 51154, 52089, 53024, 53953, 54887, 55817, 56751, 57684, 58615, 59548, 60482, 61412, 62345, 63278, 64209, 65142, 66075, 67007, 67942, 68874, 69806, 70740, 71673, 72603, 73536]]
    hit0 = 6
    data1 = [int(i*1.051) for i in [0, 25550, 28138, 30734, 33323, 35914, 38504, 41102, 43693, 46284, 48876, 51466, 54059, 56650, 59242, 61831, 64426, 67016, 69607, 72203, 74794, 77385, 79976, 82570, 85158, 87752, 90343, 92935, 95526, 98120, 100713, 103305, 105896, 108487, 111079, 113669,
                                    116262, 118852, 121444, 124037, 126627, 129220, 131816, 134405, 136998, 139590, 142183, 144772, 147361, 149956, 152549, 155139, 157732, 160324, 162914, 165507, 168099, 170690, 173281, 175873, 178467, 181058, 183649, 186241, 188834, 191424, 194016, 196606, 199201, 201794, 204384]]
    hit1 = 1
    CD = 45.0
    是否有护石 = 1

    MP = [800, 6000]
    无色消耗 = 5

    def 装备护石(self):
        self.hit0 += 7
        self.power0 *= 0.56
        self.倍率 *= 1.19


class 技能19(主动技能):
    名称 = '苍宇彗星落'
    所在等级 = 85
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i) for i in [0, 16386, 20185, 23986, 27789, 31588, 35388, 39188, 42986, 46785, 50588, 54388, 58185, 61985, 65788, 69588, 73389, 77188, 80988, 84787, 88588, 92387, 96186, 99986, 103789, 107588,
                              111388, 115188, 118988, 122786, 126587, 130388, 134187, 137987, 141788, 145587, 149388, 153187, 156988, 160787, 164588, 168387, 172186, 175987, 179787, 183587, 187388, 191188, 194988, 198786, 202587]]
    hit0 = 1
    data1 = [int(i) for i in [0, 147519, 181724, 215929, 250139, 284346, 318556, 352758, 386967, 421175, 455380, 489593, 523797, 558005, 592211, 626418, 660627, 694833, 729039, 763249, 797455, 831663, 865870, 900077, 934285, 968493,
                              1002702, 1036907, 1071113, 1105323, 1139529, 1173735, 1207945, 1242150, 1276358, 1310564, 1344773, 1378981, 1413185, 1447395, 1481602, 1515807, 1550016, 1584224, 1618433, 1652637, 1686843, 1721054, 1755261, 1789467, 1823676]]
    hit1 = 1
    data2 = [int(i) for i in [0, 22450, 27654, 32861, 38065, 43273, 48480, 53687, 58891, 64096, 69302, 74510, 79715, 84922, 90127, 95334, 100537, 105745, 110951, 116158, 121363, 126569, 131774, 136982, 142187,
                              147392, 152599, 157802, 163009, 168217, 173424, 178627, 183834, 189041, 194245, 199451, 204659, 209866, 215070, 220276, 225481, 230687, 235895, 241100, 246306, 251512, 256718, 261922, 267130, 272336, 277543]]
    hit2 = 0
    data3 = [int(i) for i in [0, 138140, 170172, 202205, 234238, 266270, 298303, 330336, 362367, 394401, 426433, 458466, 490499, 522533, 554564, 586598, 618628, 650661, 682696, 714727, 746759, 778792, 810826, 842858, 874891, 906923,
                              938957, 970988, 1003021, 1035053, 1067086, 1099118, 1131152, 1163184, 1195216, 1227248, 1259282, 1291316, 1323346, 1355379, 1387413, 1419446, 1451477, 1483511, 1515544, 1547573, 1579608, 1611642, 1643673, 1675707, 1707739]]
    hit3 = 0
    CD = 180

    MP = [2500, 5000]
    无色消耗 = 10

    形态 = ["应变", "抓取"]

    def 形态变更(self, 形态, char: Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "应变":
            self.hit0 = 1
            self.hit1 = 1
            self.hit2 = 0
            self.hit3 = 0
        if 形态 == "抓取":
            self.hit0 = 0
            self.hit1 = 0
            self.hit2 = 1
            self.hit3 = 1


class 技能20(主动技能):
    名称 = '送葬舞步'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.051) for i in [0, 14874, 16382, 17892, 19401, 20909, 22419, 23929, 25437, 26946, 28454, 29963, 31472, 32982, 34491, 35999, 37508, 39017, 40527, 42036, 43544, 45054, 46563, 48071, 49581, 51089, 52599, 54107, 55616, 57125, 58633, 60144, 61652, 63161, 64670,
                                    66178, 67688, 69198, 70706, 72215, 73724, 75233, 76743, 78251, 79761, 81269, 82778, 84287, 85795, 87306, 88814, 90323, 91831, 93340, 94850, 96358, 97868, 99377, 100885, 102395, 103903, 105412, 106922, 108431, 109940, 111449, 112957, 114468, 115976, 117485, 118993]]
    hit0 = 1
    data1 = [int(i*1.051) for i in [0, 66931, 73722, 80514, 87302, 94094, 100884, 107674, 114465, 121255, 128046, 134836, 141626, 148417, 155209, 161998, 168788, 175579, 182369, 189159, 195950, 202741, 209533, 216322, 223112, 229901, 236693, 243483, 250272, 257064, 263855, 270645, 277436, 284226,
                                    291015, 297806, 304595, 311386, 318178, 324968, 331757, 338549, 345339, 352128, 358919, 365710, 372501, 379292, 386081, 392872, 399663, 406452, 413242, 420034, 426825, 433614, 440405, 447196, 453985, 460776, 467567, 474355, 481148, 487938, 494729, 501520, 508308, 515098, 521890, 528679, 535469]]
    hit1 = 1
    data2 = [int(i*1.051) for i in [0, 66931, 73722, 80514, 87302, 94094, 100884, 107674, 114465, 121255, 128046, 134836, 141626, 148417, 155209, 161998, 168788, 175579, 182369, 189159, 195950, 202741, 209533, 216322, 223112, 229901, 236693, 243483, 250272, 257064, 263855, 270645, 277436, 284226,
                                    291015, 297806, 304595, 311386, 318178, 324968, 331757, 338549, 345339, 352128, 358919, 365710, 372501, 379292, 386081, 392872, 399663, 406452, 413242, 420034, 426825, 433614, 440405, 447196, 453985, 460776, 467567, 474355, 481148, 487938, 494729, 501520, 508308, 515098, 521890, 528679, 535469]]
    hit2 = 1
    CD = 60.0

    MP = [960, 7200]
    无色消耗 = 7


class 技能21(被动技能):
    名称 = '光芒之翼'
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
    名称 = '女皇时代·辉煌舞台'
    所在等级 = 100
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i*1.050) for i in [0, 46090, 56779, 67466, 78155, 88842, 99529, 110218, 120905, 131594, 142281, 152969, 163657, 174344, 185032, 195721, 206408, 217097, 227784, 238471, 249159, 259847, 270536, 281223, 291911, 302599, 313286, 323973, 334663, 345350, 356038, 366726, 377413, 388101,
                                    398788, 409478, 420165, 430852, 441541, 452228, 462917, 473605, 484292, 494980, 505668, 516355, 527043, 537730, 548420, 559107, 569794, 580483, 591170, 601859, 612547, 623234, 633922, 644609, 655297, 665985, 676672, 687362, 698049, 708736, 719424, 730112, 740801, 751488, 762176, 772864, 783551]]
    hit0 = 1
    data1 = [int(i*1.050) for i in [0, 92182, 113557, 134934, 156309, 177684, 199060, 220436, 241812, 263188, 284563, 305939, 327314, 348691, 370065, 391441, 412818, 434193, 455569, 476943, 498320, 519695, 541072, 562447, 583822, 605198, 626574, 647949, 669325, 690701, 712077, 733452, 754827, 776204, 797579, 818956,
                                    840330, 861706, 883082, 904458, 925834, 947208, 968585, 989961, 1011336, 1032711, 1054087, 1075463, 1096840, 1118215, 1139590, 1160965, 1182342, 1203717, 1225092, 1246469, 1267844, 1289220, 1310595, 1331971, 1353347, 1374723, 1396099, 1417473, 1438849, 1460226, 1481601, 1502976, 1524352, 1545728, 1567103]]
    hit1 = 3
    data2 = [int(i*1.050) for i in [0, 23045, 28389, 33733, 39077, 44421, 49765, 55108, 60452, 65797, 71140, 76484, 81827, 87172, 92516, 97860, 103204, 108548, 113891, 119235, 124580, 129923, 135267, 140611, 145954, 151300, 156644, 161987, 167331, 172674, 178019, 183363, 188706, 194050, 199394,
                                    204738, 210082, 215426, 220769, 226114, 231459, 236802, 242146, 247490, 252833, 258177, 263522, 268865, 274209, 279552, 284896, 290242, 295585, 300929, 306273, 311616, 316961, 322305, 327648, 332992, 338336, 343680, 349024, 354368, 359711, 365056, 370401, 375744, 381088, 386431, 391775]]
    hit2 = 6
    CD = 290

    MP = [4025, 8055]
    无色消耗 = 15


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'grappler_female'
        self.名称 = '归元·柔道家'
        self.角色 = '格斗家(女)'
        self.职业 = '柔道家'
        # 用来筛CP武器的
        self.转职 = '柔道家(女)'
        self.武器选项 = ['手套', '臂铠', '东方棍', '爪']
        self.输出类型选项 = ['物理固伤']
        self.防具精通属性 = ['力量']
        self.类型 = '物理固伤'
        self.武器类型 = '臂铠'
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
        self.buff = 2.07

        super().__init__()
