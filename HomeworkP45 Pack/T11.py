#11
dic_score={"徐丽":[88,90,98,95],"张兴":[85,92,95,98],"刘宁":[89,89,90,92],"张旭":[82,86,89,90]}
for key in dic_score.keys():
    dic_score[key]+=[sum(dic_score[key])/len(dic_score[key])]
print(dic_score)
print("姓名","\t","语文","\t","数学","\t","英语","\t","计算机","\t","平均分")
for key in dic_score.keys():
    print(key,"\t",dic_score[key][0],"\t",dic_score[key][1],"\t",dic_score[key][2],"\t",dic_score[key][3],"\t",dic_score[key][4])