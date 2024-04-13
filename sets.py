# s1={1,'apple',2,'ball',3,'cat'}
# s2={4,'dog',5,'eagle',6,'fox'}

# l=[7,8,9]#add any iterable
# s1.add('goal')
# s1.update(s2)

# s1.update(l)
# print(s1)
# print(s2)
# # to remove an item
# s1.remove("apple")
# s1.discard('fox')
# print(s1)
# # to empty the set
# del s2
# print(s2)
a={1,2,3,4,5,6}
b={5,6,7,8,9}
# c=a.difference(b)
# print(c)
# d=a.symmetric_difference(b)
# print(d)

# a.symmetric_difference_update(b)
# print(a)
a.intersection_update(b)
print(a)
