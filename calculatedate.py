import datetime
import time


def check_leap(year):
    if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
        return True
    else:
        return False


def main():
    date_str = input('请输入日期(yyyy-mm-dd):')
    indate = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    check_leap(indate.year)
    time.sleep(5)
    print(indate)


if __name__ == '__main__':
    main()
