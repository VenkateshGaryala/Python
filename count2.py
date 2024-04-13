l=[1,2,3,4,1,5,6,3,7,8]
a=int(input())
i = 0

while i < len(l):
    if l[i]==a:
        if i==0:
            l[i]=0
            l[i + 1]=0
            
             
            print(l)
            
        elif i == (len(l) - 1):
            l[i- 1]=0
            l[i]=0
            
            
            print(l)
            
        else:
            l[i-1]=0 
            l[i]=0
            l[i + 1]=0
            print(l)
            
    
    i += 1
print(sum(l))
        
   


