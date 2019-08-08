import math
from datetime import datetime
import copy
import time
import random
import turtle
from tkinter import *


# 1. 数字组合
# total = []
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if i != k and i != j and j != k:
#                 res = i * 100 + j * 10 + k
#                 total.append(res)
# print(total)

# 2. 奖金计算
# profit_val = float(input('请输入本月利润(万元):'))
# def calculate_bonus(profit, standard=100, rate=0.01):
#     if standard == 100:
#         new_standard = 60
#         new_rate = 0.015
#     elif standard == 60:
#         new_standard = 40
#         new_rate = 0.03
#     elif standard == 40:
#         new_standard = 20
#         new_rate = 0.05
#     else:
#         new_standard = 10
#         new_rate = 0.075
#     if profit <= 10:
#         return profit * 0.1
#     elif profit > standard:
#         bonus = (profit - standard) * rate + calculate_bonus(standard, standard=new_standard, rate=new_rate)
#         return bonus
#     elif profit <= standard:
#         return calculate_bonus(profit, standard=new_standard, rate=new_rate)
# print('应发放奖金总数为%.2f万元' % calculate_bonus(profit_val, ))

# 3. 完全平方数
# n = 0
# while (n + 1) ** 2 - n * n < 168:
#     n += 1
# print(n+1)

# 4. 这天第几天
# def is_leap(year):
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         return True
#     else:
#         return False
#
#
# date_str = input('请输入年月日(YYYY-MM-DD):')
# date = datetime.strptime(date_str, '%Y-%m-%d')
# date_dict = {1: 31, 2: 29 if is_leap(date.year) else 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
#              11: 30, 12: 31}
# length = 0
# for month in range(1, date.month):
#     length += date_dict[month]
# length += date.day
# print('这是今年的第{}天'.format(length))

# 5. 三数排序
# raw = [5, 2, 3]
# for i in range(1, len(raw)):
#     for j in range(0, len(raw) - i):
#         if raw[j] > raw[j + 1]:
#             raw[j], raw[j + 1] = raw[j + 1], raw[j]
# print(raw)

# 6. 斐波那契数列
# def fib(n):
#     return 1 if n <= 2 else fib(n - 1) + fib(n - 2)
#
#
# print(fib(5))

# 7. 列表拷贝
# a = [1, 2, 3]
# b = copy.deepcopy(a)
# print(b)

# 8. 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('{0}*{1} = {2}'.format(j, i, i * j), end=' ')
#     print('')

# 9. 暂停一秒输出
# print('start')
# time.sleep(1)
# print('end')

# 10. 给人看的时间
# time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
# print(time_str)
# time.sleep(1)

# 11. 养兔子
# def fib(n):
#     return 1 if n <= 2 else fib(n - 1) + fib(n - 2)
#
#
# month = int(input('求第几个月的数量?'))
# num = 2 * fib(month)
# print('{0}个月的兔子总数为{1}'.format(month, num))

# 12. 100到200的素数
# for num in range(100, 200):
#     is_ = True
#     for ele in range(2, int(math.sqrt(num))+1):
#         if num % ele == 0:
#             is_ = False
#             break
#     if is_:
#         print(num)

# 13. 水仙花数
# for i in range(1, 10):
#     for j in range(0, 10):
#         for k in range(0, 10):
#             if (i ** 3 + j ** 3 + k ** 3) == i * 100 + j * 10 + k:
#                 print(i * 100 + j * 10 + k)

# 14. 分解质因数
# num = int(input('请输入一个正整数:\n'))
# print('{}='.format(num), end='')
# flag = True
# while flag:
#     for i in range(2, num):
#         if num % i == 0:
#             num /= i
#             num = int(num)
#             print(i, end='')
#             if num > 1:
#                 print('*', end='')
#             break
#     else:
#         flag = False
#         print(num)

# 15. 分数归档
# def doc_score(score):
#     if score >= 90:
#         print('A')
#     elif score < 60:
#         print('C')
#     else:
#         print('B')

# 16. 输出日期
# def print_date(date_str, format_str):
#     print(datetime.strptime(date_str, format_str))

# 17. 字符串构成
def count_character(str_):
    count_dict = {'num': 0, 'blank': 0, 'alphabet': 0, 'other': 0}
    for char in str_:
        if char.isspace():
            count_dict['blank'] += 1
        elif char.isdigit():
            count_dict['num'] += 1
        elif char.isalpha():
            count_dict['alphabet'] += 1
        else:
            count_dict['other'] += 1
    print(count_dict)


# 18. 复读机相加
def append_str(str_, count):
    count = int(count)
    for c in range(1, count + 1):
        print(str_ * c, end='')
        if c < count:
            print('+', end='')


# 19. 完数
def factor(num):
    ele = []
    for i in range(1, num):
        if num % i == 0:
            ele.append(i)
            if num != int(num / i):
                ele.append(int(num / i))
    ele = list(set(ele))
    if sum(ele) == num:
        print(num)


# 20. 高空抛物
def cal_height(height):
    print(height / 2)
    if height > 0.01:
        cal_height(height / 2)


# 21. 猴子偷桃
def cal_peach(remain=1, count=10):
    if count == 1:
        return remain
    else:
        return cal_peach((remain + 1) * 2, count - 1)


# 22. 比赛对手
def component():
    l1 = ['x', 'y', 'z']
    l2 = ['x', 'y', 'z']
    l3 = {}
    for i in l1:
        for j in l2:
            if i != j:
                for k in ['x', 'y', 'z']:
                    if i != k and j != k:
                        if i != 'x' and k != 'x' and k != 'z':
                            l3['a'] = i
                            l3['b'] = j
                            l3['c'] = k
    print(l3)


# 23. 画菱形
def draw_diamond(n):
    a = '*'
    for i in range(1, 2 * n):
        if i < n:
            print(' ' * (n - i) + a * (i * 2 - 1))
        else:
            print(' ' * (abs(n - i)) + a * (((2 * n) - i) * 2 - 1))


# 24. 斐波那契分数列
def fib_fraction(n, numerator, denominator, sum=0):
    if n == 0:
        print(sum)
        return
    else:
        sum += numerator / denominator
        t = numerator
        numerator += denominator
        denominator = t
        fib_fraction(n - 1, numerator, denominator, sum)


# 25. 阶乘求和
def factorial_sum(n):
    sum = 0
    for i in range(1, n + 1):
        res = 1
        for j in range(1, i + 1):
            res *= j
        sum += res
    print(sum)


# 26. 递归求阶乘
def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


# 27. 递归输出
def rev(string):
    if len(string) > 1:
        rev(string[1:])
    print(string[0], end='')


# 28. 递归等差数量
def rec_age(n):
    if n == 1:
        return 10
    else:
        return rec_age(n - 1) + 2


# 29. 反向输出
def reverse_print(num):
    n = str(num)
    print(len(n))
    print(n[::-1])


# 30. 回文数
def circle_num(num):
    a = str(num)
    b = str(num)[::-1]
    if a == b:
        print('是回文数')


# 31. 字母识词
def word_alph(alph):
    spec_dict_T = {
        'h': 'thursday',
        'u': 'tuesday',
    }
    spec_dict_S = {
        'a': 'saturday',
        'u': 'sunday'
    }
    week_dict = {
        's': spec_dict_S,
        't': spec_dict_T,
        'w': 'wednesday',
        'f': 'friday',
        'm': 'monday'
    }
    w = week_dict[alph]
    if w == spec_dict_T or w == spec_dict_S:
        print(w[str(input('请输入第二个字母')).lower()])
    else:
        print(w)


# 32. 反向输出
def reverse_print_ii():
    list1 = [1, 2, 3, 4, 5]
    list1.reverse()
    print(list1)


# 33. 列表转字符串
def trans_list(list_):
    print(','.join([str(n) for n in list_]))


# 34. 调用函数
def fun1():
    print('hello')


def fun2():
    for i in range(2):
        fun1()


# 35. 设置输出颜色
# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
#
#
# print(bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC)


# 36. 算素数
def cal_prime():
    for i in range(1, 100):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)


# 37. 排序:
def bubble_sort(arr):
    arr_ = []
    arr_.extend(arr)
    for i in range(1, len(arr_)):
        for j in range(0, len(arr_) - i):
            if arr_[j] > arr_[j + 1]:
                arr_[j], arr_[j + 1] = arr_[j + 1], arr_[j]
    print(arr_)
    return arr_


# 38. 矩阵对角线之和
def cal_mitrix():
    mitrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    res = 0
    for i in range(len(mitrix)):
        res += mitrix[i][i]
    print(res)


# 39. 有序列表插入元素
def insert_element(list_, num):
    list_.append(num)
    list_ = bubble_sort(list_)


# 40. 逆序列表
def reverse_list(arr):
    arr.reverse()
    return arr


# 41. 类的方法与变量
def inc():
    i = 0
    print(i)
    i += 1


class cls:
    i = 0

    def inc(self):
        print(self.i)
        self.i += 1


# 42. 变量作用域
# 43. 作用域、类的方法与变量
# 44. 矩阵相加
def matrix_add():
    x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    res = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(x)):
        for j in range(len(x[i])):
            res[i][j] = x[i][j] + y[i][j]
    print(res)


# 45. 求和
def _sum():
    sum = 0
    for i in range(1, 101):
        sum += i
    print(sum)


# 46. 打破循环
def break_circle():
    while True:
        try:
            n = float(input('请输入一个数字\n'))
        except ValueError:
            print('请输入数字')
            continue
        dn = n ** 2
        print(dn)
        if dn < 50:
            print('小于50')
            break


# 47. 函数交换变量
def exchange(a, b):
    return b, a


# 48. 数字比大小
def print_max(a, b):
    print(a if a > b else ((str(a) + ' = ' + str(b)) if a == b else b))


# 49. lambda
def lambda_test():
    Max = lambda x, y: x * (x >= y) + y * (y > x)
    return Max


# 50. 随机数
def random_num():
    print(random.randint(10, 20))


# 51. 按位与
def bit_and(a, b):
    print(a & b)


# 52. 按位或
def bit_or(a, b):
    print(a | b)


# 53. 按位异或
def bit_oa(a, b):
    print(a ^ b)


# 54. 位取反，位移动
def bit_move(a):
    print(~a)
    print((a >> 4) & ~(-1 << 4))


# 55. 按位取反
def bit_reverse(a):
    print(~a)


# 56. 画圈
def draw_circle(r):
    turtle.pensize(1)
    turtle.pencolor('red')
    turtle.circle(r, 360, 360)
    turtle.exitonclick()


# 57. 画线
def draw_line(l):
    turtle.pensize(1)
    turtle.pencolor('red')
    turtle.forward(l)
    turtle.exitonclick()


# 58. 画矩形
def draw_rect(a, b):
    turtle.pensize(1)
    turtle.pencolor('red')
    for i in range(2):
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(b)
        turtle.right(90)
    turtle.exitonclick()


# 59. 综合画图
def draw_rabbit():
    # 绘制大耳朵兔
    turtle.speed(10)

    # 小兔的面部
    turtle.color('pink')
    turtle.pensize(5)
    turtle.circle(radius=100)  # 脸

    # 眼睛
    turtle.pencolor('black')
    # 左眼
    turtle.pu()
    turtle.goto(-45, 92)
    turtle.pd()
    turtle.begin_fill()
    turtle.color((0, 0, 0), (0, 0, 0.1))
    turtle.circle(radius=15)
    # 右眼
    turtle.pu()
    turtle.goto(45, 92)
    turtle.pd()
    turtle.circle(radius=15)
    turtle.end_fill()

    # 鼻子
    turtle.pu()
    turtle.goto(20, 60)
    turtle.color('pink')
    turtle.pd()
    turtle.begin_fill()
    turtle.goto(-20, 60)
    turtle.goto(0, 45)
    turtle.goto(20, 60)
    turtle.end_fill()

    # 嘴
    turtle.goto(0, 45)
    turtle.goto(0, 40)
    turtle.seth(-90)
    turtle.circle(10, 120)
    turtle.pu()
    turtle.goto(0, 40)
    turtle.seth(-90)
    turtle.pd()
    turtle.circle(-10, 120)

    # 小兔的耳朵
    # 左耳
    turtle.pu()
    turtle.goto(-60, 180)  #
    turtle.seth(200)
    turtle.pd()
    turtle.circle(radius=350, extent=90)
    turtle.goto(-98, 110)
    # 右耳
    turtle.pu()
    turtle.goto(60, 180)  #
    turtle.seth(-20)
    turtle.pd()
    turtle.circle(radius=-350, extent=90)
    turtle.goto(98, 110)

    # 小兔的身体
    turtle.pu()
    turtle.goto(20, 3)
    turtle.seth(-25)
    turtle.pd()
    turtle.circle(radius=-250, extent=25)
    turtle.circle(radius=-135, extent=260)
    turtle.seth(50)
    turtle.circle(radius=-250, extent=25)

    ##小兔的胳膊
    # 左臂
    turtle.pu()
    turtle.seth(180)
    turtle.goto(-30, -3)
    turtle.pd()
    # 小短胳膊
    ##circle(radius=270,extent=20)
    ##circle(radius=20,extent=190)
    turtle.circle(radius=248, extent=30)
    turtle.circle(radius=29, extent=185)
    # 右臂
    turtle.pu()
    turtle.seth(0)
    turtle.goto(30, -3)
    turtle.pd()
    turtle.circle(radius=-248, extent=30)
    turtle.circle(radius=-27, extent=184)

    ##小兔的脚
    ##左脚
    turtle.pu()
    turtle.goto(-162, -260)  #
    turtle.pd()
    turtle.seth(0)
    turtle.circle(radius=41)
    # 右脚
    turtle.pu()
    turtle.goto(164, -260)
    turtle.pd()
    turtle.circle(radius=41)

    turtle.done()
    turtle.exitonclick()


# 60. 字符串长度
def str_length(s):
    print(len(s))


# 61. 杨辉三角
def pascal_trangle(height):
    a = []
    for i in range(height):
        a.append([])
        for j in range(i + 1):
            a[i].append(0)
    for i in range(height):
        a[i][0] = 1
        a[i][i] = 1
    for i in range(2, height):
        for j in range(1, i):
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    for i in range(len(a)):
        print(' ' * (height - i - 1), end='')
        row = a[i]
        for column in row:
            print(column, end='')
            if row.index(column) != len(row) - 1:
                print(' ', end='')
        print('')


# 62. 查找字符串
def search_str(parent, condition):
    print(parent.find(condition) == 0)


# 63. 画椭圆
def draw_ellipse():
    top = 200
    bottom = 150
    canvas = Canvas(width=800, height=600, bg='white')
    canvas.create_oval(100, 100, top, bottom)
    canvas.pack()
    mainloop()


# 64. 画椭圆、矩形
# 65. 画组合图形
def draw_():
    draw_rabbit()


# 66. 三数排序
def sort_num(a, b, c):
    arr = [a, b, c]
    bubble_sort(arr)


# 67. 交换位置
def exchange_position(arr):
    arr_ = bubble_sort(arr)
    max = arr_[len(arr) - 1]
    min = arr_[0]
    arr.remove(max)
    arr.remove(min)
    arr.insert(0, max)
    arr.append(min)
    print(arr)



