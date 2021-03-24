#包含正常进度下没学到的知识点
#1 
         #以下是作答算法，只需把原来的错误算法//改为%即可
n=int(input("请输入一个整数："))
if n%3==0 or n%7==0:
    print("Yes")
else:
    print("No")
print("\n")

#2
        #交换数字在C++里面可以在视觉上用指针重指向内存达到
        #我不知道Python能不能这么搞，所以我只能用一个中转变量
a=int(input("请输入第一个整数："))
b=int(input("请输入第二个整数："))
if a-b>0:
    c=a
    a=b
    b=c
print(a,b)
print("\n")

#3
ch=input("请输入一个字符：")
if ch.isdigit()==1:
       print("输入的是数字")
elif ch.isalpha() == 1:
       print("输入的是英文字母")
else:
       print("输入的是其他字符")
print("\n")

#4   
         #原题的区间判断之看上不看下，我按习惯把上下限都加上了
km=float(input("请输入千米数："))
if km <= 0:
    print("千米数输入错误，重新输入")
elif km<=3 and km>0:
    print("您需要支付10元车费！")
elif km>3 and km<=10:
    cost=10+1.2*(km-7)
    print("您需要支付{:.1f}元车费".format(cost))
else:
    cost=13.6+1.5*(km-10)
    print("您需要支付{:.1f}元车费".format(cost))
print("\n")

#5
        #这一题从简，不加整数与数字判断
Test5_Year=int(input("请输入需要查询闰平的年份："))
if Test5_Year%400==0:
    print("您查询的年份{}是闰年".fomat(Test5_Year))
elif Test5_Year%4==0 and Test5_Year%100 != 0:
    print("您查询的年份{}是闰年".fomat(Test5_Year))
else:
    print("您查询的年份{}是平年".fomat(Test5_Year))
print("\n")

#6
Test6_x=float(input("请输入自变量x"))
if Test6_x<0:
    y=0
elif Test6_x<5 and Test6_x>=0:
    y=Test6_x
elif Test6_x<10 and Test6_X>=5:
    y=3*Test6_x-5
elif Test6_x<20 and Test6_x>=10:
    y=0.5*Test6_x-2
else:
    y=0
print("因变量y是",y)
print("\n")

#7
         #上上次作业写过了，直接复制粘贴。
NUM_IN_AREA=0
while NUM_IN_AREA==0:
          s_l=[float(input("请输入三角形第一个边的长度")),float(input("请输入第二个边的长度")),float(input("请输入第三个边的长度")),]
          if ((s_l[0]+s_l[1])<=s_l[2])or((s_l[0]+s_l[2])<=s_l[1])or((s_l[2]+s_l[1])<=s_l[0]):
                    print("输入的三边无法构成三角形")
                    NUM_IN_AREA=0
          else:
                    NUM_IN_AREA=1
l=sum(s_l)/2
import math as ma
area=ma.sqrt(l*(l-s_l[0])*(l-s_l[1])*(l-s_l[2]))
print("三角形的面积是：{}，边长是{}".format(area,s_l))
print("\n")
    
#8
        #从简，不添加非数字判断
        #不过原题好像没要求判断是否在轴上，这真的好么？
Test8_loc=[float(input("请输入横坐标x：")),float(input("请输入纵坐标y："))]
if Test8_loc[0]==0 and Test8_loc==0:
    print("目标点在原点上")
elif Test8_loc[0]==0 and Test8_loc>0:
    print("目标点在y轴的正半轴上")
elif Test8_loc[0]==0 and Test8_loc<0:
    print("目标点在y轴的负半轴上")
elif Test8_loc[0]>0 and Test8_loc==0:
    print("目标点在x轴的正半轴上")
elif Test8_loc[0]<0 and Test8_loc==0:
    print("目标点在x轴的负半轴上")
elif Test8_loc[0]>0 and Test8_loc>0:
    print("目标点在第一象限")
elif Test8_loc[0]<0 and Test8_loc>0:
    print("目标点在第二象限")
elif Test8_loc[0]<0 and Test8_loc<0:
    print("目标点在第三象限")
elif Test8_loc[0]>0 and Test8_loc<0:
    print("目标点在第四象限")
else:
    print("判断出现异常")

#9
             #从简，不添加非数字判断
Score=float(input("请输入百分制分数"))
if Score>=90:
    print("优")
elif Score<90 and Score>=80:
    print("良")
elif Score<80 and Score>=70:
    print("中")
elif Score<70 and Score>=60:
    print("及格")
else:
    print("不及格")
