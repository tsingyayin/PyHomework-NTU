#12
dic_class={"托班":["聪聪班","伶伶班","楠楠班"],"小班":["小一班","小二班"],"中班":["中一班","中二班"],"大班":["大一班","大二班"]}
dic_number={"聪聪班":26,"伶伶班":23,"楠楠班":25,"小一班":32,"小二班":31,"中一班":33,"中二班":34,"大一班":32,"大二班":33}
dic_people={}
for cls in dic_class.keys():                    #这个循环的目的是，用number的key匹配class的value
    dic_people[cls]=0                           #如果匹配，就把number的key对应的value累加配给class的value对应的key
    for name in dic_number.keys():       #在每一次获取class的key后，准备匹配number的value前要先把统计用字典
        if name in dic_class[cls]:              #对应key的value初始化为0，否则无法正确执行dic_people[cls]+=dic_number[name]
            dic_people[cls]+=dic_number[name]         
for a,b in dic_people.items():
    print("{}:{}人".format(a,b))
print("全园:{}人".format(sum(dic_people.values())))