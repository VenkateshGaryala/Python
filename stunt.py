venky=[2,5,3,7,1,8]
l2=[]
for i in range(len(venky)):
    for j in range(i-1,-1,-1):
        if(venky[j]<venky[i]):
            l2.append(venky[j])
            break
        
            
    else:
        l2.append(-1)
print(l2)  
    


'''venky=list(map(int,input().split()))
for i in range(len(venky)):
    prev=-1
    for j in range(i-1,-1,-1):
        if(venky[j]<venky[i]):
            prev=venky[j]
            break
    print(prev,end=' ')'''
    
   