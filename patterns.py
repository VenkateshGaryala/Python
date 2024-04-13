n=int(input())
arr=[]
for _ in range(n):
    a,b=map(int,input().split())
    arr.append([a,b])
q=int(input())
queries=[]
for _ in range(q):
    queries.append(list(map(int,input().split())))
final_output=[]
for lst in queries:
    if lst[0]==1:
