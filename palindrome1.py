# n=int(input())
# for i in range(n,n+100):
#     if str(i)==str(i)[::-1]:
#         print(i)
#         break
n=int(input())
a=True
i=0
v=[]
l=[]
#venkatesh

while a:
    n+=1
    if str(n)==str(n)[::-1]:
        l.append(n)
        if len(l)==30:
            a=False        
print(l)
# for b in range(2,):
#     if l[i]%b==0:
#         count+=1
#         i+=1
#         if i==len(l):
#             break

for i in l:
    count = 0
    for b in range(2, i+1):
        if i%b == 0:
            count += 1
    if count == 1:
        v.append(i)
# if count==1:
#     v.append(b)
print(v)


