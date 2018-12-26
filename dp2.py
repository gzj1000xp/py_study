import re
string1 = '{class:shared track, id:12004, index:635, name:"双截棍", persistent ID:"D35E1C608975BF66", database ID:6455, date added:date "2016年9月5日 星期一 下午7:34:32", time:"3:21", duration:201.013000488281, artist:"周杰伦", album artist:"周杰伦", composer:"", album:"范特西", genre:"其他", bit rate:256, sample rate:44100, track count:0, track number:9, disc count:0, disc number:1, size:8078921, volume adjustment:0, year:0, comment:"磨坊高品质音乐-MOOFEEL.COM", EQ:"", kind:"互联网音频流", media kind:song, video kind:none, modification date:date "2010年12月26日 星期日 下午5:31:26", enabled:true, start:0.0, finish:201.013000488281, played count:1, played date:date "2016年10月18日 星期二 上午8:59:26", skipped count:0, compilation:false, rating:0, bpm:0, grouping:"", bookmarkable:false, bookmark:0.0, shufflable:true, lyrics:"", category:"", description:"", show:"", season number:0, episode ID:"", episode number:0, unplayed:false, sort name:"", sort album:"", sort artist:"", sort composer:"", sort album artist:"", sort show:"", loved:false, disliked:false, album loved:false, album disliked:false, cloud status:matched, work:"", movement:"", movement number:0, movement count:0}'
string2 = ['{class:shared track, id:11935, index:557, name:"礼物", persistent ID:"61BB79DF321AF7F3", '
           'database ID:7591, date added:date "2009年12月18日 星期五 下午3:17:24", time:"5:23", duration:323.290985107422, '
           'artist:"许巍", album artist:"许巍", composer:"", albnre:"", bit rate:256, sample rate:44100, track count:10, '
           'track number:6, disc count:1, disc number:1, size:10674812, volume adjustment:0, year:2004, comment:"", EQ:"", '
           'kind:"AAC 音频文件", media kind:song, video kind:none, modification date:date "2013年11月5日 星期:48", enabled:true, '
           'start:0.0, finish:323.290985107422, played count:0, skipped count:0, compilation:false, rating:0, bpm:0, grouping:"", '
           'bookmarkable:false, bookmark:0.0, shufflable:true, lyrics:"", category:"", description:"", show:"", season number:0, '
           'episode ID:"", episode number:0, unplayed:false, sort name:"", sort album:"", sort artist:"", sort composer:"", '
           'sort album artist:"", sort show:"", loved:false, disliked:false, album loved:false, album disliked:false, cloud status:matched, '
           'work:"", movement:"", movement number:0, movement count:0}\n']

string3 = ['{class:shared track, id:12284, index:994, name:"Animal Instinct", persistent ID:"FF97496BDBE073F5", database ID:7445, date added:date "2017年7月15日 星期六 下午12:45:10", time:"3:31", duration:211.932998657227, artist:"The Cranberries", album artist:"The Cranberomposer:"", album:"Stars The Best of 1992-2002", genre:"", bit rate:256, sample rate:44100, track count:20, track number:12, disc count:0, disc number:0, size:9576473, volume adjustment:0, year:0, comment:"", EQ:"", kind:"AAC 音频文件", media kind:song, video kinde, modification date:date "2014年9月27日 星期六 上午11:24:10", enabled:true, start:0.0, finish:211.932998657227, played count:0, skipped count:0, compilation:false, rating:0, bpm:0, grouping:"", bookmarkable:false, bookmark:0.0, shufflable:true, lyrics:"", categorscription:"", show:"", season number:0, episode ID:"", episode number:0, unplayed:true, sort name:"", sort album:"", sort artist:"Cranberries", sort composer:"", sort album artist:"Cranberries", sort show:"", loved:false, disliked:false, album loved:false, album disliked:false, cloud status:matched, work:"", movement:"", movement number:0, movement count:0}\n']


#   去除大括号,以逗号为分隔符分割字符串
def remove_braces(inputstr):
    string_list = inputstr.split(',')
    slist = []
    for s in string_list:
        #print(s)
        if '}' in s:
            s = re.sub('}', '', s)
        elif '{' in s:
            s = re.sub('{', '', s)
        else:
            pass
        if s.find(':') == -1:
            s = s + ':'
        else:
            pass

        slist.append(s)
    while '' in slist:
        slist.remove('')
#    print(slist)
    return slist


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
#        print(s1)
        sdic[s1[0]] = s1[1]
#    print(sdic)
    return sdic


def dp(inputlist):
    a = remove_braces(inputlist)
    d = remove_quota(a)
    e = turn_into_dic(d)
    return e

#print(string3.__len__())
a = remove_braces(string3[0])
#print(a)

d = remove_quota(a)
#print(d)
#print(d.__len__())
for b1 in d:
    print(b1)


e = turn_into_dic(d)


print(e)