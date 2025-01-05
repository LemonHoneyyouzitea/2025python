# author:zzk
# 2025年01月03日
import copy


def test1():
    a = [1, 2, 3]
    b = a
    b[0] = 10
    print(a)  # [10, 2, 3]

    a = [1, 2, 3]
    b = a.copy()  # 列表自身的copy
    b[0] = 10
    print(a)  # [1, 2, 3]


def use_copy():
    """
    使用copy包中的copy
    """
    c = [1, 2, 3]
    d = copy.copy(c)
    d[0] = 10
    print(id(c))
    print(id(d))
    print(c)
    print(d)


def use_copy2():
    """
    copy是浅copy
    """

    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.copy(c)
    print(f'c--{id(c)}')
    print(f'd--{id(d)}')
    a[0] = 10
    print(f'c---{c}')
    print(f'd---{d}')
    print('-' * 50)
    print(id(c[0]), id(c[1]))
    print(id(d[0]), id(d[1]))


def use_deepcopy():
    """
    递归去copy，不管有多少层,都会新做一个空间，把数据拿进来
    """
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.deepcopy(c)
    print(id(c))
    print(id(d))
    a[0] = 10
    print(f'c--{c}')
    print(f'd--{d}')
    print('-' * 50)
    print(id(c[0], id(c[1])))
    print(id(d[0], id(d[1])))


class Hero:
    def __init__(self, name, blood):
        self.name = name
        self.blood = blood
        self.equipment = ['鞋子', '帽子']


def use_copy_own_obj():
    old_hero = Hero('lich', 90)
    new_hero = copy.copy(old_hero)
    # new_hero = copy.deepcopy(old_hero)
    new_hero.blood=80 #新对象修改后，原对象不会收到任何影响
    new_hero.equipment.append('红药水')
    print(old_hero.blood)
    print(old_hero.equipment)


if __name__ == '__main__':
    # use_copy()

    # use_copy2()
    # use_deepcopy()
    use_copy_own_obj()
