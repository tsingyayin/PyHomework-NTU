#13
INPUT=input("请输入字符串")
Dynamic=0
OUTPUT=[]
INPUT=INPUT.upper()
INPUT=INPUT.replace(" ","")
INPUT_L=len(INPUT)
while Dynamic<INPUT_L:
    INSERT=INPUT[Dynamic]
    OUTPUT_L=len(OUTPUT)
    Dynamic_2=Count=0
    while Dynamic_2<OUTPUT_L:
        if INSERT==OUTPUT[Dynamic_2]: Count+=1
        Dynamic_2+=1
    if Count==0: OUTPUT.append(INSERT)
    Dynamic+=1
OUTPUT.sort()
print(OUTPUT)
print("\n")

#14   
import random as rnd
lst1=[0]*20
i=0
while i<20:
    lst1[i]=rnd.randint(10,99)
    i += 1
print("生成的列表是",lst1)
lst2=lst1[0:10]
lst2.sort()
lst3=lst1[10:20]
lst3.sort(reverse = 1)
print("前十个的升序是{}，后十个的降序是{}".format(lst2,lst3))

#15
char=input("请输入字符串")
char_l=len(char)
char_lst=char.split()
print("字符串的逆序是",char_lst[::-1])

#16
lst_floor=[1,4,2,5,7,3]
lst_l=len(lst_floor)
Dynamic=0
while Dynamic<lst_l-1:
    floor=int(lst_floor[Dynamic+1])-int(lst_floor[Dynamic])
    if floor>0:
        print("↑"*floor,end="")
    if floor<0:
        print("↓"*(-floor),end="")
    Dynamic +=1
print("\n")

#16_2
lst_run="↑↑↓↓↓↑↑↓↑↑↑↑"
lst_l=len(lst_run)
Dynamic=0
lst_floor=[2]
while Dynamic<lst_l:
    if lst_run[Dynamic]=="↑":
        lst_floor+=[lst_floor[Dynamic]+1]
    else:
        lst_floor+=[lst_floor[Dynamic]-1]
    Dynamic+=1
print(lst_floor)