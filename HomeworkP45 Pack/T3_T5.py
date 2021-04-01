import sys
sys.path.append(r"C:\Users\Administrator\source\repos\Commonedit\Commonedit")
import commonedit as comet

#3
myDict={"方糖":99,"X1":499,"魔盒":399,"曲奇":299}
for a,b in myDict.items():
    print(a,"\t…………\t",b)
print("商品的总价是",sum(myDict.values()))
myDict_E=[(a,b) for b,a in myDict.items()]
myDict_E.sort(reverse = 1)
print("价格最高的商品名称是",myDict_E[0][1])

#4
dic_student={}
Dynamic=0
while Dynamic<5:
    Name=input("请输入第{}名学生的姓名：".format(Dynamic+1))
    Age=input("请输入第{}名学生的年龄：".format(Dynamic+1))
    Length=input("请输入第{}名学生的身高：".format(Dynamic+1))
    weight=input("请输入第{}名学生的体重：".format(Dynamic+1))
    dic_student[Name]=[Age,Length,weight]
    Dynamic += 1
for a,b in dic_student.items():
    print(a,"\t",b[0],"\t",b[1],"\t",b[2])

#5
dic_student={}
Dynamic=0
while Dynamic<5:
    Class=input("请输入第{}名学生的班级：".format(Dynamic+1))
    Name=input("请输入第{}名学生的姓名：".format(Dynamic+1))
    Age=input("请输入第{}名学生的年龄：".format(Dynamic+1))
    Length=input("请输入第{}名学生的身高：".format(Dynamic+1))
    weight=input("请输入第{}名学生的体重：".format(Dynamic+1))
    dic_student[(Class,Name)]=[Age,Length,weight]
    Dynamic += 1
for a,b in dic_student.items():
    print(a[0],'\t',a[1],"\t",b[0],"\t",b[1],"\t",b[2])