#10
dic_city={"张三风":["北京","成都"],"李茉绸":["上海","广州","兰州"],"慕容福":["太原","西安","济南","上海"]}
Count=0
namelst=""
for key in dic_city.keys():
    print("{}去过{}个城市".format(key,len(dic_city[key])))              #第一个输出要求
    if "上海" in dic_city[key]: 
        Count+=1                                        #顺便给第二个输出要求计数和列入
        namelst+=(key+"、")
namelst=namelst.rstrip("、")
print("去过上海的有{}人，他们是{}".format(Count,namelst))
