# s=input()
# l=list(s)
# i=0
# while True:
#     if i==len(l)-1 or len(l)==0:
#         break
#     if l[i]==l[i+1]:
#         l.pop(i)
#         l.pop(i)
#         i=0
#     else:
#         i+=1
# if len(l)==0:
#     print('empty')
# else:
#     new_s=''.join(l)
#     print(new_s)


#another logic
a=input()
while ('00' in a) or ('11' in a):
    a=a.replace('00','')
    a=a.replace('11','')
print(a)