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
rnd.shuffle(lst)
print(lst)

lstraw=[]
lstraw+=lst
Dynamic=0
while Dynamic<len(lst):
     lst[Dynamic]=lst[Dynamic].replace("J","11")
     lst[Dynamic]=lst[Dynamic].replace("Q","13")
     lst[Dynamic]=lst[Dynamic].replace("K","14")
     lst[Dynamic]=lst[Dynamic].replace("A","15")
     lst[Dynamic]=lst[Dynamic].replace("2","16")
     Dynamic += 1
import commonedit as comet                                  #请注意，这里使用了commonedit，请下载Commonedit Library里面的Commonedit.py文件
Dynamic=0
while Dynamic<len(lst):    
    lst[Dynamic]=comet.sepa(lst[Dynamic],"toga")[1] 
    Dynamic += 1
INPUT=int(input("请输入牌面序号"))
rndint=rnd.randint(0,51)
SysOut=int(lst[rndint])
UsrGus=int(lst[INPUT])
if UsrGus>SysOut: print("您猜的数是{},系统选的是{},您赢了！".format(lstraw(INPUT),lstraw(rndint)))
elif UsrGus==SysOut: print("您猜的数是{},系统选的是{},平局！".format(lstraw(INPUT),lstraw(rndint)))
elif UsrGus<SysOut: print("您猜的数是{},系统选的是{},您输了！".format(lstraw(INPUT),lstraw(rndint)))
else: print("???")
