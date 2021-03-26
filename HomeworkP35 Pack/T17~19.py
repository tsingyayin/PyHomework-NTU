#17
lst_sides=[3,4,5,6,6,6,4,4,3]
i=0
import math as ma
while i<len(lst_sides):
      lst_single=lst_sides[i:i+3]
      p=0.5*(lst_single[0]+lst_single[1]+lst_single[2])
      a=lst_single[0]
      b=lst_single[1]
      c=lst_single[2]
      s=ma.sqrt(p*(p-a)*(p-b)*(p-c))
      print("{}这一组边长对应的面积是{:.2f}（已经保留两位小数）".format(lst_single,s))
      i += 3
print("\n")

#18
s="语文：80，数学：82，英语：90，物理：85，化学：88，美术：80"
char=[]
char=s.split("，")
i=0
num_sum=0
num=[]
while i < len(char):
    num+=[char[i][-2::]]
    num_sum+=int(num[i])
    i += 1
print("总分是{}，平均分是{:.2f}".format(num_sum,num_sum/len(num)))
print("\n")

#19
lst=[("triangle","shape"),("red","color"),("square","shape"),("yellow","color"),("green","color"),("circle","shape")]
Dynamic=0
while Dynamic<len(lst):
    if lst[Dynamic][1]=="shape" : print(lst[Dynamic],end=" ")
    Dynamic += 1
Dynamic=0
lst_color=[]
print("\n")
while Dynamic<len(lst):
    if lst[Dynamic][1]=="color" : 
        print(lst[Dynamic],end=" ")
        lst_color+=[lst[Dynamic]]
    Dynamic += 1
print("\n")
print(lst_color)

