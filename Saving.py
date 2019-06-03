"""
52 week saving money challenge
"""
import math


def saving(week, money):
    sum = []
    if week >= 1:
        sum .append((week * money))
        week -= 1
        sum += saving(week, money)
    return sum


def main():
    total_week = 52
    money = 10
    amount = saving(total_week, money)
    amount.sort()
    print(amount)
    print(math.fsum(amount))


if __name__ == '__main__':
    main()
