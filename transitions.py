Y=int(input())
while Y!=0:
    s=input()
    s=s+s[0]
    transitions=0
    for i in range(0,len(s)-1):
        if s[i]!=s[i+1]:
            transitions+=1
    print(transitions)
    if transitions>2:
        print('non uniform')
    else:
        print("uniform")
    Y-=1