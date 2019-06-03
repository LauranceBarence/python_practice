def main():
    # file = open('./file/scores.txt', 'r', encoding='utf-8')
    # content = file.readlines()
    # file.close()
    # for str in content:
    #     data = str.split()
    #     print(data)
    utf8name = '包钦瑞'.encode('utf-8')
    gbkname = '包钦瑞'.encode('GBK')
    print(utf8name)
    print(gbkname)
    print(utf8name.decode('utf-8'))
    print(gbkname.decode('GBK'))


if __name__ == '__main__':
    main()


