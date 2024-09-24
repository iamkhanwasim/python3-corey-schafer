my_list = [1, 2, 3, 4]
fs_list = frozenset(my_list)
print(fs_list)   ##  output  frozenset({1, 2, 3, 4})

my_set = {10, 20, 30, 40}
fs_set = frozenset(my_set)
print(fs_set)   ##  output  frozenset({10, 20, 30, 40})

my_tuple = (100, 200, 300, 400)
fs_tuple = frozenset(my_tuple)
print(fs_tuple) ##  output  frozenset({100, 200, 300, 400})

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
fs_dict = frozenset(my_dict)
print(fs_dict)   ##  output  ffrozenset({'a', 'b', 'c', 'd'})

## OPERATIONS
##  Union
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([5, 6, 7, 8])
fs_union = fs1.union(fs2)
print(fs_union) ##  output frozenset({1, 2, 3, 4, 5, 6, 7, 8})


##  Intersection
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([5, 2, 7, 4])
fs_intersection = fs1.intersection(fs2)
print(fs_intersection)  ##  output frozenset({2, 4})

##  Difference
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([5, 2, 7, 4])
fs_difference = fs1.difference(fs2)
print(fs_difference)    ##output    frozenset({1, 3})

##  Symmetric_difference
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([5, 2, 7, 4])
fs_sd = fs1.symmetric_difference(fs2)
print(fs_sd)    ##output    frozenset({1, 3, 5, 7})

##  also be used with ^
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([5, 2, 7, 4])
fs_sd = fs1 ^ fs2
print(fs_sd)    ##output    frozenset({1, 3, 5, 7})

##  Subset
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([2,3])
fs_sub = fs2.issubset(fs1)
print(fs_sub)    ## output    True

##  Superset
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([2,3])
fs_sub = fs1.issuperset(fs2)
print(fs_sub)    ## output    True

##  Disjoint
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([1,7, 8, 9, 10])
fs_sub = fs1.isdisjoint(fs2)
print(fs_sub)    ## output    False

##  Membership
fs = frozenset([1,2,3,4])
print(5 in fs)  ##  output False
print(4 in fs)  ##  output True

##  Copy
fs_1 = frozenset([1,2,3,4])
fs_2 = fs_1.copy()
print(fs_1)  ##  output frozenset({1, 2, 3, 4})
print(fs_2)  ##  output frozenset({1, 2, 3, 4})

##  Iterate
fs_1 = frozenset([1,2,3,4])
for element in fs_1:
    print(element)
##  output 
# 1
# 2
# 3
# 4

