#21
lst_score=[9,10,8,9,10,7,6,8,7,8]
lst_score.sort()
del(lst_score[0])
del(lst_score[-1])
print(sum(lst_score[::1])/8)

#22
