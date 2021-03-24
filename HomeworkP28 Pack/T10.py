#10
import random as rnd
Test10_Num=rnd.randint(0,9)
GUESS_END=0
Count=0
while GUESS_END==0:
    Test10_Guess=int(input("请猜这个数（0~9含端点）"))
    if Test10_Guess<Test10_Num:
        print("你猜小了")
        Count +=1
    elif Test10_Guess>Test10_Num:
        print("你猜大了")
        Count +=1
    else:
        print("你成功猜到了这个数{}，你一共猜了{}次".format(Test10_Num,Count+1))
        GUESS_END=1
print("\n")

#11
                 #又是任何语言都跑不掉的欧几里得辗转相除法
RND1=rnd.randint(0,100)
RND2=rnd.randint(0,100)
print("随机出的两个数是{}和{}".format(RND1,RND2))
Dividend=Divisor=Remainder=1
Dividend=RND1
Divisor=RND2
while Remainder!=0:
    Remainder=Dividend%Divisor
    Dividend=Divisor
    Divisor=Remainder
print("他们的最大公约数是{}".format(Dividend))
print("他们的最小公倍数是{:.0f}".format(RND1*RND2/Dividend))
print("\n")

#12   
               #这几个题是和随机数杠上了吗？
Test12_RND=rnd.randint(100,100000)
print("随机的抛硬币次数是{}次".format(Test12_RND))
Dynamic=Coin_U=Coin_D=0
while Dynamic<Test12_RND:
    Coin=rnd.randint(0,1)
    if Coin==0:
        Coin_U+=1
    else:
        Coin_D+=1
    Dynamic+=1
print("模拟抛掷中，正面出现了{}次，反面出现了{}次".format(Coin_U,Coin_D))
print("\n")

#13
             #可能有什么数论知识或者固定算法可以快速解决这个问题
             #但是我并不知道，所以我只能穷举
             #穷举的想法很简单，从1开始，一直枚举到所有条件都符合为止
Dynamic=0              #这个动态计数没有意义，因为直接用break退出
Test13_Ans=1
while Dynamic==0:
    if Test13_Ans%2==1 and Test13_Ans%3==0 and Test13_Ans%4==1 and (Test13_Ans+1)%5==0 and Test13_Ans%6==3 and Test13_Ans%7==0 and Test13_Ans%8==1 and Test13_Ans%9==0:
        break
    Test13_Ans+=1
print("糖果的个数是",Test13_Ans)
print("\n")