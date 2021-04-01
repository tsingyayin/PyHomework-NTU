#9
lst_busstop=["龙江新城市","阳光广场","汉江路","嫩江路"]
dic_estate={"龙江新城市":["白云园","腾飞园"],"阳光广场":["龙江小区","芳草园"],"汉江路":["金信花园","龙凤花园"],"嫩江路":["西城蓝湾","花开四季"]}
dic_estate_e=dict([(a[0],b) for b,a in dic_estate.items()]+[(a[1],b) for b,a in dic_estate.items()])
Garden1,Garden2=input("请输入要查询起点的小区："),input("请输入要查询终点的小区：")
BusstopN1,BusstopN2=lst_busstop.index(dic_estate_e[Garden1]),lst_busstop.index(dic_estate_e[Garden2])
if BusstopN2>BusstopN1:
   print("起始站：{}站,终点站：{}站,共{}站路".format(dic_estate_e[Garden1],dic_estate_e[Garden2],BusstopN2-BusstopN1))
else:
   print("您需要乘坐相反方向线路")
print("\n")

#这个程序前半部分旨在先把字典倒过来，然后把每两个小区对应一个站台
#拆分为一个小区对应一个站台，然后直接把小区当做键要求返回公交站台值
#到这一步，处理对象已经变成了公交站台，所以
#后面的部分与在第六章作业里面遇到的公交站台题目一样。
