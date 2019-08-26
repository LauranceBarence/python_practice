import re

numeric = re.compile('(.*?)([0-9]+)(.*?)')
illegal = re.compile('\W+?')
alphabet = re.compile('[a-zA-Z]+')


def pwd_strength(pwd):
    strength_level = 0
    if len(pwd) >= 8:
        strength_level += 1
    else:
        print(' < 8')
    if numeric.search(pwd):
        strength_level += 1
    else:
        print('none numeric')
    if re.compile(pwd):
        strength_level += 1
    else:
        print('none alphabet')
    if illegal.search(pwd):
        print('illegal')
        return -1
    else:
        return strength_level


def main():
    for i in range(5):
        pwd = input('please input your password:\n')
        level = pwd_strength(pwd)
        if level == 3:
            break
        else:
            print('your password strength is not strong enough,please retry,you got {0} times to reset'.format(4 - i))
    else:
        print('you have no chance to retry')
        exit()


if __name__ == '__main__':
    main()
