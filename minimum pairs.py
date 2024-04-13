t=int(input())
for i in range(t):
    N=int(input())
    l=list(map(int,input().split()))
    l.sort()
    v=[]
    c=1
    for j in range(len(l)-1):
        if l[j]==l[j+1]:
            c+=1
        else:
            v.append(c)
            c=1
        v.append(c)
        print(v)
    print(N-max(v))       