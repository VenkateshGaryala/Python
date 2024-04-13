def check(c):
    return c.isalpha()

s=list(input())
print(s)
opening=[]
for i in range(len(s)):
    if s[i]=='/':
        opening+= [i]
    elif s[i]=='\\':
        s[opening[-1]:i+1]=reversed(s[opening[-1]:i+1])
        opening.pop()
        print(s)


print("".join(filter(check, s)))
# lambda c: c!='\\' and c!='/'
