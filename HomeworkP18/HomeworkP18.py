#这个作业包含一些正常进度下还没学到的知识点
#1
          #以前C++用string做int和char的中转的时候，常常因为一个string的操作方法
          #（习惯上这个方法的变量被命名做ss或s1）不能自动重置内存位（因为实际上是指针）
          #把人给坑死，自那之后对s1有心理阴影。
s1="我喜欢"
s2="Python"
print(s1+s2,s1*2,3*s2,"我" in s1,s1[0],s1[0:-1],s1[0:],s2[-3:-1],s1[::-1],s2[::2],s2[1::2],s1>s2,len(s1),len(s2))
                             #↑print(s1*s2) 它原来在这里，能执行就出了鬼了。
print("\n")

#2
Test2_Text="www.moe.gov.cn"
print("(1)",Test2_Text[0],"(2)",Test2_Text[0:3],"(3)",Test2_Text[-3:],"(4)",len(Test2_Text))   #前四个输出要求
print("(5)",Test2_Text.index('o'),"(6)",Test2_Text.count('o'))                                             #第五、第六个要求
Test2_Text=Test2_Text.replace(".","-")
print("(7)",Test2_Text)                                                                                                  #第七个输出要求   
Test2_Text=Test2_Text.upper()
print("(8)",Test2_Text)                                                                                                   #第八个输出要求
print("(9)",Test2_Text.split('-'))                                                                                      #第九个输出要求
Test2_Text=Test2_Text.replace("-","")                                               #其实偷了个懒，先输出再去字符简单一些
print("这字符串最终变成了",Test2_Text)
print("\n")

#3
          #还是用列表，扩展到10以内任意人数
INPUT_END=0
while INPUT_END==0:
         number=int(input("请输入宿舍人数（十个人以内）："))
         if number<1 or number>10:
                  print("这个数字似乎不合要求")
                  INPUT_END=0
         else:
                  INPUT_END=1
Dynamic=0
Name=[" "]*number                               #定义列表长度这玩意我一开始忘了，最开始这个地方用的是字典
while Dynamic<=number-1:
          Name[Dynamic]=input("请输入第{}个人的姓名：".format(Dynamic+1))          
          Dynamic += 1
Dynamic=0
FULL=""
           #必须预先定义空字符串
while Dynamic<=number-1:
          FULL += Name[Dynamic][-1]
          Dynamic += 1
print("建议宿舍取名为：",FULL)
print("\n")

#4
Test4_Text="JanFebMarAprMayJunJulAugSepOctNovDec"
INPUT_END=0
while INPUT_END==0:
         Search=int(input("请用罗马数字输入欲查询缩写的月份数："))
         if Search<1 or Search>12:
                  print("这好像不是一个合理的月份数值，请重新输入")
                  INPUT_END=0
         else:
                  INPUT_END=1
print("您想查询的第",Search,"月的英文缩写是",Test4_Text[(Search-1)*3:(Search-1)*3+3])
print("\n")

#5,6,7  →这三个直接做第七个
             #题目要求的做法
INPUT_END=0
while INPUT_END==0:
         Money_Text=input("可以转换人民币￥与美元$，用相应符号做结尾以进行转换")
         if Money_Text[-1]=='￥' or Money_Text[-1]== '$':
                   INPUT_END=1
         else:
                   print("您没有以系统给定的符号做结尾，请重新输入")
                   INPUT_END=0 
Money=float(Money_Text[0:-1])
if Money_Text[-1]=="￥":
         print("人民币",Money,"￥   对应的美元是",round(Money*0.1456,2),"$")
else:
         print("美元",Money,"$   对应的人民币是",round(Money*6.868,2),"￥")
print("\n")
            #方便用户的方法：因为￥$并不容易很快的用键盘输入（虽然shift+4也不慢），
            #因此最好用国际通用三字母缩写
INPUT_END=0
while INPUT_END==0:
         Money_Text=input("可以转换人民币CNY与美元USD，用相应的缩写做结尾以进行转换，不区分大小写")
         Money_Text=Money_Text.upper()                    #用于不区分大小写
         if Money_Text[-3:]=="CNY" or Money_Text[-3:]=="USD":
                   INPUT_END=1
         else:
                   print("您没有以系统给定的符号做结尾，请重新输入")
                   INPUT_END=0
Money=float(Money_Text[0:-3])
if Money_Text[-3:]=="CNY":
         print("人民币",Money,"￥   对应的美元是",round(Money*0.1456,2),"$")
else:
         print("美元",Money,"$   对应的人民币是",round(Money*6.868,2),"￥")
print("\n")
