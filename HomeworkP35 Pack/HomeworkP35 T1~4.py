#1
import random as rnd
lst_who,lst_where,lst_what=["小马","小羊","小鹿"],["草地上","电影院","家里"],["看电影","听故事","吃晚饭"]
Test1_RND1=rnd.randint(0,2)
Test1_RND2=rnd.randint(0,2)
Test1_RND3=rnd.randint(0,2)
print("数字{},{},{}对应生成的句子是:{}{}{}".format(Test1_RND1,Test1_RND2,Test1_RND3,lst_who[Test1_RND1],lst_where[Test1_RND2],lst_what[Test1_RND3]))
print("\n")

#2
           #这一题是输入为罗马数字所以可用列表，其实到后面用字典的话会更好一点
           #而且，因为每个月天数是固定的，因此从效率上说不如用元组
           #从简，不做非数字判断
Test2_Day=[31,28,31,30,31,30,31,31,30,31,30,31]
SEARCH_END=0
while SEARCH_END==0:
      Test2_Search=int(input("请输入欲查询天数的月份数字,输入0结束查询:"))
      if Test2_Search!=0: 
          print("第{}月的天数是{}".format(Test2_Search,Test2_Day[Test2_Search-1]))
      else:
          SEARCH_END=1
print("\n")

#3
           #上一个兔子数列我用的是列表唯二两项反复迭代的方式，这个貌似要求的是
           #不断增加列表长度？这里定义一个外部迭代返回函数
lst_fib=[1,1]
def rabbit(a,b):
    a=a+b
    b=a+b
    return [a,b]
Dynamic=1
while Dynamic<=20:
    lst_fib+=rabbit(lst_fib[Dynamic-1],lst_fib[Dynamic])
    Dynamic+=2
print(lst_fib)
print("\n")

#4
print("本公交由龙江新城市开往莫愁路")
print("中途经停龙江新城市,阳光广场,汉江路,嫩江路,清凉山公园,拉萨路,五台山,莫愁路")
lst_busstop=["龙江新城市","阳光广场","汉江路","嫩江路","清凉山公园","拉萨路","五台山","莫愁路"]
INPUT_END=0
while INPUT_END==0:
    Busstop1=input("请输入第一个要查询的站点：")
    Busstop2=input("请输入第二个要查询的站点：")
    if (Busstop1 not in lst_busstop) or (Busstop2 not in lst_busstop) or Busstop2==Busstop1:
        print("您输入的某个站台未出现在本线路里或者出现重复")
    else:
        INPUT_END=1
BusstopN1=lst_busstop.index(Busstop1)
BusstopN2=lst_busstop.index(Busstop2)
if BusstopN2>BusstopN1:
    print("从{}前往{}需要{}站路".format(Busstop1,Busstop2,BusstopN2-BusstopN1))
else:
    print("您需要乘坐相反方向线路")
print("\n")

