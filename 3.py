a=["Ganges","Godavari"]

count=0
for i in range(0,len(a)):
    for j in a[i]:
        #print(ord(j))
        count+=ord(j)
    #sums.append(count)
    a[i]=count
    count = 0
        
print(a)
#print(sums)
