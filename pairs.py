l1=[3,4,-7,1,3,3,1,-4]
k=7

l3=[]
for i in range(len(l1)-1):
    sum=0
    for j in range(i,len(l1)):
        sum+=l1[j]
        if sum==k:
            l2=[]
            for v in range(i,j+1):
                
                l2.append(l1[v])
            l3.append(l2)
print(l3)              

