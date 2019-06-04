import math


# 取绝对值的三种方式

def abs_value1(val):
    print(abs(val))


def abs_value2(val):
    if val > 0:
        print(val)
    else:
        print(-val)


def abs_value3(val):
    print(math.fabs(val))


def main():
    while True:
        try:
            num = float(input("请输入一个数字"))
            abs_value1(num)
            abs_value2(num)
            abs_value3(num)
            break
        except ValueError:
            print("请输入正确的数字")


if __name__ == '__main__':
    main()
