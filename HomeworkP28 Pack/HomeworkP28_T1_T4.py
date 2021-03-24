#大概看了一下，这一节的程序或多或少都有些麻烦。所以切成多个文件分开完成。

#1
Test1_Num=1
Dynamic=1
while Dynamic<=10:
    Test1_Num *= Dynamic
    Dynamic +=1
print(Test1_Num)
print("\n")

#2
Test2_Num=1
Dynamic=0
while Dynamic<=50:
    Test2_Num+=(2*Dynamic-1)
    Dynamic+=1 
print(Test2_Num)
print("\n")

#3
Dynamic=1
Count=0
while Dynamic<=100:
    if Dynamic%3==0 and Dynamic%5 != 0:
        print(Dynamic,end=" ")
        Count +=1
    if Count ==5:                      #用于一行输出五个数，下一题也可用这个结构。
        print("\n")                               #其实与其让第四题题目里面那种算法的计数器k值累加
        Count=0                         #不如采用循环计数，以避免占用过多内存  
    Dynamic+=1
print("\n")

#4
            #用我上次写的任意年份输出闰年和上一题的一行输出五个数来拼一下
Test4_Year=1000
Count=0
while Test4_Year<=2000:
      if Test4_Year%400==0:
           print(Test4_Year,end=" ")
           Count+=1
      elif Test4_Year%4==0 and Test4_Year%100 != 0:
           print(Test4_Year,end=" ")
           Count+=1
      if Count ==5:                     
        print("\n")                               
        Count=0
      Test4_Year+=1
print("\n")