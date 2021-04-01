USRIPT=input("请输入一段英文字符").lower()
IPTCOUNT={}
for alpha in USRIPT:
    if alpha.isalpha()==1:
        if alpha in IPTCOUNT.keys() : IPTCOUNT[alpha]+=1
        else : IPTCOUNT[alpha]=1
print(IPTCOUNT)
