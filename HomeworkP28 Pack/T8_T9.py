#8                   
              #说实话这个range我不是很清楚想让我怎么用
for Test8_Num in range(1,100,2):
    Test8_Sum=Test8_Num*(Test8_Num+1)*(Test8_Num+2)
print(Test8_Sum)
print("\n")

#9
INPUT_END=0
while INPUT_END==0:
     a=input("请输入一个数字a的值")
     n=int(input("请输入正整数n的值"))
     if int(a)<0 or int(a)>9 or n<0:
           print("您输入的某一项有误，请重新输入")
           INPUT_END=0
     else:
           INPUT_END=1
Dynamic=Test9_Sum=0
while Dynamic<n:
      Test9_Sum+=int(a*(Dynamic+1))
      Dynamic+=1
print("数列s=a+aa+aaa+……+aaa__n个___aaa的值是",Test9_Sum)

      #本来以为这两题很多，还单独切一个文件，写完发现没有多少