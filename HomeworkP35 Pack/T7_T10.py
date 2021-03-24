#7
Goodman=["甲","乙","丙","丁"]
for UNKNOWN in Goodman:
    if  (UNKNOWN!="甲")+(UNKNOWN=="丙")+(UNKNOWN=="丁")+(UNKNOWN!="丁")==3: 
        print("做好事的是",UNKNOWN)
print("\n")

#8
ls=["A","B","C","D","E"]
import random as rnd
ANS=0
while ANS==0:
    rnd.shuffle(ls)
    if ((ls[1]=="D")+(ls[2]=="B")==1)+((ls[1]=="C")+(ls[3]=="E")==1)+((ls[0]=="E")+(ls[4]=="A")==1)+((ls[2]=="C")+(ls[3]=="A")==1)+((ls[1]=="B")+(ls[4]=="D")==1)==5: break
print(ls)
print("\n")

#9
lst=[""]*10
i=0
while i<10:
    lst[i]=input("请输入第{}名学生的姓名".format(i+1))
    i+=1
print("姓名清单是",lst)

#10
lst=[]
i=0
while i<10:
    lst.insert(0,input("请输入第{}名学生的姓名".format(i+1)))
    i+=1
print("姓名清单是",lst)