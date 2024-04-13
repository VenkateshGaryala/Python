venky=[2,5,3,7,1,8]
l2=[]
for i in range(len(venky)):
    for j in range(i+1,len(venky)):
        if(venky[j]>venky[i]):
            l2.append(venky[j])
            break
        
            
    else:
        l2.append(-1)
print(l2)  
    
