'''l1=list(map(int,input().split()))
l2=sorted(l1)
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i]==l2[j]:
            print(j+1)'''

l1=list(map(int,input().split()))
l2=sorted(l1[:])
l3=list(reversed(l2))
print(l3)