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
def is_prime(num):
    if num<2:
        return False
    else:
        for i in range(2,int(num/2)+1):
            if num%i==0:
                return False
        return True
m=int(input("enter the num:"))
if m<3 or m>5:
    print("invalid")
else:
    groups=[l1[i:i + m]for i in range(0,len(l1))]
    print("groups of",m,"values:")
    for group in groups:
        count = 0
        for j in group:
            if is_prime(j):
                count+=1
        if count>=2:
            print(group)
max_seq=[]
seq=[]
for num in l1:
    if is_prime(num):
        seq=[]
    elif not seq:
        seq.append(num)
    elif num==seq[-1]+1:
        seq.append(num)
        if len(seq)>len(max_seq):
            max_seq=seq
        else:
            seq=[num]
print(max_seq)