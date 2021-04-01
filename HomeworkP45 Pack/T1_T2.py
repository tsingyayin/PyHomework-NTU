
#1
P1_dic={"A":"·-","B":"-···","C":"-·-·","D":"-··","E":"·","F":"··-·","G":"--·","H":"····","I":"··","J":"·---","K":"-·-","L":"·-··","M":"--","N":"-·","O":"---","P":"·--·","Q":"--·-","R":"·-·","S":"···","T":"-","U":"··-","V":"···-","W":"·--","X":"-··-","Y":"-·--","Z":"--··"}
UsrINPUT=input("请输入英文字符串：")
UsrINPUT=UsrINPUT.upper()
UseINPUT_Len=len(UsrINPUT)
Dynamic=0
print("您的输入对应的摩斯电码是：")
while Dynamic<UseINPUT_Len :
    print(P1_dic[UsrINPUT[Dynamic]],end="")
    Dynamic +=1
print("\n")

#2
dic_student={}
Dynamic=0
while Dynamic<5:
    StuName=input("请输入第{}个学生的姓名".format(Dynamic+1))
    StuAge=input("请输入第{}个学生的年龄".format(Dynamic+1))
    dic_student[StuName]=StuAge
    Dynamic+=1
for a,b in dic_student.items():
    print("{: <10}{}".format(a,b))


