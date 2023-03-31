# n=[1,2,3,4]
# str_num=''.join(str(i) for i in n)
# l=int(str_num)
# print(l,type(l))
result=1
l1=[]
l1.append(result)
for i in range(1,100):
    j = 3
    res = i * j
    result+=i
    l1.append(res)
    l1.append(result)
print(l1)


