import random
import matplotlib.pyplot as plt
import numpy
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
"""
    4.0
"""
# class Dice:
#     def __init__(self):
#         self.point = None
#
#     def roll(self):
#         # points = [1, 2, 3, 4, 5, 6]
#         # random.shuffle(points)
#         # self.point = random.choice(points)
#         self.point = random.randint(1, 6)
#
#
# def execute(times):
#     dice1 = Dice()
#     dice2 = Dice()
#     result = {}
#     for i in range(times):
#         dice1.roll()
#         dice2.roll()
#         if (dice1.point + dice2.point) not in result.keys():
#             result[dice1.point + dice2.point] = {'count': 1, 'P': 1.0 / times}
#         else:
#             result[dice1.point + dice2.point]['count'] += 1
#             result[dice1.point + dice2.point]['P'] = result[dice1.point + dice2.point]['count'] / times
#     return result
#
#
# def draw_chart(result_dict):
#     x = [x for x in result_dict]
#     x.sort()
#     y = [result_dict[y]['P'] for y in result_dict]
#     test = []
#     for k in result_dict:
#         test.extend([k] * result_dict[k]['count'])
#     plt.hist(test, bins=range(2, 14), edgecolor='white')
#     plt.show()

"""
    5.0ver
"""


def execute(times):
    points1 = numpy.random.randint(1, 7, size=times)
    points2 = numpy.random.randint(1, 7, size=times)
    points3 = numpy.random.randint(1, 7, size=times)
    result = points1 + points2 + points3
    return result


def draw_chart(result):
    tick_labels = [str(x) + '点' for x in range(3, 19)]
    tick_pos = numpy.arange(3, 19)
    plt.hist(result, bins=range(3, 20), density=1, edgecolor='white', linewidth=1)
    hist, bins = numpy.histogram(result, bins=range(3, 20))
    print(hist, bins, sep='\n')
    plt.xticks(tick_pos, tick_labels)
    plt.title('直方图')
    plt.show()


def main():
    result = execute(50000)
    draw_chart(result)


if __name__ == '__main__':
    main()
