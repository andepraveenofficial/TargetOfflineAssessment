# permutations library
 
from itertools import permutations
 
items = list(map(int, input().split()))  # 1 2 3

print(items)

print("------------")

arrangements = list(permutations(items))

print(arrangements)
print(len(arrangements))

print("==============")


#=====================#
# Input :
#--------------#
# 1 2 3
#--------------#
# Output :
#--------------#
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
#====================#