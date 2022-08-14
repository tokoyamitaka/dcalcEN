from core.basic.skill import 技能
from core.basic.character import Character
from core.basic.skill import 主动技能, 被动技能


class 技能0(主动技能):
    名称 = '崩拳'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [30, 252]
    data0 = [(i*1.0) for i in [0, 3247, 3576, 3906, 4236, 4565, 4895, 5224, 5553, 5883, 6213, 6542, 6872, 7202, 7530, 7860, 8189, 8519, 8849, 9177, 9507, 9837, 10166, 10496, 10826, 11155, 11484, 11814, 12143, 12473, 12802, 13132, 13462, 13790, 14120, 14450, 14779, 15109, 15439, 15767, 16097, 16427, 16756, 17086, 17415, 17744, 18074, 18403, 18733, 19063, 19392, 19722, 20051, 20380, 20710, 21040, 21369, 21699, 22027, 22357, 22687, 23016, 23346, 23676, 24004, 24334, 24664, 24993, 25323, 25653, 25981]]
    hit0 = 1
    CD = 6.0
    TP成长 = 0.1
    TP上限 = 7


class 技能1(被动技能):
    名称 = '拳套精通'
    所在等级 = 15
    等级上限 = 10
    基础等级 = 10
    # 拳套精通cd
    关联技能 = ['无']
    冷却关联技能 = ['崩拳', '铁山靠', '碎骨', '寸拳', '升龙拳', '闪电之舞', '纷影连环踢', '破碎拳', '回天连环击', '虎啸神拳', '无影脚', '雷霆之舞']

    def 加成倍率(self, 武器类型):
        return 1.0

    def CD缩减倍率(self, 武器类型):
        if 武器类型 == '拳套':
            if self.等级 == 0:
                return 1.0
            else:
                return (1 - 0.01 * self.等级)
        else:
            return 1.0


class 技能2(主动技能):
    名称 = '铁山靠'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [50, 420]
    data0 = [(i*1.0) for i in [0, 4708, 5186, 5663, 6141, 6618, 7096, 7573, 8051, 8528, 9006, 9484, 9962, 10440, 10917, 11395, 11873, 12350, 12828, 13305, 13783, 14260, 14738, 15215, 15693, 16172, 16649, 17127, 17604, 18082, 18559, 19037, 19515, 19992, 20470, 20947, 21425, 21902, 22380, 22859, 23336, 23814, 24291, 24769, 25246, 25724, 26202, 26679, 27157, 27634, 28112, 28589, 29068, 29546, 30023, 30501, 30978, 31456, 31933, 32411, 32888, 33366, 33844, 34321, 34799, 35277, 35755, 36233, 36710, 37188, 37665]]
    hit0 = 1
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 7
    演出时间 = 0.5


class 技能3(主动技能):
    名称 = '碎骨'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [50, 420]
    data0 = [(i*1.0) for i in [0, 4811, 5300, 5787, 6276, 6764, 7252, 7740, 8229, 8716, 9205, 9694, 10181, 10669, 11158, 11645, 12134, 12623, 13110, 13599, 14087, 14575, 15063, 15552, 16039, 16528, 17015, 17504, 17992, 18480, 18968, 19457, 19944, 20433, 20921, 21409, 21897, 22386, 22873, 23362, 23850, 24338, 24826, 25315, 25802, 26291, 26780, 27267, 27756, 28244, 28732, 29220, 29709, 30196, 30685, 31173, 31661, 32149, 32637, 33125, 33614, 34101, 34590, 35078, 35566, 36054, 36543, 37030, 37519, 38007, 38495]]
    hit0 = 1
    CD = 7.0
    TP成长 = 0.1
    TP上限 = 7


class 技能4(被动技能):
    名称 = '柔化肌肉'
    所在等级 = 30
    等级上限 = 15
    基础等级 = 5

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        return round(1.125 + 0.015 * self.等级, 5)


class 技能5(被动技能):
    名称 = '弱点感知'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级 <= 10:
                return round(1.01 + 0.01 * self.等级, 5)
            else:
                return round(1.11 + 0.02 * (self.等级-10), 5)


class 技能6(主动技能):
    名称 = '升龙拳'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [(i*1.0) for i in [0, 2326, 2562, 2798, 3034, 3270, 3506, 3742, 3978, 4214, 4450, 4686, 4922, 5158, 5394, 5630, 5866, 6102, 6337, 6573, 6809, 7045, 7281, 7517, 7753, 7989, 8225, 8461, 8697, 8933, 9169, 9405, 9641, 9877, 10113, 10349, 10585, 10821, 11057, 11293, 11529, 11765, 12001, 12237, 12473, 12709, 12945, 13181, 13417, 13653, 13889, 14125, 14361, 14597, 14833, 15069, 15305, 15541, 15777, 16013, 16249, 16485, 16721, 16957, 17192, 17428, 17664, 17900, 18136, 18372, 18608]]
    hit0 = 4
    data1 = [(i*1.0) for i in [0, 2015, 2219, 2423, 2628, 2832, 3037, 3241, 3445, 3651, 3855, 4058, 4264, 4468, 4673, 4877, 5081, 5286, 5490, 5695, 5899, 6103, 6308, 6512, 6716, 6921, 7125, 7331, 7535, 7739, 7944, 8148, 8352, 8557, 8761, 8966, 9170, 9374, 9579, 9783, 9988, 10192, 10396, 10602, 10806, 11010, 11215, 11419, 11624, 11828, 12032, 12237, 12441, 12645, 12850, 13054, 13259, 13463, 13667, 13873, 14077, 14281, 14486, 14690, 14895, 15099, 15303, 15508, 15712, 15917, 16121]]
    hit1 = 1
    CD = 20
    TP成长 = 0.1
    TP上限 = 5
    演出时间 = 2.0

    MP = [170, 1428]
    无色消耗 = 1


class 技能7(主动技能):
    名称 = '寸拳'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [(i*1.0) for i in [0, 10762, 11853, 12945, 14037, 15129, 16221, 17312, 18404, 19495, 20588, 21680, 22771, 23864, 24955, 26047, 27139, 28230, 29323, 30414, 31506, 32597, 33690, 34782, 35873, 36965, 38056, 39149, 40241, 41332, 42424, 43516, 44608, 45699, 46791, 47884, 48975, 50067, 51158, 52250, 53343, 54434, 55526, 56617, 57710, 58801, 59893, 60985, 62076, 63169, 64260, 65352, 66444, 67536, 68628, 69719, 70811, 71902, 72995, 74087, 75178, 76270, 77362, 78454, 79546, 80637, 81730, 82821, 83913, 85004, 86096]]
    hit0 = 1
    CD = 15
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 0.5

    MP = [130, 1092]
    无色消耗 = 1

    def 装备护石(self):
        self.倍率 = 1.33


class 技能8(主动技能):
    名称 = '闪电之舞'
    所在等级 = 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [(i*1.0) for i in [0, 2331, 2567, 2804, 3040, 3277, 3513, 3750, 3986, 4223, 4461, 4697, 4934, 5170, 5407, 5643, 5880, 6116, 6353, 6589, 6826, 7062, 7299, 7535, 7772, 8008, 8245, 8481, 8718, 8954, 9191, 9427, 9664, 9900, 10137, 10373, 10611, 10847, 11084, 11320, 11557, 11793, 12030, 12266, 12503, 12739, 12976, 13212, 13449, 13685, 13922, 14158, 14395, 14631, 14868, 15104, 15341, 15577, 15814, 16050, 16287, 16523, 16761, 16997, 17234, 17470, 17707, 17943, 18180, 18416, 18653]]
    hit0 = 7
    CD = 20
    TP成长 = 0.1
    TP上限 = 5
    演出时间 = 1
    是否有护石 = 1
    演出时间 = 2.2

    MP = [180, 1512]
    无色消耗 = 1

    def 装备护石(self, x):
        self.hit0 += 2
        self.倍率 = 0.99
        self.CDR *= 0.85
        self.演出时间 = 2.7


class 技能9(主动技能):
    名称 = '纷影连环踢'
    所在等级 = 45
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [(i*1.0) for i in [0, 741, 817, 892, 968, 1042, 1118, 1193, 1269, 1343, 1419, 1494, 1570, 1645, 1720, 1795, 1871, 1946, 2021, 2096, 2172, 2247, 2323, 2397, 2473, 2548, 2624, 2698, 2774, 2849, 2925, 2999, 3075, 3150, 3226, 3300, 3376, 3451, 3527, 3601, 3677, 3752, 3828, 3903, 3978, 4053, 4129, 4204, 4279, 4354, 4430, 4505, 4581, 4655, 4731, 4806, 4882, 4956, 5032, 5107, 5183, 5257, 5333, 5408, 5484, 5558, 5634, 5709, 5785, 5859, 5935]]
    hit0 = 10
    data1 = [(i*1.0) for i in [0, 16460, 18131, 19801, 21471, 23141, 24810, 26480, 28150, 29821, 31491, 33161, 34831, 36500, 38170, 39840, 41511, 43181, 44851, 46520, 48190, 49860, 51530, 53201, 54871, 56540, 58210, 59880, 61550, 63221, 64891, 66561, 68230, 69900, 71570, 73240, 74911, 76581, 78250, 79920, 81590, 83260, 84930, 86601, 88270, 89940, 91610, 93280, 94950, 96619, 98291, 99960, 101630, 103300, 104970, 106640, 108311, 109980, 111650, 113320, 114990, 116660, 118329, 120000, 121670, 123340, 125010, 126680, 128349, 130019, 131690]]
    hit1 = 1
    CD = 40.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 4

    MP = [400, 3360]
    无色消耗 = 2

    def 装备护石(self):
        self.hit0 = 20
        self.power0 = 0.77
        self.power1 = 1.21
        self.演出时间 = 4.4


class 技能10(被动技能):
    名称 = '武神步'
    所在等级 = 48
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        return round(1.05 + 0.02 * self.等级, 5)


class 技能11(主动技能):
    名称 = '武神强踢'
    所在等级 = 50
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [(i*1.0) for i in [0, 57363, 70663, 83964, 97267, 110568, 123870, 137173, 150474, 163774, 177076, 190378, 203680, 216980, 230281, 243584, 256885, 270187, 283489, 296791, 310091, 323392, 336695, 349996, 363297, 376599, 389901, 403202, 416504, 429805, 443108, 456408, 469709, 483012, 496313, 509613, 522916, 536217, 549519, 562820, 576122, 589424, 602725, 616027, 629327, 642630, 655930, 669233, 682534, 695836, 709137, 722439, 735741, 749041, 762344, 775644, 788947, 802247, 815550, 828851, 842152, 855455, 868755, 882058, 895358, 908661, 921961, 935264, 948565, 961866, 975167]]
    hit0 = 1
    CD = 145.0
    演出时间 = 0.5

    MP = [900, 7560]
    无色消耗 = 5

    # 6级特效+10%强踢攻击力,体现在技能面板上
    #def 等效百分比(self, 武器类型):
        #if self.等级 >= 6:
            #self.倍率 *= 1.1
        #return super().等效百分比(武器类型)


class 技能12(主动技能):
    名称 = '破碎拳'
    所在等级 = 60
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [(i*1.0) for i in [0, 24876, 27398, 29922, 32446, 34969, 37493, 40016, 42540, 45064, 47587, 50111, 52635, 55158, 57682, 60205, 62729, 65253, 67776, 70300, 72824, 75347, 77871, 80395, 82918, 85442, 87965, 90489, 93013, 95536, 98060, 100584, 103107, 105631, 108155, 110678, 113202, 115725, 118249, 120773, 123296, 125820, 128344, 130867, 133391, 135915, 138438, 140962, 143485, 146009, 148533, 151056, 153580, 156104, 158626, 161151, 163675, 166197, 168721, 171244, 173768, 176292, 178815, 181339, 183863, 186386, 188910, 191433, 193957, 196481, 199004]]
    hit0 = 1
    CD = 30
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.5

    MP = [450, 1260]
    无色消耗 = 1

    def 装备护石(self):
        self.倍率 = 1.28


class 技能13(主动技能):
    名称 = '回天连环击'
    所在等级 = 70
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    # 横扫地面攻击力：<data0>%
    data0 = [(i*1.0) for i in [0, 3776, 4160, 4543, 4926, 5309, 5693, 6075, 6459, 6842, 7225, 7608, 7992, 8374, 8758, 9141, 9524, 9907, 10291, 10673, 11057, 11440, 11824, 12206, 12590, 12972, 13356, 13739, 14123, 14505, 14889, 15271, 15655, 16038, 16422, 16804, 17188, 17570, 17954, 18337, 18721, 19103, 19487, 19869, 20253, 20636, 21020, 21402, 21786, 22168, 22552, 22935, 23319, 23701, 24085, 24467, 24851, 25234, 25618, 26000, 26384, 26766, 27150, 27533, 27917, 28299, 28683, 29065, 29449, 29832, 30216]]
    hit0 = 1
    # 寸劲攻击力：<data1>%
    data1 = [(i*1.0) for i in [0, 7834, 8628, 9423, 10218, 11012, 11806, 12602, 13397, 14191, 14986, 15781, 16576, 17370, 18165, 18961, 19755, 20549, 21344, 22139, 22933, 23729, 24523, 25318, 26112, 26908, 27703, 28497, 29291, 30086, 30882, 31676, 32471, 33266, 34061, 34855, 35650, 36445, 37239, 38033, 38829, 39624, 40418, 41213, 42009, 42802, 43597, 44392, 45188, 45982, 46777, 47572, 48368, 49163, 49958, 50754, 51549, 52345, 53140, 53935, 54731, 55526, 56321, 57117, 57912, 58707, 59503, 60298, 61093, 61889, 62684]]
    hit1 = 1
    # 正拳攻击力：<data2>%
    data2 = [(i*1.0) for i in [0, 11634, 12814, 13995, 15175, 16354, 17536, 18715, 19896, 21075, 22257, 23436, 24616, 25798, 26978, 28158, 29337, 30519, 31698, 32879, 34059, 35240, 36420, 37599, 38781, 39960, 41141, 42321, 43502, 44682, 45862, 47042, 48223, 49403, 50584, 51763, 52945, 54124, 55304, 56485, 57665, 58846, 60025, 61207, 62386, 63567, 64746, 65928, 67107, 68287, 69469, 70651, 71833, 73015, 74196, 75378, 76560, 77742, 78924, 80106, 81287, 82469, 83651, 84833, 86015, 87196, 88378, 89560, 90742, 91924, 93106]]
    hit2 = 1
    # 环绕攻击力：<data3>%
    data3 = [(i*1.0) for i in [0, 15262, 16811, 18360, 19909, 21457, 23005, 24553, 26102, 27650, 29199, 30747, 32296, 33844, 35393, 36941, 38490, 40038, 41587, 43135, 44684, 46231, 47779, 49329, 50878, 52426, 53975, 55523, 57070, 58619, 60168, 61716, 63266, 64814, 66363, 67910, 69459, 71007, 72556, 74104, 75653, 77201, 78751, 80298, 81847, 83395, 84944, 86492, 88041, 89589, 91136, 92683, 94231, 95778, 97325, 98872, 100419, 101967, 103514, 105061, 106608, 108155, 109703, 111250, 112797, 114344, 115891, 117438, 118986, 120533, 122080]]
    hit3 = 1
    CD = 50
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 2.2

    MP = [935, 1960]
    无色消耗 = 2

    def 装备护石(self):
        self.hit0 = 0
        self.power1 = 1.42
        self.power2 = 1.42
        self.power3 = 1.28


class 技能14(主动技能):
    名称 = '虎啸神拳'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [(i*1.0) for i in [0, 2140, 2357, 2574, 2792, 3008, 3226, 3442, 3660, 3877, 4094, 4312, 4528, 4746, 4962, 5180, 5398, 5614, 5832, 6048, 6266, 6482, 6700, 6918, 7134, 7352, 7568, 7786, 8004, 8220, 8438, 8654, 8872, 9088, 9306, 9524, 9740, 9958, 10174, 10392, 10610, 10826, 11044, 11260, 11478, 11694, 11912, 12130, 12346, 12564, 12780, 12998, 13215, 13432, 13650, 13866, 14084, 14300, 14518, 14735, 14952, 15170, 15386, 15604, 15821, 16038, 16255, 16472, 16690, 16906, 17124]]
    hit0 = 1
    data1 = [(i*1.0) for i in [0, 20913, 23035, 25157, 27279, 29399, 31521, 33643, 35765, 37887, 40008, 42130, 44251, 46373, 48495, 50617, 52738, 54860, 56982, 59104, 61226, 63346, 65468, 67590, 69712, 71834, 73955, 76077, 78199, 80320, 82442, 84563, 86685, 88807, 90929, 93051, 95171, 97293, 99415, 101537, 103659, 105780, 107902, 110024, 112146, 114268, 116388, 118510, 120632, 122754, 124876, 126997, 129119, 131240, 133362, 135484, 137605, 139727, 141849, 143971, 146093, 148213, 150335, 152457, 154579, 156701, 158822, 160944, 163066, 165188, 167309]]
    hit1 = 1
    data2 = [(i*1.0) for i in [0, 5527, 6087, 6648, 7208, 7770, 8331, 8891, 9452, 10013, 10573, 11134, 11695, 12256, 12817, 13377, 13938, 14498, 15059, 15620, 16181, 16742, 17302, 17863, 18424, 18984, 19545, 20107, 20667, 21228, 21788, 22349, 22909, 23470, 24032, 24592, 25153, 25714, 26274, 26835, 27395, 27957, 28518, 29078, 29639, 30199, 30760, 31321, 31882, 32443, 33003, 33564, 34125, 34685, 35246, 35806, 36368, 36929, 37489, 38050, 38610, 39171, 39732, 40293, 40854, 41415, 41975, 42536, 43096, 43657, 44219]]
    hit2 = 1
    CD = 40.0
    是否有护石 = 1

    MP = [580, 4500]
    无色消耗 = 3

    def 装备护石(self):
        self.hit0 = 15*2
        self.power0 = 0.83


class 技能15(被动技能):
    名称 = '神武之力'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        return round(1.22 + 0.02 * self.等级, 5)


class 技能16(主动技能):
    名称 = '无影脚'
    所在等级 = 80
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    # 扫腿攻击力：<int>%
    data0 = [(i*1.0) for i in [0, 6749, 7433, 8118, 8801, 9486, 10171, 10855, 11539, 12225, 12909, 13594, 14280, 14964, 15648, 16332, 17018, 17702, 18386, 19072, 19756, 20439, 21126, 21810, 22494, 23179, 23864, 24548, 25233, 25917, 26602, 27286, 27973, 28657, 29341, 30026, 30711, 31394, 32079, 32763, 33447, 34133, 34818, 35503, 36188, 36872, 37556, 38241, 38926, 39610, 40294, 40980, 41665, 42349, 43034, 43718, 44402, 45088, 45772, 46456, 47141, 47826, 48510, 49194, 49881, 50565, 51249, 51935, 52619, 53303, 53988]]
    hit0 = 1
    # 第2击物理攻击力：<data1>%
    data1 = [(i*1.0) for i in [0, 3412, 3757, 4103, 4450, 4796, 5141, 5487, 5834, 6179, 6525, 6872, 7218, 7564, 7909, 8256, 8601, 8947, 9294, 9641, 9987, 10334, 10678, 11024, 11370, 11717, 12063, 12409, 12756, 13101, 13446, 13792, 14139, 14485, 14831, 15178, 15524, 15870, 16216, 16563, 16908, 17254, 17600, 17946, 18292, 18638, 18985, 19331, 19676, 20022, 20368, 20714, 21060, 21408, 21754, 22098, 22445, 22791, 23137, 23484, 23830, 24176, 24520, 24868, 25213, 25559, 25906, 26252, 26598, 26943, 27291]]
    hit1 = 1
    # 第3击物理攻击力：<data2>%
    data2 = [(i*1.0) for i in [0, 3415, 3762, 4109, 4455, 4801, 5148, 5495, 5841, 6189, 6535, 6881, 7226, 7573, 7921, 8266, 8613, 8959, 9306, 9653, 9999, 10345, 10692, 11039, 11385, 11733, 12079, 12424, 12772, 13118, 13465, 13812, 14158, 14504, 14850, 15198, 15544, 15890, 16237, 16584, 16930, 17277, 17624, 17968, 18317, 18662, 19010, 19357, 19702, 20048, 20395, 20742, 21088, 21435, 21781, 22128, 22475, 22821, 23168, 23513, 23861, 24207, 24554, 24901, 25246, 25593, 25940, 26287, 26633, 26980, 27326]]
    hit2 = 1
    # 抽打物理攻击力：<int>%
    data3 = [(i*1.0) for i in [0, 53359, 58772, 64184, 69598, 75012, 80425, 85838, 91251, 96664, 102076, 107490, 112903, 118316, 123731, 129143, 134556, 139970, 145384, 150795, 156209, 161623, 167036, 172450, 177863, 183275, 188689, 194103, 199515, 204928, 210343, 215756, 221168, 226581, 231995, 237407, 242820, 248234, 253648, 259061, 264474, 269887, 275300, 280714, 286127, 291539, 296954, 302368, 307779, 313193, 318607, 324018, 329432, 334845, 340259, 345673, 351085, 356499, 361912, 367325, 372738, 378151, 383565, 388979, 394392, 399804, 405218, 410631, 416043, 421457, 426871]]
    hit3 = 1
    CD = 45.0
    是否有护石 = 1
    演出时间 = 2

    MP = [800, 6000]
    无色消耗 = 5

    def 装备护石(self):
        self.hit0 = 0
        self.hit1 = 0
        self.hit2 = 0
        self.power3 = 1.66


class 技能17(主动技能):
    名称 = '极尽霸皇断空拳'
    备注 = '直击'
    所在等级 = 85
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    # 断空拳物理攻击力：<data0>%
    data0 = [(i*1.0) for i in [0, 135271, 166638, 198004, 229371, 260738, 292106, 323473, 354840, 386207, 417575, 448941, 480309, 511677, 543043, 574411, 605778, 637145, 668512, 699879, 731246, 762614, 793981, 825348, 856716, 888082, 919450, 950817, 982184, 1013551, 1044919, 1076286, 1107653, 1139021, 1170387, 1201755, 1233122, 1264489, 1295854, 1327221, 1358589, 1389956, 1421323, 1452690, 1484058, 1515424, 1546792, 1578160, 1609526, 1640894, 1672261, 1703628, 1734995, 1766362, 1797729, 1829097, 1860464, 1891831, 1923199, 1954565, 1985933, 2017300, 2048667, 2080034, 2111402, 2142769, 2174136, 2205504, 2236870, 2268238, 2299605]]
    hit0 = 1
    CD = 180.0
    演出时间 = 1.2

    MP = [2500, 5000]
    无色消耗 = 10


class 技能18(主动技能):
    名称 = '雷霆之舞'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    # 第1~7击物理攻击力：<int>%
    data0 = [(i*1.0) for i in [0, 13029, 14351, 15672, 16995, 18316, 19638, 20959, 22282, 23603, 24925, 26248, 27569, 28891, 30213, 31535, 32856, 34178, 35500, 36822, 38143, 39466, 40787, 42109, 43430, 44753, 46074, 47396, 48719, 50040, 51362, 52684, 54006, 55327, 56650, 57971, 59293, 60614, 61937, 63258, 64580, 65901, 67224, 68546, 69867, 71190, 72511, 73833, 75155, 76477, 77798, 79121, 80442, 81764, 83085, 84408, 85729, 87051, 88374, 89695, 91017, 92338, 93661, 94982, 96304, 97626, 98948, 100269, 101592, 102913, 104235]]
    hit0 = 7
    # 最后一击物理攻击力：<int>%
    data1 = [(i*1.0) for i in [0, 39088, 43053, 47019, 50984, 54950, 58916, 62881, 66847, 70811, 74777, 78743, 82708, 86674, 90639, 94605, 98571, 102535, 106501, 110466, 114432, 118397, 122363, 126329, 130294, 134260, 138224, 142190, 146156, 150121, 154087, 158052, 162018, 165984, 169949, 173915, 177879, 181845, 185811, 189776, 193742, 197707, 201673, 205639, 209603, 213569, 217534, 221500, 225466, 229431, 233397, 237362, 241328, 245294, 249258, 253224, 257189, 261155, 265121, 269086, 273052, 277017, 280983, 284949, 288913, 292879, 296844, 300810, 304776, 308741, 312707]]
    hit1 = 1
    CD = 60.0
    演出时间 = 6.2

    MP = [870, 6750]
    无色消耗 = 7



class 技能19(被动技能):
    名称 = '疾风劲'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能20(主动技能):
    名称 = '陨星灭天击'
    所在等级 = 100
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    # 地面强击物理攻击力：<int>%
    data0 = [(i*1.0) for i in [0, 41602, 51248, 60895, 70542, 80188, 89835, 99482, 109129, 118776, 128422, 138069, 147716, 157362, 167009, 176656, 186303, 195950, 205596, 215243, 224890, 234537, 244184, 253830, 263476, 273123, 282770, 292417, 302064, 311710, 321357, 331004, 340651, 350297, 359944, 369591, 379238, 388885, 398531, 408178, 417825, 427472, 437119, 446764, 456411, 466058, 475705, 485352, 494998, 504645, 514292, 523939, 533586, 543232, 552879, 562526, 572173, 581820, 591466, 601113, 610760, 620407, 630054, 639701, 649346, 658993, 668640, 678287, 687934, 697580, 707227]]
    hit0 = 1
    # 上踢物理攻击力：<int>%
    data1 = [(i*1.0) for i in [0, 41602, 51248, 60895, 70542, 80188, 89835, 99482, 109129, 118776, 128422, 138069, 147716, 157362, 167009, 176656, 186303, 195950, 205596, 215243, 224890, 234537, 244184, 253830, 263476, 273123, 282770, 292417, 302064, 311710, 321357, 331004, 340651, 350297, 359944, 369591, 379238, 388885, 398531, 408178, 417825, 427472, 437119, 446764, 456411, 466058, 475705, 485352, 494998, 504645, 514292, 523939, 533586, 543232, 552879, 562526, 572173, 581820, 591466, 601113, 610760, 620407, 630054, 639701, 649346, 658993, 668640, 678287, 687934, 697580, 707227]]
    hit1 = 2
    # 回旋踢物理攻击力：<int>%
    data2 = [(i*1.0) for i in [0, 83203, 102495, 121789, 141083, 160376, 179670, 198963, 218257, 237551, 256844, 276138, 295431, 314724, 334018, 353311, 372605, 391899, 411192, 430486, 449779, 469073, 488367, 507659, 526952, 546246, 565540, 584833, 604127, 623420, 642714, 662007, 681301, 700594, 719888, 739182, 758475, 777769, 797062, 816356, 835650, 854943, 874237, 893528, 912822, 932116, 951409, 970703, 989996, 1009290, 1028584, 1047877, 1067171, 1086464, 1105758, 1125052, 1144345, 1163639, 1182932, 1202226, 1221520, 1240813, 1260107, 1279401, 1298692, 1317986, 1337279, 1356573, 1375867, 1395160, 1414454]]
    hit2 = 1
    # 终结攻击物理攻击力：<int>% x 6
    data3 = [(i*1.0) for i in [0, 208008, 256236, 304471, 352706, 400939, 449174, 497406, 545641, 593876, 642109, 690343, 738578, 786810, 835045, 883278, 931513, 979747, 1027980, 1076215, 1124448, 1172682, 1220917, 1269146, 1317380, 1365614, 1413848, 1462083, 1510316, 1558550, 1606783, 1655018, 1703253, 1751485, 1799719, 1847954, 1896187, 1944422, 1992655, 2040889, 2089124, 2137357, 2185592, 2233820, 2282055, 2330290, 2378523, 2426758, 2474990, 2523225, 2571459, 2619693, 2667927, 2716160, 2764395, 2812629, 2860862, 2909097, 2957329, 3005564, 3053799, 3102032, 3150266, 3198501, 3246730, 3294964, 3343197, 3391432, 3439667, 3487899, 3536134]]
    hit3 = 1
    CD = 290

    MP = [4028, 8056]
    无色消耗 = 15


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'striker_female'
        self.名称 = '归元·散打'
        self.角色 = '格斗家(女)'
        self.角色类型 = '输出'
        self.职业 = '散打'
        # 用来筛CP武器的
        self.转职 = '散打(女)'
        self.武器选项 = ['拳套']
        self.输出类型选项 = ['物理百分比']
        self.防具精通属性 = ['力量']
        self.类型 = '物理百分比'
        self.武器类型 = '拳套'
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
        self.buff = 2.13

        super().__init__()
