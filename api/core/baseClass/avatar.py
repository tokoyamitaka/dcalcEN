from core.baseClass.property import 角色属性
from typing import Tuple


装扮选项属性 = {
    "神器": {
        "智力": 65,
        "体力": 65,
        "精神": 65,
        "力量": 65,
        "施放速度": 14,
        "移动速度": 7,
        "攻击速度": 7,
    },
    "稀有": {
        "智力": 55,
        "体力": 55,
        "精神": 55,
        "力量": 55,
        "施放速度": 12,
        "移动速度": 6,
        "攻击速度": 6,
    },
    "高级": {
        "智力": 45,
        "体力": 45,
        "精神": 45,
        "力量": 45,
        "施放速度": 12,
        "移动速度": 5,
        "攻击速度": 5,
    }
}


class 装扮:
    部位: str
    品质: str
    套装: str
    选项集合: Tuple[str]

    def 效果(self, 角色: 角色属性, 选项: str):
        if 选项 in self.选项集合:
            数值 = 装扮选项属性[self.品质][选项]
            角色.基础属性加成(**{选项: 数值})
        elif str(选项) == '0':
            pass
        else:
            角色.get_skill_by_name(选项).等级 += 1


class 神器装扮头发(装扮):
    部位 = "头发"
    品质 = "神器"
    套装 = "神器装扮"
    id = 1
    选项集合 = ("智力", "精神", "施放速度")


class 神器装扮帽子(装扮):
    部位 = "帽子"
    品质 = "神器"
    套装 = "神器装扮"
    选项集合 = ("智力", "精神", "施放速度")


class 神器装扮脸部(装扮):
    部位 = "脸部"
    品质 = "神器"
    套装 = "神器装扮"
    # 逗号不能删
    选项集合 = ("攻击速度",)


class 神器装扮胸部(装扮):
    部位 = "胸部"
    品质 = "神器"
    套装 = "神器装扮"
    选项集合 = ("攻击速度",)


class 神器装扮上衣(装扮):
    部位 = "上衣"
    品质 = "神器"
    套装 = "神器装扮"
    选项集合 = ()


class 神器装扮腰带(装扮):
    部位 = "腰带"
    品质 = "神器"
    套装 = "神器装扮"
    选项集合 = ("力量", "体力")


class 神器装扮下装(装扮):
    部位 = "下装"
    品质 = "神器"
    套装 = "神器装扮"
    选项集合 = ()


class 神器装扮鞋(装扮):
    部位 = "鞋"
    品质 = "神器"
    套装 = "神器装扮"
    选项集合 = ("力量", "体力", "移动速度")


class 稀有装扮头发(装扮):
    部位 = "头发"
    品质 = "稀有"
    套装 = "稀有装扮"
    选项集合 = ("智力", "精神", "施放速度")


class 稀有装扮帽子(装扮):
    部位 = "帽子"
    品质 = "稀有"
    套装 = "稀有装扮"
    选项集合 = ("智力", "精神", "施放速度")


class 稀有装扮脸部(装扮):
    部位 = "脸部"
    品质 = "稀有"
    套装 = "稀有装扮"
    选项集合 = ("攻击速度",)


class 稀有装扮胸部(装扮):
    部位 = "胸部"
    品质 = "稀有"
    套装 = "稀有装扮"
    选项集合 = ("攻击速度",)


class 稀有装扮上衣(装扮):
    部位 = "上衣"
    品质 = "稀有"
    套装 = "稀有装扮"
    选项集合 = ()


class 稀有装扮腰带(装扮):
    部位 = "腰带"
    品质 = "稀有"
    套装 = "稀有装扮"
    选项集合 = ("力量", "体力")


class 稀有装扮下装(装扮):
    部位 = "下装"
    品质 = "稀有"
    套装 = "稀有装扮"
    选项集合 = ()


class 稀有装扮鞋(装扮):
    部位 = "鞋"
    品质 = "稀有"
    套装 = "稀有装扮"
    选项集合 = ("力量", "体力", "移动速度")


class 高级装扮头发(装扮):
    部位 = "头发"
    品质 = "高级"
    套装 = "高级装扮"
    选项集合 = ("智力", "精神", "施放速度")


class 高级装扮帽子(装扮):
    部位 = "帽子"
    品质 = "高级"
    套装 = "高级装扮"
    选项集合 = ("智力", "精神", "施放速度")


class 高级装扮脸部(装扮):
    部位 = "脸部"
    品质 = "高级"
    套装 = "高级装扮"
    选项集合 = ("攻击速度",)


class 高级装扮胸部(装扮):
    部位 = "胸部"
    品质 = "高级"
    套装 = "高级装扮"
    选项集合 = ("攻击速度",)


class 高级装扮上衣(装扮):
    部位 = "上衣"
    品质 = "高级"
    套装 = "高级装扮"
    选项集合 = ()


class 高级装扮腰带(装扮):
    部位 = "腰带"
    品质 = "高级"
    套装 = "高级装扮"
    选项集合 = ("力量", "体力")


class 高级装扮下装(装扮):
    部位 = "下装"
    品质 = "高级"
    套装 = "高级装扮"
    选项集合 = ()


class 高级装扮鞋(装扮):
    部位 = "鞋"
    品质 = "高级"
    套装 = "高级装扮"
    选项集合 = ("力量", "体力", "移动速度")


神器装扮集合 = (神器装扮头发, 神器装扮帽子, 神器装扮脸部, 神器装扮胸部,
          神器装扮上衣, 神器装扮腰带, 神器装扮下装, 神器装扮鞋)
稀有装扮集合 = (稀有装扮头发, 稀有装扮帽子, 稀有装扮脸部, 稀有装扮胸部,
          稀有装扮上衣, 稀有装扮腰带, 稀有装扮下装, 稀有装扮鞋)
高级装扮集合 = (高级装扮头发, 高级装扮帽子, 高级装扮脸部, 高级装扮胸部,
          高级装扮上衣, 高级装扮腰带, 高级装扮下装, 高级装扮鞋)

装扮集合 = tuple(map(lambda x: x(), (神器装扮集合 + 稀有装扮集合 + 高级装扮集合)))


class 装扮套装:
    名称: str
    兼容于: str = None
    所需数量: int

    def 效果(self, 属性: 角色属性):
        pass


class 神器装扮3(装扮套装):
    名称 = "神器装扮"
    兼容于 = "稀有装扮"
    所需数量 = 3

    def 效果(self, 属性: 角色属性):
        # print("effect unique suit 3")
        属性.基础属性加成(四维=50, 三速=3)


class 神器装扮8(装扮套装):

    名称 = "神器装扮"
    兼容于 = "稀有装扮"
    所需数量 = 8

    def 效果(self, 属性: 角色属性):
        # print("effect unique suit 8")
        属性.基础属性加成(四维=50, 三速=3)
        属性.属性强化加成(10)


class 稀有装扮3(装扮套装):

    名称 = "稀有装扮"
    所需数量 = 3

    def 效果(self, 属性: 角色属性):
        # print("effect rare suit 3")
        属性.基础属性加成(四维=40, 三速=2)


class 稀有装扮8(装扮套装):

    名称 = "稀有装扮"
    所需数量 = 8

    def 效果(self, 属性: 角色属性):
        # print("effect rare suit 8")
        属性.基础属性加成(四维=40, 三速=2)
        属性.所有属性强化加成(6)


class 节日装扮8(装扮套装):

    名称 = "节日装扮"
    所需数量 = 8

    def 效果(self, 属性: 角色属性):
        属性.基础属性加成(四维=25, 三速=2)


class 高级装扮3(装扮套装):

    名称 = "高级装扮"
    所需数量 = 3

    def 效果(self, 属性: 角色属性):
        # print("effect uncommon suit 3")
        属性.基础属性加成(四维=10)


class 高级装扮8(装扮套装):

    名称 = "高级装扮"
    所需数量 = 8

    def 效果(self, 属性: 角色属性):
        # print("effect uncommon suit 8")
        属性.基础属性加成(四维=10, 三速=1)


装扮套装集合 = tuple(
    map(lambda x: x(), (神器装扮3, 神器装扮8, 稀有装扮3, 稀有装扮8, 节日装扮8, 高级装扮3, 高级装扮8)))
