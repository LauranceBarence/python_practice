# import re

# s = 'Total income is around $131,000, ended with 1000'

# pattern = re.compile('>(.*?)<')
# print(pattern.findall(s))
#
# print(pattern.search(s))
#
# print(re.findall('>(.*?)<',s))
#
# print(re.search('>(.*?)<',s))
#
# print(re.sub("(?<=<h1 id='title'>)(.*?)(?=<)", '戊戌变法', s))

# print(re.fullmatch('www.chinahadoop.cn',s))

# print(re.findall('[\d,]+', s))

from lxml import etree
import re

with open('./file/test.html', 'r', encoding='utf8') as f:

    c = f.read()

s = re.sub('\n', '',c)
tree = etree.HTML(s)

ret = tree.xpath('//*[contains(@class,"ref")]')
print(ret[1].text)

# ret = tree.xpath('//p | //h1')
# print(len(ret))
# retor = tree.xpath('//*[self::p or self::h1]')
# print(len(retor))

# ret1 = tree.xpath('/html/body/div/p')
# ret2 = tree.xpath('/html/body/div//p')
#
# print(len(ret1))
# print(len(ret2))
# print(ret1[3].text)
# print(ret2[6].text)
