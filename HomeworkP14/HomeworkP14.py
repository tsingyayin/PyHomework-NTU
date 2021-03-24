#P14的作业
#这个作业含有一些正常进度下没有学习到的知识点
#1
x=5
y=2
print(x+y,x-y,x*y,x/y,x//y,x%y,x**y,x>y,x==y,x and y,x or y,not x) 
                           #and 返回0或均非0时最后一个，or返回第一个非0
                           #not 布尔取反，非0均假
                           #这是笔记，因为我忘了。。。
print("\n")

#2 
revenue=98765
costs=40000
profit=revenue-costs     #常规减法
print(profit)
print("\n")

#3
       #题目要求的写法
balance=100
balance=balance*1.05
balance=balance*1.05
balance=balance*1.05
print(balance)
       #缩减运算符、多定义对多赋值和while循环写法
balance,i=100,0       
while i<3:
      balance *= 1.05
      i+=1
print(balance)
print("\n")

#4
      #题目要求的写法
score1=float(input("请输入第一个数值"))
score2=float(input("请输入第二个数值"))
score3=float(input("请输入第三个数值"))
Sum=score1+score2+score3                                                             #拒绝sum作为变量名称从我做起
avg=Sum/3
print("总分是",Sum,"平均数是",avg)
      #缩减写法(不甚严谨的使用了列表和列表相关的操作,仅用户前端视觉相同)
score=[float(input("请输入第一个数值")),float(input("请输入第二个数值")),float(input("请输入第三个数值"))]
print("总分是",sum(score),"平均数是",sum(score)/3)      
print("\n")

#5
      #这题真的有什么意义么。。。
print("油耗是",24/(23690-23352),"升每千米")
print("\n")

#6
      #题目要求的写法
Test6_Num=int(input("请输入需要被反序的三位数"))                             #按题目要求就不加入任何超限判断了                                                         
Test6_Num_A=int(Test6_Num/100)
Test6_Num_B=int((Test6_Num-Test6_Num_A*100)/10)
Test6_Num_C=int(Test6_Num-Test6_Num_A*100-Test6_Num_B*10)    #把每一位都处理为个位数，小数用int扔掉
Test6_Num_Output=Test6_Num_C*100+Test6_Num_B*10+Test6_Num_A
print("反序结果是",Test6_Num_Output)
      #最佳写法：利用字符串
      #没有C语言的GOTO写诸葛亮判断是真的要命，必须用while之类的来搞
      #其实对于通用的字符串反序，上面的数学反序才真正需要超限判断
NUM_IN_AREA=0
while NUM_IN_AREA==0:
          Test6_Text=input("请输入需要被反序的三位数")
          if (int(Test6_Text)<100)or(int(Test6_Text)>999):
                    print("你的三位数输入了个寂寞，请重来")
                    NUM_IN_AREA=0
          else:
                    NUM_IN_AREA=1
print("反序结果是",Test6_Text[::-1])
print("\n")

#7
       #不管题目有没有要求，三角形成立合法性判断我还是写一下
NUM_IN_AREA=0
while NUM_IN_AREA==0:
          s_l=[float(input("请输入三角形第一个边的长度")),float(input("请输入第二个边的长度")),float(input("请输入第三个边的长度")),]
          if ((s_l[0]+s_l[1])<=s_l[2])or((s_l[0]+s_l[2])<=s_l[1])or((s_l[2]+s_l[1])<=s_l[0]):
                    print("你的三角形成立了个寂寞，请重来")
                    NUM_IN_AREA=0
          else:
                    NUM_IN_AREA=1
l=sum(s_l)/2
import math as ma
area=ma.sqrt(l*(l-s_l[0])*(l-s_l[1])*(l-s_l[2]))
print("三角形的面积是：",area)
print("\n")


#8
       #先来解答题目中不一样的问题。由于半径是3，所以体积的一个立方被三分之四消成了
       #在数学上与面积公式等价的平方，但是由于计算顺序问题，三分之四毕竟是先算的，就引起了
       #float型末尾四舍五入的取值问题。
R=float(input("请输入球体的半径"))
print("球的面积为",4*ma.pi*R**2,"\n","球的体积为",(4/3)*ma.pi*R**3)
print("\n")

#9
      #我也不知道题目需要哪个算法，总之单式循环365遍和365次方应该都行，循环就不写了。
level_Start=1
level_Final=(level_Start*1.01)**365
print("天天向上是",level_Final)
level_Final=(level_Start*0.99)**365
print("天天向下是",level_Final)
