#12
lst_info=[["李玉","男",25],["金忠","男",23],["刘研","女",21],["莫心","女",24],["沈冲","男",28]]
Public_INPUT="1"
while Public_INPUT != 0:
    Public_INPUT=input("请输入需要被删除的员工姓名:")
    lst_l=len(lst_info)
    if Public_INPUT=="0":
        print("程序已退出")
        break
    Dynamic=0
    while Dynamic<=lst_l:
        if Dynamic == lst_l:
            print("没有找到这个员工信息，请重新输入!")
            break
        if Public_INPUT==lst_info[Dynamic][0]:
            del lst_info[Dynamic]
            print("已经成功删除！现在的名单是",lst_info)
            break
        Dynamic+=1
    
#13
lst_odd=[1,3,5,7,9]
lst_even=[2,4,6,8,10]
lst_num=lst_odd+lst_even
lst_num.sort(reverse=1)
print(lst_num)


