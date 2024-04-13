n=int(input())
var=n
a=[i for i in range(1,n+1)]

j=n-1
k=0
while var!=0:
    b=a[:k+1]
    s=j*' '+' '.join(map(str,b))
    print(s)
    k+=1
    j-=1
    var-=1
