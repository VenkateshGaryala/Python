a=4

b=[1,2,3,4]
A=b
B=b[::-1]
l=[]
i=0
for _ in range(len(A)):
    if len(A)!=0 and len(B)!=0:
        if A[i]>B[i]:
            l.append(1)
            B.pop(i)
        elif A[i]<B[i]:
            l.append(2)
            A.pop(i)
        else:
            l.append(0)
            A.pop(i)
            B.pop(i)
print(l)
print(A)
print(B)
