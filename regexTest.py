import re

s = "www.chinahadoop.cn"

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

print(re.fullmatch('www.chinahadoop.cn',s))