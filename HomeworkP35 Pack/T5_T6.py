#5
lst_student=["001","李梅",19,"002","刘祥",20,"003","张武",18]
lst_student+=["004","刘宁",20]                #第一个题目要求
lst_student+=["006","梁峰",19]
ADD=["005","林歌",20]
Dynamic=1
while Dynamic<=3:                              #第二个题目要求
    lst_student.insert(Dynamic+11,ADD[Dynamic-1])
    Dynamic+=1
print("003号学生的相关信息是",lst_student[lst_student.index("003"):lst_student.index("003")+3])
print("所有学生的姓名是：",lst_student[1::3])                              #后面三个题目要求
print("平均年龄是{:.2f}岁（已经保留两位小数）".format(sum(lst_student[2::3])/int(lst_student[-3])))

#6
lst_student=[["001","李梅",19],["002","刘祥",20],["003","张武",18]]
lst_student+=[["004","刘宁",20]]
lst_student+=[["006","梁峰",19]]
lst_student.insert(-1,["005","林歌",20])
print("003号学生的相关信息是",lst_student[2])
Dynamic=0
namelist=[]
while Dynamic<len(lst_student):
     namelist+=[lst_student[Dynamic][1]]
     Dynamic+=1
print("所有学生的姓名是",namelist)
Dynamic=0
namelist=[]
while Dynamic<len(lst_student):
    if lst_student[Dynamic][2]>19: namelist+=[lst_student[Dynamic][1]]
    Dynamic +=1
print("大于19岁的学生是",namelist)
