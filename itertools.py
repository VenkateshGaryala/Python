#from itertools import chain
#st1 = "Geeks"
#st2 = "for"
#st3 = "Geeks"
#res = list(chain(st1, st2, st3))
#print("before joining :", res)
#ans = ''.join(res)
#print("After joining :", ans)

from itertools import chain
l=['123','234','345','456']
print(list((chain(l))))
print(list(chain.from_iterable(l)))
       ####sum of iterables
print(sum(list(map(int,list(chain.from_iterable(l))))))
