from core.basic.property import CharacterProperty
from core.equipment.property import 成长词条计算

entry_func_list = {}  # id : enteyfunc 词条函数(数组)列表
entry_chose = []  # (20000 + id, [chose1, 2, 3...]) 额外选项设置，参考20074消灭敌人词条
multi_select = {}  # id : True/False 设置选项是否支持多选
variable_set = {}  # id : setfunc  参数返回设置函数

# region 无效果词条

zs_bd_rate = 0


def set_zs_bd_rate(x):
    global zs_bd_rate
    zs_bd_rate = x[0]/100


entry_chose.append((20000, ["冰冻结算灼烧比例：{}%".format(str(i))
                            for i in range(0, 101)], ""))
multi_select[20000] = False
variable_set[20000] = set_zs_bd_rate


def entry_980(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['拥有该装备属性的队员之间获得以下效果。', '- 互相分摊所受伤害。', '- 受到其他队员的被击伤害时， 增加自身2%的攻击速度、 施放速度， 效果持续5秒。 (最多叠加5次)', '被击伤害 +10%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1247(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['技能MP消耗量 -50%', '被击时，所受伤害 +15%']
    if mode == 0:
        char.MP消耗量加成(-0.5)
        pass
    if mode == 1:
        pass


def entry_1248(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['生成自动恢复到HP45%的保护罩。（若10秒内未被攻击，则保护罩会在10秒内恢复到最大值）', '进入地下城时，锁定可使用的HP最大值的45%。(恢复HP时无法超过锁定之后的HP值)']
    if mode == 0:
        pass
    if mode == 1:
        global hp_rate_num
        hp_rate_num = min(55, hp_rate_num)
        pass


def entry_1232(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['上一次赋予敌人的控制型异常状态将变为下一次韧性条的弱点属性。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1226(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被非破招攻击时所受伤害 +20%', '被破招攻击时所受伤害 -20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1227(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身进入睡眠状态时， 无法使用消耗品并获得无敌Buff， 效果持续10秒。 (冷却时间30秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1228(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['受到总HP15%以上的伤害时， 使500px范围内的敌人进入石化状态。 (冷却时间30秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1221(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身每被施加1种异常状态， 被击时减少5%的所受伤害。  (最多减少30%)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1213(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身中毒状态下， 攻击时使敌人进入中毒状态。 (冷却时间5秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '中毒' in own_state_type and '中毒' not in state_type:
            state_type.append('中毒')
        pass


def entry_1210(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身石化状态下， 被击时使500px范围内所有敌人进入石化状态。 (冷却时间30秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1211(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['睡眠期间， 受到伤害不会醒来。', '睡眠状态下， 被击时恢复15%的HP。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1206(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身进入出血状态时， 攻击10次时， 10秒内恢复15%的HP。 (冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1207(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身出血状态下， 攻击时使敌人进入出血状态。 (冷却时间8秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '出血' in own_state_type and '出血' not in state_type:
            state_type.append('出血')
        pass


def entry_1209(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身进入石化时所受伤害 -30%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1201(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身冰冻状态下， 所受伤害减少30%， 5秒内恢复20%的HP。 (冷却时间5秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1192(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['装备的HP恢复效果 +10%', '被击时所受伤害 +20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1193(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['装备的HP恢复效果 +20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1194(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['装备的MP恢复效果 +30%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1195(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['装备时， 每20秒使自身的周围250px的敌人进入诅咒状态。', '维持前冲时， 诅咒范围逐渐增加， 每秒减少0.5%的HP。 (HP不会因该效果而降到1%以下)', '非前冲状态时， 诅咒范围逐渐减少。']
    if mode == 0:
        pass
    if mode == 1:
        if '诅咒' not in state_type:
            state_type.append('诅咒')
        pass


def entry_1196(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['穿戴时， 每20秒生成火焰Buff， 效果持续20秒。', '- 火焰Buff状态下， 赋予火属性攻击。', '被冰属性攻击时， 火焰Buff删除。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1189(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['周围250px内存在敌人时， 每秒恢复100点HP。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1184(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['待机、 行走、 前冲状态下， 输入[装备属性指令]时， 角色变小， 效果持续25秒。 (冷却时间60秒)', '- 角色大小 -50%', '- 回避率 +75%', '- 无法使用技能与基本攻击', '- 移动速度 +30%', '- 每秒恢复1%的HP和MP', '(持续时间内， 输入[装备属性指令]、 无法行动状态、 死亡、 强制发动技能时， 效果解除。 只有待机、 行走、 前冲状态下， 才能再次输入操作键解除效果)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1177(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['移动速度为100%以上时， Lv30以下技能攻击范围 +10%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1178(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['用下列技能精准阻挡敌人攻击时， 仅限1次技能增加30%的技能攻击力， 效果持续2秒。', '- [格挡]、 [招架]、 [格挡反击]、 [武器格挡]、 [盾牌格挡]、 [圣盾]、 [远程格挡]', '(施放该技能后0.5秒内阻挡敌人攻击， 被视作精准阻挡。)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1179(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['用下列技能精准阻挡敌人攻击时， 强制控制敌人2秒。', '- [格挡]、 [招架]、 [格挡反击]、 [武器格挡]、 [盾牌格挡]、 [圣盾]、 [远程格挡]', '(施放该技能后0.5秒内阻挡敌人攻击， 被视作精准阻挡。)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1182(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['云朵存在时，赋予武器冰属性攻击和暗属性攻击']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1167(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['物品栏负重上限 +2kg', 'HP MAX +300']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1168(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['物品栏负重上限 +3kg', 'MP MAX +500']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1170(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['消耗品、 装备的MP恢复效果 +10%', 'HP和MP每分钟恢复量固定为0。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1171(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['消耗品的MP恢复效果 +50%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1172(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['使用消耗品恢复HP时， 被击伤害减少20%， 效果持续30秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1163(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['伪装Buff状态下， 增加45%的回避率， 被击时所受伤害增加10%。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1165(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['物理防御力 +2000', '魔法防御力 -500']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1154(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['跳跃时， 可以再次跳跃。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1155(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['跳跃过程中， 进入霸体状态。 (落地时解除霸体)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1156(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['跳跃时，进入霸体状态']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1157(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['跳跃时，有1%的几率移除自身的异常状态(冷却时间60秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1158(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['跳跃状态下， 再次按住跳跃键(C)0.5秒， 可进入飞行状态， 获得下列效果， 持续5秒。 (冷却时间30秒)', '- 飞行期间按2次方向键， 可在空中前冲。 (最多2次)', '- 飞行期间， 进入霸体状态。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1159(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['跳跃状态下， 减少15%的被击伤害。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1160(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['跳跃状态下， 输入[装备属性指令]时， 乘坐旋风， 以悬空状态移动，  效果持续10秒。 (冷却时间40秒)', '- 依靠旋风之力， 吸附周围敌人。', '- 悬空状态下， 进入霸体状态。', '(持续时间内， 再次输入[装备属性指令]、 无法行动状态、 死亡、 强制发动技能时， 效果解除。 只有在悬空状态下， 才能再次输入[装备属性指令]解除效果)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1161(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['跳跃状态下， 增加10%攻击速度和15%的施放速度， 减少10%的移动速度。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1149(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[跃翔]Lv +5', '施放[跃翔]时， 进入霸体， 效果持续30秒。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1150(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['跳跃攻击时， 立即落地， 生成冲击波。 (冷却时间5秒)', '每100px的角色高度， 冲击波伤害增加2倍。 (最多适用300px)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1151(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['跳跃力 +100', '跳跃期间按拍卖行键， 立即开始下落， 并增加下落速度。 (冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1152(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['跳跃力 +50', '跳跃时，回避率 +3%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1140(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['死亡时，角色会哭泣', '复活后，攻击速度 +30%，施放速度 +45%，移动速度 +30%，效果持续30秒(冷却60秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1134(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['受身蹲伏状态下， 按方向键时2秒内隐藏在暗影中， 可以移动。 (冷却时间5秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1125(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['受到异常状态影响时，移除异常状态(冷却时间100 秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1126(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['受到超过总HP20%的伤害时， 减少25%的被击伤害， 效果持续10秒。 (冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


own_state_type = []
own_state_type_list = ['', '出血', '中毒', '灼烧', '感电', '眩晕',
                       '诅咒', '睡眠', '束缚', '冰冻', '减速', '石化', '失明', '混乱']


def set_own_state_type(x):
    global own_state_type
    own_state_type = []
    for i in x:
        own_state_type.append(own_state_type_list[i])


entry_chose.append((21127, ['选择自身异常状态'] + ['自身处于{}状态'.format(i)
                                           for i in own_state_type_list[1:]], ""))
variable_set[21127] = set_own_state_type


def entry_1127(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['受到超过总HP20%的伤害时， 使自身进入眩晕状态。 (冷却时间30秒)', '自身进入眩晕状态时， 增加20%的冷却时间恢复速度。 (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        if '眩晕' in own_state_type:
            char.技能恢复加成(0.2, 1, 100, [50, 85, 100])
        pass


def entry_1128(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['受到超过总HP25%的伤害时， 使周围300px范围内敌人进入眩晕状态。 (冷却时间20秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1129(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['受到总HP25%以上的伤害时， 生成相当于HP最大值25%的保护罩， 效果持续20秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1130(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['受到总HP25%以上的伤害时， 使自身进入石化状态。 (冷却时间20秒)', '自身进入石化状态时， 已使用技能的剩余冷却时间 -5%。 (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1131(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['受到总HP25%以上的伤害时， 使自身进入睡眠状态。 (冷却时间30秒)', '自身进入睡眠状态时， 技能、 消耗品的HP恢复效果增加50%。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1132(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['受身蹲伏的蹲伏姿势时， 无敌时间上限增加1秒。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1104(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放技能时， 按照MP消耗量的10%， 恢复相应的HP。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1107(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放技能时， 有10%的几率在剩余冷却时间低于20秒的技能中， 随机初始化其中1个技能的冷却时间。 (冷却时间20秒； 觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1097(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[后跳]期间， 所受伤害减少10%。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1098(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[后跳]期间， 增加200%的移动速度。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1099(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[后跳]时， 增加8%的攻击速度和施放速度， 效果持续10秒。 (最多叠加3次)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1100(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[后跳]时， 发动回避之吼， 落地前增加50%的回避率。 (3秒内可连续使用3次， 3秒之后属性发动冷却时间7秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1101(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['技能施放期间被击时， 技能不会强制中断， 而是继续进行。 (冷却时间10秒； 被控制时除外)', '技能施放期间被击时， 所受伤害 +15%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1075(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['生成草坪休息点，HP MAX +10%，持续30秒(冷却10秒，最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1076(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['生命值低于50%时，发动渔夫的祝福，回复20%的生命值(冷却时间40秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1065(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['待机、 行走、 前冲状态下， 输入[装备属性指令]时， 角色变大， 效果持续25秒。(冷却时间60秒)', '- 所受伤害 -20%', '- 无法使用技能与普通攻击。', '- 移动速度 -20%', '- 前冲状态下， 持续引发冲击波； 跳跃落地时， 引发更强大的冲击波。', '- 变大状态下， 进入霸体状态。', '(持续时间内， 再次输入[装备属性指令]、 进入无法行动状态、 死亡或强制发动技能时， 解除效果； 只有在待机、 行走、 前冲状态下才能通过再次输入[装备属性指令]解除效果)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1066(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['前冲攻击时， 疾跑至前方400px距离。 (冷却时间30秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1067(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['前冲期间， 每0.5秒减少3%的所受伤害。 (最多叠加10次； 停止时叠加次数减1)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1068(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['前冲时， 增加100%的移动速度， 效果持续0.5秒。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1069(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['前冲状态下， 增加20%的回避率。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1070(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['前冲状态下， 每0.2秒， 增加3%的移动速度。 (最多叠加15次； 非前冲状态下每0.5秒减少1次。)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1051(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['魔法防御力 +2000', '物理防御力 -500']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1043(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每累积消耗50个无色小晶块， 恢复10%的HP。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1038(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每次拾取掉落地面的道具时， 增加10%的移动速度， 效果持续10秒。 (最多叠加3次)', '每5秒， 减少5%的移动速度。 (最多叠加5次； 拾取道具时， 叠加层数初始化)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1039(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每攻击5次， 增加5%的攻击速度， 效果持续30秒。 (最多增加50%)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.05 * min(10, int(combo_num / 5)))
        pass


def entry_1024(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每30秒以相同几率消耗普通、 高级灵魂中的1个， 获得以下效果。', '- 消耗1个普通灵魂， 恢复10%的HP。', '- 消耗1个普通灵魂， 恢复10%的MP。', '- 消耗1个高级灵魂， 恢复10%的HP和MP。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1003(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['落地时， 生成相当于HP最大值10%的保护罩， 效果持续1秒。 (冷却时间5秒)', '跳跃力 -100']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1005(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['落地时引发冲击波， 对周围敌人造成伤害。', '发动冲击波时， 有30%的几率引发强大冲击波， 使敌人进入眩晕状态。 (冷却时间20秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1006(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每10%的回避率， 增加5%的移动速度。 (最多增加25%)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1007(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每10%的移动速度， 增加500点物理和魔法防御力。 (最多叠加20次)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1008(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每10%的移动速度， 增加1%的物理、 魔法暴击率。 (最多增加10%)', '移动速度 -30%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1009(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每10秒，HP MAX +100(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1010(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每10秒，MP MAX +100(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1000(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['在空中被击状态下， 按拍卖行键可恢复滞空姿势。 (冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1001(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['聊天输入包含“哇”的文字时， 召唤可搭乘的prototype-0。 (冷却时间120秒， 地图中存在已召唤的prototype-0时无法召唤。)', 'Prototype-0 持续时间 : 40秒', '消灭敌人时， 召唤冷却时间 -1秒', '施放技能时， 召唤冷却时间 -1秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_989(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['装备的HP恢复效果 +30%', '技能、消耗品的HP恢复效果 -10%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_992(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['角色进入灼伤、 中毒、 出血、 感电中1种以上的异常状态时， 攻击时有5%的几率使敌人进入和角色相同的异常状态。 (冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_993(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['睡眠状态下， 技能冷却时间恢复速度增加50%。 (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        if "睡眠" in own_state_type:
            char.技能恢复加成(1, 100, 0.5, [50, 85, 100])
        pass


def entry_994(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['角色进入睡眠状态时， 10秒内恢复60%的HP。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_995(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['角色所经之处生成寒冰迷雾， 持续3秒。 (冷却时间0.5秒； 跳跃、 使用技能时的移动不会生成)', '使寒冰迷雾中停留2秒的敌人进入冰冻状态。  (冷却时间25秒)']
    if mode == 0:
        pass
    if mode == 1:
        if "冰冻" not in state_type:
            state_type.append('冰冻')
        pass


def entry_996(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['角色所经之处生成火焰地带， 效果持续3秒。 (冷却时间0.5秒； 跳跃、 使用技能时的移动不会生成)', '使接触火焰地带的敌人进入灼伤状态。 (冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        if "灼烧" not in state_type:
            state_type.append('灼烧')
        pass


def entry_985(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['技能、 装备的HP恢复效果 +20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_977(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['火属性攻击时， 使敌人进入灼伤状态。 (冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_975(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['火、 冰、 光、 暗属性强化数值全部相同时， 赋予武器所有属性攻击。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_970(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击灼伤状态敌人时， 引发火属性爆炸。 (冷却时间1秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_968(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击灼伤状态敌人时， 使450px范围内所有敌人进入灼伤异常状态。(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_964(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击灼伤状态敌人时， 获得1个火种， 持续5秒。 (冷却时间0.1秒)', '火种达到5个时， 消耗所有火种， 引发爆炸。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_961(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击异常状态敌人时， 恢复1500点HP。 (冷却时间0.5秒)', '自身进入异常状态时， 减少2.5%的HP。 (HP不会因该效果而降到1%以下； 冷却时间20秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_962(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击异常状态敌人时， 恢复1%的HP。(冷却时间1秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_965(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击灼伤状态的敌人时， 除觉醒技能外的所有技能的剩余冷却时间减少0.5%。 (冷却时间0.5秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_966(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击灼伤状态敌人时， 使其进入冰冻状态。(冷却时间5秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_953(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时有15%几率扔出最多5个农作物', '每扔出一个农作物，增加3%的物理、魔法暴击率，效果持续30秒(最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_954(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时有3%几率使敌人进入冰冻状态，持续1秒(冷却时间1秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_955(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时有5%几率增加7%命中率，效果持续10秒(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_944(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 有50%的几率， 根据冰属性强化数值， 发动冰属性元素攻击。  (冷却时间5秒)', '- 冰属性强化在100~150之间 : 发动冰冻针刺。', '- 冰属性强化在150~250之间 : 发动冰冻吐息。', '- 冰属性强化超过250 : 发动暴雪。', '- 暴雪使命中敌人进入冰冻状态10秒。  (冷却时间30秒)', '- 发动暴雪时， 增加20点冰属性抗性， 效果持续30秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_945(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 有50%的几率， 根据光属性强化数值， 发动光属性元素攻击。  (冷却时间5秒)', '- 光属性强化在100~150之间 : 发动闪光爆炸。', '- 光属性强化在150~250之间 : 发动雷光链。', '- 光属性强化在250以上时发动雷暴。', '- 雷暴命中的敌人进入感电状态10秒。 (冷却时间15秒)', '- 发动雷暴时， 增加20的光属性抗性， 效果持续30秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_946(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 有50%的几率，根据火属性强化数值， 发动火属性元素攻击。 (冷却时间5秒)', '- 火属性强化在100~150之间 : 发动火焰爆炸。', '- 火属性强化在150~250之间 : 发动地炎。', '- 火属性强化超过250 : 发动陨石。', '- 陨石使命中的敌人进入灼伤状态10秒。 (冷却时间15秒)', '- 发动陨石时， 增加20点火属性抗性， 效果持续30秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_947(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 有50%的几率，根据暗属性强化数值， 发动暗属性元素攻击。 (冷却时间5秒)', '- 暗属性强化在100~150之间 : 发动暗黑爆炸。', '- 暗属性强化在150~250之间 : 发动暗黑球。', '- 暗属性强化超过250 : 发动黑洞。', '- 黑洞使命中敌人进入失明状态10秒。 (冷却时间30秒)', '发动黑洞时， 增加20点暗属性抗性， 效果持续30秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_948(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 有50%的几率生成黑白球， 持续10秒。 (冷却时间1秒)', '- 黑球 : 增加8%的攻击速度和12%的施放速度， 效果持续15秒。 (最多叠加3次)', '- 白球 : 生成相当于HP最大值10%的保护罩， 效果持续15秒。 (最多叠加1次)', '获得球时， 减少1%的HP和MP， 增加20%的移动速度， 效果持续15秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.08*3)
        char.移动速度增加(0.2)
        pass


def entry_949(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 增加1个电池。 (冷却时间10秒)', '每1个电池， 攻击强化 +667', '累积5个电池时， 引发强烈爆炸， 减少30%的HP， 并初始化电池数量。', '电池爆炸时， 减少20000点物理、 魔法防御力， 增加40%的攻击速度、 施放速度和移动速度， 效果持续30秒。', '施放[后跳]时， 减少1个电池。']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(667, lv)*4)
        pass


def entry_950(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 在自身脚下生成光之领域。', '站在光之领域上时， 减少10%的所受伤害。', '离开光之领域时， 光之领域立即删除。', '光之领域最多生成1个。', '- 站在光之领域上攻击20次时， 光之领域大小增加。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_951(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 生成幽灵。 (冷却时间0.5秒)', '- 幽灵追击周围200px内最近的敌人后， 引发爆炸。', '- 没有可追击的敌人时， 3秒后原地爆炸。', '- 生成幽灵时， 有30%的几率生成2个幽灵。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_952(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时有1%几率使敌人进入诅咒状态，持续3 秒(冷却时间1秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '诅咒' not in state_type:
            state_type.append('诅咒')
        pass


def entry_933(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 恢复0.1%的MP。 (冷却时间0.1秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_934(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 恢复3%的HP。 (冷却时间5秒)', '技能、 消耗品的HP恢复效果 -99%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_935(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 锁定可使用的HP最大值的10%， 攻击强化 +889 (冷却时间10秒； 最多叠加5次； HP不会因该装备效果而降低到1%以下； 恢复HP时无法超过锁定之后的HP值)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(889, lv)*5)
        pass


def entry_939(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 消耗2%的HP， 使周围500px内引发爆炸。 (冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_940(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 有20%的几率， 向300px范围内的敌人发动闪电。 (冷却时间1秒)', '闪电使命中的敌人进入感电状态。 (冷却时间15秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '感电' not in state_type:
            state_type.append('感电')
        pass


def entry_941(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时，有10%的几率扔出1个农作物(冷却20秒，最多存在1次)', '收获农作物时获得效果', '- 大白菜：恢复18%的HP', '- 巨型南瓜：恢复15%HP和 MP', '- 大萝卜：回复18%的MP', '- 巨枝：回复15%的HP，身体变得强壮，持续 30 秒', '- 大白菜：MP恢复15%，头脑变得清醒，持续30秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_942(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时，有3%的几率使敌人进入失明状态(冷却时间1秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '失明' not in state_type:
            state_type.append('失明')
        pass


def entry_926(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 发动暗属性爆炸， 对自身与敌人造成伤害。 (冷却时间5秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_927(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 发动冰属性爆炸， 对自身与敌人造成伤害。 (冷却时间5秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_928(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 发动光属性爆炸， 对自身与敌人造成伤害。 (冷却时间5秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_929(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 发动火属性爆炸， 对自身与敌人造成伤害。 (冷却时间5秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_931(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击异常状态的敌人时， 每1种异常状态， 增加4000点物理、 魔法防御力。 (最多叠加3次)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_919(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击感电状态的敌人时， 向周围300px内随机位置释放雷电， 使敌人与自身进入感电状态。 (冷却时间15秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '感电' in state_type and '感电' not in own_state_type:
            own_state_type.append('感电')
        pass


def entry_923(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击石化状态的敌人时， 积累伤害； 石化结束时， 一次性造成积累的伤害。', '- 每命中1个技能，累积伤害增幅2%。 (最多增幅20%)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_924(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 有2%的几率， 使300px范围内的敌人进入石化状态。 (冷却时间30秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_921(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击感电状态敌人时， 引发EMP冲击， 消耗2%的MP， 对敌人造成光属性伤害。 (冷却时间10秒)', '攻击感电状态的敌人时， EMP冲击冷却时间减少1秒。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_913(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['根据前冲持续时间， 获得攻击速度、 移动速度、 施放速度增加Buff， 效果持续20秒。 (效果从前冲结束后开始适用； 冷却时间20秒)', '- 前冲1秒以上 : 增加5%的攻击、 移动速度和7.5%的施放速度。', '- 前冲2秒以上 : 增加10%的攻击、 移动速度和15%的施放速度。', '- 前冲4秒以上 : 增加20%的攻击、 移动速度和30%的施放速度。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_915(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击50次领主、 稀有、 精英怪物时， 发动血管破裂， 使其剩余HP减少2%。 (最多5次， 辅助职业不发动)', '- 每次发动血管破裂时， 条件次数增加5倍。', '- 对领主发动血管破裂时， 增加15%的攻击速度、移动速度和22.5%的施放速度， 效果持续30秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_916(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击30次冰冻状态的敌人时， 冰冻异常状态的持续时间增加5秒。 (冷却时间15秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_918(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击感电状态敌人时， 引发闪光爆炸。 (冷却时间0.5秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_906(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['复活后，300秒内每次受到攻击，恢复10%的生命值(最多5次)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_889(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['穿戴时， 生成灵魂剑。', '使用技能时， 增加5个灵魂剑的灵魂能量。 (最多50个)', '普通攻击、 跳跃、 前冲攻击时， 消耗1个灵魂能量， 灵魂剑对敌人造成额外伤害。 (冷却时间0.1秒)', '灵魂能量达到最大时， 普通攻击、 跳跃、 前冲攻击时， 消耗所有灵魂能量， 灵魂剑对敌人造成额外伤害。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_890(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['地图中存在控制型异常状态的敌人时， 技能冷却时间恢复速度 +50% (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        for i in ['冰冻', '眩晕', '睡眠', '石化', '减速', '束缚', '失明', '混乱', '诅咒']:
            if i in state_type:
                char.技能恢复加成(1, 100, 0.5, [50, 85, 100])
                return
        pass


def entry_894(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['待机、 行走、 前冲状态下， 输入[装备属性指令]时， 瞬移至一定距离的位置。 (冷却时间20秒)', '- 瞬移时， 可按方向键调整方向。', '瞬移后， 增加30%的移动速度， 效果持续10秒。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_895(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['待机、 行走时， Y轴移动速度 +50%', '前冲时， Y轴移动速度 -50%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_896(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['待机、 行走时， 获得伪装Buff。 (Buff解除后再次适用的冷却时间为5秒)', '前冲、 被击时， 解除伪装Buff。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_897(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['待机、 行走时， 移动速度 +200%', '前冲时， 移动速度 -100%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_898(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['使敌人进入3个异常状态时， 使该敌人周围300px内的其他没有异常状态的敌人进入相同的异常状态。 (冷却时间3秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_900(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['直视自身周围300px以内敌人3秒时， 使敌人进入石化状态。 (冷却时间30秒)', '自身进入异常状态时， 减少2.5%的HP。 (HP不会因该效果而降到1%以下； 冷却时间20秒)', '攻击石化状态的敌人时， 技能攻击力 +5%']
    if mode == 0:
        pass
    if mode == 1:
        if '石化' in state_type:
            char.技能攻击力加成(part=part, x=0.05)
            pass


def entry_901(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['地图上有小太阳时，赋予武器光属性攻击和火属性攻击效果']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_880(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['草莓极光状态下，消耗品的HP恢复效果提高20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_874(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['冰属性攻击灼伤状态敌人时， 引发爆炸。 (冷却时间0.5秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_868(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被击时， 优先消耗MP。', '进入地下城时， 锁定可使用的HP最大值的99%。 (恢复HP时无法超过锁定之后的HP值)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_869(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被击时， 10秒内分摊所受伤害的50%。', '分摊受到伤害期间， 消耗品的HP恢复效果增加20%。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_870(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被正面被击时所受伤害 -40%', '被背击、 破招攻击时所受伤害 +20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_871(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['正面被击时， 有20%的几率生成相当于HP最大值10%的保护罩。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_862(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被击时， 向自身周围300px随机位置召唤无人机， 投放急救箱。', '(急救箱只能由发动者拾取； 冷却时间30秒)', '拾取急救箱后， 恢复30%的HP和MP。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_863(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被击时， 按跳跃键(C)， 从当前位置瞬移至一定距离。 (冷却时间10秒)', '- 瞬移时， 可按方向键调整方向。', '瞬移后， 恢复10%的HP。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_860(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被击时， 减少1点所有属性强化和1%的被击时所受伤害。 (最多叠加20次， 被击冷却时间2秒， 该属性的被击判定仅适用于受到总HP1%以上的伤害。)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_858(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被击时， 恢复5%的HP。 (冷却时间20秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_853(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被击后3秒内攻击敌人时， 根据攻击时间恢复所受伤害。 (冷却时间3秒)', '- 1秒内攻击时， 恢复所受伤害的70%。', '- 2秒内攻击时， 恢复所受伤害的50%。', '- 3秒内攻击时， 恢复所受伤害的20%。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_851(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被火属性攻击时， 5秒内恢复5%的HP。 (冷却时间3秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_848(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被攻击时，有25%的几率使自身受到惊吓，物理、魔法防御力 +10%，效果持续10秒(最多叠加2次)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_846(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被冰属性攻击时， 5秒内恢复5%的HP。 (冷却时间3秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_844(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被暗属性攻击时， 5秒内恢复5%的HP。 (冷却时间3秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_849(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被光属性攻击时， 5秒内恢复5%的HP。 (冷却时间3秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_393(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['破招攻击时，Lv1~30技能剩余冷却时间 -10%(冷却时间5秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_810(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['5秒内未攻击时所受伤害 -50%  (最多叠加1次； 攻击或施放技能时Buff解除)', '被破招攻击时所受伤害 +30%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_812(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['HP MAX +1500', 'MP MAX -200']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_834(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['Y轴移动速度 +20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_835(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['维持[受身蹲伏]时， 每秒恢复5%的HP， 最多持续4秒。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_839(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['暴击5次时， 使角色周围450px内所有敌人进入灼伤状态。 (冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '灼烧' not in state_type:
            state_type.append('灼烧')
        pass


def entry_842(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['背击5次时， 使角色周围450px内所有敌人进入中毒状态。 (冷却时间5秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '灼烧' not in state_type:
            state_type.append('灼烧')
        pass


def entry_343(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身移动速度超过100%以上时，HP、MP MAX +2000']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_345(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['命中率 +20%', 'HP、MP MAX -1200']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_368(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['装备保护罩效果 +20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_375(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['剩余MP在30%以下时，消耗10个无色小晶块，恢复30%的MP(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_384(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv20技能时，进入2秒霸体状态，霸体解除时，攻击速度+15%，施放速度+22.5%(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_385(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv25技能时，进入2秒霸体状态，霸体解除时，攻击速度+15%，施放速度+22.5%(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_386(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv30技能时，进入2秒霸体状态，霸体解除时，攻击速度+15%，施放速度+22.5%(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_0(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return "空词条"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['HP最大值 +600']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_2(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['HP最大值 +5%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_3(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['MP最大值 +945']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_4(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['MP MAX +5%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_5(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['物理防御力 +7000', '魔法防御力 +7000']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_6(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['物理防御力 +5%', '魔法防御力 +5%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_12(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每分钟恢复460.2点HP']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_13(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每分钟恢复348点MP']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_14(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['跳跃力 +20', '跳跃时， 增加30%的移动速度。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_24(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['背包负重 +5kg']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_35(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['敌人韧性减少量 +10%', '自身触发的束缚状态持续时间 +1秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_59(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时，有50%的几率使敌人进入灼伤状态(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '灼烧' not in state_type:
            state_type.append('灼烧')
        pass


def entry_60(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时，有50%的几率使敌人进入中毒状态(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '中毒' not in state_type:
            state_type.append('中毒')
        pass


def entry_61(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 有50%的几率使敌人进入出血状态。 (冷却时间8秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '出血' not in state_type:
            state_type.append('出血')
        pass


def entry_62(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 有50%的几率使敌人进入感电状态。 (冷却时间15秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '感电' not in state_type:
            state_type.append('感电')
        pass


def entry_63(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时，有50%的几率使敌人进入冰冻状态(冷却时间25秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '冰冻' not in state_type:
            state_type.append('冰冻')
        pass


def entry_64(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时，有50%的几率使敌人进入减速状态(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '减速' not in state_type:
            state_type.append('减速')
        pass


def entry_65(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时，有50%的几率使敌人进入眩晕状态(冷却时间20秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '眩晕' not in state_type:
            state_type.append('眩晕')
        pass


def entry_66(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时，有50%的几率使敌人进入诅咒状态(冷却时间25秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '诅咒' not in state_type:
            state_type.append('诅咒')
        pass


def entry_67(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时，有50%的几率使敌人进入失明状态(冷却时间25秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '失明' not in state_type:
            state_type.append('失明')
        pass


def entry_68(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时，有50%的几率使敌人进入石化状态(冷却时间30秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '石化' not in state_type:
            state_type.append('石化')
        pass


def entry_69(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时，有50%的几率使敌人进入睡眠状态(冷却时间30秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '睡眠' not in state_type:
            state_type.append('睡眠')
        pass


def entry_70(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时，有50%的几率使敌人进入混乱状态(冷却时间25秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '混乱' not in state_type:
            state_type.append('混乱')
        pass


def entry_71(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时，有50%的几率使敌人进入束缚状态(冷却时间25秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '束缚' not in state_type:
            state_type.append('束缚')
        pass


def entry_72(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 有20%的几率进入霸体状态， 效果持续5秒。 (冷却时间8秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_73(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放时，有20%的几率进入霸体状态，持续5秒(冷却时间8秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_89(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身施加的出血状态持续时间 -10%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_90(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身触发的中毒状态持续时间 -10%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_91(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身施加的灼伤状态持续时间 -10%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_92(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身施加的感电状态持续时间 -10%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_93(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身施加的冰冻持续时间 +2秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_94(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身触发的减速状态持续时间 +2秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_95(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身施加的眩晕持续时间 +2秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_96(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身触发的诅咒状态持续时间 +2秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_97(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身施加的失明持续时间 +2秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_98(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身施加的石化持续时间 +2秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_99(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身触发的睡眠状态持续时间 +2秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_100(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身触发的混乱状态持续时间 +2秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_101(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身触发的束缚状态持续时间 +2秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_111(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['前冲时，有20%的几率进入霸体状态，效果持续3秒(冷却时间5秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_112(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['跳跃时，有50%的几率进入霸体状态，效果持续3秒(冷却时间5秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_115(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['受到超过最大HP的20%以上的伤害时，生成相当于最大HP30%的保护罩，持续3秒(冷却时间30秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_128(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv15技能范围 +15%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_129(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv20技能范围 +15%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_130(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv25技能范围 +15%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_131(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv30技能范围 +15%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_132(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv35技能范围 +15%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_133(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv40技能范围 +15%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_134(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv45技能范围 +15%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_135(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv60技能范围 +15%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_136(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv70技能范围 +15%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_137(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv75技能范围 +15%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_138(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv80技能范围 +15%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_158(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['受到正面攻击时，所受伤害 -20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_159(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['受到背面攻击时，所受伤害 -20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_160(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被破招攻击时， 所受伤害 -20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_161(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被非破招攻击时， 所受伤害 -20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_162(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 恢复2200点HP。 (冷却时间1秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_163(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 恢复3500点MP。 (冷却时间1秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_164(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被攻击时，有50%的几率，进入霸体状态(冷却时间8秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_190(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身与敌人的所有异常状态持续时间 +20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_306(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['消耗品的Buff效果 +20%']
    if mode == 0:
        char.消耗品加成(0.2)
    if mode == 1:
        pass


def entry_227(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['5秒未被击时，所受伤害 -3%(最多叠加10次)', '受到总HP1%以上伤害时，所受伤害减少效果叠加次数 -2']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_230(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['<成长、传送属性>的属性触发几率 +5%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_265(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被攻击时，有30%的几率不会被击退(冷却时间3秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_307(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['消耗品的持续时间 +20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_324(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被攻击时，有30%的几率施放Lv20[念气罩](冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_325(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被攻击时，有30%的几率施放Lv20[圣光守护](冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass
# endregion

# region 常规词条


def entry_956(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击速度 +5%', '施放速度 +7.5%', '技能MP消耗量 +50%']
    if mode == 0:
        char.攻击速度增加(0.05)
        char.施放速度增加(0.075)
        char.MP消耗量加成(0.5)
    if mode == 1:
        pass


def entry_957(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击速度 +5%', '移动速度 +5%', '施法速度 +8%', 'HP MAX -250']
    if mode == 0:
        char.攻击速度增加(0.05)
        char.施放速度增加(0.08)
        char.移动速度增加(0.05)
    if mode == 1:
        pass


def entry_958(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击速度、 施放速度之和低于100%时， 技能冷却时间 -10% (觉醒技能除外)', '攻击速度、 施放速度之和高于100%时， 技能冷却时间 +10% (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能冷却缩减(1, 100, 0.1, [50, 85, 100])


def entry_959(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击控制型异常状态的敌人时， 技能攻击力+10%']
    if mode == 0:
        pass
    if mode == 1:
        for i in ['冰冻', '眩晕', '睡眠', '石化', '减速', '束缚', '失明', '混乱', '诅咒']:
            if i in state_type:
                char.技能攻击力加成(part=part, x=0.1)
                return


def entry_960(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击异常状态敌人时， 增加5%的技能攻击力。', '攻击非异常状态敌人时， 减少5%的技能攻击力。']
    if mode == 0:
        pass
    if mode == 1:
        if len(state_type) > 0:
            char.技能攻击力加成(part=part, x=0.05)
        else:
            char.技能攻击力加成(part=part, x=-0.05)


def entry_963(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击和施放技能时， 向自身周围300px随机位置召唤无人机， 投放补给箱。 (补给箱只能由发动者拾取； 冷却时间20秒)', '拾取补给箱后， 攻击强化 +3409， 效果持续20秒。']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(3409, lv))


def entry_967(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击灼伤状态敌人时， 增加5点火属性强化， 减少10点火属性抗性， 效果持续5秒。 (冷却时间1秒； 最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        if '灼烧' in state_type:
            char.火属性强化加成(5*5)
            char.火属性抗性加成(-10*5)


def entry_969(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击灼伤状态敌人时， 引发火焰爆炸。 (冷却时间0.5秒)', '攻击灼伤状态的敌人时， 技能攻击力 +2%']
    if mode == 0:
        pass
    if mode == 1:
        if '灼烧' in state_type:
            char.技能攻击力加成(part=part, x=0.02)


def entry_971(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['光属性抗性 +50', '火、 冰、 暗属性抗性 -20']
    if mode == 0:
        char.光属性抗性加成(50)
        char.火属性抗性加成(-20)
        char.冰属性抗性加成(-20)
        char.暗属性抗性加成(-20)
    if mode == 1:
        pass


def entry_972(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['光属性强化高于150时， 物理、 魔法暴击 +15%']
    if mode == 0:
        pass
    if mode == 1:
        char.暴击率增加(0.15)


def entry_973(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['回避率 +10%', '被击时， 增加10%的物理、 魔法暴击率， 效果持续20秒。 (最多叠加1次)']
    if mode == 0:
        char.回避率增加(0.1)
    if mode == 1:
        char.暴击率增加(0.1)


def entry_974(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['回避率 +5%', '混乱抗性 +15%']
    if mode == 0:
        char.回避率增加(0.05)
        char.异常抗性加成('混乱', 0.15)
    if mode == 1:
        pass


def entry_976(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['火、 冰、 光、 暗属性强化数值全部相同时， 增加25点所有属性抗性。']
    if mode == 0:
        pass
    if mode == 1:
        if len(list(set([char.火属性强化(), char.光属性强化(), char.冰属性强化(), char.暗属性强化()]))) == 1:
            char.所有属性抗性加成(25)


def entry_978(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['火属性抗性 +50', '冰、 光、 暗属性抗性 -20']
    if mode == 0:
        char.火属性抗性加成(50)
        char.光属性抗性加成(-20)
        char.冰属性抗性加成(-20)
        char.暗属性抗性加成(-20)
    if mode == 1:
        pass


def entry_979(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['火属性强化高于150时， 物理、 魔法暴击 +15%']
    if mode == 0:
        pass
    if mode == 1:
        char.暴击率增加(0.15)


def entry_981(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['消灭敌人时， 恢复10%的MP。', '技能MP消耗量 +50%']
    if mode == 0:
        pass
    if mode == 1:
        char.MP消耗量加成(0.5)
        pass


def entry_1223(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['角色的命中率为50%以上时， 所有职业1~25所有技能Lv +1']
    if mode == 0:
        pass
    if mode == 1:
        char.技能等级加成('所有', 1, 25, 1)


def entry_1224(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身对敌人施加的冰冻状态不会被灼伤攻击解除。', '攻击冰冻状态的敌人时， 技能攻击力 +5%']
    if mode == 0:
        pass
    if mode == 1:
        if '冰冻' in state_type:
            char.技能攻击力加成(part=part, x=0.05)


def entry_1225(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身使敌人进入的冰冻状态被灼伤异常状态解除时， 统一适用的灼伤伤害 +30%']
    if mode == 0:
        pass
    if mode == 1:
        char.冰冻结算灼烧加成 *= 1.35
        # char.异常增伤('灼烧', 0.3)
        pass


def entry_1229(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身受到的睡眠持续时间 -50%', '睡眠抗性 -20%']
    if mode == 0:
        char.异常抗性加成('睡眠', -0.2)
    if mode == 1:
        pass


def entry_1230(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['角色的移动速度为80%以上时， 所有职业1~25所有技能Lv +1']
    if mode == 0:
        pass
    if mode == 1:
        char.技能等级加成('所有', 1, 25, 1)


def entry_1231(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['诅咒抗性 +25%', '所有异常状态抗性 -5%']
    if mode == 0:
        char.异常抗性加成('诅咒', 0.25)
        char.所有异常抗性加成(-0.05)
    if mode == 1:
        pass


def entry_1237(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['', '该装备的成长属性等级之和达到240，增加1%的技能攻击力', ' - 该装备的成长属性等级之和每增加40级，额外增加1%的技能攻击力', ' - 穿戴100级以下装备时不适用该效果']
    if mode == 0:
        if char.穿戴低于105():
            return
        x = sum(char.词条等级.get(part, [0]))
        if x >= 240:
            char.技能攻击力加成(part=part, x=0.01 * int((x - 200) / 40))
    if mode == 1:
        pass


def entry_1239(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['装备提供的异常状态抗性总和超过5%以上时，增加相同数值的异常伤害(最多增加10%)', '- 包括武器、防具、首饰、特殊装备、时装、徽章']
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('中毒', 0.1)
        char.异常增伤('灼烧', 0.1)
        char.异常增伤('感电', 0.1)
        char.异常增伤('出血', 0.1)


def entry_1240(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['穿戴装备的强化/增幅数值总和每增加6，攻击强化 272(最多叠加24次)', '- 包括武器、防具、首饰、特殊装备']
    if mode == 0:
        x = char.获取强化等级()
        char.攻击强化加成(成长词条计算(272, lv) * min(24, int(x / 6)))
    if mode == 1:
        pass


def entry_1241(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['该装备的强化/增幅数值总和每增加1，所有速度 +2%(最多叠加12次)']
    if mode == 0:
        x = char.获取强化等级([part])
        char.所有速度增加(0.02 * min(12, x))
    if mode == 1:
        pass


def entry_1243(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['地下城入场时，攻击强化 2223', '连击维持时间 -0.5秒']
    if mode == 0:
        char.攻击强化加成(成长词条计算(2223, lv))
    if mode == 1:
        pass


def entry_1245(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['物理伤害减少率和魔法伤害减少率总和超过60%以上时，技能冷却时间恢复速度 +15%(觉醒技能除外)']
    if mode == 0:
        char.技能恢复加成(1, 100, 0.15, [50, 85, 100])
    if mode == 1:
        pass


def entry_1246(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['装备提供的攻击速度增加量总和超过140%以上时，技能攻击力 +30%', '- 包括防具、首饰、特殊装备、时装、徽章、宠物、守护珠、称号']
    if mode == 0:
        if char.攻击速度() > 1.4:
            char.技能攻击力加成(part=part, x=0.3)
    if mode == 1:
        pass


def entry_1249(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['HP低于40%时，物理、魔法防御力+14000，攻击强化 +2816']
    if mode == 0:
        pass
    if mode == 1:
        if hp_rate_num < 40:
            char.攻击强化加成(成长词条计算(2816, lv))
        pass


def entry_1250(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['最高属性强化每增加50，技能冷却时间恢复速度 +4%(最多叠加6次，觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        属强 = max(char.火属性强化(), char.光属性强化(), char.暗属性强化(), char.冰属性强化())
        char.技能恢复加成(1, 100, 0.04 * min(int(属强/50), 6), exc=[50, 85, 100])
        char.条件冷却恢复加成("所有", 0.04 * 6)


def entry_1251(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['最高属性强化每增加50，所有速度 +3%(最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        属强 = max(char.火属性强化(), char.光属性强化(), char.暗属性强化(), char.冰属性强化())
        char.所有速度增加(0.03 * min(int(属强/50), 5))


def entry_1252(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['根据最高属性强化数值适用以下效果：', '- 200~249: 攻击强化 1037', '- 250~299: 攻击强化 1927', '- 300~： 攻击强化 2816，技能攻击力 +7%']
    if mode == 0:
        pass
    if mode == 1:
        属强 = max(char.火属性强化(), char.光属性强化(), char.暗属性强化(), char.冰属性强化())
        if 属强 >= 200 and 属强 <= 249:
            char.攻击强化加成(成长词条计算(1037, lv))
        if 属强 >= 250 and 属强 <= 299:
            char.攻击强化加成(成长词条计算(1927, lv))
        if 属强 >= 300:
            char.攻击强化加成(成长词条计算(2816, lv))
            char.技能攻击力加成(part=part, x=0.07)


def entry_1253(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['最高属性抗性超过75以上时，攻击强化 700']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(700, lv))


def entry_1254(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['根据穿戴的所有装备的品级百分比总和适用以下效果：', '- 800%以上：移动速度 +5%', '- 900%以上：攻击速度 +5%，施放速度 +7.5%', '- 1000%以上：物理、魔法暴击率 +5%', '- 1080%以上：技能攻击力 +5%', '- 包括武器、防具、首饰、特殊装备，不包括称号和副武器']
    if mode == 0:
        pass
    if mode == 1:
        char.移动速度增加(0.05)
        char.攻击速度增加(0.05)
        char.施放速度增加(0.075)
        char.暴击率增加(0.05)
        char.技能攻击力加成(part=part, x=0.05)


def entry_1255(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['根据该装备的品级百分比适用以下效果：', '- 85%以下: 攻击强化 445', '- 85%~90%: 攻击强化 1186', '- 90%以上: 攻击强化 3557']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(3557, lv))


def entry_1256(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时，适用的属性攻击对应的属性抗性每增加10，相应的属性强化 +10，效果持续30秒(最多增加40，冷却时间1秒)']
    if mode == 0:
        pass
    if mode == 1:
        char.所有属性强化加成(10 * 4)


def entry_1257(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时，使用的属性攻击对应的属性抗性 +10(最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.所有属性抗性加成(10)


def entry_1190(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['周围有草坪时，所有属性抗性 +20，所有异常状态抗性 +10%，命中率 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.所有属性抗性加成(20)
        char.所有异常抗性加成(0.1)
        char.命中率增加(0.1)


def entry_1191(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['装扮栏中装扮个数超过120个时， 获得聚光灯效果， 进入霸体状态， 并减少8%的技能冷却时间。 (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能冷却缩减(1, 100, 0.08, [50, 85, 100])
        char.条件冷却加成("所有[除觉醒]", 0.08)


def entry_1197(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['穿戴时， 每10秒进入无法通过技能、 消耗品解除的出血状态， 效果持续10秒。', '出血每减少1100点HP， 攻击强化 +326 (最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        if '出血' not in own_state_type:
            own_state_type.append("出血")
        char.攻击强化加成(成长词条计算(326, lv) * 10)


def entry_1198(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['灼伤伤害 +15%', '灼伤抗性 +10%']
    if mode == 0:
        char.异常增伤('灼烧', 0.15)
        char.异常抗性加成('灼烧', 0.10)
    if mode == 1:
        pass


def entry_1199(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['灼伤伤害 +20%']
    if mode == 0:
        char.异常增伤('灼烧', 0.20)
    if mode == 1:
        pass


def entry_1200(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['灼伤抗性 +3%', '冰冻抗性 -1.5%']
    if mode == 0:
        char.异常抗性加成('灼烧', 0.03)
        char.异常抗性加成('冰冻', -0.015)
    if mode == 1:
        pass


def entry_1202(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身进入出血状态时， 增加10%的出血伤害。']
    if mode == 0:
        pass
    if mode == 1:
        if '出血' in own_state_type:
            char.异常增伤('出血', 0.10)


def entry_1203(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身进入出血状态时， 增加20%的攻击、 移动速度和30%的施放速度。', '出血抗性 -20%']
    if mode == 0:
        pass
    if mode == 1:
        if '出血' in own_state_type:
            char.攻击速度增加(0.2)
            char.移动速度增加(0.2)
            char.施放速度增加(0.3)
            char.异常抗性加成('出血', -0.2)


def entry_1204(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身进入出血状态时， 攻击强化 +2223', '自身进入出血状态时， 每秒减少3%的攻击、 移动、 施放速度。 (最多叠加5次； 解除出血时立即解除)', '出血伤害 +5%']
    if mode == 0:
        pass
    if mode == 1:
        if '出血' in own_state_type:
            char.攻击强化加成(成长词条计算(2223, lv))
            char.攻击速度增加(-0.15)
            char.移动速度增加(-0.15)
            char.施放速度增加(-0.15)
            char.异常增伤('出血', 0.05)


def entry_1205(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身进入出血状态时， 增加10%的物理暴击率、 10%的魔法暴击率、 5%的攻击速度和7.5%的施放速度。', '被击时， 使自身进入出血状态。 (冷却时间5秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '出血' in own_state_type:
            char.暴击率增加(0.1)
            char.攻击速度增加(0.05)
            char.施放速度增加(0.075)


def entry_1208(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身进入感电状态时， 增加10%的物理暴击率、 10%的魔法暴击率、 5%的攻击速度和7.5%的施放速度。', '被击时， 使自身进入感电状态。 (冷却时间5秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '感电' in own_state_type:
            char.暴击率增加(0.1)
            char.攻击速度增加(0.05)
            char.施放速度增加(0.075)


def entry_1212(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身进入中毒状态时， 增加10%的物理暴击率、 10%的魔法暴击率、 5%的攻击速度和7.5%的施放速度。', '被击时， 使自身进入中毒状态。 (冷却时间5秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '中毒' in own_state_type:
            char.暴击率增加(0.1)
            char.攻击速度增加(0.05)
            char.施放速度增加(0.075)


def entry_1214(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身进入灼伤状态时， 增加10%的物理暴击率、 10%的魔法暴击率、 5%的攻击速度和7.5%的施放速度。', '被击时， 使自身进入灼伤状态。 (冷却时间5秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '灼烧' in own_state_type:
            char.暴击率增加(0.1)
            char.攻击速度增加(0.05)
            char.施放速度增加(0.075)


def entry_1215(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身的异常状态个数超过1个时， Lv45以下技能冷却时间恢复速度 +50%']
    if mode == 0:
        pass
    if mode == 1:
        if len(own_state_type) >= 1:
            char.技能恢复加成(1, 45, 0.5)
            char.条件冷却恢复加成("Lv1~45", 0.5)


def entry_1216(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身的异常状态个数超过3个时， Lv60以上技能冷却时间恢复速度 +50% (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        if len(own_state_type) >= 3:
            char.技能恢复加成(60, 100, 0.5, [50, 85, 100])
            char.条件冷却恢复加成("Lv60~100[觉醒除外]", 0.5)


def entry_1217(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身进入感电状态时， 增加20%的攻击、 移动速度和30%的施放速度。']
    if mode == 0:
        pass
    if mode == 1:
        if '感电' in own_state_type:
            char.攻击速度增加(0.2)
            char.施放速度增加(0.3)


def entry_1218(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身攻击对领主怪物每造成HP最大值10%的伤害时， 攻击强化 +593， 并减少10%的物理、 魔法防御力。 (最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(593, lv) * 5)


def entry_1219(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['获得2个以上消耗品效果时， 自身进入出血状态， 效果持续10秒。 (冷却时间10秒)', '自身进入出血状态时， 冷却时间恢复速度增加10%。 (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        if '出血' not in own_state_type:
            own_state_type.append("出血")
        if '出血' in own_state_type:
            char.技能恢复加成(1, 100, 0.1, [50, 85, 100])
            char.条件冷却恢复加成("所有[觉醒除外]", 0.1)


def entry_1220(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身只处于中毒状态时， 每10秒以相同几率获得下列效果之一，  持续10秒。', '- 所有速度 +30%', '- 技能攻击力 +10%', '- 冷却时间恢复速度 +30% (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        if '中毒' in own_state_type:
            # char.所有速度增加(0.3)
            char.技能攻击力加成(part=part, x=0.1)
            # char.技能恢复加成(1, 100, 0.3, [50, 85, 100])


def entry_1222(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身进入灼伤状态时， 每秒增加3点所有属性强化， 效果持续15秒。 (最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        if '灼烧' in own_state_type:
            for i in range(0, 10):
                char.所有属性强化加成(3, mode=1)


def entry_1166(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['物理、 魔法防御力 -21000', '技能冷却时间 -10% (觉醒技能除外)']
    if mode == 0:
        char.技能冷却缩减(1, 100, 0.1, [50, 85, 100])
        char.条件冷却加成("所有[除觉醒]", 0.1)
    if mode == 1:
        pass


def entry_1169(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['向地图内最强敌人生成标志。', '500px范围内存在拥有标志的敌人时， 施放[后跳]时， 移动至拥有标志敌人的后方。 (冷却时间20秒)', '攻击拥有标志的敌人时， 增加8%的技能攻击力， 效果持续5秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        if '背面攻击' in attack_type:
            char.技能攻击力加成(part=part, x=0.08)


def entry_1173(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['使用消耗品恢复MP时， 攻击强化 +2519， 效果持续30秒。 (最多叠加1次)', '消耗品的MP恢复效果 -80%']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(2519, lv))


def entry_1174(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['无色小晶块技能攻击力 +8%', '无色小晶块技能的无色小晶块消耗量 +2个']
    if mode == 0:
        for skill in char.技能队列:
            if skill["无色消耗"] > 0:
                skill["无色消耗"] += 2
                skill["倍率"] *= 1.08
    if mode == 1:
        pass


def entry_1176(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['眩晕状态解除时， 30秒内攻击强化 +3853 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(3853, lv))


def entry_1180(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['渔夫的祝福激活时，所有异常状态抗性 +20%，回避率 +5%，效果持续30秒']
    if mode == 0:
        pass
    if mode == 1:
        char.所有异常抗性加成(0.2)
        char.回避率增加(0.05)


def entry_1183(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['按照技能MP消耗量增加属性之和的5%， 增加技能攻击力。 (最多增加25%)', '技能MP消耗量 +100%']
    if mode == 0:
        char.MP消耗量加成(1.0)
    if mode == 1:
        char.技能攻击力加成(part=part, x=min((char.MP消耗倍率() - 1)*0.05, 0.25))


def entry_1185(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['中毒抗性 +1%', '魔法防御力 +500']
    if mode == 0:
        char.异常抗性加成('中毒', 0.01)
    if mode == 1:
        pass


def entry_1186(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['中毒伤害 +15%', '中毒抗性 +10%']
    if mode == 0:
        char.异常抗性加成('中毒', 0.10)
        char.异常增伤('中毒', 0.15)
    if mode == 1:
        pass


def entry_1187(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['中毒伤害 +10%', '中毒抗性 -20%']
    if mode == 0:
        char.异常抗性加成('中毒', -0.20)
        char.异常增伤('中毒', 0.10)
    if mode == 1:
        pass


def entry_1188(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['中毒伤害 +20%']
    if mode == 0:
        char.异常增伤('中毒', 0.20)
    if mode == 1:
        pass


def entry_1105(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放技能时， 攻击强化 +504， 技能MP消耗量增加20%， 效果持续20秒。 (最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(504, lv)*5)
        char.MP消耗量加成(0.2*5)


def entry_1106(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放技能时， 消耗剩余HP的30%， 攻击强化 +2223、 技能攻击力增加6%， 效果持续30秒。 (冷却时间30秒)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(2223, lv))
        char.技能攻击力加成(part=part, x=0.06)


def entry_1123(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['使用消耗品时， 自身进入无法通过技能、 消耗品解除的中毒状态。', '自身处于中毒状态时， 增加25%的技能冷却时间恢复速度。(觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        if '中毒' not in own_state_type:
            own_state_type.append('中毒')
        if '中毒' in own_state_type:
            char.技能恢复加成(1, 100, 0.25, [50, 85, 100])


def entry_1124(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['受到惊吓时，攻击速度 +20%，移动速度 +20%，施放速度 +30%，效果持续30秒(最多叠加 1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.2)
        char.移动速度增加(0.2)
        char.施放速度增加(0.3)


def entry_1133(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[受身蹲伏]结束时， 攻击强化 +2519， 效果持续60秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(2519, lv))


def entry_1139(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['睡眠抗性 -50%', '所有异常状态抗性 +20%']
    if mode == 0:
        char.所有属性抗性加成(0.2)
        char.异常抗性加成('睡眠', -0.5)
    if mode == 1:
        pass


def entry_1141(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['将所有被击伤害的50%转换为中毒伤害。', '攻击中毒状态的敌人时， 技能攻击力 +2%']
    if mode == 0:
        pass
    if mode == 1:
        if '中毒' in state_type:
            char.技能攻击力加成(part=part, x=0.02)


def entry_1142(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['将所有被击伤害的50%转换为灼伤伤害。', '攻击灼伤状态的敌人时， 技能攻击力 +2%']
    if mode == 0:
        pass
    if mode == 1:
        if '灼烧' in state_type:
            char.技能攻击力加成(part=part, x=0.02)


def entry_1143(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['将所有被击伤害的50%转换为出血伤害。', '攻击出血状态的敌人时， 技能攻击力 +2%']
    if mode == 0:
        pass
    if mode == 1:
        if '出血' in state_type:
            char.技能攻击力加成(part=part, x=0.02)


def entry_1144(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['将所有被击伤害的50%转换为感电伤害。', '攻击感电状态的敌人时， 技能攻击力 +2%']
    if mode == 0:
        pass
    if mode == 1:
        if '感电' in state_type:
            char.技能攻击力加成(part=part, x=0.02)


def entry_1145(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有异常状态抗性 +15%', '- HP最大值 -300']
    if mode == 0:
        char.所有异常抗性加成(0.15)
    if mode == 1:
        pass


def entry_1146(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有异常状态抗性 +25%', '移动速度 -5%']
    if mode == 0:
        char.所有异常抗性加成(0.25)
        char.移动速度增加(-0.05)
    if mode == 1:
        pass


def entry_1147(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv1~30技能攻击力 +12%', '不消耗无色的技能无色小晶块消耗量 +2']
    if mode == 0:
        char.技能倍率加成(1, 30, 0.12)
        for skill in char.技能队列:
            if skill["无色消耗"] == 0 and skill['名称'] != '基础精通':
                skill["无色消耗"] = 2
    if mode == 1:
        pass


def entry_1148(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有属性抗性之和在100以下时， 所有属性强化 +30']
    if mode == 0:
        pass
    if mode == 1:
        char.所有属性强化加成(30)


def entry_1153(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['跳跃落地时，掉落一个西瓜，赋予武器冰属性攻击，冰属性抗性 +10，移动速度 +10%，效果持续20秒(最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.冰属性抗性加成(10)
        char.移动速度增加(0.1)


def entry_1162(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['停止时， 每0.5秒攻击强化 +445 (最多叠加10次； 移动时叠加次数减1)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(445, lv) * 10)


def entry_1164(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['武器的耐久度减少率 +100%', '技能攻击力 +6%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(part=part, x=0.06)


def entry_1058(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[基础精通]技能攻击力增加量 +30%']
    if mode == 0:
        char.基础精通加成(0.3)
    if mode == 1:
        pass


def entry_1071(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['将伤害的50%转换为中毒伤害。', '中毒伤害 +10%']
    if mode == 0:
        if '中毒' not in state_type:
            state_type.append("中毒")
        char.伤害类型转化('直伤', '中毒', 0.5)
        char.异常增伤('中毒', 0.1)
    if mode == 1:
        pass


def entry_1072(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['将伤害的50%转换为灼伤伤害。', '灼伤伤害 +10%']
    if mode == 0:
        if '灼烧' not in state_type:
            state_type.append("灼烧")
        char.伤害类型转化('直伤', '灼烧', 0.5)
        char.异常增伤('灼烧', 0.1)
    if mode == 1:
        pass


def entry_1073(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['将伤害的50%转换为出血伤害。', '出血伤害 +10%']
    if mode == 0:
        if '出血' not in state_type:
            state_type.append("出血")
        char.伤害类型转化('直伤', '出血', 0.5)
        char.异常增伤('出血', 0.1)
    if mode == 1:
        pass


def entry_1074(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['将伤害的50%转换为感电伤害。', '感电伤害 +10%']
    if mode == 0:
        if '感电' not in state_type:
            state_type.append("感电")
        char.伤害类型转化('直伤', '感电', 0.5)
        char.异常增伤('感电', 0.1)
    if mode == 1:
        pass


def entry_1080(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv1~35技能时， Lv1~35技能攻击力减少2%， Lv40~80技能冷却时间恢复速度增加10%， 效果持续20秒。 (最多叠加5次； 觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        for i in range(0, 5):
            char.技能倍率加成(1, 35, -0.02)
            char.技能恢复加成(40, 80, 0.1, [50, 85, 100])


def entry_1081(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv30以下技能时， [基础精通]攻击力增加15%， Lv15~30主动技能攻击力增加5%， 效果持续10秒。  (冷却时间1秒； 最多叠加3次)', '施放Lv45以上技能时， [基础精通]攻击力增加， Lv15~30主动技能攻击力增加效果减少1层叠加数。']
    if mode == 0:
        pass
    if mode == 1:
        for item in range(0, 3):
            char.基础精通加成(0.15)
            char.技能倍率加成(15, 30, 0.05, type="active")


def entry_1082(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv35技能时， 增加20点所有属性强化， 效果持续30秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.所有属性强化加成(20)


def entry_1083(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv35以下技能时， 增加4点火属性强化， 效果持续15秒。 (最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        char.火属性强化加成(4 * 5)


def entry_1084(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv35以下技能时， 增加4点暗属性强化， 效果持续15秒。 (最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        char.暗属性强化加成(4 * 5)


def entry_1085(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv35以下技能时， 增加4点冰属性强化， 效果持续15秒。 (最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        char.冰属性强化加成(4 * 5)


def entry_1086(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv35以下技能时， 增加4点光属性强化， 效果持续15秒。 (最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        char.光属性强化加成(4 * 5)


def entry_1087(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv40~80技能时， Lv40~80技能攻击力减少2%， Lv1~35技能冷却时间恢复速度增加10%， 效果持续20秒。 (最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能倍率加成(40, 80, -0.02 * 5)
        char.技能恢复加成(1, 35, 0.1 * 5, [50, 85, 100])
        char.条件冷却恢复加成("Lv1~35", 0.1)


def entry_1088(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv40技能时， 增加20点所有属性强化， 效果持续30秒。(最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.所有属性强化加成(20)


def entry_1089(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv40以上技能时， 增加3点火属性抗性， 效果持续15秒。 (最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        char.火属性抗性加成(3 * 5)


def entry_1090(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv40以上技能时， 增加3点暗属性抗性， 效果持续15秒。 (最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        char.暗属性抗性加成(3 * 5)


def entry_1091(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv40以上技能时， 增加3点冰属性抗性， 效果持续15秒。 (最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        char.冰属性抗性加成(3 * 5)


def entry_1092(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv40以上技能时， 增加3点光属性抗性， 效果持续15秒。 (最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        char.光属性抗性加成(3 * 5)


def entry_1093(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv45技能时， 增加20点所有属性强化， 效果持续30秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.所有属性强化加成(20)


def entry_1094(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv60技能时， 增加20点所有属性强化， 效果持续30秒。(最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.所有属性强化加成(20)


def entry_1095(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv70技能时， 增加20点所有属性强化， 效果持续30秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.所有属性强化加成(20)


def entry_1102(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放技能时， 根据消耗的无色小晶块个数， 增加该技能的攻击力。', '- 消耗1个以上小晶块， 增加2%的技能攻击力。', '- 消耗15个以上小晶块， 增加10%的技能攻击力。', '- 消耗30个以上小晶块， 增加20%的技能攻击力。']
    if mode == 0:
        for skill in char.技能队列:
            无色消耗 = skill["无色消耗"]
            if skill['名称'] == '炫纹发射':
                无色消耗 = min(无色消耗, 3)
            if 无色消耗 >= 30:
                skill["倍率"] *= 1.2
            elif 无色消耗 >= 15:
                skill["倍率"] *= 1.1
            elif 无色消耗 >= 1:
                skill["倍率"] *= 1.02
    if mode == 1:
        pass


def entry_1004(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['落地时， 2秒内攻击强化 +2223、 移动速度 +100% (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(2223, lv))


def entry_1011(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每10秒使自身进入无法通过技能、 消耗品解除的感电异常状态， 效果持续10秒。', '自身进入感电状态时， 增加15点所有属性强化和15点所有属性抗性。']
    if mode == 0:
        pass
    if mode == 1:
        if '感电' not in own_state_type:
            own_state_type.append('感电')
        char.所有属性强化加成(15)
        char.所有属性抗性加成(15)


def entry_1012(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每11点火属性抗性， 使所有速度增加5%。 (最多增加45%)', '被击时， 减少30%的所有速度， 效果持续10秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.所有速度增加(0.45)


def entry_1013(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每1点暗属性抗性， 增加1点暗属性强化。 (最多增加30点)', '暗属性抗性 -20']
    if mode == 0:
        pass
    if mode == 1:
        char.暗属性强化加成(30)
        char.暗属性抗性加成(-20)


def entry_1014(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每1点冰属性抗性， 增加1点冰属性强化。 (最多增加30点)', '冰属性抗性 -20']
    if mode == 0:
        pass
    if mode == 1:
        char.冰属性强化加成(30)
        char.冰属性抗性加成(-20)


def entry_1015(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每1点光属性抗性， 增加1点光属性强化。 (最多增加30点)', '光属性抗性 -20']
    if mode == 0:
        pass
    if mode == 1:
        char.光属性强化加成(30)
        char.光属性抗性加成(-20)


def entry_1016(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每1点火属性抗性， 增加1点火属性强化。 (最多增加30点)', '火属性抗性 -20']
    if mode == 0:
        pass
    if mode == 1:
        char.火属性强化加成(30)
        char.火属性抗性加成(-20)


def entry_1017(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['扩展技能栏中每放入1个技能， 使不在扩展技能栏中的技能攻击力增加2%。 (最多增加14%)', '扩展技能栏中的技能攻击力 -20%']
    if mode == 0:
        num = len(list(filter(lambda i: i != "", char.hotkey[:7]))) * 0.02
        for i in char.技能栏:
            if i.是否有伤害 == 1:
                if i.名称 in char.hotkey[:7]:
                    i.倍率 *= 0.8
                else:
                    i.倍率 *= (num + 1)
    if mode == 1:
        pass


def entry_1020(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每1名异常状态敌人， 攻击强化 +326 (最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(326, lv) * min(enemy_num, 10) *
                    (1 if len(state_type) > 0 else 0))


def entry_1021(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每20%的移动速度， 增加6点最高属性强化。 (最多增加30点)']
    if mode == 0:
        pass
    if mode == 1:
        char.所有属性强化加成(30)


def entry_1022(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每25点最高的属性抗性数值， 除觉醒技能外的冷却时间减少5% (最多减少15%)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能冷却缩减(1, 100, 0.15, [50, 85, 100])
        char.条件冷却加成("所有[除觉醒]", 0.15)


def entry_1023(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每30%的移动速度， 技能冷却时间恢复速度增加10%。 (最多增加30%； 觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(1, 100, 0.3, [48, 50, 85, 100])
        char.条件冷却恢复加成("所有[觉醒除外]", 0.3)


def entry_1025(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每30秒消耗1个稀有灵魂， 攻击强化 +2371， 效果持续30秒。', '累计消耗5个稀有灵魂时， 攻击强化 +1186']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(2371, lv) + 成长词条计算(1186, lv))


def entry_1026(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每40秒出现一朵云朵，持续40秒', '云朵存在时，提供增益，持续40秒', '- 暗属性抗性 +15', '- 冰属性抗性 +15', '- 攻击速度 +10%', '- 施放速度 +15%']
    if mode == 0:
        pass
    if mode == 1:
        char.暗属性抗性加成(15)
        char.冰属性抗性加成(15)
        char.攻击速度增加(0.1)
        char.施放速度增加(0.15)


def entry_1027(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每40秒出现一个小太阳，持续40秒', '地图上有小太阳时，发动buff', '- 火属性抗性 +15', '- 光属性抗性 +15', '- 移动速度 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.火属性抗性加成(15)
        char.光属性抗性加成(15)
        char.移动速度增加(0.1)


def entry_1028(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每5点暗属性抗性， 增加1%的攻击速度和1.5%的施放速度。 (最多叠加10次)', '暗属性抗性 -15']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.01 * 10)
        char.施放速度增加(0.015 * 10)
        char.暗属性抗性加成(-15)


def entry_1029(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每5点冰属性抗性， 增加1%的攻击速度和1.5%的施放速度。 (最多叠加10次)', '冰属性抗性 -15']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.01 * 10)
        char.施放速度增加(0.015 * 10)
        char.冰属性抗性加成(-15)


def entry_1030(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每5点光属性抗性， 增加1%的攻击速度和1.5%的施放速度。 (最多叠加10次)', '光属性抗性 -15']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.01 * 10)
        char.施放速度增加(0.015 * 10)
        char.光属性抗性加成(-15)


def entry_1031(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每5点火属性抗性， 增加1%的攻击速度和1.5%的施放速度。 (最多叠加10次)', '火属性抗性 -15']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.01 * 10)
        char.施放速度增加(0.015 * 10)
        char.火属性抗性加成(-15)


def entry_1032(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每剩余8%的MP， 物理暴击率、 魔法暴击率增加3%。  (最多增加30%)', '技能MP消耗量 +100%']
    if mode == 0:
        char.MP消耗量加成(1.0)
    if mode == 1:
        char.暴击率增加(min(0.3, 0.03 * int(mp_rate_num/8)))


def entry_1033(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每剩余8%的MP， 除觉醒技能外的技能冷却时间恢复速度增加3%。 (最多增加30%)', '技能MP消耗量 +100%']
    if mode == 0:
        char.MP消耗量加成(1.0)
    if mode == 1:
        char.技能恢复加成(1, 100, min(0.3, 0.03 * int(mp_rate_num/8)), [50, 85, 100])
        char.条件冷却恢复加成("所有[觉醒除外]", 0.3)


def entry_1034(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每8点暗属性强化， 增加1点火、 冰、 光属性强化。 (最多增加50点)', '每10点暗属性强化， 减少1点火、 冰、 光属性抗性。 (最多减少30点)']
    if mode == 0:
        pass
    if mode == 1:
        char.火属性强化加成(min(50, int(char.暗属性强化() / 8)))
        char.冰属性强化加成(min(50, int(char.暗属性强化() / 8)))
        char.光属性强化加成(min(50, int(char.暗属性强化() / 8)))
        # char.暗属性强化加成(50)
        char.火属性抗性加成(-min(30, int(char.暗属性强化() / 10)))
        char.冰属性抗性加成(-min(30, int(char.暗属性强化() / 10)))
        char.光属性抗性加成(-min(30, int(char.暗属性强化() / 10)))
        # char.暗属性抗性加成(-30)


def entry_1035(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每8点冰属性强化， 增加1点火、 光、 暗属性强化。 (最多增加50点)', '每10点冰属性强化， 减少1点火、 光、 暗属性抗性。 (最多减少30点)']
    if mode == 0:
        pass
    if mode == 1:
        char.火属性强化加成(min(50, int(char.冰属性强化() / 8)))
        # char.冰属性强化加成(50)
        char.光属性强化加成(min(50, int(char.冰属性强化() / 8)))
        char.暗属性强化加成(min(50, int(char.冰属性强化() / 8)))
        char.火属性抗性加成(-min(30, int(char.冰属性强化() / 10)))
        # char.冰属性抗性加成(-30)
        char.光属性抗性加成(-min(30, int(char.冰属性强化() / 10)))
        char.暗属性抗性加成(-min(30, int(char.冰属性强化() / 10)))


def entry_1036(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每8点光属性强化， 增加1点火、 冰、 暗属性强化。 (最多增加50点)', '每10点光属性强化， 减少1点火、 冰、 暗属性抗性。 (最多减少30点)']
    if mode == 0:
        pass
    if mode == 1:
        char.火属性强化加成(min(50, int(char.光属性强化() / 8)))
        char.冰属性强化加成(min(50, int(char.光属性强化() / 8)))
        # char.光属性强化加成(50)
        char.暗属性强化加成(min(50, int(char.光属性强化() / 8)))
        char.火属性抗性加成(-min(30, int(char.光属性强化() / 10)))
        char.冰属性抗性加成(-min(30, int(char.光属性强化() / 10)))
        # char.光属性抗性加成(-30)
        char.暗属性抗性加成(-min(30, int(char.光属性强化() / 10)))


def entry_1037(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每8点火属性强化， 增加1点冰、 光、 暗属性强化。 (最多增加50点)', '每10点火属性强化， 减少1点冰、 光、 暗属性抗性。 (最多减少30点)']
    if mode == 0:
        pass
    if mode == 1:
        # char.火属性强化加成(50)
        char.冰属性强化加成(min(50, int(char.火属性强化() / 8)))
        char.光属性强化加成(min(50, int(char.火属性强化() / 8)))
        char.暗属性强化加成(min(50, int(char.火属性强化() / 8)))
        # char.火属性抗性加成(-30)
        char.冰属性抗性加成(-min(30, int(char.火属性强化() / 10)))
        char.光属性抗性加成(-min(30, int(char.火属性强化() / 10)))
        char.暗属性抗性加成(-min(30, int(char.火属性强化() / 10)))


def entry_1040(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['当前HP比HP最大值每减少10%， 攻击强化 +165， 物理防御力、魔法防御力减少2200。 (最多叠加9次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(165, lv) * min((90-hp_rate_num)/10, 9))


def entry_1041(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['MP每减少10%， 攻击强化 +362 (最多叠加9次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(362, lv) * min((90-mp_rate_num)/10, 9))


def entry_1042(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['当前HP比HP最大值每减少5%， 攻击强化 +156 (最多叠加19次)', '施放技能时， 消耗1%的HP。 (该属性不会使HP减少至1%以下)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(156, lv) * min((90-hp_rate_num)/5, 19))


def entry_1045(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每秒暗属性强化 +2  (最多叠加10次)', '受到总HP1%以上的伤害时， 暗属性强化叠加数 -5', '被击时， 火、 冰、 光属性抗性 -1  (最多叠加10次)', '物理、 魔法暴击率 +5%']
    if mode == 0:
        pass
    if mode == 1:
        char.暗属性强化加成(2 * 10)
        char.暴击率增加(0.05)


def entry_1046(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每秒冰属性强化 +2  (最多叠加10次)', '受到总HP1%以上的伤害时， 冰属性强化叠加数 -5', '被击时， 火、 光、 暗属性抗性 -1  (最多叠加10次)', '物理、 魔法暴击率 +5%']
    if mode == 0:
        pass
    if mode == 1:
        char.冰属性强化加成(2 * 10)
        char.暴击率增加(0.05)


def entry_1047(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每秒光属性强化 +2  (最多叠加10次)', '受到总HP1%以上的伤害时， 光属性强化叠加数 -5', '被击时， 火、 冰、 暗属性抗性 -1  (最多叠加10次)', '物理、 魔法暴击率 +5%']
    if mode == 0:
        pass
    if mode == 1:
        char.光属性强化加成(2 * 10)
        char.暴击率增加(0.05)


def entry_1048(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每秒火属性强化 +2  (最多叠加10次)', '受到总HP1%以上的伤害时， 火属性强化叠加数 -5', '被击时， 冰、 光、 暗属性抗性 -1  (最多叠加10次)', '物理、 魔法暴击率 +5%']
    if mode == 0:
        pass
    if mode == 1:
        char.火属性强化加成(2 * 10)
        char.暴击率增加(0.05)


def entry_1049(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每使用5次技能， 增加20%的技能攻击力和10%的冷却时间。']
    if mode == 0:
        pass
    if mode == 1:
        for index in range(0, len(char.技能队列)):
            if (index+1) % 5 == 0:
                char.技能队列[index]["倍率"] *= 1.2
                char.技能队列[index]["CDR"] *= 1.1
            pass


mp_used = 0
mp_used_list = [0, 1, 2, 3, 4, 5]


def set_mp_used(x):
    global mp_used
    mp_used = mp_used_list[x[0]]


entry_chose.append((21050,
                    ['已消耗MP 0~29999',
                     '已消耗MP 30000~59999',
                     '已消耗MP 60000~89999',
                     '已消耗MP 90000~119999',
                     '已消耗MP 120000~149999',
                     '已消耗MP 150000+',
                     ], ""))
multi_select[21050] = False
variable_set[21050] = set_mp_used


def entry_1050(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每使用30000点MP， 攻击强化 +889， 效果持续20秒。 (最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        # 先当全程
        char.攻击强化加成(成长词条计算(889, lv) * mp_used)


def entry_1052(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['农夫的祝福激活时，所有属性抗性 +40，回避率 +5%，效果持续30秒']
    if mode == 0:
        pass
    if mode == 1:
        char.所有属性抗性加成(40)
        char.回避率增加(0.05)


def entry_982(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['消灭敌人时， 恢复5%的HP。', '攻击石化状态的敌人时， 技能攻击力 +5%']
    if mode == 0:
        pass
    if mode == 1:
        if '石化' in state_type:
            char.技能攻击力加成(part=part, x=0.05)


def entry_983(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[基础精通]技能攻击力增加量 +30%', 'Lv15~30主动技能攻击力 +10%', '无色小晶块技能攻击力 -15%']
    if mode == 0:
        char.基础精通加成(0.3)
        char.技能倍率加成(15, 30, 0.1, type="active")
        for skill in char.技能队列:
            if skill["无色消耗"] > 0:
                skill["倍率"] *= 0.85
    if mode == 1:
        pass


def entry_984(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[基础精通]技能攻击力增加量 +30%', 'Lv15~30主动技能攻击力 +10%', '无色小晶块技能冷却时间 +10%']
    if mode == 0:
        char.基础精通加成(0.3)
        char.技能倍率加成(15, 30, 0.1, type="active")
        for skill in char.技能队列:
            if skill["无色消耗"] > 0:
                skill["CDR"] *= 1.1
        char.条件冷却加成("消耗无色", -0.1)
    if mode == 1:
        pass


def entry_986(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['技能MP消耗量 +100%', '技能冷却时间 - 12% (觉醒技能除外)']
    if mode == 0:
        char.MP消耗量加成(1.0)
        char.技能冷却缩减(1, 100, 0.12, [50, 85, 100])
        char.条件冷却加成("所有[除觉醒]", 0.12)
    if mode == 1:
        pass


def entry_987(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['技能MP消耗量 -20%', 'MP最大值 +4196']
    if mode == 0:
        char.MP消耗量加成(-0.2)
    if mode == 1:
        pass


def entry_988(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['技能MP消耗量超过4000的技能攻击力 +15% (觉醒技能除外)']
    if mode == 0:
        for skill in char.技能栏:
            if skill.是否有伤害 == 1 and skill.MP消耗(武器类型=char.武器类型, 输出类型=char.类型, 额外倍率=char.MP消耗倍率(), char=char) >= 4000 and (skill.所在等级 not in [50, 85, 100] or skill.名称 == '末日虫洞'):
                skill.倍率 *= 1.15
    if mode == 1:
        pass


def entry_990(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['快捷栏中每存在1个冷却中的技能， 快捷栏技能的冷却时间恢复速度增加3.5%。 (最多增加42%； 觉醒技能除外)']
    if mode == 0:
        pass  # 暂未实现
    if mode == 1:
        pass


def entry_991(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['冷却时间超过15秒的技能攻击力 +10%', '冷却时间低于15秒的技能攻击力 -15%']
    if mode == 0:
        pass
    if mode == 1:
        for skill in char.技能队列:
            if char.get_skill_by_name(skill['名称']).等效CD(武器类型=char.武器类型, 输出类型=char.类型, 额外CDR=skill['CDR'], 恢复=False) >= 15:
                skill['倍率'] *= 1.1
            else:
                skill['倍率'] *= 0.85


def entry_999(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['觉醒技能攻击力 -25%', '觉醒除外转职技能攻击力 +20%']
    if mode == 0:
        char.技能倍率加成(1, 100, 0.2, [50, 85, 100])
        char.技能倍率加成(50, 50, -0.25)
        char.技能倍率加成(85, 85, -0.25)
        char.技能倍率加成(100, 100, -0.25)
    if mode == 1:
        pass


def entry_1002(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['落地时， 增加20%的物理和魔法防御力、 攻击强化 +593， 效果持续10秒。  (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(593, lv))


def entry_902(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['地下城入场后， 每失去10%的HP， 攻击强化 +400 (最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(400, lv) * 10)


def entry_903(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['进入地下城时， 攻击强化 +3260', '被击时所受伤害 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(3260, lv))


def entry_905(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['拥有20个宠物 (不包含宠物蛋) 时， 获得光谱， 增加15%的所有速度， 减少8%的技能冷却时间。(觉醒技能除外， 光谱特效仅适用1个)']
    if mode == 0:
        pass
    if mode == 1:
        char.所有速度增加(0.15)
        char.技能冷却缩减(1, 100, 0.08, [50, 85, 100])
        char.条件冷却加成("所有[除觉醒]", 0.08)


def entry_910(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['根据孵化的宠物数量， 发动不同效果。', '- 3~9个 : 攻击强化 +1482', '- 10个以上 : 攻击强化 +2075']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(2075, lv))


def entry_907(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['感电抗性 +3%', '中毒抗性 +3%', '出血抗性 +3%']
    if mode == 0:
        char.异常抗性加成('感电', 0.03)
        char.异常抗性加成('中毒', 0.03)
        char.异常抗性加成('出血', 0.03)
    if mode == 1:
        pass


def entry_908(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['感电伤害 +15%', '感电抗性 +10%']
    if mode == 0:
        char.异常抗性加成('感电', 0.10)
        char.异常增伤('感电', 0.15)
    if mode == 1:
        pass


def entry_909(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['感电伤害 +20%']
    if mode == 0:
        char.异常增伤('感电', 0.2)
    if mode == 1:
        pass


def entry_914(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['根据装扮栏中装扮数量， 发动额外效果。', '21~50个 : 攻击强化 +1482', '51个以上 : 攻击强化 +2668']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(2668, lv))


def entry_917(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击冰冻状态敌人时， 引发寒冰爆炸。 (冷却时间0.5秒)', '攻击冰冻状态的敌人时， 技能攻击力 +5%']
    if mode == 0:
        pass
    if mode == 1:
        if '冰冻' in state_type:
            char.技能攻击力加成(part=part, x=0.05)


def entry_920(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击感电状态敌人时， 使其进入眩晕状态。 (冷却时间20秒)', '攻击眩晕状态的敌人时， 技能攻击力 +5%']
    if mode == 0:
        pass
    if mode == 1:
        if '感电' in state_type and '眩晕' not in state_type:
            state_type.append('眩晕')
        if '眩晕' in state_type:
            char.技能攻击力加成(part=part, x=0.05)


def entry_922(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击石化状态的敌人时，地图上所有石化的敌人共享所受伤害的20%。']
    if mode == 0:
        pass
    if mode == 1:
        if '石化' in state_type:
            char.技能攻击力加成(part=part, x=0.2)


def entry_925(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 增加3%的所有异常状态抗性， 效果持续20秒。 (最多叠加5次； 被击时减少2层叠加数)']
    if mode == 0:
        pass
    if mode == 1:
        char.所有异常抗性加成(0.03 * 5)


def entry_930(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击异常状态的敌人时， 每1种异常状态， 攻击强化 +889 (最多叠加3次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(889, lv) * min(3, len(state_type)))


def entry_932(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 增加2%的攻击和施放速度。 (最多叠加15次； 非攻击状态下每0.5秒减少1次。)']
    if mode == 0:
        pass
    if mode == 1:
        char.所有速度增加(0.02 * 15)


def entry_936(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 增加2%的技能冷却时间恢复速度。 (觉醒技能除外； 冷却时间1秒； 最多叠加10次)', '受到总HP1%以上的伤害时， 技能冷却时间恢复速度增加效果的叠加数减少2层。']
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(1, 100, 0.02 * 10, [50, 85, 100])
        char.条件冷却恢复加成("所有[觉醒除外]", 0.2)


def entry_937(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 攻击强化 +356 (最多叠加10次； 被击时减少1次)', '该装备属性的攻击强化效果每次叠加时， 减少2%的移动速度。 (最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(356, lv) * 10)
        char.移动速度增加(0.01 * 10)


def entry_938(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 消耗10%的MP， 增加15%的攻击、 移动速度和20%的施放速度， 效果持续30秒。 (冷却时间30秒)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.15)
        char.施放速度增加(0.20)
        char.移动速度增加(0.15)


def entry_943(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 有5%的几率消耗3个红色小晶块， 使自身与300px内的敌人进入灼伤状态。 (冷却时间10秒)', '灼伤伤害 +10%']
    if mode == 0:
        pass
    if mode == 1:
        if '灼烧' not in state_type:
            state_type.append('灼烧')
        if '灼烧' not in own_state_type:
            own_state_type.append('灼烧')
        if '灼烧' in own_state_type:
            char.异常增伤('灼烧', 0.1)


def entry_875(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['冰属性抗性 +50', '火、 光、 暗属性抗性 -20']
    if mode == 0:
        char.冰属性抗性加成(50)
        char.火属性抗性加成(-20)
        char.光属性抗性加成(-20)
        char.暗属性抗性加成(-20)
    if mode == 1:
        pass


def entry_876(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['冰属性强化高于150时， 物理、 魔法暴击 +15%']
    if mode == 0:
        pass
    if mode == 1:
        char.暴击率增加(0.15)


def entry_879(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['无需无色小晶块的技能冷却时间 -30%', '无色小晶块技能冷却时间 +15%']
    if mode == 0:
        # char.条件冷却加成('消耗无色', -0.15)
        # char.条件冷却加成('不消耗无色', 0.3)
        for skill in char.技能队列:
            if skill["无色消耗"] == 0:
                skill["CDR"] *= 0.7
        for skill in char.技能队列:
            if skill["无色消耗"] > 0:
                skill["CDR"] *= 1.15
        char.条件冷却加成("消耗无色", -0.15)
        char.条件冷却加成("不消耗无色", 0.3)
    if mode == 1:
        pass


def entry_881(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['出血抗性 +1%', '物理防御力 +500']
    if mode == 0:
        char.异常抗性加成('出血', 0.01)
    if mode == 1:
        pass


def entry_882(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['出血伤害 +15%', '出血抗性 +10%']
    if mode == 0:
        char.异常增伤('出血', 0.15)
        char.异常抗性加成('出血', 0.1)
    if mode == 1:
        pass


def entry_883(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['出血伤害 +20%']
    if mode == 0:
        char.异常增伤('出血', 0.2)
    if mode == 1:
        pass


def entry_392(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['受基础精通影响攻击时，所有属性强化 +35，效果持续10秒(冷却时间15秒)']
    if mode == 0:
        pass
    if mode == 1:
        # 期望/全程
        char.所有属性强化加成(35/15*10)
        pass


def entry_538(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['Lv30 buff技能Lv+1', 'Lv50 主动技能Lv+2']
    if mode == 0:
        char.buff技能等级加成(30, 1)
        char.技能等级加成('主动', 50, 50, 2)
    if mode == 1:
        pass


def entry_791(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv1~100所有技能攻击力 +10%']
    if mode == 0:
        char.技能倍率加成(1, 100, 0.1)
    if mode == 1:
        pass


def entry_792(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv1~100所有技能Lv +1 (觉醒技能除外)']
    if mode == 0:
        char.技能等级加成('所有', 1, 100, 1, [50, 85, 100])
    if mode == 1:
        pass


def entry_811(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['HP最大值 +10%', '所有异常状态抗性 +10%']
    if mode == 0:
        char.所有异常抗性加成(0.1)
    if mode == 1:
        pass


def entry_836(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['暗属性抗性 +20']
    if mode == 0:
        char.暗属性抗性加成(20)
    if mode == 1:
        pass


def entry_837(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['暗属性抗性 +50', '火、 冰、 光属性抗性 -20']
    if mode == 0:
        char.暗属性抗性加成(50)
        char.火属性抗性加成(-20)
        char.冰属性抗性加成(-20)
        char.光属性抗性加成(-20)
    if mode == 1:
        pass


def entry_838(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['暗属性强化高于150时， 物理、 魔法暴击率 +15%']
    if mode == 0:
        pass
    if mode == 1:
        char.暴击率增加(0.15)


def entry_843(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['背击时， 使敌人进入出血、 灼伤、 中毒、 感电异常状态中的1个， 效果持续10秒。 (冷却时间10秒)', '所有异常状态抗性 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.所有异常抗性加成(0.1)


def entry_845(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被暗属性攻击时， 增加30点暗属性强化， 效果持续10秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.暗属性强化加成(30)


def entry_847(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被冰属性攻击时， 增加30点冰属性强化， 效果持续10秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.冰属性强化加成(30)


def entry_850(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被光属性攻击时， 增加30点光属性强化， 效果持续10秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.光属性强化加成(30)


def entry_852(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被火属性攻击时， 增加30点火属性强化， 效果持续10秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.火属性强化加成(30)


def entry_854(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被击伤害 +10%', '物理暴击率 +5%', '魔法暴击率 +5%']
    if mode == 0:
        pass
    if mode == 1:
        char.暴击率增加(0.05)


def entry_855(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被击时， 增加20点冰属性强化， 效果持续10秒。 (最多叠加1次)', 'HP最大值 -1000']
    if mode == 0:
        pass
    if mode == 1:
        char.冰属性强化加成(20)


def entry_856(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被击时， 增加20点暗属性强化， 效果持续10秒。 (最多叠加1次)', 'HP最大值 -1000']
    if mode == 0:
        pass
    if mode == 1:
        char.暗属性强化加成(20)


def entry_857(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被击时， 增加20点光属性强化， 效果持续10秒。 (最多叠加1次)', 'HP最大值 -1000']
    if mode == 0:
        pass
    if mode == 1:
        char.光属性强化加成(20)


def entry_859(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被击时， 增加20点火属性强化， 效果持续10秒。 (最多叠加1次)', 'HP最大值 -1000']
    if mode == 0:
        pass
    if mode == 1:
        char.火属性强化加成(20)


def entry_861(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被击时， 消耗MP最大值的10%， 增加15%的攻击、 移动速度和20%的施放速度， 效果持续30秒。 (冷却时间30秒)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.15)
        char.移动速度增加(0.15)
        char.施放速度增加(0.20)


def entry_864(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被击时所受攻击适用为冰属性。', '被击时， 增加5点冰属性抗性， 效果持续10秒。 (最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        char.冰属性抗性加成(5 * 5)


def entry_865(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被击时所受攻击适用为光属性。', '被击时， 增加5点光属性抗性， 效果持续10秒。 (最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        char.光属性抗性加成(5 * 5)


def entry_866(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被击时所受攻击适用为火属性。', '被击时， 增加5点火属性抗性， 效果持续10秒。 (最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        char.火属性抗性加成(5 * 5)


def entry_867(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被击时所受攻击适用为暗属性。', '被击时， 增加5点暗属性抗性， 效果持续10秒。 (最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        char.暗属性抗性加成(5 * 5)


def entry_872(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['冰冻抗性 +3%', '灼伤抗性 -1.5%']
    if mode == 0:
        char.异常抗性加成('冰冻', 0.03)
        char.异常抗性加成('灼烧', -0.015)
    if mode == 1:
        pass


def entry_873(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['冰冻抗性 -3%', '聊天中输入包含“冰”的文字时， 自身进入冰冻状态， 效果持续10秒。 (冷却时间30秒)', '角色进入该装备属性的冰冻状态时， 聊天中输入包含“叮”的文字时， 冰冻状态解除。']
    if mode == 0:
        char.异常抗性加成('冰冻', -0.03)
    if mode == 1:
        if '冰冻' not in own_state_type:
            own_state_type.append('冰冻')
        pass


def entry_7(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['物理暴击率 +5%', '魔法暴击率 +5%']
    if mode == 0:
        char.物理暴击率增加(0.05)
        char.魔法暴击率增加(0.05)
    if mode == 1:
        pass


def entry_8(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击速度 +8%', '施放速度 +12%']
    if mode == 0:
        char.攻击速度增加(0.08)
        char.施放速度增加(0.12)
    if mode == 1:
        pass


def entry_9(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['移动速度 +8%']
    if mode == 0:
        char.移动速度增加(0.08)
    if mode == 1:
        pass


def entry_10(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['命中率 +10%']
    if mode == 0:
        char.命中率增加(0.1)
    if mode == 1:
        pass


def entry_11(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['回避率 +8%']
    if mode == 0:
        char.回避率增加(0.08)
    if mode == 1:
        pass


def entry_15(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['冰属性强化 +15']
    if mode == 0:
        char.冰属性强化加成(15)
    if mode == 1:
        pass


def entry_16(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['光属性强化 +15']
    if mode == 0:
        char.光属性强化加成(15)
    if mode == 1:
        pass


def entry_17(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['火属性强化 +15']
    if mode == 0:
        char.火属性强化加成(15)
    if mode == 1:
        pass


def entry_18(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['暗属性强化 +15']
    if mode == 0:
        char.暗属性强化加成(15)
    if mode == 1:
        pass


def entry_19(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有属性强化 +10']
    if mode == 0:
        char.所有属性强化加成(10)
    if mode == 1:
        pass


def entry_20(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['火属性抗性 +10']
    if mode == 0:
        char.火属性抗性加成(10)
    if mode == 1:
        pass


def entry_21(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['冰属性抗性 +10']
    if mode == 0:
        char.冰属性抗性加成(10)
    if mode == 1:
        pass


def entry_22(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['光属性抗性 +10']
    if mode == 0:
        char.光属性抗性加成(10)
    if mode == 1:
        pass


def entry_23(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['暗属性抗性 +10']
    if mode == 0:
        char.暗属性抗性加成(10)
    if mode == 1:
        pass


def entry_25(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有属性抗性 +8']
    if mode == 0:
        char.所有属性抗性加成(8)
    if mode == 1:
        pass


def entry_26(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有属性强化 +15', '所有属性抗性 -10']
    if mode == 0:
        char.所有属性强化加成(15)
        char.所有属性抗性加成(-10)
    if mode == 1:
        pass


def entry_27(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['物理暴击率 +7%', '魔法暴击率 +7%', '所有异常状态抗性 -10%']
    if mode == 0:
        char.物理暴击率增加(0.07)
        char.魔法暴击率增加(0.07)
        char.所有异常抗性加成(-0.1)
    if mode == 1:
        pass


def entry_28(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['该装备的成长属性等级之和每达到40，增加3%的技能攻击力', ' - 穿戴神话装备时不适用', ' - 仅适用上衣、手镯、耳环中最高的1个']
    if mode == 0:
        if not char.已穿戴神话():  # 判断是否穿戴神话装备
            x = sum(char.词条等级.get(part, [0]))
            temp = {}
            for i in ['上衣', '手镯', '耳环']:  # 计算3个部位最高值
                temp[i] = sum(char.词条等级.get(i, [0]))
            temp = sorted(temp.items(), key=lambda x: x[1], reverse=True)
            if part == temp[0][0]:
                char.技能攻击力加成(part=part, x=0.03 * int(x / 40))
    if mode == 1:
        pass


def entry_29(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['Lv30 buff技能Lv+1', 'Lv50 主动技能Lv+1']
    if mode == 0:
        char.buff技能等级加成(30, 1)
        char.技能等级加成('主动', 50, 50, 1)
    if mode == 1:
        pass


def entry_30(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['Lv30 buff技能Lv+3', 'Lv50 主动技能Lv+4']
    if mode == 0:
        char.buff技能等级加成(30, 3)
        char.技能等级加成('主动', 50, 50, 4)
    if mode == 1:
        pass


def entry_31(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['该装备的附魔效果 +70% (技能Lv效果与冒险家名望除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.部位附魔[part](char, rate=0.7)


def entry_32(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['该装备的附魔效果 +70% (技能Lv效果与冒险家名望除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.部位附魔[part](char, rate=0.7)


def entry_33(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 该装备的附魔效果增加30%， 效果持续10秒。 (最多叠加1次， 技能Lv效果与冒险家名望除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.部位附魔[part](char, rate=0.3)


def entry_34(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时， 该装备的附魔效果增加30%， 效果持续10秒。 (最多叠加1次， 技能Lv效果与冒险家名望除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.部位附魔[part](char, rate=0.3)


def entry_36(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['控制敌人时，所有属性强化 +20，效果持续20秒']
    if mode == 0:
        pass
    if mode == 1:
        char.所有属性强化加成(20)


def entry_102(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['中毒伤害 +10%']
    if mode == 0:
        char.异常增伤('中毒', 0.1)
    if mode == 1:
        pass


def entry_103(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['灼伤伤害 +10%']
    if mode == 0:
        char.异常增伤('灼烧', 0.1)
    if mode == 1:
        pass


def entry_104(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['感电伤害 +10%']
    if mode == 0:
        char.异常增伤('感电', 0.1)
    if mode == 1:
        pass


def entry_105(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['出血伤害 +10%']
    if mode == 0:
        char.异常增伤('出血', 0.1)
    if mode == 1:
        pass


def entry_114(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['受身蹲伏结束后60秒内，攻击速度+40%，移动速度+40%，施放速度+60%(冷却时间10秒，最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.基础属性加成(攻击速度=0.4, 移动速度=0.4, 施放速度=0.6)


def entry_123(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时，消耗1个红色小晶块，火属性强化 +25，效果持续30秒(冷却时间30秒)']
    if mode == 0:
        pass
    if mode == 1:
        char.火属性强化加成(25)


def entry_124(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时，消耗1个蓝色小晶块，冰属性强化 +25，效果持续30秒(冷却时间30秒)']
    if mode == 0:
        pass
    if mode == 1:
        char.冰属性强化加成(25)


def entry_125(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时，消耗1个白色小晶块，光属性强化 +25，效果持续30秒(冷却时间30秒)']
    if mode == 0:
        pass
    if mode == 1:
        char.光属性强化加成(25)


def entry_126(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时，消耗1个黑色小晶块，暗属性强化 +25，效果持续30秒(冷却时间30秒)']
    if mode == 0:
        pass
    if mode == 1:
        char.暗属性强化加成(25)


def entry_127(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['使用消耗品时，攻击速度、移动速度、施放速度 +20%，效果持续30秒(冷却时间10秒，最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.基础属性加成(攻击速度=0.2, 移动速度=0.2, 施放速度=0.2)


def entry_152(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['技能MP消耗量 -7%']
    if mode == 0:
        pass
    if mode == 1:
        char.MP消耗量加成(-0.07)


def entry_154(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被火属性攻击时， 增加20点火属性抗性， 效果持续10秒。 (冷却时间5秒； 最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.火属性抗性加成(20)


def entry_155(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被冰属性攻击时， 增加20点冰属性抗性， 效果持续10秒。 (冷却时间5秒； 最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.冰属性抗性加成(20)


def entry_156(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被光属性攻击时， 增加20点光属性抗性， 效果持续10秒。 (冷却时间5秒； 最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.光属性抗性加成(20)


def entry_157(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被暗属性攻击时， 增加20点暗属性抗性， 效果持续10秒。 (冷却时间5秒； 最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.暗属性抗性加成(20)


def entry_167(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击速度 +30%', '物理防御力 -20000', '魔法防御力 -20000']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.3)


def entry_168(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放速度 +45%', '物理防御力 -20000', '魔法防御力 -20000']
    if mode == 0:
        pass
    if mode == 1:
        char.施放速度增加(0.45)


def entry_170(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['被击伤害 -25%', '移动速度 -20%']
    if mode == 0:
        char.移动速度增加(-0.2)
    if mode == 1:
        pass


def entry_171(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['HP MAX +1200', '攻击速度 -15%', '施放速度 -22.5%']
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.施放速度增加(-0.225)
    if mode == 1:
        pass


def entry_172(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['MP MAX +1890', '移动速度 -20%']
    if mode == 0:
        char.移动速度增加(-0.2)
    if mode == 1:
        pass


def entry_173(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['火属性强化 +35', '所有异常状态抗性 -10%']
    if mode == 0:
        char.火属性强化加成(35)
        char.所有异常抗性加成(-0.1)
    if mode == 1:
        pass


def entry_174(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['冰属性强化 +35', '所有异常状态抗性 -10%']
    if mode == 0:
        char.冰属性强化加成(35)
        char.所有异常抗性加成(-0.1)
    if mode == 1:
        pass


def entry_175(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['光属性强化 +35', '所有异常状态抗性 -10%']
    if mode == 0:
        char.光属性强化加成(35)
        char.所有异常抗性加成(-0.1)
    if mode == 1:
        pass


def entry_176(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['暗属性强化 +35', '所有异常状态抗性 -10%']
    if mode == 0:
        char.暗属性强化加成(35)
        char.所有异常抗性加成(-0.1)
    if mode == 1:
        pass


def entry_177(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['角色伤害的10%转化为中毒伤害']
    if mode == 0:
        if '中毒' not in state_type:
            state_type.append("中毒")
        char.伤害类型转化('直伤', '中毒', 0.1)
    if mode == 1:
        pass


def entry_178(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['角色伤害的10%转化为灼伤伤害']
    if mode == 0:
        if '灼烧' not in state_type:
            state_type.append("灼烧")
        char.伤害类型转化('直伤', '灼烧', 0.1)
    if mode == 1:
        pass


def entry_179(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['角色伤害的10%转化为感电伤害']
    if mode == 0:
        if '感电' not in state_type:
            state_type.append("感电")
        char.伤害类型转化('直伤', '感电', 0.1)
    if mode == 1:
        pass


def entry_180(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['角色伤害的10%转化为出血伤害']
    if mode == 0:
        if '出血' not in state_type:
            state_type.append("出血")
        char.伤害类型转化('直伤', '出血', 0.1)
    if mode == 1:
        pass


def entry_181(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['剩余HP超过50%以上时，攻击强化 +1778']
    if mode == 0:
        pass
    if mode == 1:
        if hp_rate_num >= 50:
            char.攻击强化加成(成长词条计算(1778, lv))
        pass


def entry_182(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身所有属性抗性之和超过250以上时，中毒伤害 +15%']
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('中毒', 0.15)


def entry_192(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身所有属性强化之和超过850以上时，移动速度 +40%']
    if mode == 0:
        pass
    if mode == 1:
        # 判断暂未实现
        char.移动速度增加(0.4)


def entry_197(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身所有属性强化之和超过850以上时，所有异常状态抗性 +30%']
    if mode == 0:
        pass
    if mode == 1:
        # 判断暂未实现
        char.所有异常抗性加成(0.3)


def entry_198(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身所有异常状态抗性之和超过50%以上时，攻击速度 +20%，施放速度 +30%']
    if mode == 0:
        pass
    if mode == 1:
        # 判断暂未实现
        char.攻击速度增加(0.2)
        char.施放速度增加(0.3)


def entry_76(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['出血抗性 +8%']
    if mode == 0:
        char.异常抗性加成('出血', 0.08)
    if mode == 1:
        pass


def entry_77(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['中毒抗性 +8%']
    if mode == 0:
        char.异常抗性加成('中毒', 0.08)
    if mode == 1:
        pass


def entry_78(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['灼伤抗性 +8%']
    if mode == 0:
        char.异常抗性加成('灼烧', 0.08)
    if mode == 1:
        pass


def entry_79(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['感电抗性 +8%']
    if mode == 0:
        char.异常抗性加成('感电', 0.08)
    if mode == 1:
        pass


def entry_80(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['冰冻抗性 +8%']
    if mode == 0:
        char.异常抗性加成('冰冻', 0.08)
    if mode == 1:
        pass


def entry_81(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['减速抗性 +8%']
    if mode == 0:
        char.异常抗性加成('减速', 0.08)
    if mode == 1:
        pass


def entry_82(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['眩晕抗性 +8%']
    if mode == 0:
        char.异常抗性加成('眩晕', 0.08)
    if mode == 1:
        pass


def entry_83(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['诅咒抗性 +8%']
    if mode == 0:
        char.异常抗性加成('诅咒', 0.08)
    if mode == 1:
        pass


def entry_84(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['失明抗性 +8%']
    if mode == 0:
        char.异常抗性加成('失明', 0.08)
    if mode == 1:
        pass


def entry_85(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['石化抗性 +8%']
    if mode == 0:
        char.异常抗性加成('石化', 0.08)
    if mode == 1:
        pass


def entry_86(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['睡眠抗性 +8%']
    if mode == 0:
        char.异常抗性加成('睡眠', 0.08)
    if mode == 1:
        pass


def entry_87(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['混乱抗性 +8%']
    if mode == 0:
        char.异常抗性加成('混乱', 0.08)
    if mode == 1:
        pass


def entry_88(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['束缚抗性 +8%']
    if mode == 0:
        char.异常抗性加成('束缚', 0.08)
    if mode == 1:
        pass


def entry_218(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['受基础精通影响攻击时，出血、中毒、灼伤、感电伤害 +20%，效果持续10秒(冷却时间15秒)']
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('出血', 0.2)
        char.异常增伤('中毒', 0.2)
        char.异常增伤('灼烧', 0.2)
        char.异常增伤('感电', 0.2)


def entry_226(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['5秒未前冲时，攻击强化 +267(最多叠加10次)', '前冲时，攻击强化效果叠加次数 -1']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(267, lv) * 10)


def entry_228(char: CharacterProperty = {}, mode: int = 0, text=False, part='', lv=0):
    if text:
        return ['2秒滞空时，所有属性强化 +6(最多叠加10次)', '受到总HP1%以上伤害时，所有属性强化增加效果叠加次数 -2']
    if mode == 0:
        pass
    if mode == 1:
        char.所有属性强化加成(6 * 10)


def entry_238(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['物理防御力+25000', '魔法防御力+25000', '物理暴击率 -8%', '魔法暴击率 -8%']
    if mode == 0:
        pass
    if mode == 1:
        char.暴击率增加(-0.08)


def entry_252(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['剩余MP超过50%以上时，物理、魔法暴击率 +15%']
    if mode == 0:
        pass
    if mode == 1:
        char.暴击率增加(0.15)


def entry_259(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['技能快捷栏中每存在1个空栏，技能攻击力 +2%(最多增加12%)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(part=part, x=min(
            0.12, len(list(filter(lambda i: i == "", char.hotkey)))*0.02))


def entry_264(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['移动速度 +30%', '物理防御力-20000', '魔法防御力-20000']
    if mode == 0:
        char.移动速度增加(0.3)
    if mode == 1:
        pass


def entry_288(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv15技能时，进入2秒霸体状态，霸体解除时，攻击速度+15%，施放速度+22.5%(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.15)
        char.施放速度增加(0.225)


def entry_294(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时，攻击强化 +111(最多叠加20次)', '受到总HP1%以上伤害时，攻击强化效果叠加次数 -4']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(111, lv) * 20)


def entry_296(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['出血伤害 +30%', '所受伤害 +20%']
    if mode == 0:
        char.异常增伤('出血', 0.3)
    if mode == 1:
        pass


def entry_297(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['感电伤害 +30%', '所受伤害 +20%']
    if mode == 0:
        char.异常增伤('感电', 0.3)
    if mode == 1:
        pass


def entry_298(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['灼伤伤害 +30%', '所受伤害 +20%']
    if mode == 0:
        char.异常增伤('灼烧', 0.3)
    if mode == 1:
        pass


def entry_299(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['中毒伤害 +30%', '所受伤害 +20%']
    if mode == 0:
        char.异常增伤('中毒', 0.3)
    if mode == 1:
        pass


# endregion

# region 敌人类型词条
enemy_type = []
enemy_type_list = ['', '机械', '恶魔', '精灵',
                   '天使', '龙族', '人型', '野兽', '植物', '不死', '昆虫']


def set_enemy_type(x):
    global enemy_type
    enemy_type = []
    for i in x:
        enemy_type.append(enemy_type_list[i])


entry_chose.append((20037, ['选择敌人类型'] + ['攻击{}敌人'.format(i)
                                         for i in enemy_type_list[1:]], ""))
variable_set[20037] = set_enemy_type


def entry_37(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击机械型敌人时，技能攻击力 +7%']
    if mode == 0:
        if '机械' in enemy_type:
            char.技能攻击力加成(part=part, x=0.07)
    if mode == 1:
        pass


def entry_38(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击恶魔型敌人时，技能攻击力 +7%']
    if mode == 0:
        if '恶魔' in enemy_type:
            char.技能攻击力加成(part=part, x=0.07)
    if mode == 1:
        pass


def entry_39(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击精灵型敌人时，技能攻击力 +7%']
    if mode == 0:
        if '精灵' in enemy_type:
            char.技能攻击力加成(part=part, x=0.07)
    if mode == 1:
        pass


def entry_40(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击天使型敌人时，技能攻击力 +7%']
    if mode == 0:
        if '天使' in enemy_type:
            char.技能攻击力加成(part=part, x=0.07)
    if mode == 1:
        pass


def entry_41(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击龙族型敌人时，技能攻击力 +7%']
    if mode == 0:
        if '龙族' in enemy_type:
            char.技能攻击力加成(part=part, x=0.07)
    if mode == 1:
        pass


def entry_106(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击人型敌人时，技能攻击力 +7%']
    if mode == 0:
        if '人型' in enemy_type:
            char.技能攻击力加成(part=part, x=0.07)
    if mode == 1:
        pass


def entry_107(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击野兽型敌人时，技能攻击力 +7%']
    if mode == 0:
        if '野兽' in enemy_type:
            char.技能攻击力加成(part=part, x=0.07)
    if mode == 1:
        pass


def entry_108(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击植物型敌人时，技能攻击力 +7%']
    if mode == 0:
        if '植物' in enemy_type:
            char.技能攻击力加成(part=part, x=0.07)
    if mode == 1:
        pass


def entry_109(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击不死型敌人时，技能攻击力 +7%']
    if mode == 0:
        if '不死' in enemy_type:
            char.技能攻击力加成(part=part, x=0.07)
    if mode == 1:
        pass


def entry_110(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击昆虫型敌人时，技能攻击力 +7%']
    if mode == 0:
        if '昆虫' in enemy_type:
            char.技能攻击力加成(part=part, x=0.07)
    if mode == 1:
        pass


# endregion

# region 敌人状态词条
state_type = []
state_type_list = ['', '出血', '中毒', '灼烧', '感电', '眩晕',
                   '诅咒', '睡眠', '束缚', '冰冻', '减速', '石化', '失明', '混乱']


def set_state_type(x):
    global state_type
    state_type = []
    for i in x:
        state_type.append(state_type_list[i])


entry_chose.append((20042, ['选择敌人状态'] + ['攻击{}敌人'.format(i)
                                         for i in state_type_list[1:]], ""))
variable_set[20042] = set_state_type


def entry_42(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击出血状态的敌人时， 技能攻击力 +5%']
    if mode == 0:
        if '出血' in state_type:
            char.技能攻击力加成(part=part, x=0.05)
    if mode == 1:
        pass


def entry_43(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击中毒状态的敌人时， 技能攻击力 +5%']
    if mode == 0:
        if '中毒' in state_type:
            char.技能攻击力加成(part=part, x=0.05)
    if mode == 1:
        pass


def entry_44(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击灼伤状态的敌人时， 技能攻击力 +5%']
    if mode == 0:
        if '灼烧' in state_type:
            char.技能攻击力加成(part=part, x=0.05)
    if mode == 1:
        pass


def entry_45(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击感电状态的敌人时， 技能攻击力 +5%']
    if mode == 0:
        if '感电' in state_type:
            char.技能攻击力加成(part=part, x=0.05)
    if mode == 1:
        pass


def entry_46(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击眩晕状态的敌人时， 技能攻击力 +15%']
    if mode == 0:
        if '眩晕' in state_type:
            char.技能攻击力加成(part=part, x=0.15)
    if mode == 1:
        pass


def entry_47(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击诅咒状态敌人时，技能攻击力 +10%']
    if mode == 0:
        if '诅咒' in state_type:
            char.技能攻击力加成(part=part, x=0.10)
    if mode == 1:
        pass


def entry_48(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击睡眠状态敌人时，技能攻击力 +15%']
    if mode == 0:
        if '睡眠' in state_type:
            char.技能攻击力加成(part=part, x=0.15)
    if mode == 1:
        pass


def entry_49(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击束缚状态敌人时，技能攻击力 +10%']
    if mode == 0:
        if '束缚' in state_type:
            char.技能攻击力加成(part=part, x=0.10)
    if mode == 1:
        pass


def entry_50(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击冰冻状态的敌人时， 技能攻击力 +15%']
    if mode == 0:
        if '冰冻' in state_type:
            char.技能攻击力加成(part=part, x=0.15)
    if mode == 1:
        pass


def entry_51(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击减速状态敌人时，技能攻击力 +10%']
    if mode == 0:
        if '减速' in state_type:
            char.技能攻击力加成(part=part, x=0.10)
    if mode == 1:
        pass


def entry_52(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击失明状态的敌人时， 技能攻击力 +10%']
    if mode == 0:
        if '失明' in state_type:
            char.技能攻击力加成(part=part, x=0.10)
    if mode == 1:
        pass


def entry_53(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击石化状态的敌人时， 技能攻击力 +15%']
    if mode == 0:
        if '石化' in state_type:
            char.技能攻击力加成(part=part, x=0.15)
    if mode == 1:
        pass


def entry_54(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击混乱状态敌人时，技能攻击力 +10%']
    if mode == 0:
        if '混乱' in state_type:
            char.技能攻击力加成(part=part, x=0.10)
    if mode == 1:
        pass


def entry_55(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击无力化状态下的敌人时，出血伤害 +15%']
    if mode == 0:
        for i in ['冰冻', '眩晕', '睡眠', '石化', '减速', '束缚', '失明', '混乱', '诅咒']:
            if i in state_type:
                char.异常增伤('出血', 0.15)
                return
    if mode == 1:
        pass


def entry_56(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击无力化状态下的敌人时，中毒伤害 +15%']
    if mode == 0:
        for i in ['冰冻', '眩晕', '睡眠', '石化', '减速', '束缚', '失明', '混乱', '诅咒']:
            if i in state_type:
                char.异常增伤('中毒', 0.15)
                return
    if mode == 1:
        pass


def entry_57(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击无力化状态下的敌人时，灼伤伤害 +15%']
    if mode == 0:
        for i in ['冰冻', '眩晕', '睡眠', '石化', '减速', '束缚', '失明', '混乱', '诅咒']:
            if i in state_type:
                char.异常增伤('灼烧', 0.15)
                return
    if mode == 1:
        pass


def entry_58(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击无力化状态下的敌人时，感电伤害 +15%']
    if mode == 0:
        for i in ['冰冻', '眩晕', '睡眠', '石化', '减速', '束缚', '失明', '混乱', '诅咒']:
            if i in state_type:
                char.异常增伤('感电', 0.15)
                return
    if mode == 1:
        pass


# endregion

# region 攻击领主相关
boss_time = 0
boss_time_list = [0, 1, 2]


def set_boss_time(x):
    global boss_time
    boss_time = boss_time_list[x[0]]


entry_chose.append((20216, ['选择攻击领主状态'] + ['前20秒(正面)', '20-30秒(负面)'], ""))
multi_select[20216] = False
variable_set[20216] = set_boss_time


def entry_216(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击领主敌人时，中毒伤害 +20%，效果持续20秒', '20秒后，中毒伤害 -10%，效果持续10秒']
    if mode == 0:
        pass
    if mode == 1:
        if boss_time == 1:
            char.异常增伤('中毒', 0.2)
        elif boss_time == 2:
            char.异常增伤('中毒', -0.1)


def entry_217(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击领主敌人时，暗属性强化 +35，效果持续20秒', '20秒后，暗属性强化 -10，效果持续10秒']
    if mode == 0:
        pass
    if mode == 1:
        if boss_time == 1:
            char.暗属性强化加成(35)
        elif boss_time == 2:
            char.暗属性强化加成(-10)


def entry_376(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击领主敌人时，攻击强化 +N，效果持续20秒', '20秒后，攻击强化 -N，效果持续10秒']
    if mode == 0:
        pass
    if mode == 1:
        if boss_time == 1:
            char.攻击强化加成(成长词条计算(0, lv))
        elif boss_time == 2:
            char.攻击强化加成(-成长词条计算(0, lv))


def entry_377(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击领主敌人时，攻击速度 +25%，施放速度 +37.5%，效果持续20秒', '20秒后，攻击速度 -10%，施放速度 -15%，效果持续10秒']
    if mode == 0:
        pass
    if mode == 1:
        if boss_time == 1:
            char.攻击速度增加(0.25)
            char.施放速度增加(0.375)
        elif boss_time == 2:
            char.攻击速度增加(-0.1)
            char.施放速度增加(-0.15)


def entry_378(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击领主敌人时，出血伤害 +20%，效果持续20秒', '20秒后，出血伤害 -10%，效果持续10秒']
    if mode == 0:
        pass
    if mode == 1:
        if boss_time == 1:
            char.异常增伤('出血', 0.2)
        elif boss_time == 2:
            char.异常增伤('出血', -0.1)


def entry_379(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击领主敌人时，冰属性强化 +35，效果持续20秒', '20秒后，冰属性强化 -10，效果持续10秒']
    if mode == 0:
        pass
    if mode == 1:
        if boss_time == 1:
            char.冰属性强化加成(35)
        elif boss_time == 2:
            char.冰属性强化加成(-10)


def entry_382(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击领主敌人时，灼伤伤害 +20%，效果持续20秒', '20秒后，灼伤伤害 -10%，效果持续10秒']
    if mode == 0:
        pass
    if mode == 1:
        if boss_time == 1:
            char.异常增伤('灼烧', 0.2)
        elif boss_time == 2:
            char.异常增伤('灼烧', -0.1)


def entry_383(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击领主敌人时，火属性强化 +35，效果持续20秒', '20秒后，火属性强化 -10，效果持续10秒']
    if mode == 0:
        pass
    if mode == 1:
        if boss_time == 1:
            char.火属性强化加成(35)
        elif boss_time == 2:
            char.火属性强化加成(-10)


def entry_389(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击领主敌人时，感电伤害 +20%，效果持续20秒', '20秒后，感电伤害 -10%，效果持续10秒']
    if mode == 0:
        pass
    if mode == 1:
        if boss_time == 1:
            char.异常增伤('感电', 0.2)
        elif boss_time == 2:
            char.异常增伤('感电', -0.1)


def entry_390(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击领主敌人时，光属性强化 +35，效果持续20秒', '20秒后，光属性强化 -10，效果持续10秒']
    if mode == 0:
        pass
    if mode == 1:
        if boss_time == 1:
            char.光属性强化加成(35)
        elif boss_time == 2:
            char.光属性强化加成(-10)


def entry_381(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['受到领主敌人攻击时，所受伤害 -20%，效果持续20秒', '20秒后，所受伤害 +10%，效果持续10秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


# endregion

# region 攻击类型选择
attack_type = []
attack_type_list = ['', '普通敌人', '稀有敌人', '领主敌人', '正面攻击', '背面攻击', '破招攻击',
                    '非破招攻击']


def set_attack_type(x):
    global attack_type
    attack_type = []
    for i in x:
        attack_type.append(attack_type_list[i])


entry_chose.append((20351, ['选择攻击类型'] + ['{}'.format(i)
                                         for i in attack_type_list[1:]], ""))
variable_set[20351] = set_attack_type


def entry_351(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击普通敌人时，技能攻击力 +15%']
    if mode == 0:
        pass
    if mode == 1:
        if '普通敌人' in attack_type:
            char.技能攻击力加成(part=part, x=0.15)


def entry_369(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击绿名/稀有敌人时，技能攻击力 +8%']
    if mode == 0:
        pass
    if mode == 1:
        if '稀有敌人' in attack_type:
            char.技能攻击力加成(part=part, x=0.08)


def entry_387(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['正面攻击敌人时，技能攻击力 +8%']
    if mode == 0:
        pass
    if mode == 1:
        if '正面攻击' in attack_type:
            # 期望处理
            if '背面攻击' in attack_type:
                char.技能攻击力加成(part=part, x=0.04)
            else:
                char.技能攻击力加成(part=part, x=0.08)


def entry_388(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['背击攻击敌人时，技能攻击力 +8%']
    if mode == 0:
        pass
    if mode == 1:
        if '背面攻击' in attack_type:
            if '正面攻击' in attack_type:
                char.技能攻击力加成(part=part, x=0.04)
            else:
                char.技能攻击力加成(part=part, x=0.08)


def entry_399(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['破招攻击时，技能攻击力 +8%']
    if mode == 0:
        pass
    if mode == 1:
        if '破招攻击' in attack_type:
            if '非破招攻击' in attack_type:
                char.技能攻击力加成(part=part, x=0.04)
            else:
                char.技能攻击力加成(part=part, x=0.08)


def entry_400(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['非破招攻击时，技能攻击力 +8%']
    if mode == 0:
        pass
    if mode == 1:
        if '非破招攻击' in attack_type:
            if '破招攻击' in attack_type:
                char.技能攻击力加成(part=part, x=0.04)
            else:
                char.技能攻击力加成(part=part, x=0.08)


def entry_405(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击领主敌人时，技能攻击力 +6%']
    if mode == 0:
        pass
    if mode == 1:
        if '领主敌人' in attack_type:
            char.技能攻击力加成(part=part, x=0.06)


# endregion

# region 消灭敌人词条
kill_num = 0
kill_num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def set_kill_num(x):
    global kill_num
    kill_num = kill_num_list[x[0]]


entry_chose.append((20074, ['选择消灭敌人层数'] + ['消灭敌人：{}个'.format(i)
                                           for i in kill_num_list[1:]], ""))
multi_select[20074] = False
variable_set[20074] = set_kill_num


def entry_74(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，物理、魔法暴击率+2%，效果持续60秒']
    if mode == 0:
        pass
    if mode == 1:
        if '领主敌人' in attack_type:
            char.暴击率增加(0.02 * kill_num)


def entry_187(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，中毒伤害 +3%，效果持续60秒']
    if mode == 0:
        pass
    if mode == 1:
        if '领主敌人' in attack_type:
            char.异常增伤('中毒', 0.03 * kill_num)


def entry_191(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，出血伤害 +3%，效果持续60秒']
    if mode == 0:
        pass
    if mode == 1:
        if '领主敌人' in attack_type:
            char.异常增伤('出血', 0.03 * kill_num)


def entry_196(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，灼伤伤害 +3%，效果持续60秒']
    if mode == 0:
        pass
    if mode == 1:
        if '领主敌人' in attack_type:
            char.异常增伤('灼烧', 0.03 * kill_num)


def entry_231(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，冰属性强化 +4，效果持续60秒']
    if mode == 0:
        pass
    if mode == 1:
        if '领主敌人' in attack_type:
            char.冰属性强化加成(4 * kill_num)


def entry_232(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，火属性强化 +4，效果持续60秒']
    if mode == 0:
        pass
    if mode == 1:
        if '领主敌人' in attack_type:
            char.火属性强化加成(4 * kill_num)


def entry_233(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，光属性强化 +4，效果持续60秒']
    if mode == 0:
        pass
    if mode == 1:
        if '领主敌人' in attack_type:
            char.光属性强化加成(4 * kill_num)


def entry_234(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，暗属性强化 +4，效果持续60秒']
    if mode == 0:
        pass
    if mode == 1:
        if '领主敌人' in attack_type:
            char.暗属性强化加成(4 * kill_num)


def entry_295(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，Lv80~95主动技能Lv+1(觉醒技能除外)，效果持续60秒']
    if mode == 0:
        pass
    if mode == 1:
        if '领主敌人' in attack_type:
            char.技能等级加成('主动', 80, 95, kill_num, exc=[85])


def entry_300(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，Lv70~75主动技能Lv+1，效果持续60秒']
    if mode == 0:
        pass
    if mode == 1:
        if '领主敌人' in attack_type:
            char.技能等级加成('主动', 70, 75, kill_num)


def entry_308(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，Lv35~40主动技能Lv+1，效果持续60秒']
    if mode == 0:
        pass
    if mode == 1:
        if '领主敌人' in attack_type:
            char.技能等级加成('主动', 35, 40, kill_num)


def entry_322(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，Lv45~60主动技能Lv+1，效果持续60秒']
    if mode == 0:
        pass
    if mode == 1:
        if '领主敌人' in attack_type:
            char.技能等级加成('主动', 45, 60, kill_num)


def entry_329(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，技能攻击力 +2%，效果持续60秒']
    if mode == 0:
        pass
    if mode == 1:
        if '领主敌人' in attack_type:
            char.技能倍率加成(1, 100, 0.02 * kill_num)


def entry_360(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，感电伤害 +3%，效果持续60秒']
    if mode == 0:
        pass
    if mode == 1:
        if '领主敌人' in attack_type:
            char.异常增伤('感电', 0.03 * kill_num)


def entry_235(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['消灭敌人时，所有速度 +5%，效果持续10秒(最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.05 * 5)
        char.施放速度增加(0.05 * 5)
        char.移动速度增加(0.05 * 5)


def entry_239(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['消灭敌人时，恢复5%的已消耗HP']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_240(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['消灭敌人时，恢复5%的已消耗MP']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1175(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['消灭敌人时， 所有职业Lv1~80技能范围增加5%。 (觉醒技能除外， 最多叠加5次)', '施放技能时， 减少4%的技能攻击力， 效果持续10秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        if kill_num >= 1:
            char.技能攻击力加成(part=part, x=-0.04)
# endregion

# region 无色相关词条


def entry_75(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['使用消耗10个以上无色小晶块的技能时，技能冷却时间恢复速度 +30%，效果持续20秒(冷却时间15秒，最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(1, 100, 0.3)
        char.条件冷却恢复加成("所有", 0.3)


def entry_222(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['使用消耗10个以上无色小晶块的技能时，攻击速度 +30%，施放速度 +45%，效果持续20秒(冷却时间15秒，最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.3)
        char.施放速度增加(0.45)


def entry_249(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放不消耗无色小晶块的技能时，技能攻击力 +15%']
    if mode == 0:
        pass
    if mode == 1:
        for skill in char.技能队列:
            if skill["无色消耗"] == 0 or skill['名称'] == '神罚之锤':
                skill["倍率"] *= 1.15


def entry_878(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['不消耗无色小晶块的技能攻击力 -5%', '无色小晶块技能攻击力 +10%', '每次施放无色小晶块技能时， 该技能的无色消耗量增加2倍。 (最多叠加3次)']
    if mode == 0:
        pass
    if mode == 1:
        for index in range(0, len(char.技能队列)):
            skill = char.技能队列[index]
            if skill["无色消耗"] == 0 or skill['名称'] == '神罚之锤':
                skill["倍率"] *= 0.95
            if skill["无色消耗"] > 0:
                skill["倍率"] *= 1.1
                skill["无色消耗"] *= 2**min(len(list(filter(lambda i: i['名称'] ==
                                                        skill['名称'], char.技能队列[0:index]))), 3)
        # todo 施放一次翻倍


def entry_877(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['不消耗无色小晶块的技能攻击力 +20%', '无色小晶块技能攻击力 -10%']
    if mode == 0:
        pass
    if mode == 1:
        for skill in char.技能队列:
            if skill["无色消耗"] == 0 or skill['名称'] == '神罚之锤':
                skill["倍率"] *= 1.2
            if skill["无色消耗"] > 0:
                skill["倍率"] *= 0.9


def entry_899(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放不消耗无色小晶块的技能时， 生成相当于HP最大值10%的保护罩， 效果持续1.5秒。 (冷却时间0.5秒； 最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1096(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放不消耗无色小晶块的技能时， 减少10%的技能MP消耗量， 效果持续10秒。 (最多叠加3次)', '施放无色技能时，技能MP消耗量减少层数初始化。']
    if mode == 0:
        pass
    if mode == 1:
        char.MP消耗量加成(-0.3)
        pass


def entry_1108(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放消耗无色小晶块技能时， 增加10点暗属性强化， 效果持续20秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.暗属性强化加成(10)


def entry_1109(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放消耗无色小晶块技能时， 增加10点冰属性强化， 效果持续20秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.冰属性强化加成(10)


def entry_1110(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放消耗无色小晶块技能时， 根据消耗的无色小晶块数量， 获得能量。 (最多获得100点)', '获得的能量达到100时， 消耗所有能量， 减少5%的技能剩余冷却时间。 (觉醒技能除外)', '普通攻击、 跳跃、 前冲攻击及施放不消耗无色小晶块的技能时， 减少1个能量。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1111(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放消耗无色小晶块技能时， 增加10点光属性强化， 效果持续20秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.光属性强化加成(10, mode=1)


def entry_1112(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放消耗无色小晶块技能时， 增加10点火属性强化， 效果持续20秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.火属性强化加成(10, mode=1)


def entry_1113(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放消耗无色小晶块技能时， 增加8点所有属性强化， 效果持续20秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.所有属性强化加成(8, mode=1)


def entry_1114(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放无色小晶块技能时， 增加10%的移动速度， 效果持续10秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.移动速度增加(0.10)


def entry_1115(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放无需无色小晶块的技能时， 增加10%的攻击速度和15%的施放速度， 效果持续10秒。 (冷却时间5秒； 最多叠加1次)', '无需无色小晶块的技能冷却时间 +20%']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.10)
        char.施放速度增加(0.15)
        char.条件冷却加成("消耗无色", -0.2)
        for skill in char.技能队列:
            if skill["无色消耗"] == 0:
                skill["CDR"] *= 1.2


def entry_1116(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放消耗3个以上无色小晶块的技能时， 增加20点所有属性强化， 效果持续20秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.所有属性强化加成(20, mode=1)


def entry_1117(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放无色小晶块技能时，10秒内恢复5%的MP。 (冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1118(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放无色小晶块技能时， 减少10%的MP消耗量， 效果持续20秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.MP消耗量加成(-0.1)
        pass


def entry_1119(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放消耗无色小晶块技能时， 增加3点所有属性强化， 效果持续10秒。(最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        for i in range(0, 5):
            char.所有属性强化加成(3, mode=1)


def entry_1120(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放无色小晶块技能时， 增加5%的攻击速度和7.5%的施放速度， 效果持续30秒。 (冷却时间5秒； 最多叠加3次。)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.05 * 3)
        char.施放速度增加(0.075 * 3)


def entry_1238(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['使用消耗无色小晶块的技能时，召唤D011-Risa，适用以下效果，持续20秒(冷却时间0.5秒，最多5个)', '- 地图中最强的敌人处于的异常状态适用于D011-Risa', '- 在D011-Risa周围500px范围内是，所有异常状态抗性 +2%(最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        char.所有异常抗性加成(0.02 * 5)


# endregion

# region 连击相关词条
combo_num = 0
combo_num_list = [0, 3, 6, 9, 12, 15, 18, 21,
                  24, 27, 30, 50, 200, 400, 600, 800, 1000]


def set_combo_num(x):
    global combo_num
    combo_num = combo_num_list[x[0]]


entry_chose.append((20113, ['选择连击次数'] + ['{}连击'.format(i)
                                         for i in combo_num_list[1:]], ""))
multi_select[20113] = False
variable_set[20113] = set_combo_num


def entry_113(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每达成3次连击，光属性强化+4(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        for i in range(0, min(10, int(combo_num / 3))):
            char.光属性强化加成(4, mode=1)


def entry_116(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每达成3次连击，攻击速度 +3%，施放速度 +4.5%(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        char.基础属性加成(攻击速度=0.03 * min(10, int(combo_num / 3)),
                    施放速度=0.045 * min(10, int(combo_num / 3)))


def entry_117(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每达成3次连击，攻击强化 +416(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(416, lv) * min(10, int(combo_num / 3)))


def entry_122(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每达成3次连击，移动速度 +3%(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        char.基础属性加成(移动速度=0.03 * min(10, int(combo_num / 3)))


def entry_153(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每进行5次攻击，获得效果(最多叠加20次)', '- 攻击强化 +89', '- 物理防御力 -500', '- 魔法防御力 -500']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(89, lv)*20)
        pass


def entry_219(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每达成3次连击，物理、魔法防御力 +1400(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_220(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每达成3次连击，回避率 +3%(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        char.回避率增加(0.03 * min(10, int(combo_num / 3)))


def entry_221(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每达成3次连击，物理、魔法暴击率 +2%(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        char.暴击率增加(0.02 * min(10, int(combo_num / 3)))


def entry_282(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每达成10次连击，敌人韧性减少量 +5%(最多增加30%)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_284(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px范围内，每存在1个敌人，攻击强化 +296(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(296, lv)*10)
        pass


def entry_336(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每达成3次连击，火属性强化+4(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        for i in range(0, min(10, int(combo_num / 3))):
            char.火属性强化加成(4, mode=1)


def entry_337(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每达成3次连击，冰属性强化+4(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        for i in range(0, min(10, int(combo_num / 3))):
            char.冰属性强化加成(4, mode=1)


def entry_338(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每达成3次连击，暗属性强化+4(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        for i in range(0, min(10, int(combo_num / 3))):
            char.暗属性强化加成(4, mode=1)


def entry_891(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['连击30次时， 攻击强化 +2223， 效果持续30秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        if combo_num >= 30:
            char.攻击强化加成(成长词条计算(2223, lv))


def entry_892(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['连击15次时， 使角色周围450px内所有敌人进入出血状态。 (冷却时间8秒)']
    if mode == 0:
        pass
    if mode == 1:
        if combo_num >= 15 and '出血' not in state_type:
            state_type.append('出血')
        pass


def entry_893(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['连击达到200次时， 500px内稀有、 领主怪物的剩余HP减少1%。 (冷却时间30秒； 辅助职业不适用)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_911(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['连击10次时， 攻击强化 +3705、 MP消耗量 +175%， 效果持续30秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        if combo_num >= 10:
            char.攻击强化加成(成长词条计算(3705, lv))
            char.MP消耗量加成(1.75)


def entry_912(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['连击20次时， 无视敌人8%的防御力， 效果持续30秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        if combo_num >= 20:
            char.百分比防御减少(0.08)


def entry_1044(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每连击200次， 减少1点武器耐久度。 (冷却时间10秒)', '每次连招效果减少耐久度时， 所有技能冷却时间恢复速度增加10%。 (最多叠加5次； 觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(1, 100, 0.1 * min(10, int(combo_num / 200)), [50, 85, 100])
        char.条件冷却恢复加成("所有[觉醒除外]", 0.1 * min(10, int(combo_num / 200)))


def entry_1242(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['地下城入场时激活Buff，冷却时间恢复速度 +25%(最多叠加1次，觉醒技能除外)', '每达成6次连击，冷却时间恢复速度 -5%(最多叠加5次)', '- 施放技能时，冷却时间恢复速度减少效果叠加次数 -1']
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(1, 100, 0.25, [50, 85, 100])
        char.条件冷却恢复加成("所有[觉醒除外]", 0.25)
# endregion

# region 施放冷却时间词条


def entry_118(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放冷却时间在20秒以下的技能时，灼伤伤害 +10%，效果持续3秒(冷却时间3秒，最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('灼烧', 0.1)


def entry_119(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放冷却时间在20秒以下的技能时，出血伤害 +10%，效果持续3秒(冷却时间3秒，最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('出血', 0.1)


def entry_120(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放冷却时间在20秒以下的技能时，感电伤害 +10%，效果持续3秒(冷却时间3秒，最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('感电', 0.1)


def entry_121(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放冷却时间在20秒以下的技能时，中毒伤害 +10%，效果持续3秒(冷却时间3秒，最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('中毒', 0.1)


def entry_245(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放冷却时间在25秒以上的技能时，出血伤害 +20%，效果持续10秒(冷却时间5秒，最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('出血', 0.20)


def entry_246(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放冷却时间在25秒以上的技能时，感电伤害 +20%，效果持续10秒(冷却时间5秒，最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('感电', 0.20)


def entry_257(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放冷却时间在25秒以上的技能时，灼伤伤害 +20%，效果持续10秒(冷却时间5秒，最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('灼烧', 0.2)


def entry_258(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放冷却时间在25秒以上的技能时，中毒伤害 +20%，效果持续10秒(冷却时间5秒，最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('中毒', 0.2)


def entry_267(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放冷却时间在20秒以下的技能时，火属性强化 +25，效果持续10秒(冷却时间3秒，最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.火属性强化加成(25, mode=1)


def entry_268(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放冷却时间在20秒以下的技能时，冰属性强化 +25，效果持续10秒(冷却时间3秒，最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.冰属性强化加成(25, mode=1)


def entry_269(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放冷却时间在20秒以下的技能时，光属性强化 +25，效果持续10秒(冷却时间3秒，最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.光属性强化加成(25, mode=1)


def entry_270(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放冷却时间在20秒以下的技能时，暗属性强化 +25，效果持续10秒(冷却时间3秒，最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.暗属性强化加成(25, mode=1)


def entry_346(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放冷却时间在25秒以上的技能时，火属性强化 +25，效果持续10秒(冷却时间5秒，最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.火属性强化加成(25, mode=1)


def entry_347(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放冷却时间在25秒以上的技能时，冰属性强化 +25，效果持续10秒(冷却时间5秒，最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.冰属性强化加成(25, mode=1)


def entry_348(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放冷却时间在25秒以上的技能时，光属性强化 +25，效果持续10秒(冷却时间5秒，最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.光属性强化加成(25, mode=1)


def entry_349(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放冷却时间在25秒以上的技能时，暗属性强化 +25，效果持续10秒(冷却时间5秒，最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.暗属性强化加成(25, mode=1)
# endregion

# region 异常抗性词条


def entry_169(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有异常状态抗性 +20%', '所有属性强化 -15']
    if mode == 0:
        char.所有属性强化加成(-15)
        char.所有异常抗性加成(0.2)
    if mode == 1:
        pass


def entry_188(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['感电抗性 +20%', '攻击速度 -15%', '施放速度 -22.5%']
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.施放速度增加(-0.225)
    if mode == 1:
        pass


def entry_193(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['中毒抗性 +20%', '攻击速度 -15%', '施放速度 -22.5%']
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.施放速度增加(-0.225)
    if mode == 1:
        pass


def entry_199(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['冰冻抗性 +20%', '攻击速度 -15%', '施放速度 -22.5%']
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.施放速度增加(-0.225)
    if mode == 1:
        pass


def entry_204(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['减速抗性 +20%', '攻击速度 -15%', '施放速度 -22.5%']
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.施放速度增加(-0.225)
    if mode == 1:
        pass


def entry_229(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['诅咒抗性 +20%', '攻击速度 -15%', '施放速度 -22.5%']
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.施放速度增加(-0.225)
    if mode == 1:
        pass


def entry_285(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['出血抗性 +20%', '攻击速度 -15%', '施放速度 -22.5%']
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.施放速度增加(-0.225)
    if mode == 1:
        pass


def entry_293(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['灼伤抗性 +20%', '攻击速度 -15%', '施放速度 -22.5%']
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.施放速度增加(-0.225)
    if mode == 1:
        pass


def entry_305(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['失明抗性 +20%', '攻击速度 -15%', '施放速度 -22.5%']
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.施放速度增加(-0.225)
    if mode == 1:
        pass


def entry_309(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['混乱抗性 +20%', '攻击速度 -15%', '施放速度 -22.5%']
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.施放速度增加(-0.225)
    if mode == 1:
        pass


def entry_323(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['束缚抗性 +20%', '攻击速度 -15%', '施放速度 -22.5%']
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.施放速度增加(-0.225)
    if mode == 1:
        pass


def entry_361(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['睡眠抗性 +20%', '攻击速度 -15%', '施放速度 -22.5%']
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.施放速度增加(-0.225)
    if mode == 1:
        pass


def entry_366(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['眩晕抗性 +20%', '攻击速度 -15%', '施放速度 -22.5%']
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.施放速度增加(-0.225)
    if mode == 1:
        pass


def entry_372(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['石化抗性 +20%', '攻击速度 -15%', '施放速度 -22.5%']
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.施放速度增加(-0.225)
    if mode == 1:
        pass


def entry_301(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身最高的异常状态抗性数值超过50%以上时，火属性强化 +35']
    if mode == 0:
        pass
    if mode == 1:
        char.火属性强化加成(35)


def entry_302(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身最高的异常状态抗性数值超过50%以上时，冰属性强化 +35']
    if mode == 0:
        pass
    if mode == 1:
        char.冰属性强化加成(35)


def entry_303(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身最高的异常状态抗性数值超过50%以上时，光属性强化 +35']
    if mode == 0:
        pass
    if mode == 1:
        char.光属性强化加成(35)


def entry_304(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身最高的异常状态抗性数值超过50%以上时，暗属性强化 +35']
    if mode == 0:
        pass
    if mode == 1:
        char.暗属性强化加成(35)


def entry_352(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每12%的出血抗性，出血伤害 +5%(最多增加15%)']
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('出血', 0.05 * 3)


def entry_353(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每12%的中毒抗性，中毒伤害 +5%(最多增加15%)']
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('中毒', 0.05 * 3)


def entry_354(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每12%的感电抗性，感电伤害 +5%(最多增加15%)']
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('感电', 0.05 * 3)


def entry_355(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每12%的灼伤抗性，灼伤伤害 +5%(最多增加15%)']
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('灼烧', 0.05 * 3)


def entry_394(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['出血抗性 +5%', '出血伤害 +5%']
    if mode == 0:
        char.异常增伤('出血', 0.05)
        char.异常抗性加成('出血', 0.05)
    if mode == 1:
        pass


def entry_395(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['中毒抗性 +5%', '中毒伤害 +5%']
    if mode == 0:
        char.异常增伤('中毒', 0.05)
        char.异常抗性加成('中毒', 0.05)
    if mode == 1:
        pass


def entry_401(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['灼伤抗性 +5%', '灼伤伤害 +5%']
    if mode == 0:
        char.异常增伤('灼烧', 0.05)
        char.异常抗性加成('灼烧', 0.05)
    if mode == 1:
        pass


def entry_402(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['感电抗性 +5%', '感电伤害 +5%']
    if mode == 0:
        char.异常增伤('感电', 0.05)
        char.异常抗性加成('感电', 0.05)
    if mode == 1:
        pass


# endregion

# region 队友数量词条
teammate_num = 0
teammate_num_list = [0, 1, 2, 3, 4]


def set_teammate_num(x):
    global teammate_num
    teammate_num = teammate_num_list[x[0]]


entry_chose.append((20165, ['选择队员数量'] + ['队员：{}名'.format(i)
                                         for i in teammate_num_list[1:]], ""))
multi_select[20165] = False
variable_set[20165] = set_teammate_num


def entry_165(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['队伍去每存在一名获得该词条的队友(包括自己)，攻击强化 +N']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(0, lv) * teammate_num)


def entry_166(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['队伍去每存在一名获得该词条的队友(包括自己)，所受伤害 -7%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1018(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每存在1名包含自身在内的队员时，攻击强化 +371 (最多叠加4次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(371, lv) * teammate_num)


def entry_1019(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每1名适用该装备属性的队员 (包含自身)， 攻击强化 +1112 (最多叠加4次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(1112, lv) * teammate_num)


def entry_1244(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['物理伤害减少率和魔法伤害减少率总和超过60%以上时，攻击强化 4001', '每存在1名队友，所有技能范围 +5%(最多叠加4次，觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(4001, lv))


# endregion

# region 选择敌人数量
enemy_num = 0
enemy_num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60]


def set_enemy_num(x):
    global enemy_num
    enemy_num = enemy_num_list[x[0]]


entry_chose.append((20183, ['选择敌人数量'] + ['{}个敌人'.format(i)
                                         for i in enemy_num_list[1:]], ""))
multi_select[20183] = False
variable_set[20183] = set_enemy_num


def entry_183(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px范围内，每存在1个敌人，火属性强化 +7(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        for i in range(0, min(10, enemy_num)):
            char.火属性强化加成(7, mode=1)


def entry_184(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px范围内，每存在1个敌人，冰属性强化 +7(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        for i in range(0, min(10, enemy_num)):
            char.冰属性强化加成(7, mode=1)


def entry_185(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px范围内，每存在1个敌人，光属性强化 +7(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        for i in range(0, min(10, enemy_num)):
            char.光属性强化加成(7, mode=1)


def entry_186(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px范围内，每存在1个敌人，暗属性强化 +7(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        for i in range(0, min(10, enemy_num)):
            char.暗属性强化加成(7, mode=1)


def entry_266(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['地图每存在1个敌人，攻击强化 +44(最多叠加60次)', '受到总HP1%以上伤害时，攻击强化效果叠加次数 -12']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(44, lv) * min(60, enemy_num))


def entry_283(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px范围内，每存在1个敌人，技能冷却时间 -4%(觉醒技能除外，最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能冷却缩减(1, 100, 0.04 * min(10, enemy_num), [50, 85, 100])
        char.条件冷却加成("所有[除觉醒]", 0.04)


def entry_289(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px范围内，每存在1个敌人，攻击速度+3%，施放速度+4.5%(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.03 * min(10, enemy_num))
        char.施放速度增加(0.045 * min(10, enemy_num))


def entry_290(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px范围内，每存在1个敌人，物理、魔法防御力 +1500(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_291(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px范围内，每存在1个敌人，所有属性抗性 +3(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        char.所有属性抗性加成(3 * min(10, enemy_num))


def entry_292(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px范围内，每存在1个敌人，所有异常状态抗性 +3%(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        char.所有异常抗性加成(0.03 * min(10, enemy_num))


def entry_409(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px范围内，每存在1个敌人，物理、魔法暴击率 +2%(最多增加20%)']
    if mode == 0:
        pass
    if mode == 1:
        char.暴击率增加(0.02 * min(10, enemy_num))


def entry_139(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px范围内每存在1名出血状态的对象， 攻击强化 +356 (最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(356, lv) * min(10, enemy_num)
                    * (1 if '出血' in state_type else 0))


def entry_140(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px范围内每存在1名中毒状态的对象， 攻击强化 +356 (最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(356, lv) * min(10, enemy_num)
                    * (1 if '中毒' in state_type else 0))


def entry_141(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px范围内每存在1名灼伤状态的对象， 攻击强化 +356 (最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(356, lv) * min(10, enemy_num)
                    * (1 if '灼烧' in state_type else 0))


def entry_142(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px范围内每存在1名感电状态的对象， 攻击强化 +356 (最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(356, lv) * min(10, enemy_num)
                    * (1 if '感电' in state_type else 0))


def entry_143(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px范围内每存在1名冰冻状态的对象， 攻击强化 +385 (最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        攻击强化 = 成长词条计算(385, lv)
        char.攻击强化加成(攻击强化 * min(10, enemy_num)*(1 if '冰冻' in state_type else 0))


def entry_144(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px范围内，每存在1个减速状态的对象，攻击强化 +385(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        攻击强化 = 成长词条计算(385, lv)
        char.攻击强化加成(攻击强化 * min(10, enemy_num)*(1 if '减速' in state_type else 0))


def entry_145(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px范围内，每存在1个眩晕状态的对象，攻击强化 +385(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        攻击强化 = 成长词条计算(385, lv)
        char.攻击强化加成(攻击强化 * min(10, enemy_num)*(1 if '眩晕' in state_type else 0))


def entry_146(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px范围内每存在1名诅咒状态的对象， 攻击强化 +385 (最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        攻击强化 = 成长词条计算(385, lv)
        char.攻击强化加成(攻击强化 * min(10, enemy_num)*(1 if '诅咒' in state_type else 0))


def entry_147(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px范围内每存在1名失明状态的对象， 攻击强化 +385 (最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        攻击强化 = 成长词条计算(385, lv)
        char.攻击强化加成(攻击强化 * min(10, enemy_num)*(1 if '失明' in state_type else 0))


def entry_148(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px范围内每存在1名石化状态的对象， 攻击强化 +385 (最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        攻击强化 = 成长词条计算(385, lv)
        char.攻击强化加成(攻击强化 * min(10, enemy_num)*(1 if '石化' in state_type else 0))


def entry_149(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px范围内，每存在1个睡眠状态的对象，攻击强化 +385(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        攻击强化 = 成长词条计算(385, lv)
        char.攻击强化加成(攻击强化 * min(10, enemy_num)*(1 if '睡眠' in state_type else 0))


def entry_150(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px范围内，每存在1个混乱状态的对象，攻击强化 +385(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        攻击强化 = 成长词条计算(385, lv)
        char.攻击强化加成(攻击强化 * min(10, enemy_num))


def entry_151(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px范围内，每存在1个束缚状态的对象，攻击强化 +385(最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        攻击强化 = 成长词条计算(385, lv)
        char.攻击强化加成(攻击强化 * min(10, enemy_num))


def entry_804(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['150px内存在敌人时， 每1秒增加2%的技能攻击力。 (最多叠加5次； 150px内没有敌人时每1秒减少1层叠加数)']
    if mode == 0:
        pass
    if mode == 1:
        # if enemy_num > 0:
        for i in range(0, 5):
            char.技能攻击力加成(part=part, x=0.02)


def entry_805(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['150px内存在敌人时， 增加10%的所有速度， 效果持续10秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        # if enemy_num > 0:
        char.所有速度增加(0.1)


def entry_806(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['450px范围内每1名出血状态敌人， 技能、 消耗品、 装备的HP恢复效果增加5%。 (最多增加50%)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_807(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['450px范围内每1名出血状态敌人， 增加10%的冷却时间恢复速度。 (最多增加30%； 觉醒技能除外)', '攻击出血状态的敌人时， 技能攻击力 +2%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(1, 100, 0.1*min(3, enemy_num), [50, 85, 100])
        char.条件冷却恢复加成("所有[觉醒除外]", 0.1*min(3, enemy_num))
        if '出血' in state_type:
            char.技能攻击力加成(part=part, x=0.02)


def entry_808(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px内存在出血状态敌人时， 增加20%的出血抗性。', '攻击出血状态的敌人时， 技能攻击力 +2%']
    if mode == 0:
        pass
    if mode == 1:
        if enemy_num > 0:
            char.异常抗性加成('出血', 0.2)
        if '出血' in state_type:
            char.技能攻击力加成(part=part, x=0.02)


def entry_809(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['500px范围内每存在1名灼伤状态的敌人， 增加3%的所有速度和1点火属性抗性。 (最多叠加10次)', '稀有、 领主怪物进入灼伤状态时， 所有速度、 火属性抗性叠加为最大值。']
    if mode == 0:
        pass
    if mode == 1:
        if '灼烧' in state_type:
            char.所有速度增加(0.03 * 10)
            char.火属性抗性加成(1 * 10)


# endregion

# region 选择地下城类型
dungeons_type = []
dungeons_type_list = ['', '[贵族机要]', '[毁坏的寂静城(高级)]', '[机械战神试验场]']


def set_dungeons_type(x):
    global dungeons_type
    dungeons_type = []
    for i in x:
        dungeons_type.append(dungeons_type_list[i])


entry_chose.append((20189, ['选择地下城类型'] + ['{}'.format(i)
                                          for i in dungeons_type_list[1:]], ""))
variable_set[20189] = set_dungeons_type


def entry_189(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['进入[贵族机要]地下城时，技能攻击力 +15%']
    if mode == 0:
        pass
    if mode == 1:
        if '[贵族机要]' in dungeons_type:
            char.技能攻击力加成(part=part, x=0.15)


def entry_207(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['进入[毁坏的寂静城(高级)]地下城时，技能攻击力 +15%']
    if mode == 0:
        pass
    if mode == 1:
        if '[毁坏的寂静城(高级)]' in dungeons_type:
            char.技能攻击力加成(part=part, x=0.15)


def entry_225(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['进入[机械战神试验场]地下城时，技能攻击力 +15%']
    if mode == 0:
        pass
    if mode == 1:
        if '[机械战神试验场]' in dungeons_type:
            char.技能攻击力加成(part=part, x=0.15)


# endregion
# region 敌人韧性相关
toughness_num = 0
toughness_num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def set_toughness_num(x):
    global toughness_num
    toughness_num = toughness_num_list[x[0]]


entry_chose.append((20194, ['选择敌人韧性削减'] + ['韧性减少：{}%'.format(i * 10)
                                           for i in toughness_num_list[1:]], ""))
multi_select[20194] = False
variable_set[20194] = set_toughness_num


def entry_194(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每减少敌人10%的韧性，Lv45技能冷却时间恢复速度 +3%(最多增加30%)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(45, 45, 0.03 * min(10, toughness_num))
        char.条件冷却恢复加成("Lv45", 0.03 * min(10, toughness_num))


def entry_195(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['根据敌人韧性破坏次数，攻击强化 +193']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(193, lv) * toughness_num)


def entry_200(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每减少敌人10%的韧性，Lv75技能冷却时间恢复速度 +3%(最多增加30%)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(75, 75, 0.03 * min(10, toughness_num))
        char.条件冷却恢复加成("Lv70", 0.03 * min(10, toughness_num))


def entry_205(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['根据敌人韧性破坏次数，出血伤害 +5%(最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('出血', 0.05 * min(5, toughness_num))


def entry_206(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['根据敌人韧性破坏次数，灼伤伤害 +5%(最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('灼烧', 0.05 * min(5, toughness_num))


def entry_213(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['敌人韧性减少量 +20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_286(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['敌人韧性每减少10%，Lv95技能冷却时间恢复速度 +3%(最多增加30%)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(95, 95, 0.03 * min(10, toughness_num))
        char.条件冷却恢复加成("Lv95", 0.03 * min(10, toughness_num))


def entry_287(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['敌人韧性每减少10%，Lv60技能冷却时间恢复速度 +3%(最多增加30%)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(60, 60, 0.03 * min(10, toughness_num))
        char.条件冷却恢复加成("Lv60", 0.03 * min(10, toughness_num))


def entry_310(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['根据敌人韧性破坏次数，中毒伤害 +5%(最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('中毒', 0.05 * min(5, toughness_num))


def entry_311(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['根据敌人韧性破坏次数，感电伤害 +5%(最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('感电', 0.05 * min(5, toughness_num))


def entry_362(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每减少敌人10%的韧性，Lv80技能冷却时间恢复速度 +3%(最多增加30%)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(80, 80, 0.03 * min(10, toughness_num))
        char.条件冷却恢复加成("Lv80", 0.03 * min(10, toughness_num))


def entry_367(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每减少敌人10%的韧性，Lv70技能冷却时间恢复速度 +3%(最多增加30%)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(70, 70, 0.03 * min(10, toughness_num))
        char.条件冷却恢复加成("Lv70", 0.03 * min(10, toughness_num))


def entry_373(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每减少敌人10%的韧性，Lv35技能冷却时间恢复速度 +3%(最多增加30%)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(35, 35, 0.03 * min(10, toughness_num))
        char.条件冷却恢复加成("Lv35", 0.03 * min(10, toughness_num))


def entry_374(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每减少敌人10%的韧性，Lv40技能冷却时间恢复速度 +3%(最多增加30%)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(40, 40, 0.03 * min(10, toughness_num))
        char.条件冷却恢复加成("Lv40", 0.03 * min(10, toughness_num))


def entry_396(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['敌人韧性减少量 +10%', '自身触发的眩晕状态持续时间 +1秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_397(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['敌人韧性减少量 +10%', '自身触发的诅咒状态持续时间 +1秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_398(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['敌人韧性减少量 +10%', '自身触发的石化状态持续时间 +1秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_403(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['敌人韧性减少量 +10%', '自身触发的冰冻状态持续时间 +1秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_404(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['敌人韧性减少量 +10%', '自身触发的失明状态持续时间 +1秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_406(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['敌人韧性减少量 +10%', '自身触发的睡眠状态持续时间 +1秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_407(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['敌人韧性减少量 +10%', '自身触发的减速状态持续时间 +1秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_408(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['敌人韧性减少量 +10%', '自身触发的混乱状态持续时间 +1秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1258(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['敌人韧性减少量 +25%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1259(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每减少敌人10%的韧性，技能攻击力 +2%(最多叠加10次)', '- 无力化效果消失时，技能攻击力增加效果重置']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(part=part, x=0.02 * min(10, toughness_num))
# endregion

# region 异常状态解除相关 (未实现)


def entry_201(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身异常状态解除时，Lv60技能技能冷却时间恢复速度 +30%，效果持续5秒(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_202(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身异常状态解除时，Lv45技能技能冷却时间恢复速度 +30%，效果持续5秒(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_203(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身异常状态解除时，Lv35技能技能冷却时间恢复速度 +30%，效果持续5秒(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_208(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身异常状态解除时，Lv40技能技能冷却时间恢复速度 +30%，效果持续5秒(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_209(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身异常状态解除时，Lv70技能技能冷却时间恢复速度 +30%，效果持续5秒(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_210(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身异常状态解除时，Lv75技能技能冷却时间恢复速度 +30%，效果持续5秒(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_214(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身异常状态解除时，Lv80技能技能冷却时间恢复速度 +30%，效果持续5秒(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_215(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身异常状态解除时，Lv95技能技能冷却时间恢复速度 +30%，效果持续5秒(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass
# endregion

# region 普攻相关 (未实现)


def entry_211(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放普通攻击最后一击时，冷却时间最长的技能剩余冷却时间 -3%(冷却时间1秒，觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_212(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放普通攻击最后一击时，冷却时间最短的技能剩余冷却时间 -3%(冷却时间1秒，觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1060(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['普通攻击、 跳跃、 前冲攻击时， 不消耗无色小晶块的技能减少1%的剩余冷却时间。 (冷却时间0.1秒)', '施放无色小晶块技能时， 不消耗无色小晶块的技能冷却时间增加2%， 效果持续30秒。 (最多叠加10次)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_380(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放普通攻击最后一击时，攻击强化 +N，效果持续10秒']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(0, lv))


def entry_391(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放普通攻击最后一击时，攻击速度 +20%，施放速度 +30%，效果持续10秒']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.2)
        char.施放速度增加(0.3)


def entry_1056(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['普通攻击、 跳跃攻击、 前冲攻击时， Lv15~35主动技能攻击力增加3%， 效果持续10秒。 (最多叠加10次)', '施放Lv45以上技能时， 技能攻击力增加效果叠加数 -1']
    if mode == 0:
        pass
    if mode == 1:
        for item in range(0, 10):
            char.技能倍率加成(15, 35, 0.03, type="active")
        pass


def entry_1057(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['普通攻击、 跳跃攻击、 前冲攻击时， Lv15~35主动技能冷却时间恢复速度增加1%， 效果持续10秒。 (最多叠加10次)', '施放Lv45以上技能时， 技能冷却时间恢复速度增加效果叠加数 -1']
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(15, 35, 0.01*10)
        char.条件冷却恢复加成("Lv15~35", 0.1)
        pass


def entry_1059(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['普通攻击、 跳跃、 前冲攻击时， 有10%的几率， 以增加300%的攻击力发动攻击。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1061(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['普通攻击、 跳跃攻击、 前冲攻击时， 增加10%的攻击速度和施放速度， 效果持续2秒。 (最多叠加3次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.3)
        char.施放速度增加(0.3)
        pass


def entry_1062(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['普通攻击、 跳跃攻击、 前冲攻击时， [基础精通]攻击力增加15%， 效果持续5秒。 (冷却时间0.1秒； 最多叠加3次)', '施放技能时， 消耗所有基础精通叠加层数； 根据消耗层数， 按比例增加5%的技能攻击力和8%的技能冷却时间， 效果持续5秒。 (只能在没有该Buff时发动)']
    if mode == 0:
        pass
    if mode == 1:
        for item in range(0, 3):
            char.基础精通加成(0.15)
        char.技能冷却缩减(1, 100, - 0.08*3)
        char.技能倍率加成(1, 100, 0.05*3)
        char.条件冷却加成("所有", -0.08*3)
        pass


def entry_1063(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['普通攻击、 跳跃、 前冲攻击时， 有15%的几率使敌人进入灼伤、 感电、 出血、 中毒异常状态中的1种。 (冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1064(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['普通攻击、 跳跃攻击、 前冲攻击时， 增加10%的攻击速度和施放速度， 效果持续5秒。 (冷却时间0.1秒； 最多叠加3次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.3)
        char.施放速度增加(0.3)
        pass


# endregion

# region 敌人距离相关
distance_num = 0
distance_num_list = [0, 50, 100, 150, 200, 250, 300]


def set_distance_num(x):
    global distance_num
    distance_num = distance_num_list[x[0]]


entry_chose.append((20253, ['选择敌人距离'] + ['距离{}~{}px'.format(i, i + 50)
                                         for i in distance_num_list[1:]], ""))
multi_select[20253] = False
variable_set[20253] = set_distance_num


def entry_253(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['越靠近敌人时，技能攻击力 +1%(与敌人距离50px以内时，最多增加5%)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(part=part, x=0.01 * max(0, 250 - distance_num) / 50)


def entry_254(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['越远离敌人时，技能攻击力 +1%(与敌人距离300px以外时，最多增加5%)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(part=part, x=0.01 *
                     min(5, max(0, distance_num - 50) / 50))


def entry_1181(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['与敌人距离100px以内时， 攻击强化 +2964']
    if mode == 0:
        pass
    if mode == 1:
        if distance_num < 100:
            char.攻击强化加成(成长词条计算(2964, lv))
# endregion

# region 进入地下城时相关


def entry_223(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['进入地下城时，每30秒以相同几率发动属性，效果持续20秒', '- 攻击速度 +25%', '- 施放速度 +37.5%', '- 移动速度 +25%']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.25)
        char.施放速度增加(0.375)
        char.移动速度增加(0.25)


def entry_224(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['进入地下城时，每30秒以相同几率发动属性，效果持续20秒', '- 攻击强化 +3417', '- 所受伤害 -25%']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(3417, lv)*0.5*20/30)


def entry_997(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['进入地下城时， 攻击强化 +2223', '技能MP消耗量 +100%']
    if mode == 0:
        pass
    if mode == 1:
        char.MP消耗量加成(1)
        char.攻击强化加成(成长词条计算(2223, lv))


def entry_998(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['进入地下城时，制造一个草莓极光，被击5次后被销毁(冷却时间30秒)', '- 草莓极光状态下，所受伤害 -15%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1103(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['使用技能时， 增加5%的攻击速度和8%的施放速度， 效果持续10秒。 (最多叠加5次)', '地下城入场时， 减少5%的技能冷却时间 (觉醒技能除外) 和2%的技能攻击力。']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.05 * 5)
        char.施放速度增加(0.08 * 5)
        char.技能冷却缩减(1, 100, 0.05, [50, 85, 100])
        char.条件冷却加成("所有[除觉醒]", 0.05)
        char.技能攻击力加成(part=part, x=-0.02)
# endregion

# region 冷却技攻互换技能


def entry_236(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['Lv95所有技能冷却时间 +30%', 'Lv80所有技能攻击力 +20%']
    if mode == 0:
        char.技能冷却缩减(95, 95, -0.3)
        char.条件冷却加成("Lv95", -0.3)
        char.技能倍率加成(80, 80, 0.2)
    if mode == 1:
        pass


def entry_237(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['Lv80所有技能冷却时间 +30%', 'Lv80所有技能攻击力 +20%']
    if mode == 0:
        char.技能冷却缩减(80, 80, -0.3)
        char.条件冷却加成("Lv80", -0.3)
        char.技能倍率加成(80, 80, 0.2)
    if mode == 1:
        pass


def entry_241(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['Lv35所有技能冷却时间 +30%', 'Lv35所有技能攻击力 +20%']
    if mode == 0:
        char.技能冷却缩减(35, 35, -0.3)
        char.条件冷却加成("Lv35", -0.3)
        char.技能倍率加成(35, 35, 0.2)
    if mode == 1:
        pass


def entry_242(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['Lv40所有技能冷却时间 +30%', 'Lv35所有技能攻击力 +20%']
    if mode == 0:
        char.技能冷却缩减(40, 40, -0.3)
        char.条件冷却加成("Lv40", -0.3)
        char.技能倍率加成(35, 35, 0.2)
    if mode == 1:
        pass


def entry_243(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['Lv40所有技能冷却时间 +30%', 'Lv40所有技能攻击力 +20%']
    if mode == 0:
        char.技能冷却缩减(40, 40, -0.3)
        char.条件冷却加成("Lv40", -0.3)
        char.技能倍率加成(40, 40, 0.2)
    if mode == 1:
        pass


def entry_244(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['Lv45所有技能冷却时间 +30%', 'Lv40所有技能攻击力 +20%']
    if mode == 0:
        char.技能冷却缩减(45, 45, -0.3)
        char.条件冷却加成("Lv45", -0.3)
        char.技能倍率加成(40, 40, 0.2)
    if mode == 1:
        pass


def entry_250(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['Lv45所有技能冷却时间 +30%', 'Lv45所有技能攻击力 +20%']
    if mode == 0:
        char.技能冷却缩减(45, 45, -0.3)
        char.条件冷却加成("Lv45", -0.3)
        char.技能倍率加成(45, 45, 0.2)
    if mode == 1:
        pass


def entry_251(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['Lv60所有技能冷却时间 +30%', 'Lv45所有技能攻击力 +20%']
    if mode == 0:
        char.技能冷却缩减(60, 60, -0.3)
        char.条件冷却加成("Lv60", -0.3)
        char.技能倍率加成(45, 45, 0.2)
    if mode == 1:
        pass


def entry_255(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['Lv60所有技能冷却时间 +30%', 'Lv60所有技能攻击力 +20%']
    if mode == 0:
        char.技能冷却缩减(60, 60, -0.3)
        char.条件冷却加成("Lv60", -0.3)
        char.技能倍率加成(60, 60, 0.2)
    if mode == 1:
        pass


def entry_256(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['Lv70所有技能冷却时间 +30%', 'Lv60所有技能攻击力 +20%']
    if mode == 0:
        char.技能冷却缩减(70, 70, -0.3)
        char.条件冷却加成("Lv70", -0.3)
        char.技能倍率加成(60, 60, 0.2)
    if mode == 1:
        pass


def entry_260(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['Lv70所有技能冷却时间 +30%', 'Lv70所有技能攻击力 +20%']
    if mode == 0:
        char.技能冷却缩减(70, 70, -0.3)
        char.条件冷却加成("Lv70", -0.3)
        char.技能倍率加成(70, 70, 0.2)
    if mode == 1:
        pass


def entry_261(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['Lv75所有技能冷却时间 +30%', 'Lv70所有技能攻击力 +20%']
    if mode == 0:
        char.技能冷却缩减(75, 75, -0.3)
        char.条件冷却加成("Lv75", -0.3)
        char.技能倍率加成(70, 70, 0.2)
    if mode == 1:
        pass


def entry_262(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['Lv75所有技能冷却时间 +30%', 'Lv75所有技能攻击力 +20%']
    if mode == 0:
        char.技能冷却缩减(75, 75, -0.3)
        char.条件冷却加成("Lv75", -0.3)
        char.技能倍率加成(75, 75, 0.2)
    if mode == 1:
        pass


def entry_263(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['Lv80所有技能冷却时间 +30%', 'Lv75所有技能攻击力 +20%']
    if mode == 0:
        char.技能冷却缩减(80, 80, -0.3)
        char.条件冷却加成("Lv80", -0.3)
        char.技能倍率加成(75, 75, 0.2)
    if mode == 1:
        pass


# endregion

# region 技能指令相关
def entry_1138(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['无色小晶块技能的指令使用效果 +400% (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        for skill in char.技能栏:
            if skill.是否有伤害 == 1 and skill.无色消耗 > 0 and skill.手搓 and skill.所在等级 not in [50, 85, 100]:
                skill.手搓收益 += 4
        pass


def entry_247(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['使用技能指令施放技能时，该技能攻击力 +12%(觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.指令技攻加成(0.12)


def entry_248(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['技能指令效果 +100%(觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        for skill in char.技能栏:
            if skill.是否有伤害 == 1 and skill.手搓 and skill.所在等级 not in [50, 85, 100]:
                skill.手搓收益 += 1
        pass


def entry_1121(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['使用指令施放非快捷栏技能时， 减少15%的冷却时间。 (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        # char.指令冷却缩减(0.15)
        # 暂未判断是否指令
        char.条件冷却加成("手搓非快捷栏", 0.15)
        for i in char.技能栏:
            if i.所在等级 not in [50, 85, 100] and i.手搓 == True and i.名称 not in char.hotkey:
                if i.是否有伤害 == 1:
                    i.CDR *= (1 - 0.15)


def entry_1122(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['使用指令施放快捷栏技能时， 增加10%的技能攻击力。']
    if mode == 0:
        pass
    if mode == 1:
        # char.指令技攻加成(0.10, exc=[])
        for i in char.技能栏:
            if i.手搓 == True and i.名称 in char.hotkey:
                if i.是否有伤害 == 1:
                    i.倍率 *= (1 + 0.1 * char.技能伤害增加增幅)


def entry_1135(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['用指令施放技能时，该技能攻击力增加5%。  (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.指令技攻加成(0.05)


def entry_1136(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['用指令施放技能时， 增加5%的所有速度， 效果持续3秒。 (最多叠加3次)']
    if mode == 0:
        pass
    if mode == 1:
        char.所有速度增加(0.05*3)


def entry_1137(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['使用指令施放技能时， 根据输入的方向键数量， 增加技能攻击力。 (觉醒技能除外)', '- 1个方向键 : 技能攻击力 +7%', '- 2个方向键 : 技能攻击力 +9%', '- 3个方向键 : 技能攻击力 +11%', '- 4个方向键 : 技能攻击力 +15%']
    if mode == 0:
        pass
    if mode == 1:
        for i in char.技能栏:
            if i.手搓 == True and i.所在等级 not in [50, 85, 100] and i.名称 != '神罚之锤':
                if i.是否有伤害 == 1:
                    if i.手搓指令数 == 1:
                        i.倍率 *= 1.07
                    if i.手搓指令数 == 2:
                        i.倍率 *= 1.09
                    if i.手搓指令数 == 3:
                        i.倍率 *= 1.11
                    if i.手搓指令数 == 4:
                        i.倍率 *= 1.15
# endregion

# region 等级技能加等级、加攻、减CD


def entry_271(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv45技能攻击力 +20%']
    if mode == 0:
        char.技能倍率加成(45, 45, 0.2)
    if mode == 1:
        pass


def entry_272(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv35技能攻击力 +20%']
    if mode == 0:
        char.技能倍率加成(35, 35, 0.2)
    if mode == 1:
        pass


def entry_277(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv40技能攻击力 +20%']
    if mode == 0:
        char.技能倍率加成(40, 40, 0.2)
    if mode == 1:
        pass


def entry_278(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv30技能攻击力 +20%']
    if mode == 0:
        char.技能倍率加成(30, 30, 0.2)
    if mode == 1:
        pass


def entry_312(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv60技能攻击力 +20%']
    if mode == 0:
        char.技能倍率加成(60, 60, 0.2)
    if mode == 1:
        pass


def entry_313(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv70技能攻击力 +20%']
    if mode == 0:
        char.技能倍率加成(70, 70, 0.2)
    if mode == 1:
        pass


def entry_318(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv20技能攻击力 +20%']
    if mode == 0:
        char.技能倍率加成(20, 20, 0.2)
    if mode == 1:
        pass


def entry_319(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv25技能攻击力 +20%']
    if mode == 0:
        char.技能倍率加成(25, 25, 0.2)
    if mode == 1:
        pass


def entry_326(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv95技能攻击力 +20%']
    if mode == 0:
        char.技能倍率加成(95, 95, 0.2)
    if mode == 1:
        pass


def entry_330(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv75技能攻击力 +20%']
    if mode == 0:
        char.技能倍率加成(75, 75, 0.2)
    if mode == 1:
        pass


def entry_331(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv80技能攻击力 +20%']
    if mode == 0:
        char.技能倍率加成(80, 80, 0.2)
    if mode == 1:
        pass


def entry_273(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv45技能冷却时间 -20%']
    if mode == 0:
        char.技能冷却缩减(45, 45, 0.2)
        char.条件冷却加成("Lv45", 0.2)
    if mode == 1:
        pass


def entry_274(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv35技能冷却时间 -20%']
    if mode == 0:
        char.技能冷却缩减(35, 35, 0.2)
        char.条件冷却加成("Lv35", 0.2)
    if mode == 1:
        pass


def entry_279(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv40技能冷却时间 -20%']
    if mode == 0:
        char.技能冷却缩减(40, 40, 0.2)
        char.条件冷却加成("Lv40", 0.2)
    if mode == 1:
        pass


def entry_280(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv30技能冷却时间 -20%']
    if mode == 0:
        char.技能冷却缩减(30, 30, 0.2)
        char.条件冷却加成("Lv30", 0.2)
    if mode == 1:
        pass


def entry_314(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv60技能冷却时间 -20%']
    if mode == 0:
        char.技能冷却缩减(60, 60, 0.2)
        char.条件冷却加成("Lv60", 0.2)
    if mode == 1:
        pass


def entry_315(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv70技能冷却时间 -20%']
    if mode == 0:
        char.技能冷却缩减(70, 70, 0.2)
        char.条件冷却加成("Lv70", 0.2)
    if mode == 1:
        pass


def entry_320(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv20技能冷却时间 -20%']
    if mode == 0:
        char.技能冷却缩减(20, 20, 0.2)
        char.条件冷却加成("Lv20", 0.2)
    if mode == 1:
        pass


def entry_321(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv25技能冷却时间 -20%']
    if mode == 0:
        char.技能冷却缩减(25, 25, 0.2)
        char.条件冷却加成("Lv25", 0.2)
    if mode == 1:
        pass


def entry_327(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv95技能冷却时间 -20%']
    if mode == 0:
        char.技能冷却缩减(95, 95, 0.2)
        char.条件冷却加成("Lv95", 0.2)
    if mode == 1:
        pass


def entry_332(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv75技能冷却时间 -20%']
    if mode == 0:
        char.技能冷却缩减(75, 75, 0.2)
        char.条件冷却加成("Lv75", 0.2)
    if mode == 1:
        pass


def entry_333(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv80技能冷却时间 -20%']
    if mode == 0:
        char.技能冷却缩减(80, 80, 0.2)
        char.条件冷却加成("Lv80", 0.2)
    if mode == 1:
        pass


def entry_275(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv45主动技能Lv+1']
    if mode == 0:
        char.技能等级加成('z', 45, 45, 1)
    if mode == 1:
        pass


def entry_276(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv35主动技能Lv+1']
    if mode == 0:
        char.技能等级加成('主动', 35, 35, 1)
    if mode == 1:
        pass


def entry_281(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv40主动技能Lv+1']
    if mode == 0:
        char.技能等级加成('主动', 40, 40, 1)
    if mode == 1:
        pass


def entry_316(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv60主动技能Lv+1']
    if mode == 0:
        char.技能等级加成('主动', 60, 60, 1)
    if mode == 1:
        pass


def entry_317(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv70主动技能Lv+1']
    if mode == 0:
        char.技能等级加成('主动', 70, 70, 1)
    if mode == 1:
        pass


def entry_328(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv95主动技能Lv+1']
    if mode == 0:
        char.技能等级加成('主动', 95, 95, 1)
    if mode == 1:
        pass


def entry_334(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv75主动技能Lv+1']
    if mode == 0:
        char.技能等级加成('主动', 75, 75, 1)
    if mode == 1:
        pass


def entry_335(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv80主动技能Lv+1']
    if mode == 0:
        char.技能等级加成('主动', 80, 80, 1)
    if mode == 1:
        pass


# endregion

# region 属性抗性相关词条
def entry_339(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['火属性抗性 +40', '命中率 -15%']
    if mode == 0:
        char.火属性抗性加成(40)
        char.命中率增加(-0.15)
    if mode == 1:
        pass


def entry_340(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['冰属性抗性 +40', '命中率 -15%']
    if mode == 0:
        char.冰属性抗性加成(40)
        char.命中率增加(-0.15)
    if mode == 1:
        pass


def entry_341(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['光属性抗性 +40', '命中率 -15%']
    if mode == 0:
        char.光属性抗性加成(40)
        char.命中率增加(-0.15)
    if mode == 1:
        pass


def entry_342(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['暗属性抗性 +40', '命中率 -15%']
    if mode == 0:
        char.暗属性抗性加成(40)
        char.命中率增加(-0.15)
    if mode == 1:
        pass


def entry_344(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身所有属性抗性之和超过250以上时，出血伤害 +15%']
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('出血', 0.15)


def entry_350(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身所有属性抗性之和超过250以上时，灼伤伤害 +15%']
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('灼烧', 0.15)


def entry_356(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身所有属性抗性之和超过250以上时，感电伤害 +15%']
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('感电', 0.15)


# endregion

# region 剩余冷却缩减 (未实现)
def entry_357(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv25~40技能时，Lv45技能剩余冷却时间 -10%(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_358(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv30~45技能时，Lv60技能剩余冷却时间 -10%(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_359(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv15~30技能时，Lv35技能剩余冷却时间 -10%(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_363(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv35~60技能时，Lv70技能剩余冷却时间 -10%(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_364(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv40~70技能时，Lv75技能剩余冷却时间 -10%(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_365(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv20~35技能时，Lv40技能剩余冷却时间 -10%(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_370(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv60~80技能时，Lv95技能剩余冷却时间 -10%(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_371(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放Lv40~75技能时，Lv80技能剩余冷却时间 -10%(冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


# endregion

# region HP范围
hp_rate_num = 0
hp_rate_num_list = [90, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]


def set_hp_rate_num(x):
    global hp_rate_num
    hp_rate_num = hp_rate_num_list[x[0]]


entry_chose.append((20814, ['选择HP范围'] +
                    ['10%以下',
                     '10%~20%',
                     '20%~30%',
                     '30%~40%',
                     '40%~50%',
                     '50%~60%',
                     '60%~70%',
                     '70%~80%',
                     '80%~90%',
                     '90%以上',
                     ], ""))
multi_select[20814] = False
variable_set[20814] = set_hp_rate_num


def entry_814(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['HP为0时， 进入狂暴状态， 不会死亡， 效果持续5秒。', '- 狂暴状态下， 被击时伤害无效。', '- 狂暴状态下， 攻击强化 +4446', '- 施放技能时每消耗1个无色小晶块， 增加0.1秒狂暴化时间。 (一次性增加的持续时间最多不超过5秒)', '- 狂暴化状态结束时， 角色死亡。']
    if mode == 0:
        pass
    if mode == 1:
        if hp_rate_num < 10:
            char.攻击强化加成(成长词条计算(4446, lv))
        pass


def entry_815(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['HP为0时， 获得不死Buff效果， 效果持续5秒。(冷却时间300秒)', '- 恢复10%的HP。', '- 所有HP恢复效果无效。', '- 被击时伤害无效化。', '- 不死Buff效果结束时， 锁定可使用的HP最大值的30%。 (最多叠加1次； 恢复HP时无法超过锁定之后的HP值)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_816(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['HP为0时， 获得英雄气魄Buff效果。', '- 所有HP恢复效果无效。', '- 被击时， 代替HP消耗MP， MP为0时死亡。', '- 英雄气魄Buff效果期间， 每秒减少2%的MP。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_817(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['HP为0时， 自身进入睡眠状态， 并恢复10%的HP。 (冷却时间300秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_818(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['HP低于10%时， 15秒内恢复50%的HP。 (冷却时间60秒)', '技能、 消耗品、 装备的HP恢复效果 -20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_819(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['HP低于20%时， 被击时消耗所有MP， 按照消耗的MP恢复HP。 (冷却时间60秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_820(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['HP低于30%时， 攻击领主怪物时恢复1%的HP。 (冷却时间1秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_821(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身HP低于50%时， 所有速度 +20%']
    if mode == 0:
        pass
    if mode == 1:
        if hp_rate_num < 50:
            char.所有速度增加(0.2)


def entry_822(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['HP低于50%时， 增加20%的物理、 魔法暴击率。', 'HP高于10%时， 攻击时减少5%的HP。 (HP不会因该效果而降到5%以下； 冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        if hp_rate_num < 50:
            char.暴击率增加(0.2)


def entry_823(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['HP高于70%时， 技能冷却时间 -10% (觉醒技能除外)', 'HP为50%~70%之间时， 技能冷却时间 -12% (觉醒技能除外)', 'HP低于50%时， 技能冷却时间 -15% (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        if hp_rate_num >= 70:
            char.技能冷却缩减(1, 100, 0.10, [50, 85, 100])
            char.条件冷却加成("所有[除觉醒]", 0.1)
        elif hp_rate_num >= 50:
            char.技能冷却缩减(1, 100, 0.12, [50, 85, 100])
            char.条件冷却加成("所有[除觉醒]", 0.12)
        else:
            char.技能冷却缩减(1, 100, 0.15, [50, 85, 100])
            char.条件冷却加成("所有[除觉醒]", 0.15)


def entry_824(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['HP高于90%时， 每2秒发动1次增加2%的物理、 魔法暴击率的效果， 该效果持续20秒。 (最多叠加5次)', 'HP低于90%时， 每3秒解除1层物理、 魔法暴击率增加层数。']
    if mode == 0:
        pass
    if mode == 1:
        if hp_rate_num >= 90:
            char.暴击率增加(0.02 * 5)


def entry_825(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['HP高于90%时， 冷却时间恢复速度 +10% (觉醒技能除外)', '被击伤害 +30%']
    if mode == 0:
        pass
    if mode == 1:
        if hp_rate_num >= 90:
            char.技能恢复加成(1, 100, 0.10, [50, 85, 100])
            char.条件冷却恢复加成("所有[除觉醒]", 0.1)


def entry_826(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['HP低于90%时， 攻击时恢复2%的HP。 (冷却时间5秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1077(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['HP低于50%时， 物理、 魔法防御力 +7000、 攻击强化 +2223、 技能攻击力 +5%', '被击伤害 +10%']
    if mode == 0:
        pass
    if mode == 1:
        if hp_rate_num <= 50:
            char.攻击强化加成(成长词条计算(2223, lv))
            char.技能攻击力加成(part=part, x=0.05)


def entry_1078(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身HP高于80%时， 攻击强化 +445', '自身HP为50%~80%之间时， 攻击强化 +2668', '自身HP低于50%时， 攻击强化 +2668、 技能攻击力 +5%']
    if mode == 0:
        pass
    if mode == 1:
        if hp_rate_num >= 80:
            char.攻击强化加成(成长词条计算(445, lv))
        elif hp_rate_num >= 50 and hp_rate_num < 80:
            char.攻击强化加成(成长词条计算(2668, lv))
        elif hp_rate_num < 50:
            char.攻击强化加成(成长词条计算(2668, lv))
            char.技能攻击力加成(part=part, x=0.05)


# endregion

# region MP范围
mp_rate_num = 0
mp_rate_num_list = [90, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]


def set_mp_rate_num(x):
    global mp_rate_num
    mp_rate_num = mp_rate_num_list[x[0]]


entry_chose.append((20813, ['选择MP范围'] +
                    ['10%以下',
                     '10%~20%',
                     '20%~30%',
                     '30%~40%',
                     '40%~50%',
                     '50%~60%',
                     '60%~70%',
                     '70%~80%',
                     '80%~90%',
                     '90%以上',
                     ], ""))
multi_select[20813] = False
variable_set[20813] = set_mp_rate_num


def entry_813(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['MP最大值 +4196', '每剩余20000点MP， 攻击强化 +267 (最多叠加10次)', '自身MP低于60%时， 技能攻击力 -4%']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(267, lv) * 10)
        if mp_rate_num < 60:
            char.技能攻击力加成(part=part, x=-0.04)


def entry_827(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['MP最大值 +2000', '技能MP消耗量 +100%']
    if mode == 0:
        char.MP消耗量加成(1)
        pass
    if mode == 1:
        pass


def entry_828(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['MP最大值 +4196', '技能MP消耗量 +50%']
    if mode == 0:
        char.MP消耗量加成(0.5)
        pass
    if mode == 1:
        pass


def entry_829(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['MP低于50%时，发动农夫的祝福，恢复20%的MP(冷却时间40)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_830(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['剩余MP低于10%的状态超过10秒时， 10秒内攻击强化 +3557']
    if mode == 0:
        pass
    if mode == 1:
        if mp_rate_num < 10:
            char.攻击强化加成(成长词条计算(3557, lv))


def entry_831(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['剩余MP低于20%时， 攻击强化 +2223']
    if mode == 0:
        pass
    if mode == 1:
        if mp_rate_num < 20:
            char.攻击强化加成(成长词条计算(2223, lv))


def entry_832(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['MP低于50% : 每分钟HP和MP恢复量 +5000%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_833(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['MP高于90%时， 每2秒发动1次攻击强化 +711效果， 该效果持续20秒。 (最多叠加5次)', 'MP低于90%时， 每3秒解除1层攻击强化叠加层数。']
    if mode == 0:
        pass
    if mode == 1:
        if mp_rate_num >= 90:
            char.攻击强化加成(成长词条计算(711, lv) * 5)


def entry_1079(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['自身MP高于90%时， 攻击强化 +445', '自身MP在60%~90%之间时， 攻击强化 +2668', '自身MP低于60%时， 攻击强化 +4298']
    if mode == 0:
        pass
    if mode == 1:
        if mp_rate_num >= 90:
            char.攻击强化加成(成长词条计算(445, lv))
        elif mp_rate_num >= 60:
            char.攻击强化加成(成长词条计算(2668, lv))
        else:
            char.攻击强化加成(成长词条计算(4298, lv))
# endregion

# region 装备指令相关


def entry_793(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['输入[装备属性指令]时， 施放无色小晶块技能时， 用白色小晶块替代无色小晶块， 效果持续300秒。 (冷却时间10秒)', '消耗白色小晶块攻击时， 使敌人进入感电状态。 (冷却时间15秒)', '攻击感电状态的敌人时， 技能攻击力 +2%']
    if mode == 0:
        pass
    if mode == 1:
        if '感电' not in state_type:
            state_type.append('感电')
        if '感电' in state_type:
            char.技能攻击力加成(part=part, x=0.02)


def entry_794(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['输入[装备属性指令]时， 施放无色小晶块技能时， 用黑色小晶块替代无色小晶块， 效果持续300秒。 (冷却时间10秒)', '消耗黑色小晶块攻击时， 使敌人进入失明状态。 (冷却时间25秒)', '攻击失明状态的敌人时， 技能攻击力 +10%']
    if mode == 0:
        pass
    if mode == 1:
        if '失明' not in state_type:
            state_type.append('失明')
        if '失明' in state_type:
            char.技能攻击力加成(part=part, x=0.1)


def entry_795(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['输入[装备属性指令]时， 施放无色小晶块技能时， 用红色小晶块替代无色小晶块， 效果持续300秒。 (冷却时间10秒)', '消耗红色小晶块攻击时， 使敌人进入灼伤状态。 (冷却时间10秒)', '攻击灼伤状态的敌人时， 技能攻击力 +2%']
    if mode == 0:
        pass
    if mode == 1:
        if '灼烧' not in state_type:
            state_type.append('灼烧')
        if '灼烧' in state_type:
            char.技能攻击力加成(part=part, x=0.02)


def entry_796(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['输入[装备属性指令]时， 施放无色小晶块技能时， 用金色小晶块替代无色小晶块， 效果持续300秒。 (冷却时间10秒)', '消耗金色小晶块攻击时， 使敌人进入眩晕状态。 (冷却时间20秒)', '攻击眩晕状态的敌人时， 技能攻击力 +5%']
    if mode == 0:
        pass
    if mode == 1:
        if '眩晕' not in state_type:
            state_type.append('眩晕')
        if '眩晕' in state_type:
            char.技能攻击力加成(part=part, x=0.05)


def entry_797(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['输入[装备属性指令]时， 施放无色小晶块技能时， 用蓝色小晶块替代无色小晶块， 效果持续300秒。 (冷却时间10秒)', '消耗蓝色小晶块攻击时， 使敌人进入冰冻状态。 (冷却时间25秒)', '攻击冰冻状态的敌人时， 技能攻击力 +5%']
    if mode == 0:
        pass
    if mode == 1:
        if '冰冻' not in state_type:
            state_type.append('冰冻')
        if '冰冻' in state_type:
            char.技能攻击力加成(part=part, x=0.05)


def entry_798(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['输入[装备属性指令]时， 将地图上掉落的道具移动至角色脚下。 (冷却时间30秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_799(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['输入[装备属性指令]时， 按照火、 冰、 光、 暗的顺序变更武器攻击属性。 (冷却时间0.5秒)', '利用该装备效果赋予攻击属性时， 减少10点相应的属性强化和10点属性抗性。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_800(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['输入[装备属性指令]时， 消耗HP最大值的15%， 召唤神圣之盾， 效果持续5秒。  (冷却时间45秒； HP不会因该效果而降到1%以下)', '- 神圣之盾HP相当于自身HP最大值的30%。', '- 防御前方敌人的攻击， 但限制移动。', '- 神圣之盾存在于地图中时， 增加20%的物理和魔法防御力。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_801(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['输入[装备属性指令]时， 选择1名队员， 带到自身位置。 (冷却时间50秒， 队员无敌时无法选择。)', '使带到自身位置的队员增加20%的移动速度， 效果持续20秒。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_802(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['输入[装备属性指令]时， 召唤被诅咒的傀儡， 使周围500px内敌人进入诅咒状态， 效果持续30秒。 (冷却时间30秒)', '自身位于被诅咒的傀儡范围内时， 增加20%的技能冷却时间恢复速度。 (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(1, 100, 0.2, [50, 85, 100])
        pass


def entry_803(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['输入[装备属性指令]时， 召唤亚空间， 持续2秒。 (冷却时间60秒)', '- 在亚空间周围按跳跃键时， 进入亚空间。', '- 只能由属性发动者进入亚空间。', '- 在亚空间内部时无敌。', '- 亚空间结束时， 增加30%的所有速度， 效果持续10秒。']
    if mode == 0:
        pass
    if mode == 1:
        pass


# endregion

# region 金币相关词条
gold_num = 0
gold_num_list = [i for i in range(21)] + [40]


def set_gold_num(x):
    global gold_num
    gold_num = gold_num_list[x[0]]


entry_chose.append((20840, ['选择金币数量'] + ['{}千万'.format(i)
                                         for i in gold_num_list[1:]], ""))
multi_select[20840] = False
variable_set[20840] = set_gold_num


def entry_840(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['持有金币和金库内金币总和达到1亿时， 物理、 魔法暴击 +10%', '持有金币和金库内金币总和达到4亿时， 技能攻击力 +3%']
    if mode == 0:
        pass
    if mode == 1:
        if gold_num >= 10:
            char.物理暴击率增加(0.1)
            char.魔法暴击率增加(0.1)
        if gold_num >= 40:
            char.技能攻击力加成(part=part, x=0.03)


def entry_841(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['持有金币和金库内金币总和每达到1000万， 攻击强化 +222 (最多叠加20次)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(成长词条计算(222, lv) * min(20, gold_num))
# endregion


# region 条件技能等级


def entry_884(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['除Buff技能外所有职业Lv40主动技能Lv +10 (不包含的Buff技能 : [念兽 : 龙虎啸]、 [爱之急救]、 [生命源泉]、 [复苏之光]、 [忍法 : 六道轮回])', '施放Lv40技能时， 该技能 Lv -1 (最多减少至Lv10； 该效果适用至地下城通关)', '剩余HP为70%以下的状态维持120秒时， 恢复减少的技能Lv。 (冷却时间120秒)']
    if mode == 0:
        pass
    if mode == 1:
        skills = char.技能获取(40, 40, ['猫拳', '爱之急救', '生命源泉', '复苏之光', '六道'])
        for index in range(0, len(char.技能队列)):
            skill = char.技能队列[index]
            if skill["名称"] in skills:
                skill["等级变化"] += 10-min(len(list(filter(lambda i: i['名称'] ==
                                                        skill['名称'], char.技能队列[0:index-1]))), 10)
        pass


def entry_885(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['除Buff技能外所有职业Lv45主动技能Lv +10 (不包含Buff技能 : [圣愈之风]、 [新生圣歌])', '缔造者[末日虫洞]技能Lv +10', '施放Lv45技能时， 该技能Lv -1', '缔造者施放[末日虫洞]时， 该技能Lv -1', '(最多减少至Lv10； 该效果适用至地下城通关)', '剩余HP为70%以下的状态维持120秒时， 恢复减少的技能Lv。 (冷却时间120秒)']
    if mode == 0:
        pass
    if mode == 1:
        skills = char.技能获取(45, 45)
        for index in range(0, len(char.技能队列)):
            skill = char.技能队列[index]
            if skill["名称"] in skills:
                skill["等级变化"] += 10-min(len(list(filter(lambda i: i['名称'] ==
                                                        skill['名称'], char.技能队列[0:index-1]))), 10)


def entry_886(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['除Buff技能外所有职业Lv35主动技能Lv +10 (不包含的Buff技能 : [嗜血]、 [暗影蓄能]、 [挑衅]、 [幻影化身]、 [忍法 : 残影术])', '缔造者[烈焰飓风]、 [极冰护盾]技能Lv +10', '施放Lv35技能时， 该技能Lv -1', '缔造者施放[烈焰飓风]、 [极冰护盾]时， 该技能Lv -1', '(最多减少至Lv10； 该效果适用至地下城通关时)', '剩余HP为70%以下的状态维持120秒时， 恢复减少的技能Lv。 (冷却时间120秒)']
    if mode == 0:
        pass
    if mode == 1:
        skills = char.技能获取(35, 35)
        for index in range(0, len(char.技能队列)):
            skill = char.技能队列[index]
            if skill["名称"] in skills:
                skill["等级变化"] += 10-min(len(list(filter(lambda i: i['名称'] ==
                                                        skill['名称'], char.技能队列[0:index]))), 10)


def entry_887(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['除Buff技能外所有职业Lv60主动技能Lv +10', '施放Lv60技能时， 该技能Lv -1 (最多减少至Lv10； 该效果适用至地下城通关。)', '剩余HP在70%以下的状态维持120秒时， 恢复减少的技能Lv。 (冷却时间120秒)']
    if mode == 0:
        pass
    if mode == 1:
        skills = char.技能获取(60, 60)
        for index in range(0, len(char.技能队列)):
            skill = char.技能队列[index]
            if skill["名称"] in skills:
                skill["等级变化"] += 10-min(len(list(filter(lambda i: i['名称'] ==
                                                        skill['名称'], char.技能队列[0:index-1]))), 10)


def entry_888(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['除Buff技能外所有职业Lv70主动技能Lv +10 (不包含的Buff技能 : [永恒的占有]、 [圣洁之翼])', '施放Lv70技能时， 该技能Lv -1 (最多减少Lv10； 该效果适用至地下城通关)', '剩余HP为70%以下的状态维持120秒时， 恢复减少的技能Lv。']
    if mode == 0:
        pass
    if mode == 1:
        skills = char.技能获取(70, 70)
        for index in range(0, len(char.技能队列)):
            skill = char.技能队列[index]
            if skill["名称"] in skills:
                skill["等级变化"] += 10-min(len(list(filter(lambda i: i['名称'] ==
                                                        skill['名称'], char.技能队列[0:index-1]))), 10)
# endregion

# region 破招相关词条


def entry_1053(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['破招3次时， 使角色周围450px内所有敌人进入感电状态。 (冷却时间15秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '感电' not in state_type:
            state_type.append("感电")
        pass


def entry_1054(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['破招攻击力 +15%', '每3秒减少1%的MP。']
    if mode == 0:
        pass
    if mode == 1:
        if '破招攻击' in attack_type:
            if '非破招攻击' in attack_type:
                char.技能攻击力加成(part=part, x=0.075)
            else:
                char.技能攻击力加成(part=part, x=0.15)
        pass


def entry_1055(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['破招时， 增加10%的技能攻击力， 效果持续5秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        if '破招攻击' in attack_type:
            if '非破招攻击' in attack_type:
                char.技能攻击力加成(part=part, x=0.05)
            else:
                char.技能攻击力加成(part=part, x=0.1)


def entry_904(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['非破招时， 增加35%的技能攻击力。', '破招时， 减少20%的技能攻击力。']
    if mode == 0:
        pass
    if mode == 1:
        if '非破招攻击' in attack_type and '破招攻击' in attack_type:
            char.技能攻击力加成(part=part, x=0.08)
        elif '非破招攻击' in attack_type:
            char.技能攻击力加成(part=part, x=0.35)
        elif '破招攻击' in attack_type:
            char.技能攻击力加成(part=part, x=-0.2)
# endregion

# region 职业词条
# region 鬼剑士


def entry_539(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[嗜血]删除技能蓄气功能。', '技能施放期间可施放[嗜血]。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_540(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[嗜血]技能时， 消耗10%的HP， 获得3层血气。 (最多叠加10次)', '进入地下城时，获得1层血气。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_541(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[血气之刃]、 [暴怒狂斩]时， 消耗1层血气， 增加30%的攻击力和15%的攻击范围。']
    if mode == 0:
        pass
    if mode == 1:
        char.单技能加成('血气之刃', 1.3)
        char.单技能加成('暴怒狂斩', 1.3)
        pass


def entry_542(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[血气之刃]、 [暴怒狂斩]时， 恢复5%的HP。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_543(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[万剑归宗]终结攻击发动后技能不结束。 (持续时间内最多发动1次终结攻击)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_544(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['受[基础精通]影响的技能攻击时， [万剑归宗]持续时间 +0.5秒  (一次增加的持续时间不会超过[万剑归宗]技能的持续时间上限)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_545(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['万剑归宗的穿云刺会在除觉醒技能外的所有转职技能中发动。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_546(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['万剑归宗穿云刺发射数 +1']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_547(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[冥炎之卡洛]获得冥界之力， 黑色火焰强化为冥界火焰。', '冥界火焰叠加个数上限 +2']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_548(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[冰霜之萨亚]、 [瘟疫之罗刹]、 [死亡墓碑]、 [冥祭之沼]、 [幽魂之布雷德]攻击时附着冥界火焰。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_549(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['使用特定技能攻击附着冥界火焰的对象时， 火焰同时爆炸。', '冥界火焰爆炸攻击力为冥炎之卡洛火焰攻击力的500%。', '[冥界火焰爆炸对象技能]', '- [鬼斩]', '- [月光斩]', '- [鬼斩 : 狂怒]', '- [鬼影闪]', '- [鬼斩 : 炼狱]', '- [冥炎剑]', '- [幽魂降临 : 式]', '- [鬼神剑·黄泉摆渡]']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_550(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每1个冥界火焰， 爆炸攻击力增加10%。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_551(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[杀意波动]技能波动范围 +20%', '[邪光波动阵]波动范围比率 +25%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_552(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放特定技能时， 获得雷神之力， 可以无施放动作发动[邪光波动阵]。', '- 爆炎 · 波动剑', '- 不动明王阵', '- 天雷 · 波动剑']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_553(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[爆炎·波动剑]爆炸间隔距离减少90%， 爆炸位置变更， 爆炸间隔减少30%。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_554(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[爆炎·波动剑]第2击爆炸大小增加45%， 第3击爆炸大小增加70%。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_555(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['剑术系列技能命中时， 鬼步冷却时间初始化。 (通过鬼步施放剑术系列技能时不初始化)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_556(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['共鸣系列技能命中时， 鬼步冷却时间初始化。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_557(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[鬼步]攻击力 +20%']
    if mode == 0:
        char.get_skill_by_name("鬼步").倍率 *= 1.2
        pass
    if mode == 1:
        pass


def entry_558(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[鬼步]Y轴攻击范围 +10%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_559(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[恶即斩]技能强化， 使用究极魔剑雷沃汀， 使敌人一刀两断。', '恶即斩攻击力 -15%']
    if mode == 0:
        pass
    if mode == 1:
        恶即斩 = char.get_skill_by_name("恶即斩")
        恶即斩.CP武器 = True
        恶即斩.倍率 *= 0.85
        pass


def entry_560(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['恶即斩以最大蓄气发动。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_561(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[恶即斩]攻击时对敌人造成2秒伤痕。', '[破军旋舞斩]攻击伤痕状态的敌人时， [恶即斩]技能的剩余冷却时间减少10%。 (每次[破军旋舞斩]技能仅适用1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("恶即斩").CDR *= 0.9
        pass


def entry_562(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['伤痕持续时间 +2秒', '[瞬影三绝斩]攻击伤痕状态的敌人时， [恶即斩]技能的剩余冷却时间减少10%。 (每次[瞬影三绝斩]技能仅适用1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("恶即斩").CDR *= 0.9
        pass


def entry_563(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['变更为最多填充3次的技能', '- 不再自动蓄气。', '- 除[蛇腹剑 : 破]外的转职技能攻击时， [蛇腹剑 : 破]填充1次。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_564(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[蛇腹剑 : 破]从地面召唤的剑 +3个']
    if mode == 0:
        char.get_skill_by_name("蛇腹剑：破").hit0 += 3
        char.get_skill_by_name("群魔乱舞").hit0 += 3
        pass
    if mode == 1:
        pass


def entry_565(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['可强制中断除觉醒技能外的转职技能的施放后僵直并立即发动[蛇腹剑 : 破]。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_566(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['可强制中断[蛇腹剑 : 破]的施放后僵直并使用转职技能。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_567(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[啸空十字斩]追击前方最强敌人。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_568(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[啸空十字斩]水平、 垂直斩击同时完成， 斩击后角色方向转换。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_569(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[一花渡江]、 [啸空十字斩]、 [樱花劫]、 [落英惊鸿掌]冷却时间 -20%']
    if mode == 0:
        char.单技能加成('一花渡江', CD=0.8)
        char.单技能加成('啸空十字斩', CD=0.8)
        char.单技能加成('樱花劫', CD=0.8)
        char.单技能加成('落英惊鸿掌', CD=0.8)
        pass
    if mode == 1:
        pass


def entry_570(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['可强制中断转职技能并施放[啸空十字斩]、 [落英惊鸿掌]。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_571(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[汲魂之力]灵魂吸收个数上限 +30个']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_572(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[释魂狂怒]攻击成功时， 额外灵魂吸收个数 +5个', '[暗影盛宴]爆炸攻击时， 增加5个灵魂额外吸收个数。', '[暗影绽放 : 死亡荆棘]爆炸命中时， 增加5个灵魂额外吸收个数。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_573(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[释魂飞弹]每消耗2个灵魂， 特定技能的剩余冷却时间减少1%。', '- [暗影盛宴]', '- [天罚死光]', '- [天罚之剑]', '- [暗影绽放 : 死亡荆棘]']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_574(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[释魂飞弹]追踪攻击最大距离 +20%', '[释魂飞弹]每发射1个能量消耗的灵魂个数 +2个']
    if mode == 0:
        char.get_skill_by_name('释魂飞弹').power0 += 2
        pass
    if mode == 1:
        pass


def entry_575(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[鬼缚钉]斩击攻击删除， 斩击攻击力合算至踢击攻击力。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_576(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['可强制中断[鬼缚钉]的施放后僵直并连接转职技能。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_577(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['除[回旋十字斩]、 觉醒技能外的转职技能命中时， 可强制中断技能的施放后僵直并连接[鬼缚钉]技能。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_578(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[收刀术]成功连接时， 连接的技能与使用的收刀术技能的剩余冷却时间减少15%。 (用觉醒技能连接收刀术时， 连接技能和收刀术技能的剩余冷却时间不减少)']
    if mode == 0:
        pass
    if mode == 1:
        pass


# endregion

# region 格斗家

cp_striker_male = 0
cp_striker_male_list = [1, 0]


def set_cp_striker_male(x):
    global cp_striker_male
    cp_striker_male = cp_striker_male_list[x[0]]


entry_chose.append((30579, ['CP武器-[双重释放]Buff触发',
                            'CP武器-[双重释放]Buff未触发',
                            ], "striker_male"))
multi_select[30579] = False
variable_set[30579] = set_cp_striker_male


def entry_579(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[双重释放]效果变更为持续10秒的猛烈火焰。', '- 1次限制删除， 对象技能限制删除， 强化攻击力增加量删除。', '- 技能攻击力 +45% (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        if cp_striker_male == 1:
            双重释放 = char.get_skill_by_name('双重释放')
            双重释放.hit0 = 0
            双重释放.是否有伤害 = 0
            双重释放.额外倍率 = 1.45
        pass


def entry_580(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[柔化肌肉]强制中断时， [双重释放]剩余冷却时间减少2%。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_581(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[柔化肌肉]技能强制中断次数 +2']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_582(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[柔化肌肉]强制中断时， 下一个技能攻击力变化值增加2%。']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name('柔化肌肉').额外加成 = 0.02
        pass


def entry_583(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[念兽 : 猛虎震地]时， 多段攻击与爆炸攻击删除， 生成念兽， 咆哮后引发爆炸。', '- 咆哮攻击 : 和[念兽 : 猛虎震地]多段攻击次数相同，和[念兽 : 猛虎震地]多段攻击力相同。', '- 爆炸攻击 : 和[念兽 : 猛虎震地]多段攻击次数相同，和[念兽 : 猛虎震地]多段攻击力相同。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_584(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[念兽 : 猛虎震地]强化； 将念兽咆哮命中的敌人吸附至中央。', '[念兽 : 猛虎震地]攻击范围 +20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_585(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[禅语·形灭]后可以移动。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_586(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[禅语·形灭]施放速度 +20%', '[禅语·形灭]攻击范围 +10%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_587(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['抓取技能失败时， 该技能冷却时间减少至5秒。(冷却时间10秒)', '- 无情摔击', '- 霹雳旋踢', '- 浮空凌云踢(地面上使用)', '- 地狱风火轮', '- 死亡旋律(地面上使用)', '- 武莲华', '- 黑震旋风']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_588(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[地狱风火轮]变更为2次蓄气技能。', '- 1次蓄气冷却时间 : 12秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_589(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['地狱风火轮下踢时， 引发地震。', '地震攻击力为下踢攻击力的50%']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("地狱风火轮").power3 *= 1.5
        pass


def entry_590(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['可强制中断[地狱风火轮]的施放后僵直并连接转职技能。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_591(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[狂·霸王拳]终结冲击波范围删除， 变更为用火焰瓶炸弹下劈。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_592(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[狂·霸王拳]时， 对周围敌人造成与抓取敌人相同的伤害， [狂·霸王拳]抓取失败时， 向地面下劈。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_593(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[狂 · 霸王拳]添加功能 : 技能的异常状态效果冷却时间减少 : 每个异常状态 +10%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_594(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[狂 · 霸王拳]添加功能 : 异常状态效果攻击范围增加 : 每个异常状态 +10%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_595(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[闪电之舞]1:1攻击时， 在对象左右移动攻击。']
    if mode == 0:
        pass
    if mode == 1:
        闪电之舞 = char.get_skill_by_name("闪电之舞")
        if '闪电之舞' in char.护石栏:
            闪电之舞.hit0 = 13
        else:
            闪电之舞.hit0 = 9
        pass


def entry_596(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[闪电之舞]移动次数减少4次， 攻击速度增加30%。', '[闪电之舞]攻击力 -15%']
    if mode == 0:
        pass
    if mode == 1:
        闪电之舞 = char.get_skill_by_name("闪电之舞")
        闪电之舞.倍率 *= 0.85
        pass


def entry_597(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[闪电之舞]攻击时， 生成冲击波。', '- 1:1状态下， 不发动冲击波。', '- 直接打击的对象不被冲击波攻击。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_598(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[闪电之舞]移动范围 +5%', '[闪电之舞]攻击时， 使敌人进入感电状态。 (冷却时间15秒)']
    if mode == 0:
        pass
    if mode == 1:
        if '感电' not in state_type:
            state_type.append('感电')
        pass


def entry_599(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[蓄念炮]蓄气时间删除。', '[蓄念炮]冷却时间删除。']
    if mode == 0:
        char.get_skill_by_name("念气波").CP武器 = True
        pass
    if mode == 1:
        pass


def entry_600(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['转职为气功师后， [念气波]冷却时间减少功能删除。', '[念气波]冷却时间增加4秒， 技能攻击力增加120%， 大小增加20%。']
    if mode == 0:
        char.get_skill_by_name("念气波").倍率 *= 2.2
        pass
    if mode == 1:
        pass


def entry_601(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[念气波]技能命中时， [聚能念气炮]剩余冷却时间减少5%。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_602(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[念气波]技能时， 有10%的几率， 发射攻击力增加500%的念气波。']
    if mode == 0:
        char.get_skill_by_name("念气波").倍率 *= 1.5
        pass
    if mode == 1:
        pass


def entry_603(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['转职技能命中时， 获得技术得分。 (最多20分)', '- Lv30以下转职技能 : 1分', '- Lv35~Lv80转职技能 : 2分', '- [末日风暴]、 [苍宇彗星落]、 [送葬舞步] : 5分', '- [女皇时代·辉煌舞台] : 10分', '- 无情抓取连接/空中使用技能时， 附加1分']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_604(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['技术得分超过1分 : [无情抓取]技能连接时， [无情抓取]恢复时间 -3秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_605(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['技术得分超过6分 : 抓取技能攻击失败时， 消耗3分技术得分， 该技能冷却时间减少至3秒。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_606(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['技术得分超过11分 : 施放觉醒技能时， 消耗所有分数， 除觉醒技能外的所有技能剩余冷却时间减少30%。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_607(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['特定技能攻击因街霸技能效果进入异常状态的敌人时， 发动即爆之血， 立即适用异常状态剩余伤害。', '- [擒月炎]摆拳攻击时， 发动即爆之血。', '- [猛毒擒月炎]摆拳攻击时， 发动即爆之血。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_608(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['添加发动即爆之血技能。', '- [伏虎霸王拳]终结冲击波攻击时， 发动即爆之血。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_609(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[擒月炎]异常状态附加攻击力 +5%', '[猛毒擒月炎]每1个异常状态的伤害增加率 +5%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_610(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[狂霸王拳]每1个异常状态的附加攻击力增加率 +5%']
    if mode == 0:
        pass
    if mode == 1:
        pass

# endregion

# region 神枪手


def entry_611(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[激光炮]变更为填充3次的技能； 对命中的敌人生成电磁场标志。', '- 每次填充冷却时间 : 7秒', '- 电磁场标志持续时间 : 10秒']
    if mode == 0:
        pass
    if mode == 1:
        skill = char.get_skill_by_name("激光炮")
        skill.基础施放次数 = 3
        skill.CD = 7
        pass


def entry_612(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[激光炮]大小 +40%， 攻击力 +20%', '[蓄电激光炮]蓄电时间上限 -50%']
    if mode == 0:
        skill = char.get_skill_by_name("激光炮")
        skill.倍率 *= 1.2

        pass
    if mode == 1:
        pass


def entry_613(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[FM-92刺弹炮]时， 前方存在电磁场标志敌人时， 向敌人发射追击的破甲弹。', '- 以领主/稀有/精英/HP多的顺序追击。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_614(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[FM-92刺弹炮]攻击力 +15%', '[FM-92刺弹炮]爆炸范围 +25%']
    if mode == 0:
        char.get_skill_by_name("FM92刺弹炮").倍率 *= 1.15
        pass
    if mode == 1:
        pass


def entry_615(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[机械引爆]引爆以下机器人时， 生成R-步行者。 ([机械引爆]引爆R-步行者时， 对敌人造成相当于RX-78追击者攻击力50%的伤害。)', '[R-步行者生成对象技能]', '- RX-78追击者', '- Ez-8自爆者', '- RX-60陷阱追击者']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_616(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['R-步行者生成对象技能增加', '- 空战机械 : 风暴', '- 空投支援', '- 拦截机工厂']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_617(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['R-步行者生成对象技能增加', '- Ez-10反击者', '- TX-45 特攻队']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_618(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[RX-78追击者]攻击力 +5%', 'R-步行者生成数量上限 +5', 'R-步行者受[机械引爆]爆炸伤害变化率效果影响。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_619(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['穿戴时， 生成光谱。', '施放[双鹰回旋]时， 增加30%的攻击速度， 效果持续4秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_620(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['投掷第二把鹰枪后， 成功抓取鹰枪时， 鹰枪投掷与抓取之间施放的技能减少20%的剩余冷却时间。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_621(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['鹰枪大小 +10%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_622(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[花式枪术]可强制中断次数上限 +1']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_623(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[聚合弹]轰炸地下城内最强的敌人。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_624(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['适用[超负荷装填]时， 基本攻击10次时， 填装强化[聚合弹]技能的特殊弹药。', '- 最大可填充弹药数 : 3个', '- 进入地下城时基本弹药数 : 1个']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_625(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[聚合弹]技能时， 消耗获得的[超负荷装填]强化弹药， 攻击力增加。', '- 消耗1个强化弹药 : 聚合弹攻击力 +15%', '- 消耗2个强化弹药 : 聚合弹攻击力 +40%', '- 消耗3个强化弹药 : 聚合弹攻击力 +80%']
    if mode == 0:
        pass
    if mode == 1:
        聚合弹 = char.get_skill_by_name("聚合弹")
        聚合弹.倍率 *= 1.8
        聚合弹.CP武器 = True
        pass


def entry_626(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放其他技能期间， 可以无施放动作立即发动[聚合弹]。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_627(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[M-3喷火器]时， 压缩火焰后发射。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_628(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[聚焦喷火器]时， 压缩火焰后发射。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_629(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[聚焦喷火器]变更为填充3次的技能。', '- 每次发射攻击力 : 总攻击力的50%', '- 每次填充冷却时间 : 4秒']
    if mode == 0:
        skill = char.get_skill_by_name('聚焦喷火器')
        skill.CD = 4
        skill.基础施放次数 = 3
        skill.倍率 *= 0.5
        pass
    if mode == 1:
        pass


def entry_630(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[UHT-03爆炎喷火器]移动速度增加率 +10%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_631(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[G-1 科罗纳]状态下， 改装[G-2 旋雷者[或[G-3 捕食者]时， 生成全息G-1 科罗纳， 持续8秒。', '- 全息G-1科罗纳攻击力 : G-1科罗纳攻击力的50%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_632(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['生成全息G-1 科罗纳的状态下，施放[G-磁力弹]时， 由全息G-1 科罗纳代替施放。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_633(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[改装 : G-3捕食者]强化， 发射激光并增加5%的攻击力。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_634(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[G-S.P.猎鹰]冷却时间 -20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_635(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[移动射击]左轮枪发射数 +50%', '[移动射击]技能攻击力 +30%']
    if mode == 0:
        char.单技能加成('移动射击', 1.5*1.3)
        pass
    if mode == 1:
        pass


def entry_636(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[移动射击]攻击范围 +10%', '[移动射击]期间攻击速度 +30%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_637(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[移动射击]时， 立即适用冷却时间。', '[移动射击]冷却时间 -20%']
    if mode == 0:
        char.单技能加成('移动射击', 1, 0.8)
        pass
    if mode == 1:
        pass


def entry_638(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[移动射击]期间切换地下城房间时， 保留技能效果。', '[移动射击]移动速度增加比率 +30%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_639(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['跳跃状态下，[G-14手雷]、[G-35L感电手雷]、[G-18C冰冻手雷]不消耗单兵推进器。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_640(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[G-14 手雷] / [G-35L 感电手雷] / [G-18C 冰冻手雷]最大装填数 +2']
    if mode == 0:
        char.get_skill_by_name("G35感电手雷").基础施放次数 += 2
        char.get_skill_by_name("G18冰冻手雷").基础施放次数 += 2
        pass
    if mode == 1:
        pass


def entry_641(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[G-96热压手雷]时，消耗所有手雷，投掷强化G-96热压手雷。', '- 每消耗1个手雷， [G-96热压手雷]技能攻击力增加2%。', '- 消耗对象手雷 : [G-14手雷]、[G-35L感电手雷]、[G-18C冰冻手雷]']
    if mode == 0:
        pass
    if mode == 1:
        char.单技能加成('G96热压手雷', 1.3)
        pass


def entry_642(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[空袭战略]期间， 施放[热压手雷]时， 将投掷最大强化的热压手雷。']
    if mode == 0:
        pass
    if mode == 1:
        pass

# endregion

# region 魔法师


def entry_643(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[冰之技艺]冰霜矛向冰霜武器命中的所有敌人发射。', '[冰之技艺]冰霜矛爆炸功能删除。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_644(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[冰之技艺]冰霜矛命中敌人时， 有10%的几率使敌人进入冰冻状态2秒。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_645(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[冰之技艺]冰枪攻击力占原技能攻击力百分比 +20%']
    if mode == 0:
        char.get_skill_by_name("冰之技艺").额外冰枪攻击力 += 0.2
    if mode == 1:
        pass


def entry_646(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[冰舞乱击]追击前方500px内最强敌人，同时攻击周围敌人。']
    if mode == 0:
        pass
    if mode == 1:
        pass


cp_elemental_bomber = 0
cp_elemental_bomber_list = [0, 1, 2, 3, 4, 5]


def set_cp_elemental_bomber(x):
    global cp_elemental_bomber
    cp_elemental_bomber = cp_elemental_bomber_list[x[0]]


entry_chose.append((30647, ['CP武器-[元素之力]0层',
                            'CP武器-[元素之力]1层',
                            'CP武器-[元素之力]2层',
                            'CP武器-[元素之力]3层',
                            'CP武器-[元素之力]4层',
                            'CP武器-[元素之力]5层',
                            ], "elemental_bomber"))
multi_select[30647] = False
variable_set[30647] = set_cp_elemental_bomber


def entry_647(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[元素炮]时， 向前方生成深渊之球后引发爆炸。', '[元素炮]属性变换魔法球攻击力变化率增加50%， 冷却时间增加5秒。']
    if mode == 0:
        pass
    if mode == 1:
        元素炮 = char.get_skill_by_name("元素炮")
        元素炮.倍率 *= 1.5
        元素炮.CD += 5
        pass


def entry_648(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放其他技能期间， 可以施放[元素炮]技能。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_649(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每1个元素之力， 元素炮攻击力增加量增加10%。', '施放[元素炮]时， 每消耗1个元素之力， 使技能冷却时间恢复速度增加6%， 效果持续5秒。 (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("元素炮").倍率 *= 1 + 0.1*cp_elemental_bomber
        char.技能恢复加成(1, 100, 0.06*cp_elemental_bomber, exc=[50, 85, 100])
        pass


def entry_650(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[聚能魔炮]、 [聚魔轰击]技能时， [元素炮]技能的冷却时间初始化。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_651(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[狂风冲刺]变更为填充3次的技能。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_652(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[狂风冲刺]时， 生成[游离之风]攻击敌人。', '- [狂风冲刺]的游离之风攻击力为逐风者学习的[游离之风]技能攻击力的50%。']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("狂风冲刺").CP武器 = True
        pass


def entry_653(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['强制中断技能并施放[狂风冲刺]、 [朔风牵引]、 [刃风]时， 获得1个风痕能量。 (最多叠加15次)', '风痕能量达到15个时， 施放[风暴之拳]时， 消耗所有风痕能量， 增加50%的攻击力。']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("风暴之拳").倍率 *= 1.5
        pass


def entry_654(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[游离之风]大小 +10%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_655(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[狱血之噬]施放速度 +30%', '[狱血之噬]冷却时间 -10%']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("狱血之噬").CDR *= 0.9
        pass


def entry_656(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[狱血之噬]攻击时， 获得获得2个血源之眼。 (最多5个)', '进入地下城时， 获得1个血源之眼。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_657(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[血腥狩猎]时， 消耗1个血源之眼， 强化为[致命狩猎]。', '- 攻击力 +50%', '- 攻击500px范围内所有敌人。', '- 变更为1次攻击。']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("血腥狩猎").倍率 *= 1.5
        pass


def entry_658(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[血腥炼狱]时， 消耗1个血源之眼， 强化为[血腥地狱]。', '- 攻击力 +50%', '- 施放后可以移动']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("血腥炼狱").倍率 *= 1.5
        pass


def entry_659(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[次元 : 粒子风暴]适用[次元边界]效果时， 由自身中心向开始前方生成多个次元爆炸。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_660(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[次元 : 粒子风暴]技能的攻击范围 +25%， 爆炸速度 +50%， 攻击力 +15%']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("次元：粒子风暴").倍率 *= 1.15
        pass


def entry_661(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[古史记忆]技能强化； 施放[奈雅丽]技能时， 生成分身， 代替施放。 (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_662(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[乖离 : 魅魔之舞]、 [乖离 : 异界蜂群]、 [乖离 : 禁锢]、 [乖离 : 沉沦]冷却时间 -10%']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("乖离：魅魔之舞").CDR *= 0.9
        char.get_skill_by_name("乖离：异界蜂群").CDR *= 0.9
        char.get_skill_by_name("乖离：禁锢").CDR *= 0.9
        char.get_skill_by_name("乖离：沉沦").CDR *= 0.9
        pass


cp_witch_1 = 0
cp_witch_list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def set_cp_witch_1(x):
    global cp_witch_1
    cp_witch_1 = cp_witch_list_1[x[0]]


entry_chose.append((30663, ['CP武器-生成普通糖果:{}个'.format(i)
                            for i in cp_witch_list_1], "witch"))
multi_select[30663] = False
variable_set[30663] = set_cp_witch_1

cp_witch_2 = 0
cp_witch_list_2 = [0, 1, 2, 3, 4, 5]


def set_cp_witch_2(x):
    global cp_witch_2
    cp_witch_2 = cp_witch_list_2[x[0]]


entry_chose.append((30664, ['CP武器-生成稀有糖果:{}个'.format(i)
                            for i in cp_witch_list_2], "witch"))
multi_select[30664] = False
variable_set[30664] = set_cp_witch_2

cp_witch_3 = 0
cp_witch_list_3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def set_cp_witch_3(x):
    global cp_witch_3
    cp_witch_3 = cp_witch_list_3[x[0]]


entry_chose.append((30665, ['CP武器-存储普通糖果:{}个'.format(i)
                            for i in cp_witch_list_3], "witch"))
multi_select[30665] = False
variable_set[30665] = set_cp_witch_3

cp_witch_4 = 0
cp_witch_list_4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def set_cp_witch_4(x):
    global cp_witch_4
    cp_witch_4 = cp_witch_list_4[x[0]]


entry_chose.append((30666, ['CP武器-存储稀有糖果:{}个'.format(i)
                            for i in cp_witch_list_4], "witch"))
multi_select[30666] = False
variable_set[30666] = set_cp_witch_4


def entry_663(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[超级棒棒糖]每生成1个糖果人偶， [超级棒棒糖]技能的剩余冷却时间减少3%。']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name('超级棒棒糖').CDR *= 1 - \
            (0.03*cp_witch_1 + 0.09 * cp_witch_2)
        pass


def entry_664(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['未爆炸的糖果人偶会被吸收。(最多15个)', '- 施放[超级棒棒糖]时， 根据吸收的糖果人偶数， 额外生成人偶。', '- 额外生成的糖果人偶不会被吸收； 不包含在超级棒棒糖生成个数上限中。']
    if mode == 0:
        pass
    if mode == 1:
        global cp_witch_3
        超级棒棒糖 = char.get_skill_by_name('超级棒棒糖')
        if cp_witch_4 + cp_witch_3 >= 15:
            cp_witch_3 = 15 - cp_witch_4
        超级棒棒糖.hit1 += cp_witch_3
        超级棒棒糖.hit2 += cp_witch_4
        pass


def entry_665(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[超级棒棒糖]每命中1名敌人， 使人偶生成数增加2个。', '糖果人偶攻击力 -20%']
    if mode == 0:
        pass
    if mode == 1:
        超级棒棒糖 = char.get_skill_by_name('超级棒棒糖')
        超级棒棒糖.power1 = 0.8
        超级棒棒糖.power2 = 0.8
        pass


def entry_666(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[超级棒棒糖]糖果人偶生成个数上限 +5']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_667(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['连击50次以上时， [炫纹发射]自动发动。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_668(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每次发射的炫纹数 +2', '[炫纹]技能攻击力 +10%', '[炫纹]MP消耗量 -70%']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name('炫纹发射').倍率 *= 1.1
        char.get_skill_by_name('炫纹发射').hit0 += 2
        pass


def entry_669(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[尼巫的战术]终结打击、 [天击]、 [龙牙]、 [落花掌]、 [圆舞棍]时， 每次生成的炫纹个数 +4', '[自动炫纹]一次性生成的炫纹个数 +4']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_670(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['大炫纹大小比率 +20%', '炫纹生成个数上限 +1']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_671(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['输入[装备属性指令]时， 生成元素结晶， 持续60秒。', '- 施放高级元素技能时， 该技能保存为元素结晶。(最多1个)', '- 保存技能时， 保存的技能冷却时间适用为15%。', '- 保存技能的状态下， 输入[装备属性指令]时， 发动保存的技能。', '- 发动元素结晶的技能为原本技能攻击力的15%。', '- 可以保存技能 : 杰克降临、 极冰盛宴、 天雷、 湮灭黑洞', '- 发动技能后， 元素结晶重新生成冷却时间为0.1秒']
    if mode == 0:
        pass
    if mode == 1:
        char.单技能加成('杰克降临', 1.15, 1.15)
        char.单技能加成('极冰盛宴', 1.15, 1.15)
        char.单技能加成('天雷冲击', 1.15, 1.15)
        char.单技能加成('湮灭黑洞', 1.15, 1.15)
        pass


def entry_672(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['添加元素结晶可保存技能', '- [元素之幕]、 [元素震荡]、 [圣灵水晶]']
    if mode == 0:
        pass
    if mode == 1:
        char.单技能加成('元素之幕', 1.15, 1.15)
        char.单技能加成('元素震荡', 1.15, 1.15)
        char.单技能加成('圣灵水晶', 1.15, 1.15)
        pass


def entry_673(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['保存为元素结晶的技能默认为最大蓄气状态。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_674(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[魔法记忆]施放速度提升率 +15%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_675(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[精灵召唤 : 亡魂默克尔]黑雾攻击力增加20%， 可强制控制敌人。', '[精灵召唤 : 极光格雷林]天雷攻击力增加20%， 可吸附敌人。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_676(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[精灵召唤 : 冰影阿奎利斯]七重冰导弹攻击力增加20%， 范围增加15%。', '[精灵召唤 : 火焰赫瑞克]攻击力增加20%， 可吸附敌人。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_677(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[精灵召唤 : 精灵王伊伽贝拉]发射超高密度镭射光变更为多个激光轰炸地面， 攻击力增加20%。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_678(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[蚀月附灵]技能追加操作模式无需施放动作。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_679(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[哇咔咔！]无需施放动作， 立即施放。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_680(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[咆哮吧！疯疯熊]诅咒吐息向命中的敌人赋予诅咒之息， 并发生爆炸。', '- 爆炸伤害为[咆哮吧！ 疯疯熊]诅咒吐息魔法攻击力总和的50%。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_681(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['穿戴时， 向队员赋予禁忌诅咒效果增加8%的Buff。 (解除穿戴时， 禁忌诅咒Buff效果删除； 在Buff强化装备栏穿戴时不适用该效果)', '[细心缝补]HP恢复量增加率 -50%', '[爱之急救]HP恢复量增加率 -50%']
    if mode == 0:
        buff = char.get_skill_by_name('BUFF')
        buff.倍率 *= 1.08
        pass
    if mode == 1:
        pass


def entry_682(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[细心缝补]Buff适用范围 +20%']
    if mode == 0:
        pass
    if mode == 1:
        pass

# endregion

# region 圣职者


def entry_683(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[正义审判]技能召唤光晕， 对范围内的敌人发射正义之矛后爆炸。', '- 可追击敌人数量上限 : 10名', '- 正义之矛发射数量上限 : 10个', '- 正义之矛攻击力 : 光之刃攻击力的1600%', '- 正义之矛爆炸攻击力 : 魔法阵持续时间达上限时终结攻击力的100%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_684(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['可以在其他技能施放过程中使用[正义审判]。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_685(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['穿戴时， 向队员赋予荣誉祝福效果增加8%的Buff。 (解除穿戴时， 荣誉祝福Buff效果删除； 在Buff强化装备栏穿戴时不适用该效果)', '[缓慢愈合]HP恢复量 -50%', '[圣愈之风]HP恢复量 -50%', '[圣佑结界]HP恢复量 -50%', '[圣光突袭]前冲距离 -70%', '[圣光突袭]技能攻击力 +20%']
    if mode == 0:
        buff = char.get_skill_by_name("BUFF")
        buff.倍率 *= 1.08
        char.get_skill_by_name("圣光突袭").倍率 *= 1.2
        pass
    if mode == 1:
        pass


def entry_686(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[圣光沁盾]技能不移动。', '[圣光沁盾]HP +400%', '[缓慢愈合]有效范围 +20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_687(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['前冲施放[无双击]时， 向前方突进施放。', '[无双击]可吸附霸体敌人。', '[式神 : 白虎]魔法珠大小比率 +50%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_688(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[脉轮 : 圣光]适用期间， [无双击]技能攻击力 +20%', '[无双击]范围 +20%', '[落雷符]技能攻击力 +20%', '[落雷符]范围 +20%']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("无双击").CP武器 = True
        char.get_skill_by_name("落雷符").倍率 *= 1.2
        pass


def entry_689(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[狂乱锤击]最后1击删除， 每次打击生成冲击波。', '- 最后1击攻击力合算至狂乱锤击攻击力。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_690(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[狂乱锤击]次数 +100%', '[狂乱锤击]技能冷却时间 -20%']
    if mode == 0:
        pass
    if mode == 1:
        狂乱锤击 = char.get_skill_by_name("狂乱锤击")
        狂乱锤击.倍率 *= 2
        狂乱锤击.CDR *= 0.8
        pass


def entry_691(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[正义执行 : 雷米迪奥斯的圣座]选择技能为[泯灭神击]技能时， [制裁 : 怒火疾风]变更为追击600px范围内敌人，填充3次的技能。', '- 连按攻击力增加100%， 连按次数减少9次， 终结攻击与爆炸删除。', '- 每次填充冷却时间 : 40秒', '- 以领主/稀有/精英/HP多的顺序追击', '- MP消耗量 -30%', '- 无色小晶块消耗量 -5个']
    if mode == 0:
        pass
    if mode == 1:
        觉醒 = char.get_skill_by_name("制裁：怒火疾风")
        觉醒.CD = 40
        觉醒.无色消耗 = 5
        觉醒.power0 = 2
        觉醒.hit0 = 10
        觉醒.hit1 = 0
        觉醒.hit2 = 0
        觉醒.MP = [int(i*0.7) for i in 觉醒.MP]
        for skill in char.技能队列:
            if skill["名称"] == "制裁：怒火疾风":
                skill["无色消耗"] -= 5
        pass


def entry_692(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[制裁 : 怒火疾风]敌人追击范围 +30%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_693(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[正义执行 : 雷米迪奥斯的圣座]选择技能为[泯灭神击]技能时，  额外发动以下效果。', '- 可强制中断[制裁 : 怒火疾风]并施放转职技能。', '- 强制中断转职技能并施放[制裁 : 怒火疾风]时， 不消耗[干涸之泉]能量。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_694(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[正义执行 : 雷米迪奥斯的圣座]选择技能为[泯灭神击]技能时，  额外发动以下效果。', '- 施放[刺拳猛击]时， [制裁 : 怒火疾风]技能的剩余冷却时间减少12%。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_695(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[魔化 : 末日审判者]状态下， 恶魔能量条超过30时， 消耗恶魔能量的技能攻击时， 额外消耗40点， 发动恶魔之爪。', '- [恶魔之力]的攻击力的1000%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_696(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[魔化 : 末日审判者]基本攻击与技能的恶魔能量恢复量 +10%', '恶魔之爪的恶魔之力攻击力比率 +500%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_697(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[化魔]恶魔能量恢复量 +10%', '恶魔之爪的恶魔之力攻击力比率 +500%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_698(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[魔化 : 末日审判者]攻击速度增加量 +20%， 移动速度增加量 +10%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_699(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[圣洁之光]技能接触敌人不会爆炸， 而是飞行300px后爆炸。', '- [圣洁之光]攻击力 +100%，技能冷却时间 +10%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_700(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[圣洁之光]技能命中敌人时， [神光十字]和[忏悔重击]剩余冷却时间减少2%。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_701(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['穿戴时， 向队员赋予勇气祝福效果增加8%的Buff。 (解除穿戴时， 勇气祝福Buff效果删除； 在Buff强化装备栏穿戴时不适用该效果)', '[治愈祈祷]HP恢复量 -50%', '[新生圣歌]HP恢复量 -50%', '[圣光普照]HP恢复量 -50%']
    if mode == 0:
        buff = char.get_skill_by_name("BUFF")
        buff.倍率 *= 1.08
        pass
    if mode == 1:
        pass


def entry_702(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[治愈祈祷]治疗范围 +20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_703(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[诱魔之手]技能的罪业层数增加量 +2', '[原罪释放·净化]状态下， [诱魔之手]命中时， 变身持续时间增加12秒。 (每次增加的变身持续时间不超过[原罪释放·净化]变身持续时间上限。)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_704(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每1个[七宗罪]罪业层数使罪业加身额外控制时间增加功能删除。', '[七宗罪]技能的罪业加身敌人控制时间 +1秒', '罪业层数超过3个 : 施放[罪业加身]技能时， 消耗3个罪业， 所受伤害减少15%， 效果持续10秒。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_705(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[暴食之噬]技能更变为以自身为中心吸收后爆发的技能', '[暴食之噬]攻击力+30%']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name('暴食之噬').倍率 *= 1.3
        pass


def entry_706(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['罪业层数超过3个 : 施放[暴食之噬]技能时， 消耗3个罪业， 由分身代替施放。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_707(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[火焰精华]变更为填充5次的技能。', '填充冷却时间 : 8秒']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name('火焰精华').CD = 8
        pass


def entry_708(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['发动焚烧时， [火焰精华]技能填充时间 -1秒。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_709(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[净化之焰]时， 有50%的几率， 初始化冷却时间。', '- 10秒内再次施放初始化后的[净化之焰]技能时， 初始化几率减少10%。 (最多减少10%)', '[净化之焰]攻击力 -20%']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name('净化之焰').倍率 *= 0.8
        pass


def entry_710(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[净化之焰]爆炸大小比率 +30%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_711(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[念珠连射]、 [木槵子经]攻击1次时， 获得1个神力念珠。 (最多获得20个)', '施放特定技能时， 消耗神力念珠施放效果强化的技能。', '- 不动珠箔阵 : 消耗8个神力念珠， 念珠旋转次数 +1']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name('不动珠箔阵').hit0 += 8
        pass


def entry_712(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['添加神力念珠个数消耗强化技能。', '- 百八念珠 : 念珠连射个数 +10个， 消耗10个神力念珠。', '- 退魔阴阳符 : 弹跳次数 +3次， 消耗10个神力念珠。']
    if mode == 0:
        pass
    if mode == 1:
        百八念珠 = char.get_skill_by_name('百八念珠')
        百八念珠.power0 *= 30/20
        百八念珠.power1 *= 20/10
        char.get_skill_by_name('退魔阴阳符').hit1 += 3
        pass


def entry_713(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['添加神力念珠个数消耗强化技能。', '- 天坠阴阳玉 : 念珠坠落个数 +1， 消耗15个神力念珠。', '神力念珠叠加个数上限 +5']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name('天坠阴阳玉').倍率 *= 2
        pass


def entry_714(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每施放1次[念珠连射]、 [百八念珠]、 [不动珠箔阵]冷却时间恢复速度增加1%。', '每施放1次[木槵子经]、 [百八念珠]、 [不动珠箔阵]冷却时间恢复速度增加1%。 (适用冷却时间时， 初始化[念珠连射]、 [木槵子经]产生的效果。)']
    if mode == 0:
        pass
    if mode == 1:
        pass

# endregion

# region 暗夜使者


def entry_715(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[降临 : 僵尸莱迪娅]变更为填充3次的技能。', '- 每次攻击力 : 总攻击力的45%', '- 每次填充冷却时间 : 15秒']
    if mode == 0:
        pass
    if mode == 1:
        莱迪娅 = char.get_skill_by_name("降临：僵尸莱迪娅")
        莱迪娅.基础施放次数 = 3
        莱迪娅.power0 *= 0.45
        莱迪娅.CD = 15
        pass


def entry_716(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[降临 : 僵尸莱迪娅]删除技能的额外操作功能， 直接引发爆炸。']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("降临：僵尸莱迪娅").CP武器 = True
        pass


def entry_717(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[降临 : 僵尸莱迪娅]攻击时， 向敌人生成恐怖之烙印， 持续5秒。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_718(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['对带有恐怖之烙印的敌人施放特定技能时， 该技能的剩余冷却时间减少10%。', '[对象技能]', '- 死灵之缚', '- 暗黑蛛丝引', '- 暴君极刑斩']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("暗黑蛛丝引").CD = 0.9
        char.get_skill_by_name("暴君极刑斩").CD = 0.9
        char.get_skill_by_name("死灵之缚").CD = 0.9
        pass


def entry_719(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[剑刃风暴]每次攻击获得连击点数 +100%， 移动速度 +30%， 吸附力 +30%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_720(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[剑刃风暴]变更为填充3次的技能。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_721(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[剑刃风暴]期间施放[终结追击]时， 合计[剑刃风暴]剩余伤害进行攻击。', '施放[剑刃风暴]期间， 施放[终结追击]时， 向最强敌人发射剩余匕首。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_722(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[死亡风暴]发射的匕首可贯穿敌人。', '[死亡风暴]发射的匕首个数 -10个']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name('死亡风暴').CP武器 = True
        pass


def entry_723(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[忍法 : 残影术]每消耗1个残影， 记录的[忍法 : 六道轮回]残影攻击力比率增加1.5%。 (最多叠加12次)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_724(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[忍法 : 六道轮回]技能结束时， 恢复5个残影。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_725(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[忍法 : 六道轮回]时， 进入5秒霸体。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_726(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['该装备的霸体护甲状态下， 技能冷却时间恢复速度增加50%。 (最多叠加1次，觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_727(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['背击时， 获得2个暗影之痕。(最多叠加50次)', '正面攻击时， 减少3个暗影之痕。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_728(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[剜心]背后抽取命中时， 消耗所有暗影之痕； 每消耗1个， [剜心]技能攻击力增加1%。 (最多增加50%)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_729(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[剜心]时， 获得伪装Buff， 效果持续15秒。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_730(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['该装备的伪装状态下， 技能冷却时间恢复速度增加12%。 (最多叠加1次，觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        pass

# endregion

# region 守护者


def entry_731(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[碎灵屠戮]时， 召唤亚丁的魔灵战士幻影， 引发爆炸。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_732(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['没有魔灵时， 施放[碎灵屠戮]技能时， 立即召唤所有魔灵。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_733(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[碎灵屠戮]技能期间， 可以施放[午夜嘉年华]。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_734(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[碎灵屠戮]攻击力 +10%，范围 +20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_735(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[神光冲击]消耗[天使光翼]时， 强制控制2秒吸附的敌人。', '[神光冲击]消耗[天使光翼]时， 最多消耗2个。 (消耗天使光翼最多个数时， 聚怪效果范围适用为6阶段)', '[神光冲击]攻击范围比率 +20%', '[天使光翼]聚怪效果范围 +20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_736(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[神光冲击]命中后， [天使光翼]获得量增加2个。', '敌人进入神光冲击挑衅状态时， 保持防御状态时， [天使光翼]获得时间减少50%。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_737(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[神罚之锤]技能消耗[天使光翼]， 攻击时， 使敌人进入眩晕状态。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_738(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[神罚之锤]技能消耗[天使光翼]， 攻击时， 获得以下效果。', '- 每消耗1个[天使光翼]， 技能攻击力增加4%。', '- 每消耗1个[天使光翼]， 大小增加3%。']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("神罚之锤").倍率 *= 1.32
        pass


def entry_739(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[龙刃无双]变更为填充2次的技能。', '- 攻击力 -40%', '- 每次填充冷却时间 : 10秒']
    if mode == 0:
        龙刃无双 = char.get_skill_by_name("龙刃无双")
        龙刃无双.倍率 *= 0.6
        龙刃无双.CD = 10
        pass
    if mode == 1:
        pass


def entry_740(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[龙刃无双]期间， 施放阿斯特拉技能时， [龙刃无双]冷却时间减少10%。', '- 每次施放[龙刃无双]， 冷却时间减少效果仅适用1次。']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("龙刃无双").CD *= 0.9
        pass


def entry_741(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[龙刃无双]时， 增加5%的技能攻击力， 效果持续10秒。 (最多叠加1次， 觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(part=part, x=0.05)
        pass


def entry_742(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[火焰吐息]、 [龙语召唤 : 阿斯特拉]、 [龙之撕咬]、 [魔龙之息]、 [魔龙天翔]技能冷却时间 -10%']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("火焰吐息").CDR *= 0.9
        char.get_skill_by_name("龙语召唤：阿斯特拉").CDR *= 0.9
        char.get_skill_by_name("龙之撕咬").CDR *= 0.9
        char.get_skill_by_name("魔龙之息").CDR *= 0.9
        char.get_skill_by_name("魔龙天翔").CDR *= 0.9
        pass


def entry_743(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[剑盾猛攻]连击6阶段的状态下， 施放[剑盾强袭]技能时， 进入8秒Fever Time。', 'Fever Time期间， 连锁的所有区域变更为成功区域。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_744(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['Fever Time期间， [剑盾猛攻]攻击力增加500%。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_745(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['Fever Time期间， Lv1~30技能冷却时间减少70%， 攻击力减少50%。 ([剑盾猛攻]技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_746(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[剑盾猛攻]技能时，1~30级技能的剩余冷却时间减少10%。']
    if mode == 0:
        pass
    if mode == 1:
        pass

# endregion

# region 魔枪士


def entry_747(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每存在1个暗蚀状态的敌人， 每1秒累积10%的黑雷气息； 不存在暗蚀状态的敌人时， 每1秒减少5%的黑雷气息。', '攻击领主怪物时， 累积1%的黑雷气息。', '黑雷气息达到100%时， 发动黑雷强化Buff， 效果持续5秒。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_748(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['黑雷强化Buff持续时间上限 +10秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_749(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['黑雷强化状态下， 施放[坠蚀之雨]时， 同时坠落魔枪。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_750(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['黑雷强化状态下， 施放[坠蚀之雨]时， 增加1把巨型魔枪。', '- 黑雷魔枪攻击力 : [坠蚀之雨]多段攻击力的1000%']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name('坠蚀之雨').hit0 += 10
        pass


def entry_751(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[猎杀枪]技能攻击时， 向敌人生成猎物标志， 累积一定数量时， 提升标志阶段。', '猎杀枪累积量', '- 猎杀枪 : 每次打击3个', '- 猎杀枪 : 掠食 : 每次打击10个', '- 猎杀枪 : 穿心 : 每次打击4个', '累积数量提升阶段', '- 1~19个 : 1阶段标志', '- 20~39个 : 2阶段标志', '- 超过40个 : 3阶段标志', '根据敌人猎物标志阶段， 施放[光焰枪]时消耗标志提升技能攻击力。', '- 1阶段 : 技能攻击力 +10%', '- 2阶段 : 技能攻击力 +20%', '- 3阶段 : 技能攻击力 +30%']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name('光焰枪').倍率 *= 1.3
        pass


def entry_752(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['消耗猎物标志， 可以额外增加[天龙破]、 [无尽杀戮]的技能攻击力。']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name('地龙狩').倍率 *= 1.3
        char.get_skill_by_name('无尽杀戮').倍率 *= 1.3
        pass


def entry_753(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['猎杀枪魔法枪重新生成时间 -30%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_754(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[猎杀枪 : 掠食]发射冷却时间 -30%']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name('猎杀枪').CD *= 0.7
        pass


def entry_755(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[灭天之魂]技能的[战戟猛攻]命中时能量恢复减少时间 +0.3秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_756(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['强制中断[战戟猛攻]并施放技能时， 该技能减少20%的冷却时间。 (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能冷却缩减(1, 100, 0.2, [50, 85, 100])
        pass


def entry_757(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[战戟猛攻]能量叠加次数 +1']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_758(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[战戟之魂]技能的[战戟猛攻]Buff攻击速度额外量 +10%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_759(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放特定技能时， 累积极·受创能量。', '- 双龙流云灭 : 每次攻击10点', '- 无双突刺 : 每次攻击5点', '- 无畏波动枪 : 每次攻击4点', '- 双重刺击 : 每次攻击2点', '- 刺击 : 每次攻击1点', '', '[夺命雷霆枪]攻击速度 +10%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_760(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每1点极·受创能量， [夺命雷霆枪]技能冷却时间恢复速度增加1%。']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("夺命雷霆枪").恢复 += 0.3
        pass


def entry_761(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[夺命雷霆枪]攻击时， 消耗所有极受创能量， 每1点极·受创能量可增加枪尖受创效果攻击次数。']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("夺命雷霆枪").CP武器 = True
        pass


# endregion

# region 枪剑士


def entry_762(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['每拥有1点极·受创能量， 攻击速度增加1%。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_763(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[精准射击]、 [锁定射击]攻击暗杀目标敌人时， 使敌人进入枪伤状态， 效果持续15秒。(最多叠加3次)', '[精准射击]、 [锁定射击]技能冷却时间 -15%']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("精准射击").CDR *= 0.85
        char.get_skill_by_name("锁定射击").CDR *= 0.85
        pass


def entry_764(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[双弦斩]、 [月影秘步]攻击暗杀目标敌人时， 使敌人进入斩伤状态， 效果持续15秒。(最多叠加3次)', '[双弦斩]、 [月影秘步]技能冷却时间 -15%']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("双弦斩").CDR *= 0.85
        char.get_skill_by_name("月影秘步").CDR *= 0.85
        pass


def entry_765(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[月相轮舞]攻击枪伤状态敌人时， 每1层枪伤， [月相轮舞]技能攻击力增加8%。', '- 发动效果后， 枪伤状态解除。', '[毁灭狂欢]攻击斩伤状态敌人时， 每1层斩伤， [毁灭狂欢]技能攻击力增加8%。', '- 发动效果后， 斩伤状态解除。']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("月相轮舞").倍率 *= 1.24
        char.get_skill_by_name("毁灭狂欢").倍率 *= 1.24
        pass


def entry_766(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[月光镇魂曲]攻击枪伤、 斩伤状态敌人时， 每1层枪伤或斩伤， [月光镇魂曲]技能攻击力增加8%。', '- 发动效果后， 枪伤、 斩伤状态解除。', '', '[月相轮舞]大小 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("月光镇魂曲").倍率 *= 1.48
        pass


def entry_767(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[爆裂斩]技能未命中也会爆炸。', '[爆裂斩]技能的额外攻击输入时间增加至3秒。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_768(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['可强制中断[爆裂斩]并施放转职技能。', '可强制中断转职技能并施放[爆裂斩]。', '[爆裂斩]技能结束后适用冷却时间。 (额外攻击输入时间内， 未发动额外攻击时， 适用技能冷却时间。)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_769(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[爆裂斩]时， 转职技能攻击力增加20%， 效果持续3秒。 (觉醒技能除外)', '[爆裂斩]爆炸范围 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能倍率加成(1, 100, 0.2, exc=[50, 85, 100])
        pass


def entry_770(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[爆裂斩]技能冷却时间 -35%']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("爆裂斩").CDR *= 0.65
        pass


def entry_771(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[CEAB-2 超能爆发]使用[源能提炼]能量。', '消耗[源能提炼]能量施放[CEAB-2 超能爆发]时， 以蓄气60%的状态， 发动多段攻击次数。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_772(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['消耗[源能提炼]能量施放[CEAB-2 超能爆发]时， 最大蓄气攻击力增加40%']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("CEAB-2超能爆发").倍率 *= 1.4
        pass


def entry_773(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[源能提炼]累积数上限 +2']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_774(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['消耗[源能提炼]能量时， 额外消耗1个[源能提炼]能量， 除觉醒技能外的所有技能冷却时间减少20%， 效果持续5秒。 (最多叠加1次)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能冷却缩减(1, 100, 0.2, exc=[50, 85, 100])
        pass


def entry_775(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['可强制中断转职技能的施放后僵直并立即发动[轮盘连射]。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_776(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['强制中断转职技能并施放[轮盘连射]时， 增加7%的攻击速度， 效果持续8秒。 (最多叠加3次)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_777(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['强制中断转职技能并施放[轮盘连射]时， [轮盘连射]冷却时间减少50%。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_778(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['强制中断转职技能并施放[轮盘连射]时， 强制中断的技能冷却时间减少20%。']
    if mode == 0:
        pass
    if mode == 1:
        pass

# endregion

# region 外传


def entry_779(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[时间停滞]最大连击能量增加1阶段。', '- 连击能量6阶段攻击力 : 220%']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_780(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['通过[时空主宰]效果施放其他连击技能栏技能时， 可累积连击能量。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_781(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[时空主宰]效果期间， 施放扩展技能栏技能时， 也不会结束现有连招技能。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_782(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[时空主宰]效果持续时间 +2秒']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_783(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[末日虫洞]生成隔离时间领域5秒， 囚禁内部的敌人； 持续时间结束时， 领域崩坏并发生爆炸。', '- [末日虫洞]攻击力的100%']
    if mode == 0:

        pass
    if mode == 1:
        pass


def entry_784(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['隔离时间领域持续时间内， 再次按技能键可立即引发爆炸。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_785(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['对隔离时间区域内部的终末之钟使用烈炎、 寒冰、 风暴系列技能攻击时， 每2次攻击增加5%的爆炸攻击力。 (最多增加50%)']
    if mode == 0:
        char.单技能加成('末日虫洞', 1.5)
        pass
    if mode == 1:
        pass


def entry_786(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[风暴漩涡]吸附范围 +30%', '[风暴漩涡]能量消耗量 -35%', '穿戴时[风暴漩涡]能量从0开始恢复 (复活、 进入地下城时除外)']
    if mode == 0:
        char.get_skill_by_name('风暴漩涡').最小值 *= 0.65
        pass
    if mode == 1:
        pass

# endregion

# region 合金战士


def entry_787(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['使用超频技能强制中断转职技能时， 获得1个电能。 (最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_788(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[炎神攻城炮]时， 消耗所有电能， 增加攻击力。', '- 每1个电能， 增加10%的攻击力。']
    if mode == 0:
        pass
    if mode == 1:
        char.单技能加成('炎神攻城炮', 1.5)
        pass


def entry_789(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['[超频:电流闪踢]命中敌人时， 强控敌人1.5秒。']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_790(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['施放[超频:电流闪踢]时， 消耗所有电能， 强化效果。', '- 每1个电能， 增加10%的攻击力。', '- 每1个电能， 强控时间增加0.5秒。']
    if mode == 0:
        pass
    if mode == 1:
        char.单技能加成('超频：电流闪踢', 1.5)
        pass
# endregion


# endregion


# 目前成长词条范围
for i in range(1260):
    try:
        entry_func_list[i] = eval('entry_{}'.format(i))
    except:
        pass

# region 部位固有属性


def entry_10001(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ["成长属性240级以上时增加1%技能攻击，每40级增加1%"]
    if mode == 0:
        if char.穿戴低于105():
            return
        x = sum(char.词条等级.get(part, [0]))
        if x >= 240:
            char.技能攻击力加成(part=part, x=0.01 * int((x - 200) / 40))
    if mode == 1:
        pass


def entry_10002(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
      # (上衣)
        return ["技能攻击力 +12%"]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.12)
        char.辅助属性加成(buff量=1010)
    if mode == 1:
        pass


def entry_10003(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
      # (下装)
        return ["技能攻击力 +12%"]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.12)
        char.辅助属性加成(buff量=1010)
    if mode == 1:
        pass


def entry_10004(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
      # (头肩)
        return ["技能攻击力 +34%"]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.34)
        char.辅助属性加成(buff量=1010)
    if mode == 1:
        pass


def entry_10005(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
      # (腰带)
        return ["技能攻击力 +12%"]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.12)
        char.辅助属性加成(buff量=1010)
    if mode == 1:
        pass


def entry_10006(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
      # (鞋)
        return ["技能攻击力 +29%", "移动速度 +4%"]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.29)
        char.移动速度增加(0.04)
        char.辅助属性加成(buff量=1010)
    if mode == 1:
        pass


def entry_10007(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
      # (手镯)
        return ["技能攻击力 +12%"]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.12)
        char.辅助属性加成(buff量=295)
    if mode == 1:
        pass


def entry_10008(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
      # (项链)
        return ["技能攻击力 +12%"]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.12)
        char.辅助属性加成(buff量=295)
    if mode == 1:
        pass


def entry_10009(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
      # (戒指)
        return ["技能攻击力 +12%"]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.12)
        char.辅助属性加成(buff量=295)
    if mode == 1:
        pass


def entry_10010(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
      # (辅助装备)
        return ["技能攻击力 +12%"]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.12)
        char.辅助属性加成(buff量=1875)
    if mode == 1:
        pass


def entry_10011(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
      # (魔法石)
        return["技能攻击力 +12%"]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.12)
        char.辅助属性加成(buff量=1875)
    if mode == 1:
        pass


def entry_10012(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
      # (耳环)
        return ["技能攻击力 +12%"]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.12)
        char.辅助属性加成(buff量=1010)
    if mode == 1:
        pass


def entry_10013(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
      # (胜负武器)
        return ["技能攻击力 +50%"]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.50)
        char.辅助属性加成(buff量=11695)
    if mode == 1:
        pass


def entry_10014(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
      # (吞噬武器)
        return["技能攻击力 +35%"]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.35)
        char.辅助属性加成(buff量=11695)
    if mode == 1:
        pass


# 部位固有属性
for i in range(10001, 10015):
    try:
        entry_func_list[i] = eval('entry_{}'.format(i))
    except:
        pass
# endregion 部位固有属性

#  region 宠物


def entry_10101(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        # (宠物)
        return ["Buff量 +3%", "所有职业Lv1~50 全部技能+1", "Lv30 Buff技能力量、智力增加量 +3%", "Lv30 Buff技能物理、魔法、独立攻击力 +3%"]
    if mode == 0:
        char.技能等级加成('所有', 1, 50, 1)
        char.辅助属性加成(buff百分比力智=0.03, buff百分比三攻=0.03, 百分比buff量=0.03)


def entry_11001(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击速度 +5%', '移动速度 +5%', '施放速度 +5%', '所有属性强化 +25', '所有职业Lv1~95 全部技能+1', '物理、魔法、独立攻击力 +20%', '攻击时,附加15%伤害', '所有技能冷却时间 -5%(加算)', '攻击强化 +35%']
    if mode == 0:
        char.所有属性强化加成(25)
        char.附加伤害加成(0.15)
        char.百分比三攻加成(0.2)
        char.百分比攻击强化加成(0.35)
        char.加算冷却缩减(0.05)
        char.技能等级加成('所有', 1, 95, 1)
        char.所有速度增加(0.05)
    if mode == 1:
        pass


def entry_11002(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击速度 +5%', '移动速度 +5%', '施放速度 +5%', '所有属性强化 +25', '所有职业Lv1~95 全部技能+1', '物理、魔法、独立攻击力 +15%', '攻击时,附加20%伤害', '所有技能冷却时间 -5%(加算)', '攻击强化 +35%']
    if mode == 0:
        char.所有属性强化加成(25)
        char.附加伤害加成(0.20)
        char.百分比三攻加成(0.15)
        char.百分比攻击强化加成(0.35)
        char.加算冷却缩减(0.05)
        char.技能等级加成('所有', 1, 95, 1)
        char.所有速度增加(0.05)
    if mode == 1:
        pass


def entry_11003(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击速度 +5%', '移动速度 +5%', '施放速度 +5%', '所有属性强化 +25', '所有职业Lv1~95 全部技能+1', '物理、魔法、独立攻击力 +12%', '攻击时,附加10%伤害', '所有技能冷却时间 -5%(加算)', '攻击强化 +22%']
    if mode == 0:
        char.所有属性强化加成(25)
        char.附加伤害加成(0.10)
        char.百分比三攻加成(0.12)
        char.百分比攻击强化加成(0.22)
        char.加算冷却缩减(0.05)
        char.技能等级加成('所有', 1, 95, 1)
        char.所有速度增加(0.05)
    if mode == 1:
        pass


def entry_11004(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击速度 +5%', '移动速度 +5%', '施放速度 +5%', '所有属性强化 +25', '所有职业Lv1~95 全部技能+1', '物理、魔法、独立攻击力 +10%', '攻击时,附加12%伤害', '所有技能冷却时间 -5%(加算)', '攻击强化 +22%']
    if mode == 0:
        char.所有属性强化加成(25)
        char.附加伤害加成(0.12)
        char.百分比三攻加成(0.10)
        char.百分比攻击强化加成(0.22)
        char.加算冷却缩减(0.05)
        char.技能等级加成('所有', 1, 95, 1)
        char.所有速度增加(0.05)
    if mode == 1:
        pass


def entry_11005(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击速度 +5%', '移动速度 +5%', '施放速度 +5%', '所有属性强化 +25', '所有职业Lv1~80 全部技能+1', '暴击时,额外增加20%的伤害增加量', '力量、智力 +12%', '所有技能冷却时间 -5%(加算)', '攻击强化 +32%']
    if mode == 0:
        char.所有属性强化加成(25)
        char.暴击伤害加成(0.20)
        char.百分比力智加成(0.12)
        char.百分比攻击强化加成(0.32)
        char.加算冷却缩减(0.05)
        char.技能等级加成('所有', 1, 80, 1)
        char.所有速度增加(0.05)
    if mode == 1:
        pass


def entry_11006(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击速度 +5%', '移动速度 +5%', '施放速度 +5%', '所有属性强化 +25', '所有职业Lv1~80 全部技能+1', '物理、魔法、独立攻击力 +12%', '攻击时,附加10%伤害', '所有技能冷却时间 -5%(加算)', '攻击强化 +22%']
    if mode == 0:
        char.所有属性强化加成(25)
        char.百分比三攻加成(0.12)
        char.附加伤害加成(0.10)
        char.百分比攻击强化加成(0.22)
        char.加算冷却缩减(0.05)
        char.技能等级加成('所有', 1, 80, 1)
        char.所有速度增加(0.05)
    if mode == 1:
        pass
# endregion


#  region 称号
def entry_12001(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击速度 +4%', '移动速度 +4%', '施放速度 +4%', '所有属性强化 +25', '物理、魔法、独立攻击力 +5%', '暴击时，额外增加5%的伤害增加量', '最终伤害 +5%', '力量、智力 +5%', '攻击时，附加5%的伤害', '攻击强化 +25%', '攻击时，有3%的几率增加35点力量、智力、体力、精神，效果持续20秒(冷却时间30秒)', '施放技能时，有5%的几率增加5%的物理、魔法暴击率，效果持续20秒(冷却时间30秒)']
    if mode == 0:
        char.所有属性强化加成(25)
        char.百分比三攻加成(0.05)
        char.暴击伤害加成(0.05)
        char.最终伤害加成(0.05)
        char.百分比力智加成(0.05)
        char.附加伤害加成(0.05)
        char.百分比攻击强化加成(0.25)
        char.所有速度增加(0.04)
    if mode == 1:
        char.基础属性加成(力智=35)
        char.暴击率增加(0.05)
        pass


def entry_12002(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击速度 +4%', '移动速度 +4%', '施放速度 +4%', '所有属性强化 +22', '物理、魔法、独立攻击力 +12%', '攻击时，附加10%的伤害', '攻击强化 +22%', '攻击时，有3%的几率增加35点力量、智力、体力、精神，效果持续20秒(冷却时间30秒)', '施放技能时，有5%的几率增加5%的物理、魔法暴击率，效果持续20秒(冷却时间30秒)']
    if mode == 0:
        char.所有属性强化加成(22)
        char.百分比三攻加成(0.12)
        char.附加伤害加成(0.10)
        char.百分比攻击强化加成(0.22)
        char.所有速度增加(0.04)
    if mode == 1:
        char.基础属性加成(力智=35)
        char.暴击率增加(0.05)
        pass


def entry_13001(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ["Lv1~35 全部 技能 Lv +1"]
    if mode == 0:
        char.技能等级加成('所有', 1, 35, 1)
    pass

# endregion


for i in range(10101, 14000):
    try:
        entry_func_list[i] = eval('entry_{}'.format(i))
    except:
        pass


# region 神话、改造 14001 ~ 14999
# 大祭司的神启礼服
def entry_14001(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有属性强化 +26',
                '技能攻击力 +29%',
                '攻击时,附加10%的伤害',
                '力量、智力 +10%',
                '物理、魔法、独立攻击力 +11%']
    if mode == 0:
        char.所有属性强化加成(26)
        char.技能攻击力加成(part=part, x=0.29)
        char.附加伤害加成(0.10)
        char.百分比力智加成(0.1)
        char.百分比三攻加成(0.11)
    if mode == 1:
        pass

# 大魔法师[???]的长袍


def entry_14002(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return [
            '技能攻击力 +29%',
            '所有职业Lv1~45所有技能Lv +1',
            '技能MP消耗量 -20%',
            '攻击时，额外增加11%的伤害增加量',
            '所有职业Lv1~45所有技能Lv +1',
            "力量、智力 +12%"
        ]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.29)
        char.技能等级加成('所有', 1, 45, 1)
        char.伤害增加加成(0.11)
        char.百分比力智加成(0.12)
    if mode == 1:
        char.技能等级加成('所有', 1, 45, 1)
        char.MP消耗量加成(-0.2)
        pass

# 浪漫旋律华尔兹


def entry_14003(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return [
            '技能攻击力 +31%',
            '物理、魔法、独立攻击力 +3%',
            '最终伤害 +10%',
            '攻击时，额外增加8%的伤害增加量',
            '所有属性强化 +24',
            '所有职业Lv1~45所有技能冷却时间 -10%',
        ]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.31)
        char.百分比三攻加成(0.03)
        char.最终伤害加成(0.1)
        char.伤害增加加成(0.08)
        char.所有属性强化加成(24)
    if mode == 1:
        char.技能冷却缩减(1, 45, 0.1)
        pass

# 深渊囚禁者长袍


def entry_14004(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return [
            '暗属性抗性 +10',
            '技能攻击力 +19%',
            '每5点暗属性抗性，增加1%的最终伤害(最多增加5%)',
            '所有职业Lv5~100所有技能Lv +1',
            '物理、魔法、独立攻击力 +7%',
            '物理、魔法、独立攻击力 +80'
        ]
    if mode == 0:
        char.暗属性抗性加成(10)
        char.技能攻击力加成(part=part, x=0.19)
        char.百分比三攻加成(0.07)
        char.基础属性加成(三攻=80)
        char.最终伤害加成(0.05)
        char.技能等级加成('所有', 5, 100, 1)
    if mode == 1:
        pass

# 掌管生死之阴影夹克


def entry_14005(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return [
            '所有属性强化 +18',
            '技能攻击力 +30%',
            '物理、魔法、独立攻击力 +4%',
            '力量、智力 +10%',
            '暴击时，额外增加8%的伤害增加量',
            '物理、魔法、独立攻击力 +170'
        ]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.30)
        char.所有属性强化加成(18)
        char.百分比力智加成(0.1)
        char.暴击伤害加成(0.08)
        char.基础属性加成(三攻=170)
    if mode == 1:
        char.百分比三攻加成(0.04)
        pass

# 皇家裁决者审判外套


def entry_14006(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return [
            '所有属性强化 +28',
            '技能攻击力 +29%',
            '暴击时，额外增加7%的伤害增加量',
            '攻击时，额外增加5%的伤害增加量',
            '攻击时，附加6%的伤害',
            "最终伤害 +5%"
        ]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.29)
        char.所有属性强化加成(28)
        char.附加伤害加成(0.06)
        char.暴击伤害加成(0.07)
        char.伤害增加加成(0.05)
        char.最终伤害加成(0.05)
    if mode == 1:
        pass

# 战无不胜上衣


def entry_14007(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return [
            '所有属性强化 +26',
            '技能攻击力 +30%',
            '攻击时，额外增加4%的伤害增加量',
            '物理、魔法、独立攻击力 +3%'
            '暴击时，额外增加10%的伤害增加量',
            "力量、智力 +8%"
        ]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.30)
        char.所有属性强化加成(26)
        char.暴击伤害加成(0.10)
        char.百分比三攻加成(0.03)
        char.伤害增加加成(0.04)
        char.百分比力智加成(0.08)
    if mode == 1:
        pass

# 圣者的黄昏披风


def entry_14008(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return [
            '技能攻击力 +27%',
            '物理、魔法、独立攻击力 +7%'
            '所有属性强化 +40',
            '攻击时，额外增加10%的伤害增加量',
            "攻击时，附加10%的伤害"
        ]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.27)
        char.所有属性强化加成(40)
        char.百分比三攻加成(0.07)
        char.伤害增加加成(0.10)
        char.附加伤害加成(0.10)
    if mode == 1:
        pass

# 爆裂大地之勇猛


def entry_14009(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return [
            '所有属性强化 +29',
            '技能攻击力 +30%',
            '技能快捷栏中每存在一个空栏，攻击时额外增加1%的伤害增加量(最多增加6%)',
            '物理、魔法、独立攻击力 +8%',
            '力量、智力 +8%',
            '暴击时，额外增加15%的伤害增加量'
        ]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.30)
        char.所有属性强化加成(29)
        char.伤害增加加成(
            min(0.06, len(list(filter(lambda i: i == "", char.hotkey)))*0.01))
        char.百分比三攻加成(0.08)
        char.百分比力智加成(0.08)
        char.暴击伤害加成(0.15)
    if mode == 1:
        pass

# 炙炎:霸王树


def entry_14010(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return [
            '所有属性强化 +22',
            '技能攻击力 +34%',
            "攻击速度 +15%",
            "最终伤害 +10%",
            '暴击时，额外增加8%的伤害增加量',
            '攻击时，额外增加4%的伤害增加量',
            '力量、智力 +3%',
        ]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.34)
        char.所有属性强化加成(22)
        char.伤害增加加成(0.04)
        char.暴击伤害加成(0.08)
        char.百分比力智加成(0.03)
    if mode == 1:
        char.攻击速度增加(0.15)
        pass

# 摧枯拉朽胸甲


def entry_14011(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return [
            '所有属性强化 +23',
            '所有职业Lv45 全部技能 Lv +2'
            '技能攻击力 +25%',
            "技能攻击力 +4%",
            "最终伤害 +4%",
            '攻击时，额外增加9%的伤害增加量',
            '暴击时，额外增加7%的伤害增加量',
        ]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.25)
        char.技能攻击力加成(part=part, x=0.04)
        char.所有属性强化加成(23)
        char.最终伤害加成(0.04)
        char.伤害增加加成(0.09)
        char.暴击伤害加成(0.07)
        if char.职业 == '缔造者':
            char.技能等级加成('所有', 50, 50, 2)
        else:
            char.技能等级加成('所有', 45, 45, 2)
    if mode == 1:
        pass

# 逆转结局


def entry_14012(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return [
            '攻击速度 +6%',
            '移动速度 +6%',
            '施放速度 +9%',
            "技能攻击力 +35%",
            "所有职业Lv1~48所有技能Lv+1",
            '物理、魔法、独立攻击力 +70',
            '最终伤害 +5%',
            "力量、智力 +160"
        ]
    if mode == 0:
        char.攻击速度增加(0.06)
        char.移动速度增加(0.06)
        char.施放速度增加(0.09)
        char.技能攻击力加成(part=part, x=0.35)
        char.技能等级加成('所有', 1, 48, 1)
        char.基础属性加成(三攻=70)
        char.最终伤害加成(0.05)
        char.基础属性加成(力智=100)
    if mode == 1:
        pass

# 撒旦：愤怒之王


def entry_14013(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return [
            '所有属性强化 +20',
            "技能攻击力 +34%",
            "攻击时发生持续伤害3秒,伤害量为对敌人造成伤害的5%",
            '暴击时，额外增加7%的伤害增加量',
            '攻击时，附加4%的伤害',
            "攻击时，额外增加9%的伤害增加量"
        ]
    if mode == 0:
        char.所有属性强化加成(20)
        char.技能攻击力加成(part=part, x=0.34)
        char.持续伤害加成(0.05)
        char.暴击伤害加成(0.07)
        char.附加伤害加成(0.04)
        char.伤害增加加成(0.09)
    if mode == 1:
        pass

# 天堂之翼


def entry_14014(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return [
            '所有属性强化 +22',
            "技能攻击力 +24%",
            "所有职业Lv1~80所有技能冷却时间 -13%（Lv50技能除外）",
            '攻击时，附加9%的伤害',
            "力量、智力 +4%",
            "最终伤害 +4%",
            "物理、魔法、独立攻击力 +7%"
        ]
    if mode == 0:
        char.所有属性强化加成(22)
        char.技能攻击力加成(part=part, x=0.24)
        char.技能冷却缩减(1, 80, 0.13, [50])
        char.附加伤害加成(0.09)
        char.百分比力智加成(0.04)
        char.最终伤害加成(0.04)
        char.百分比三攻加成(0.07)
    if mode == 1:
        pass

# 千链万化战甲


def entry_14015(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return [
            '所有属性强化 +29',
            '技能攻击力 +30%',
            '暴击时，额外增加10%的伤害增加',
            "物理、魔法独立攻击力 +10%",
            '攻击时，附加10%的伤害',
        ]
    if mode == 0:
        char.所有属性强化加成(29)
        char.技能攻击力加成(part=part, x=0.30)
        char.技能冷却缩减(1, 80, 0.13, [50])
        char.附加伤害加成(0.10)
        char.暴击伤害加成(0.10)
        char.百分比三攻加成(0.10)
    if mode == 1:
        pass

# 灭世之怒


def entry_14016(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return [
            '所有属性强化 +31',
            '技能攻击力 +23%',
            '攻击时附加5%的伤害',
            '最终伤害 +4% ',
            "物理、魔法、独立攻击力 +13%",
            '力量、智力 +4%',
            '技能攻击力 +5% '
        ]
    if mode == 0:
        char.所有属性强化加成(31)
        char.技能攻击力加成(part=part, x=0.23)
        char.附加伤害加成(0.5)
        char.最终伤害加成(0.04)
        char.百分比三攻加成(0.13)
        char.百分比力智加成(0.04)
        char.技能攻击力加成(part=part, x=0.05)
    if mode == 1:
        pass

# 英明循环之生命


def entry_14017(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return [
            '所有属性强化 +14',
            '技能攻击力 +25%',
            '所有职业Lv45技能攻击力-30%'
            "所有职业Lv45技能冷却时间恢复速度 +100%",
            '所有职业Lv1~45所有技能Lv +1',
            "攻击时，附加5%的伤害",
            '力量、智力+8%',
            '最终伤害+6%'
        ]
    if mode == 0:
        char.所有属性强化加成(14)
        char.技能攻击力加成(part=part, x=0.25)
        if char.职业 == '缔造者':
            char.技能倍率加成(50, 50, -0.3)
            char.技能恢复加成(50, 50, 1)
        else:
            char.技能倍率加成(45, 45, -0.3)
            char.技能恢复加成(45, 45, 1)
        char.技能等级加成('所有', 1, 45, 1)
        char.附加伤害加成(0.05)
        char.百分比力智加成(0.08)
        char.最终伤害加成(0.06)
    if mode == 1:
        pass

# 神赐的抉择


def entry_14018(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return [
            '所有属性强化 +23',
            '技能攻击力 +33%',
            '攻击时，额外增加5%的伤害增加量',
            '暴击时，额外增加7%的伤害增加量',
            "最终伤害 +6%",
            '攻击时，附加5%的伤害'

        ]
    if mode == 0:
        char.所有属性强化加成(23)
        char.技能攻击力加成(part=part, x=0.33)
        char.伤害增加加成(0.05)
        char.暴击伤害加成(0.07)
        char.最终伤害加成(0.06)
        char.附加伤害加成(0.05)
    if mode == 1:
        char.所有属性强化加成(24, 1)
        pass

# 生命脉动之地


def entry_14019(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return [
            '所有属性强化 +6',
            '技能攻击力 +30%',
            '所有属性强化 +24'
            '力量、智力 +12%',
            '攻击时，额外增加9%的伤害增加量',
            "最终伤害 +9%"
        ]
    if mode == 0:
        char.所有属性强化加成(6)
        char.技能攻击力加成(part=part, x=0.3)
        char.百分比力智加成(0.24)
        char.伤害增加加成(0.09)
        char.最终伤害加成(0.09)
    if mode == 1:
        char.所有属性强化加成(24, 1)
        pass

# 莱多：秩序创造者


def entry_14020(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return [
            '所有属性强化 +25',
            '技能攻击力 +25%',
            '物理、魔法、独立攻击力 +3%'
            '技能攻击力 +6%',
            '暴击时，额外增加9%的伤害增加',
            "力量、智力 +6%"
        ]
    if mode == 0:
        char.所有属性强化加成(25)
        char.技能攻击力加成(part=part, x=0.25)
        char.百分比力智加成(0.6)
        char.暴击伤害加成(0.09)
        char.百分比力智加成(0.06)
    if mode == 1:
        pass

# 融化黑暗之温暖


def entry_14021(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return [
            '所有属性强化+16',
            '技能攻击力+16%',
            '强化、增幅数值每增加1,额外增加1%的技能攻击力最多适用至+13) '
            'Lv15~30所有技能冷却时间恢复速度+30%',
            '所有职业Lv1~48所有技能Lv +1',
            "物理、魔法、独立攻击力+110",
            "暴击时，额外增加10%的伤害增加量",
            "攻击时，额外增加11%的伤害增加量"]
    if mode == 0:
        char.所有属性强化加成(16)
        char.技能攻击力加成(part=part, x=0.16)
        char.技能攻击力加成(part=part, x=min(char.获取强化等级([part]), 13)*0.01)
        char.技能恢复加成(15, 30, 0.3)
        char.基础属性加成(三攻=110)
        char.暴击伤害加成(0.1)
        char.伤害增加加成(0.11)
        pass
    if mode == 1:
        pass

# 伽内什的永恒庇护


def entry_14022(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ["所有属性强化+32", "攻击时，附加7%的伤害", "技能攻击力+30%", "暴击时，额外增加4%的伤害增加量", "力量、智力+10%", "攻击时，额外增加3%的伤害增加量", "物理、魔法独立攻击力 +8%"]
    if mode == 0:
        char.所有属性强化加成(32)
        char.附加伤害加成(0.07)
        char.技能攻击力加成(part=part, x=0.3)
        char.暴击伤害加成(0.04)
        char.百分比力智加成(0.1)
        char.伤害增加加成(0.03)
        char.百分比三攻加成(0.08)
        pass
    if mode == 1:
        pass

# 至高之炎 - 伊弗利特


def entry_14023(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有属性强化+35', '攻击时，附加8%的伤害', '技能攻击力+27%', '力量、智力+160', '最终伤害+12%', '物理、魔法、独立攻击力+12%']
    if mode == 0:
        char.所有属性强化加成(35)
        char.附加伤害加成(0.08)
        char.技能攻击力加成(part=part, x=0.27)
        char.基础属性加成(力智=160)
        char.最终伤害加成(0.12)
        char.百分比三攻加成(0.12)
        pass
    if mode == 1:
        pass

# 无尽的探求


def entry_14024(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有属性强化+5', '技能攻击力 +30%', '所有属性强化+36(81暗抗)', '力量、智力+240', '攻击时，附加7%的伤害', '物理、魔法、独立攻击力+12%']
    if mode == 0:
        char.所有属性强化加成(5)
        char.所有属性强化加成(36)
        char.技能攻击力加成(part=part, x=0.3)
        char.基础属性加成(力智=240)
        char.附加伤害加成(0.07)
        char.百分比三攻加成(0.12)
        pass
    if mode == 1:
        pass

# 时间回溯之针


def entry_14025(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有属性强化+5', '力量、智力+8%', '技能攻击力+30%', '所有职业Lv50所有技能冷却时间-15%', '所有职业Lv85所有技能冷却时间-15%', '力量、智力+4%', '所有属性强化+20', '物理、魔法、独立攻击力+100', '最终伤害+8%']
    if mode == 0:
        char.所有属性强化加成(5)
        char.百分比力智加成(0.08)
        char.技能攻击力加成(part=part, x=0.3)
        char.技能冷却缩减(50, 50, 0.15)
        char.技能冷却缩减(80, 80, 0.15)
        char.百分比力智加成(0.04)
        char.所有属性强化加成(20)
        char.基础属性加成(三攻=100)
        char.最终伤害加成(0.08)
        pass
    if mode == 1:
        pass

# 响彻天地的咆哮


def entry_14026(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有属性强化+31', '最终伤害+5%', '技能攻击力+25%', '技能攻击力+3%', '攻击时，附加4%的伤害', '力量、智力+7%', '物理、魔法、独立攻击力+12%']
    if mode == 0:
        char.所有属性强化加成(31)
        char.技能攻击力加成(part=part, x=0.03)
        char.附加伤害加成(0.04)
        char.百分比力智加成(0.07)
        char.百分比三攻加成(0.12)
        pass
    if mode == 1:
        char.最终伤害加成(0.05)
        char.技能攻击力加成(part=part, x=0.25)
        pass

# 狂乱之逆转宿命


def entry_14027(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有属性强化+2', '力量、智力+11%', '技能攻击力+29%', '攻击时，额外增加10%的伤害增加量', '所有属性强化+32', '暴击时，额外增加12%的伤害增加量']
    if mode == 0:
        char.所有属性强化加成(2)
        char.百分比力智加成(0.11)
        char.伤害增加加成(0.10)
        char.所有属性强化加成(32)
        char.暴击伤害加成(0.12)
        pass
    if mode == 1:
        char.技能攻击力加成(part=part, x=0.29)
        pass

# 军神的心之所念


def entry_14028(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有属性强化+25', '最终伤害+5%', '技能攻击力+30%', '攻击时，附加4%的伤害', '物理、魔法、独立攻击力+9%', '技能攻击力+4%', '最终伤害+7%']
    if mode == 0:
        char.移动速度增加(0.15)
        char.所有属性强化加成(25)
        char.最终伤害加成(0.05)
        char.技能攻击力加成(part=part, x=0.3)
        char.附加伤害加成(0.04)
        char.百分比三攻加成(0.09)
        char.技能攻击力加成(part=part, x=0.04)
        char.最终伤害加成(0.07)
        pass
    if mode == 1:
        pass

# 永恒之海


def entry_14029(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['技能攻击力+27%', '所有属性强化+12', '所有属性强化+40', '最终伤害+8%', '力量、智力+5%', '攻击时，额外增加4%的伤害增加量']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.27)
        char.所有属性强化加成(40)
        char.最终伤害加成(0.08)
        char.百分比力智加成(0.05)
        char.伤害增加加成(0.04)
        pass
    if mode == 1:
        char.所有属性强化加成(12, mode=1)
        char.攻击速度增加(0.15)
        char.移动速度增加(0.15)
        char.施放速度增加(37.5)
        pass

# 时之魅影


def entry_14030(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有属性强化+39', '攻击时，额外增加5%的伤害增加量', '技能攻击力+25%', '物理、魔法、独立攻击力+6%', '技能攻击力+4%', '攻击时，附加8%的伤害', '力量、智力+5%']
    if mode == 0:
        char.所有属性强化加成(39)
        char.伤害增加加成(0.05)
        char.技能攻击力加成(part=part, x=0.25)
        char.技能攻击力加成(part=part, x=0.04)
        char.附加伤害加成(0.08)
        char.百分比力智(0.05)
        pass
    if mode == 1:
        pass

# 等离子操控者


def entry_14031(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时，附加5%的伤害', '技能攻击力+30%', '所有属性强化+30', '攻击时，额外增加12%的伤害增加量', '力量、智力+220', '攻击时，附加12%的伤害']
    if mode == 0:
        char.附加伤害加成(0.05)
        char.技能攻击力加成(part=part, x=0.3)
        char.所有属性强化加成(30)
        char.伤害增加加成(0.12)
        char.基础属性加成(力智=220)
        char.附加伤害加成(0.12)
        pass
    if mode == 1:
        pass

# 永恒地狱黑暗之印


def entry_14032(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['技能攻击力+30%', '最终伤害+6%(18暗抗)', '最终伤害+12%', '所有属性强化+40', '攻击时，附加9%的伤害']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.3)
        char.最终伤害加成(0.6)
        char.最终伤害加成(0.12)
        char.所有属性强化加成(0.4)
        char.附加伤害加成(0.09)
        pass
    if mode == 1:
        pass

#  次元穿越之星


def entry_14033(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['技能攻击力+19%', '最终伤害+10%', '所有职业Lv50所有技能Lv+1', '所有职业Lv85所有技能Lv+1', '所有职业Lv100所有技能Lv+1', '力量、智力+300', '暴击时，额外增加11%的伤害增加量', '所有职业Lv60~100所有技能Lv+1']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.19)
        char.最终伤害加成(0.1)
        char.基础属性加成(力智=300)
        char.暴击伤害加成(0.11)
        pass
    if mode == 1:
        char.技能等级加成('所有', 50, 50, 1)
        char.技能等级加成('所有', 85, 85, 1)
        char.技能等级加成('所有', 100, 100, 1)
        pass

# 命运反抗者


def entry_14034(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有属性强化+10', '技能攻击力+27%', '物理、魔法、独立攻击力+120', '所有职业Lv1~45所有技能+1', '力量、智力+4%', '攻击时，附加7%的伤害', '最终伤害+10%(期望)']
    if mode == 0:
        char.所有属性强化加成(10)
        char.技能攻击力加成(part=part, x=0.27)
        char.基础属性加成(三攻=120)
        char.技能等级加成('所有', 1, 45, 1)
        char.百分比力智加成(0.04)
        char.附加伤害加成(0.07)
        pass
    if mode == 1:
        char.最终伤害加成(0.1)
        pass

# 心痛如绞的诀别


def entry_14035(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有属性强化+23', '技能攻击力+27%', '攻击时，附加5.3%的伤害(期望)', '所有属性强化+16', '攻击时发生持续伤害3秒，伤害量为对敌人造成伤害的10%', '暴击时，额外增加8%的伤害增加量', '力量、智力+140']
    if mode == 0:
        char.所有属性强化加成(23)
        char.技能攻击力加成(part=part, x=0.27)
        char.附加伤害加成(0.053)
        char.所有属性强化加成(16)
        char.持续伤害加成(0.1)
        char.暴击伤害加成(0.08)
        char.基础属性加成(力智=140)
        pass
    if mode == 1:
        pass

# 完美掌控


def entry_14036(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有职业Lv1~85所有技能Lv+1（特性技能除外）', '所有职业Lv100所有技能Lv+1（特性技能除外）', '所有属性强化+20*改造等级', '所有属性强化+12', '5阶段', '- 技能攻击力+1%(x20)', '6阶段', '- 技能攻击力+3%', '7阶段', '- 所有属性强化+12']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.技能等级加成('所有', 1, 85, 1)
        char.技能等级加成('所有', 100, 100, 1)
        char.所有属性强化加成(20*改造lv)
        char.所有属性强化加成(12)
        if 改造lv >= 5:
            for i in range(0, 20):
                char.技能攻击力加成(part=part, x=0.01)
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
        if 改造lv >= 7:
            char.所有属性强化加成(12)
        pass
    if mode == 1:
        pass

# 噙毒手套


def entry_14037(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['暴击时，额外增加2%*改造等级的伤害增加量', '所有属性强化+8*改造等级', '暴击时，额外增加3%的伤害增加量', '1阶段', '-暴击时，额外增加28%的伤害增加量', '4阶段', '-技能攻击力+10%', '6阶段', '-技能攻击力+3%', '7阶段', '-暴击时，额外增加3%的伤害增加量']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.暴击伤害加成(0.02*改造lv)
        char.所有属性强化加成(8*改造lv)
        char.暴击伤害加成(0.03)
        if 改造lv >= 1:
            char.暴击伤害加成(0.28)
        if 改造lv >= 4:
            char.技能攻击力加成(part=part, x=0.1)
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
        if 改造lv >= 7:
            char.暴击伤害加成(0.03)
        pass
    if mode == 1:
        pass

# 先知者的预言


def entry_14038(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ["攻击时，额外增加3%*改造等级的伤害增加量",
                '所有属性强化+4*改造等级',
                "攻击时，额外增加3%的伤害增加量"
                '1阶段', '-力量、智力+18%',
                '4阶段', "-攻击时,附加1.75%的属性伤害(期望)", "-技能攻击力+8.65%(期望)",
                "6阶段", "-技能攻击力+3%",
                "7阶段", "-攻击时，额外增加3%的伤害增加量"]
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.伤害增加加成(0.03*改造lv)
        char.伤害增加加成(0.03)
        char.所有属性强化加成(4*改造lv)
        if 改造lv >= 1:
            char.百分比力智加成(0.18)
        if 改造lv >= 4:
            char.属性附加加成(0.0175)
            char.技能攻击力加成(part=part, x=0.0865)
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
        if 改造lv >= 7:
            char.暴击伤害加成(0.03)
        pass
    if mode == 1:
        pass

# 骸麒之戒


def entry_14039(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['力量、智力+30*改造等级',
                '所有属性强化+8*改造等级',
                '攻击时，附加3%的伤害',
                '1阶段', '-攻击时，附加35%的伤害',
                '5阶段', '-攻击时，附加10%的伤害', '-技能攻击力+7%',
                '6阶段', '-技能攻击力+3%',
                '7阶段', '-攻击时，附加3%的伤害']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.基础属性加成(力智=30*改造lv)
        char.所有属性强化加成(8*改造lv)
        char.附加伤害加成(0.03)
        if 改造lv >= 1:
            char.附加伤害加成(0.35)
        if 改造lv >= 5:
            char.附加伤害加成(0.1)
            char.技能攻击力加成(part=part, x=0.07)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.附加伤害加成(0.03)
            pass
        pass
    if mode == 1:
        pass

# 窥视未来耳环


def entry_14040(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['物理、魔法、独立攻击力+40*改造等级', '所有属性强化+8*改造等级', '攻击时，额外增加3%的伤害增加量',
                '1阶段', '-攻击时，增加35%的伤害',
                '5阶段', '-所有属性强化+40',
                '6阶段', '-技能攻击力+3%',
                '7阶段', '-攻击时，额外增加3%的伤害增加量']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.基础属性加成(三攻=40*改造lv)
        char.所有属性强化加成(8*改造lv)
        char.伤害增加加成(0.03)
        if 改造lv >= 1:
            char.附加伤害加成(0.35)
            pass
        if 改造lv >= 4:
            char.所有属性强化加成(40)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.伤害增加加成(0.03)
            pass
        pass
    if mode == 1:
        pass

# 青面修罗的面具


def entry_14041(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有属性强化+16*改造等级', '所有属性强化+12',
                '1阶段', '-所有职业Lv1~85所有技能Lv+2（特性技能除外）', '-所有职业Lv100所有技能Lv+2（特性技能除外）',
                '4阶段', '-力量、智力+8%',
                '6阶段', '-技能攻击力+3%',
                '7阶段', '-所有属性强化+12']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.所有属性强化加成(16*改造lv)
        char.所有属性强化加成(12)
        if 改造lv >= 1:
            char.技能等级加成('所有', 1, 85, 2)
            char.技能等级加成('所有', 100, 100, 2)
            pass
        if 改造lv >= 4:
            char.百分比力智加成(0.08)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.所有属性强化加成(12)
            pass
        pass
    if mode == 1:
        pass

# 赤鬼的次元石


def entry_14042(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['暴击时，额外增加2%*改造等级的伤害增加量',
                '所有属性强化+8*改造等级',
                '暴击时，额外增加3%的伤害增加量',
                '1阶段', '-物理、魔法、独立攻击力+18%',
                '4阶段', '-攻击时，额外增加8%的伤害增加量', '-技能攻击力+7%',
                '5阶段', '-装备[青面修罗的面具]、[噙毒手套]中一种以上时，攻击时，附加7%的伤害',
                '6阶段', '-技能攻击力+3%',
                '7阶段', '-暴击时，额外增加3%的伤害增加量']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.所有属性强化加成(8*改造lv)
        char.暴击伤害加成(0.03)
        if 改造lv >= 1:
            char.百分比三攻加成(0.18)
            pass
        if 改造lv >= 4:
            char.伤害增加加成(0.08)
            char.技能攻击力加成(part=part, x=0.07)
            pass
        if 改造lv >= 5:
            if 40 in char.装备栏 or 36 in char.装备栏:
                char.附加伤害加成(0.07)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.暴击伤害加成(0.03)
            pass
        pass
    if mode == 1:
        pass

# 无念之仪服


def entry_14043(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['攻击时，额外增加2%*改造等级的伤害增加',
                '所有属性强化+8*改造等级',
                '攻击时，额外增加3%的伤害增加量',
                '1阶段', '-所有职业Lv50、85、100所有技能Lv+2', '-攻击时，附加4%的属性伤害',
                '5阶段', '-攻击时，额外增加5%的伤害增加量', '-技能攻击力+6%',
                '6阶段', '-技能攻击力+3%',
                '7阶段', '-攻击时，额外增加3%的伤害增加量']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.所有属性强化加成(8*改造lv)
        char.伤害增加加成(0.03)
        if 改造lv >= 1:
            char.技能等级加成('所有', 50, 50, 2)
            char.技能等级加成('所有', 85, 85, 2)
            char.技能等级加成('所有', 100, 100, 2)
            char.属性附加加成(0.04)
            pass
        if 改造lv >= 5:
            char.伤害增加加成(0.05)
            char.技能攻击力加成(part=part, x=0.06)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.伤害增加加成(0.03)
            pass
        pass
    if mode == 1:
        pass

# 无欲之花


def entry_14044(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['技能攻击力+4*改造等级',
                '攻击时，附加3%的伤害',
                '1阶段', '-攻击时，额外增加7%的伤害增加量', '-Lv50主动技能攻击力+30%', '-Lv85主动技能攻击力+25%', '-Lv100主动技能攻击力+16%',
                '5阶段', '-技能攻击力+12%',
                '6阶段', '-技能攻击力+3%',
                '7阶段', '-攻击时，附加3%的伤害']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.技能攻击力加成(part=part, x=0.04*改造lv)
        char.附加伤害加成(0.03)
        if 改造lv >= 1:
            char.伤害增加加成(0.07)
            char.技能倍率加成(50, 50, 0.3, type="active")
            char.技能倍率加成(85, 85, 0.25, type="active")
            char.技能倍率加成(100, 100, 0.16, type="active")
            pass
        if 改造lv >= 5:
            char.技能攻击力加成(part=part, x=0.12)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.附加伤害加成(0.03)
            pass
        pass
    if mode == 1:
        pass

# ["无形之气韵"]


def entry_14045(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['暴击时，额外增加2%*改造等级的伤害增加量',
                '所有属性强化+8*改造等级',
                '暴击时，额外增加3%的伤害增加量',
                '1阶段', '-暴击时，额外增加5%的伤害增加量', '-所有属性强化+30', '-所有职业Lv50~85所有技能Lv+1（特性技能除外）', '-所有职业Lv100技能Lv+1（特性技能除外）',
                '5阶段', '-暴击时，额外增加10%的伤害增加量', '-技能攻击力+2%',
                '6阶段', '-技能攻击力+3%',
                '7阶段', '-暴击时，额外增加3%的伤害增加量']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.暴击伤害加成(0.02*改造lv)
        char.所有属性强化加成(8*改造lv)
        char.暴击伤害加成(0.03)
        if 改造lv >= 1:
            char.暴击伤害加成(0.05)
            char.所有属性强化加成(30)
            char.技能等级加成('所有', 50, 85, 1)
            char.技能等级加成('所有', 100, 100, 1)
            pass
        if 改造lv >= 5:
            char.暴击伤害加成(0.06)
            char.技能攻击力加成(part=part, x=0.02)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.暴击伤害加成(0.03)
            pass
        pass
    if mode == 1:
        pass

# 无言之罪恶


def entry_14046(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['最终伤害+2%*改造等级', '所有属性强化+8*改造等级', '最终伤害+3%', '1阶段', '-技能攻击力+5%', '-所有属性强化+42', '5阶段', '-技能攻击力+9%', '6阶段', '-技能攻击力+3%', '7阶段', '-最终伤害+3%']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.最终伤害加成(0.03)
        char.最终伤害加成(0.02*改造lv)
        char.所有属性强化加成(8*改造lv)
        if 改造lv >= 1:
            char.技能攻击力加成(part=part, x=0.05)
            char.所有属性强化加成(42)
            pass
        if 改造lv >= 5:
            char.技能攻击力加成(part=part, x=0.09)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.最终伤害加成(0.03)
            pass
        pass
    if mode == 1:
        pass


# 无我之轮回
def entry_14047(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['物理、魔法、独立攻击力+2%*改造等级', '所有属性强化+8*改造等级',
                '物理、魔法、独立攻击力+3%',
                '1阶段', '-最终伤害+10%', '-物理、魔法、独立攻击力+11%',
                '5阶段', '-攻击时，附加4%的伤害', '-技能攻击力+7%',
                '6阶段', '-技能攻击力+3%',
                '7阶段', '-物理、魔法、独立攻击力+3%']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.百分比三攻加成(0.02*改造lv)
        char.所有属性强化加成(8*改造lv)
        char.百分比三攻加成(0.03)
        if 改造lv >= 1:
            char.最终伤害加成(0.1)
            char.百分比三攻加成(0.11)
            pass
        if 改造lv >= 5:
            char.附加伤害加成(0.04)
            char.技能攻击力加成(part=part, x=0.07)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.百分比三攻加成(0.03)
            pass
        pass
    if mode == 1:
        pass

# 无言怒火


def entry_14048(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['所有属性强化+16*改造等级', '所有属性强化+12',
                '1阶段', '-力量、智力+5%', '-技能攻击力+13%',
                '4阶段', '-攻击时，附加5%的属性伤害',
                '6阶段', '-技能攻击力+3%', '7阶段',
                '-所有属性强化+12']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.所有属性强化加成(16*改造lv)
        char.所有属性强化加成(12)
        if 改造lv >= 1:
            char.百分比力智加成(0.05)
            char.技能攻击力加成(part=part, x=0.13)
            pass
        if 改造lv >= 4:
            char.属性附加加成(0.05)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.所有属性强化加成(12)
            pass
        pass
    if mode == 1:
        pass

# 无形青岩


def entry_14049(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ["攻击时，额外增加2%*改造等级的伤害增加量", '所有属性强化+8*改造等级', "攻击时，额外增加3%的伤害增加量"
                "1阶段", "-攻击时，额外增加12%的伤害增加量", "攻击时，附加10%的伤害",
                "4阶段", "-发生持续伤害3秒，伤害量为对敌人造成伤害的4%", "-技能攻击力 +7%",
                "6阶段", "-技能攻击力 +3%",
                "7阶段", "-攻击时，额外增加3%的伤害增加量"
                ]
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.伤害增加加成(0.02*改造lv)
        char.所有属性强化加成(8*改造lv)
        char.伤害增加加成(0.03)
        if 改造lv >= 1:
            char.伤害增加加成(0.12)
            char.附加伤害加成(0.1)
            pass
        if 改造lv >= 4:
            char.持续伤害加成(0.04)
            char.技能攻击力加成(part=part, x=0.07)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.伤害增加加成(0.03)
            pass
        pass
    if mode == 1:
        pass

# 无念剑环


def entry_14050(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['技能攻击力+4*改造等级', '攻击时，附加3%的伤害',
                '1阶段', '-所有属性强化+40', '-攻击时，额外增加10%的伤害增加量',
                '4阶段', '-攻击时，附加10%的伤害',
                '6阶段', '-技能攻击力+3%',
                '7阶段', '-攻击时，附加3%的伤害']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.技能攻击力加成(part=part, x=0.04*改造lv)
        char.附加伤害加成(0.03)
        if 改造lv >= 1:
            char.所有属性强化加成(40)
            char.伤害增加加成(0.1)
            pass
        if 改造lv >= 4:
            char.附加伤害加成(0.1)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.附加伤害加成(0.03)
            pass
        pass
    if mode == 1:
        pass

# 支配者王冠


def entry_14051(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return['物理、魔法、独立攻击力+3%*改造等级',
               '所有属性强化+4*改造等级',
               '物理、魔法、独立攻击力+3%',
               '1阶段', '-物理、魔法、独立攻击力+14%', '-最终伤害+8%',
               '4阶段', '-技能攻击力+10%',
               '6阶段', '-技能攻击力+3%',
               '7阶段', '-物理、魔法、独立攻击力+3%']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.百分比三攻加成(0.03*改造lv)
        char.所有属性强化加成(4*改造lv)
        char.百分比三攻加成(0.03)
        if 改造lv >= 1:
            char.百分比三攻加成(0.14)
            char.最终伤害加成(0.08)
            pass
        if 改造lv >= 4:
            char.技能攻击力加成(part=part, x=0.1)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.百分比三攻加成(0.03)
            pass
        pass
    if mode == 1:
        pass

# ["灵魂掠夺者"]


def entry_14052(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['技能攻击力+4*改造等级', '攻击时，附加3%的伤害',
                '1阶段', '-暴击时，额外增加18%的伤害增加量',
                '4阶段', '-攻击时，附加4%的伤害',
                '6阶段', '-技能攻击力+3%',
                '7阶段', '-攻击时，附加3%的伤害']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.技能攻击力加成(part=part, x=0.04*改造lv)
        char.附加伤害加成(0.03)
        if 改造lv >= 1:
            char.暴击伤害加成(0.18)
            pass
        if 改造lv >= 4:
            char.附加伤害加成(0.04)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.附加伤害加成(0.03)
            pass
        pass
    if mode == 1:
        pass

# ["无我灵晶"]


def entry_14053(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0):
    if text:
        return ['暴击时，额外增加3%*改造等级的伤害增加量',
                '所有属性强化+4*改造等级',
                '暴击时，额外增加3%的伤害增加量',
                '1阶段', '-力量、智力+15%', '-所有属性强化+10',
                '4阶段', '-技能攻击力+14%',
                '6阶段', '-技能攻击力+3%',
                '7阶段', '-暴击时，额外增加3%的伤害增加量']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.暴击伤害加成(0.03*改造lv)
        char.所有属性强化加成(4*改造lv)
        char.暴击伤害加成(0.03)
        if 改造lv >= 1:
            char.百分比力智加成(0.15)
            char.所有属性强化加成(10)
            pass
        if 改造lv >= 4:
            char.技能攻击力加成(part=part, x=0.14)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:

            char.暴击伤害加成(0.03)
            pass
        pass
    if mode == 1:
        pass


# endregion
for i in range(14001, 14999):
    try:
        entry_func_list[i] = eval('entry_{}'.format(i))
    except:
        pass

# 词条效果id范围 0~18999
