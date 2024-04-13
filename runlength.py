st="aaabbbacccdeff"
v=""
count=1
for i in range(len(st)-1):
    if st[i]==st[i+1]:
        count+=1
    else:
        #print(count,str[i],end=" ")
        v+=str(count)+st[i]
        count=1
#print(count,str[i],end=" ")
v+=str(count)+st[i+1]
print(v)


