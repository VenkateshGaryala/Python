a=[1,2,3,4,90,84,3,4,7,8,9]
l=[]
count=1
for i in range(0,len(a)-1):
    if a[i]==(a[i+1]-1):
        count+=1
    else:
        l.append(count)
        count=1
l.append(count)
print(l)
