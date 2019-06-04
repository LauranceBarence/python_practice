import requests
import time
import openpyxl
import random


def word_test():
    res = requests.get("https://www.shanbay.com/api/v1/vocabtest/category/")

    category = res.json()['data']
    total_result = []
    while True:
        print(' '.join(
            [str(category.index(x) + 1) + '.' + x[1] + ('\n' if category.index(x) == 4 else '') for x in category]))
        choice = int(input('请选择你想要测试的分类:\n')) - 1

        print('测量词库生成中...')
        time.sleep(1)

        code = category[choice][0]
        word_res = requests.get('https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category=' + code)
        word_infos = word_res.json()['data']

        word_list = []
        for word_info in word_infos:
            word = {}
            word['word'] = word_info['content']
            word['definition'] = '/'.join(
                [definition['definition'].strip() for definition in word_info['definition_choices']]).split(
                '/')
            word_list.append(word)

        print('词库生成完成，测试即将开始！')
        for i in range(3, 0, -1):
            print(str(i) + '...')
            time.sleep(1)

        print('测试现在开始。如果你认识这个单词，请输入Y，否则直接敲Enter：')
        correct_list = []
        incorrect_list = []
        for index, word in enumerate(word_list):
            print('第{0}个：{1}'.format(index + 1, word['word']))
            know = input('认识请敲Y,否则敲Enter')
            if know.upper() == 'Y':
                correct_list.append(word)
            else:
                incorrect_list.append(word)

        word_list_back = []
        word_list_back.extend(correct_list)
        word_list_back.extend(incorrect_list)
        print('\n在上述' + str(len(word_list)) + '个单词当中，有' + str(len(correct_list)) + '个是你觉得自己认识的，它们是：')
        for index, word in enumerate(correct_list):
            if (index + 1) / 10 == 0:
                print(str(index + 1) + '.' + word['word'])
            else:
                print(str(index + 1) + '.' + word['word'], end=' ')
        print('接下来将对这些单词进行检测:')
        wrong_list = []
        right_count = 0
        for word in correct_list:
            word_list_back.remove(word)
            correct_answer = random.sample(word['definition'], 1)
            wrong_answers = random.sample(
                ','.join([','.join(other_word['definition']) for other_word in word_list_back]).split(','), 3)
            answer_list = []
            answer_list.extend(correct_answer)
            answer_list.extend(wrong_answers)
            choice_dict = {}
            for c in ['A', 'B', 'C', 'D']:
                c_ans = random.sample(answer_list, 1)
                answer_list.remove(c_ans[0])
                choice_dict[c] = c_ans[0]
            print('以下选项是{}的含义的是'.format(word['word']))
            for cho in choice_dict:
                print('{0} {1}'.format(cho, choice_dict[cho]))
            answer = input('输入你的答案，选出正确选项(胡乱输入会被算错哦，请慎重)').upper()
            try:
                if correct_answer[0] == choice_dict[answer]:
                    right_count += 1
                else:
                    wrong_list.append(word)
            except KeyError:
                wrong_list.append(word)
        print('你选择的{0}个单词中，你掌握了{1}个，错了{2}个'.format(len(correct_list), right_count, len(wrong_list)))
        print('以下为错误的单词')
        for wrong_word in wrong_list:
            print('{0}  含义:{1}'.format(wrong_word['word'], '/'.join(wrong_word['definition'])))
            total_result.append([wrong_word['word'], '/'.join(wrong_word['definition'])])
        is_continue = input('测试结束，是否要再来一次(y/n)?').lower()
        if is_continue == 'y':
            continue
        else:
            print('Bye Bye...')
            break
    return total_result


def save_data(data):
    wb = openpyxl.load_workbook('./file/错题集.xlsx')
    name = '错题集'+time.strftime('%d-%m-%Y')
    sheet_exist = False
    try:
        sheet = wb[name]
        sheet_exist = True
    except KeyError:
        sheet_exist = False
    if sheet_exist:
        print(sheet.title)
    else:
        sheet = wb.create_sheet(name)
        sheet['A1'] = '单词'
        sheet['C1'] = '含义'
    for row in data:
        sheet.append(row)
    wb.save('./file/错题集.xlsx')


def main():
    data = word_test()
    save_data(data)


if __name__ == '__main__':
    main()
