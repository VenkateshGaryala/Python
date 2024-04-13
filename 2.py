scores={"s1":[65,68,59,52,69,65,55,59],"s2":[60,64,60,60,88,64,68,75],"s3":[59,72,64,62,66,78,73]}

for i in scores.keys():
    print(i)
    count = 0
    x=0
    for j in scores[i]:
       
        count = count + j
        
        x=count/8
    scores[i] = x
print(scores)

