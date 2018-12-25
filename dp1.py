import re
string1 = '{{"设备"}, {"Bluetooth Mouse M557", "已连接"}, {"Jason\'s QC35", "未连接"}, {"“Jason”的 Powerbeats³", "未连接"}}'


#   去除大括号
def remove_braces(inputstr):
    string_list = inputstr.split('{')
    slist = []
    for s in string_list:
        if '}' in s:
            s = re.sub('}', '', s, 1000)

        slist.append(s)
    while '' in slist:
        slist.remove('')
#    print(slist)
    return slist


#   去除多余的词汇如'设备'
def remove_words(inputlist):
    slist = []
    for s in inputlist:
        if '设备' in s:
            pass
        else:
            slist.append(s)
#    print(slist)
    return slist


#   将字典中同一项里的逗号连接换乘冒号连接
def remove_comma(inputlist):
    slist = []
    for s in inputlist:
        if ',' in s:
            s = re.sub(', ', '', s, 1000)
        slist.append(s)
    slist2 = []
    for s in slist:
        s = re.sub('\"\"', '\":\"', s, 1000)
        slist2.append(s)
#    print(slist2)
    return slist2


#   去除多余的双引号
def remove_quota(inputlist):
    slist = []
    for s in inputlist:
        if '"' in s:
            s = re.sub('\"', '', s, 1000)
        slist.append(s)
#    print(slist)
    return slist


#   得到经典干净的字典
def turn_into_dic(inputlist):
    sdic = {}
    for s in inputlist:
        s1 = []
        s1 = s.split(':')
        sdic[s1[0]] = s1[1]
#    print(sdic)
    return sdic


def dp(inputlist):
    a = remove_braces(inputlist)
    b = remove_words(a)
    c = remove_comma(b)
    d = remove_quota(c)
    e = turn_into_dic(d)
    return e


a = remove_braces(string1)
b = remove_words(a)
c = remove_comma(b)
d = remove_quota(c)
e = turn_into_dic(d)

#print(e['Bluetooth Mouse M557'])

print(dp(string1))