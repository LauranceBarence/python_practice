# 定义两个函数：第一个函数功能为根据工作月数返回奖金额，第二个函数功能为打印出'该员工来了XX个月，获得奖金XXX元'。
# 最后传入参数('大聪'，14)调用第二个函数，打印结果'大聪来了14个月，获得奖金2520元'


def fun1(month):
    if month < 6:
        bonus = 500
    elif month > 12:
        bonus = month * 180
    else:
        bonus = month * 120
    return bonus


def fun2(name, month):
    bonus = fun1(month)
    print('{name}来了{month}个月，获得奖金{bonus}元'.format(name=name, month=month, bonus=bonus))


if __name__ == '__main__':
    fun2('大聪', 14)
