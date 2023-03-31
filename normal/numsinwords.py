l1=['','one','two','three','four','five','six','seven','eight','nine']
l2=['','ten','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
l3=['','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','ninteen']
l=[]
str=""
n=int(input("enter the number:"))
if n>=100 and n<=999:
    r=n//100
    l.append(l1[r])
    l.append('hundred')
    p = n % 100
    if p>10 and p<20:
        q=p%10
        l.append(l3[q])
    elif p<10 and p>0:
        j=p//1
        l.append(l1[j])
    else:
        k=p//10
        l.append(l2[k])
        p=p%10
        l.append(l1[p])
elif n<100 and n>0:
    if n>10 and n<20:
        q=n%10
        l.append(l3[q])
    elif n<10 and n>0:
        j=n//1
        l.append(l1[j])
    else:
        k = n // 10
        l.append(l2[k])
        n = n % 10
        l.append(l1[n])
else:
    k=n//1
    l.append(l1[k])
for i in l:
    str+=i+" "
print(str)
