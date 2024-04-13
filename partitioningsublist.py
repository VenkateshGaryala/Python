a=list(map(int,input().split()))
for i in range(len(a)):
    if sum(a[0:i])==sum(a[i:]):
        print(a[0:i],a[i:])