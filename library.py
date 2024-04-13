a=input()
a=a.split("/")

print(a)
l=[]
for i in a:
    l.append(i)
print("".join(l[::-1]))
