# import itertools 

# l=[1,2,3,4,5,6,7]
# res=itertools.accumulate(l,max)
# print(list(res)  
                                        #SETS  
import itertools
l= { 5, 3, 6, 2, 1, 9 }
v ={ 4, 2, 6, 0, 7 }
  
res=itertools.accumulate(v.difference(l))
print(list(res))
print(v.difference(l))