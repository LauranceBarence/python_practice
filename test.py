import random
import time

# 需要的数据和变量
player_list = ['【狂血战士】', '【森林箭手】', '【光明骑士】', '【独行剑客】', '【格斗大师】', '【枪弹专家】']
enemy_list = ['【暗黑战士】', '【黑暗弩手】', '【暗夜骑士】', '【嗜血刀客】', '【首席刺客】', '【陷阱之王】']
player_dict = {}
enemy_dict = {}
ordered_player_list = [0, 1, 2]
ordered_enemy_list = []


# 随机生成角色的属性
def born_role():
    health = random.randint(100, 180)
    attack = random.randint(30, 50)
    return {'health': health, 'attack': attack}


# 生成和展示角色信息
def show_role():
    players = random.sample(player_list, 3)
    enemies = random.sample(enemy_list, 3)
    for player in players:
        player_dict[player] = born_role()
    for enemy in enemies:
        enemy_dict[enemy] = born_role()
    print('----------------- 角色信息 -----------------')
    print('你的人物：')
    for player in player_dict:
        print('{0}  血量:{1}  攻击:{2}'.format(player, player_dict[player]['health'], player_dict[player]['attack']))
    print('--------------------------------------------')
    print('电脑敌人：')
    for enemy in enemy_dict:
        print('{0}  血量:{1}  攻击:{2}'.format(enemy, enemy_dict[enemy]['health'], enemy_dict[enemy]['attack']))
        ordered_enemy_list.append({'name': enemy, 'attr': enemy_dict[enemy]})
    print('--------------------------------------------')
    time.sleep(1)
    print('')
    time.sleep(1)
    print('')


# 角色排序，选择出场顺序。
def order_role():
    for player in player_dict:
        order = int(input('你要把{}放在第几位?(请输入数字1，2，3)\n'.format(player)))
        ordered_player_list[order - 1] = {'name': player, 'attr': player_dict[player]}
    time.sleep(1)
    print('')
    time.sleep(1)
    print('')


# 角色PK
def pk_role():
    total_score = 0
    for i in range(3):
        print('----------------- 第{0}局战斗,{1}VS{2} -----------------'.format(i + 1, ordered_player_list[i]['name'],
                                                                            ordered_enemy_list[i]['name']))
        while ordered_player_list[i]['attr']['health'] > 0 and ordered_enemy_list[i]['attr']['health'] > 0:
            ordered_player_list[i]['attr']['health'] = ordered_player_list[i]['attr']['health'] - \
                                                       ordered_enemy_list[i]['attr']['attack']
            ordered_enemy_list[i]['attr']['health'] = ordered_enemy_list[i]['attr']['health'] - \
                                                      ordered_player_list[i]['attr']['attack']
            print('{0}向{1}发起了攻击，{2}的血量剩余{3}'.format(ordered_player_list[i]['name'], ordered_enemy_list[i]['name'],
                                                    ordered_enemy_list[i]['name'],
                                                    ordered_enemy_list[i]['attr']['health']))
            print('{0}向{1}发起了攻击，{2}的血量剩余{3}'.format(ordered_enemy_list[i]['name'], ordered_player_list[i]['name'],
                                                    ordered_player_list[i]['name'],
                                                    ordered_player_list[i]['attr']['health']))
            print('-----------------------')
            time.sleep(1.2)
        single_score = show_result(ordered_player_list[i]['attr']['health'], ordered_enemy_list[i]['attr']['health'])
        total_score += single_score

    return total_score


# 返回单局战果和计分法所加分数。
def show_result(player_life, enemy_life):
    if player_life > 0:
        print('你打败了敌人赢了这一局,得一分！')
        return 1
    else:
        if enemy_life <= 0:
            print('你和敌人同归于尽了,不得分')
        else:
            print('你被敌人干掉了,没有分,下次努力')
        return 0


# （主函数）展开战斗流程
def main():
    choice = ''
    while choice != 'n':
        show_role()
        order_role()
        result = pk_role()
        if result >= 2:
            print('你赢了')
        else:
            print('你输了')
        choice = input('wanna play again?\n')
    print('bye-bye')
    exit()



# 启动程序（即调用主函数）
main()
