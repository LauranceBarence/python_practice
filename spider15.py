import requests
import openpyxl


def spider_data():
    result = []
    offset = 0
    while offset <= 1:
        url = 'https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles'
        params = {
            'page': 1,
            'offset': offset*20,
            'limit': 20,
            'sort_by': 'voteups',
            'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics'
        }

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        }

        res = requests.get(url, headers=headers, params=params)
        json_obj = res.json()
        data = json_obj['data']
        for article in data:
            result.append([article['title'], article['url'], article['excerpt']])
        offset += 1
    return result


def save_data(data):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet['A1'] = '标题'
    sheet['B1'] = '链接'
    sheet['C1'] = '摘要'
    for row in data:
        sheet.append(row)
    wb.save('./file/zhihu.xlsx')


def main():
    data = spider_data()
    print(data)
    save_data(data)


if __name__ == '__main__':
    main()
