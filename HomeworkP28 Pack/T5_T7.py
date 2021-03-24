#5
           #又是兔子数列问题，啥语言都跑不过
Test5_Num=[1,1]
Dynamic=1
Test5_Output=[0]*20
while Dynamic<=20:
    Test5_Output[Dynamic-1]=Test5_Num[0]
    Test5_Output[Dynamic]=Test5_Num[1]
    Test5_Num[0] += Test5_Num[1]
    Test5_Num[1] += Test5_Num[0]
    Dynamic+=2
print("这是兔子数列的前20项")
Dynamic=0
while Dynamic<20:                                                             #这一题因为上面用的是两个一组运算
     print(Test5_Output[Dynamic:Dynamic+5])                      #不方便制作5个一组的切片
     Dynamic+=5                                                                  #所以运算完统一输出，效率较低
print("\n")

#6
Dynamic=even=odd=all=0                                   #其实完全可以做到输入一个传走一个
Test6_Num=[0]*10                                                #这里使用列表有记录每个输入的潜在功能
while Dynamic<10:                                                
    Test6_Num[Dynamic]=int(input("请输入第{}个整数".format(Dynamic+1)))       #从简，不做传入非数字判断
    if Test6_Num[Dynamic]%2==0:
        even += Test6_Num[Dynamic]
    else:
        odd += Test6_Num[Dynamic]
    all +=Test6_Num[Dynamic]
    Dynamic +=1                                             #每输入一个数就做一次归类和相关计算
print("您输入的所有数据中，偶数之和是{}".format(even))
print("您输入的所有数据中，奇数之和是{}".format(odd))
print("所有数字的平均值是",all/10)
print("\n")

#7                   #6和#7两题有些区别，就不做合并了（上次USD-CNY转换那个纯属想考分支的）
                       #这题主要是，一开始并不确定输入数字的数量，因此无法合理的给定列表的初始长度
                       #也不方便用字典（虽然可以），所以上一题记录下每个输入的潜在功能就得舍弃
                       #当然也可以用累加字符串记录下每个输入，这里从简。
Dynamic=even=odd=all=INPUT_END=0
Test7_Num=" "
while INPUT_END==0 :
    Test7_Num=input("请输入第{}个整数,如若结束请输入A（不区分大小写）".format(Dynamic+1))
    Test7_Num=Test7_Num.upper()                #用于不区分大小写
    if Test7_Num=="A":
        INPUT_END=1                                       #其实可以直接用break
    elif int(Test7_Num)%2==0:                         #每输入一个数就做一次归类和相关计算
        even += int(Test7_Num)
    else:
        odd += int(Test7_Num)
    Dynamic +=1                                             
all=even+odd
print("您输入的所有数据中，偶数之和是{}".format(even,))
print("您输入的所有数据中，奇数之和是{}".format(odd))
print("所有数字的平均值是",all/(Dynamic-1))
print("\n")

