#20
lst_suit=["黑桃","红桃","梅花","方块"]
lst_face=["3","4","5","6","7","8","9","10","J","Q","K","A","2"]
Dynamic1=0
lst=[]
while Dynamic1<len(lst_suit):
    Dynamic2=0
    while Dynamic2<len(lst_face):
        lst+=[(lst_face[Dynamic2]+lst_suit[Dynamic1])]
        Dynamic2+=1
    Dynamic1+=1

import random as rnd
lstrnd=[]
lstrnd+=lst
rnd.shuffle(lstrnd)
print(lstrnd)

import commonedit as comet                           #请注意这里用了Commonedit，请到Commonedit Library下载Commonedit.py
#这是经同学点拨之后我重新想的一个算法
#首先让系统自己随机一个数字
SysOut=str(lstrnd[rnd.randint(0,51)])                     #把系统牌抽出来
UsrOut=str(lstrnd[int(comet.inrange(0,51,"T","T"))])      #把用户牌抽出来 
SysRAW=lst.index(SysOut)#查询两张牌在原始列表的位置
UsrRAW=lst.index(UsrOut)#既然不看花色，那么只需看每张牌在每个花色组里面的位置即可，即除以四取余                         
if (SysRAW%13)>(UsrRAW%13) : print("系统牌是{}，您的牌是{}，您输了！".format(SysOut,UsrOut))
if (SysRAW%13)==(UsrRAW%13) : print("系统牌是{}，您的牌是{}，平局！".format(SysOut,UsrOut))
if (SysRAW%13)<(UsrRAW%13) : print("系统牌是{}，您的牌是{}，您赢了！".format(SysOut,UsrOut))
