import csv

# CSV文件操作练习
unit_rooms = {}
to_direct = ['', '南北', '东西']


def set_header():
    file_exist = False
    try:
        with open('./file/assets.csv', 'r') as test:
            liss = []
            for i in test:
                liss.append(i)
            if len(liss) == 0:
                file_exist = True
    except FileNotFoundError:
        file_exist = True
    if file_exist:
        with open('./file/assets.csv', 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, dialect='excel')
            header = ['小区名称', '地址', '建筑时间', '楼栋', '单元', '门牌', '朝向', '面积']
            csv_writer.writerow(header)


def set_template():
    start_floor = input('请输入起始楼层：')
    end_floor = input('请输入终止楼层：')

    input('接下来请依次输入起始层每个房间的户室尾号、南北朝向及面积，按任意键继续')
    global unit_rooms
    floor_last_number = []
    unit_rooms = {}
    # 收集起始层的房间信息

    # 定义循环控制量
    room_loop = True
    start_floor_rooms = {}
    while room_loop:
        last_number = input('请输入起始楼层户室的尾号:（如01，02）')
        floor_last_number.append(last_number)
        # 将尾号用append()添加列表里，如floor_last_number = ['01','02']
        room_number = int(str(start_floor) + last_number)
        # 户室号为room_number,由楼层start_floor和尾号last_number组成,如301

        direction = int(input('请输入 %d 的朝向(南北朝向输入1，东西朝向输入2)：' % room_number))
        area = int(input('请输入 %d 的面积，单位 ㎡ ：' % room_number))
        start_floor_rooms[room_number] = [direction, area]
        # 户室号为键，朝向和面积组成的列表为值，添加到字典里，如start_floor_rooms = {301:[1,70]}
        continued = input('是否需要输入下一个尾号？按 n 停止输入，按其他任意键继续：')
        # 加入打破循环的条件
        if continued == 'n':
            room_loop = False
        else:
            room_loop = True
    unit_rooms[start_floor] = start_floor_rooms
    for i in range(int(start_floor) + 1, int(end_floor) + 1):
        floor_data = {}
        for f in unit_rooms[start_floor]:
            f_new = int(str(int(str(f)[0]) + i - 1) + str(f)[1:])
            floor_data[f_new] = unit_rooms[start_floor][f]
        unit_rooms[str(i)] = floor_data
    print(unit_rooms)


def input_data():
    title = input('请输入小区名称')
    address = input('请输入小区地址：')
    year = input('请输入小区建造年份：')
    block = input('请输入楼栋号：')
    unit = input('请输入单元号：')
    data = []
    for floor in unit_rooms.values():
        for room, info in floor.items():
            row_data = []
            row_data.append(title)
            row_data.append(address)
            row_data.append(year)
            row_data.append(block)
            row_data.append(unit)
            row_data.append(room)
            row_data.append(to_direct[info[0]])
            row_data.append(info[1])
            data.append(row_data)
    print(data)

    with open('./file/assets.csv', 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, dialect='excel')
        for floor in data:
            csv_writer.writerow(floor)


def main():
    set_header()
    set_template()
    input_data()


if __name__ == '__main__':
    main()
