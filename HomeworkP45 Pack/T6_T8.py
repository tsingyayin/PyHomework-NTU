#6
dic_country={"China":"Beijing","America":"Washington","Norway":"Oslo","Japan":"Tokyo","Germany":"Berlin","Canada":"Ottawa","France":"Paris","Thailand":"Bangkok"}
Country=input("请输入需要查询首都的国家名称（不区分大小写）：")
Country=Country[0].upper()+Country[1:].lower()
print(dic_country.get(Country,"未查询到该国家名！"))

#7
member={"John":"123","Marry":"111","Tommy":"123456"}
while 1>0:
    Usrname=input("请输入用户名：")
    Usrpswd=input("请输入密码：")
    if Usrname in member:
        if member[Usrname]==Usrpswd:
            print("登陆成功!")
            break
        else:
            print("密码不正确!")
    else:
        print("用户名不正确")

#8
dic_award={"张富":"10000","赵诺":"15000"}
for i in ["李梅","张富","付研","赵诺","刘江"]:
    if i not in dic_award : dic_award[i]="5000"
award_lst=dic_award.items()
for i in award_lst:
    print(i[0],"的年终奖是",i[1])
