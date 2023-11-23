# Third Party Packages 

"""
01 Delete duplicates without set function
02 print a to z 
03 permutations
04 combinations
"""

# 01 Delete duplicates without set function

my_list = [1, 1, 2, 2, 3, 3, 3, 4, 4]

result_list = []
for each in my_list:
    # print(each)
    if each in result_list:
        pass
    else:
        result_list.append(each)
print(result_list)    

print("------------")


# 02 print a to z
my_dictionary = dict()
for counter in range(ord("a"), ord("z")+1):
    # print(counter)
    character = chr(counter)
    # print(character)
    my_dictionary[character] = counter
print(my_dictionary)    

print("-------------")

# itertools

from itertools import permutations, combinations

my_list = [1,2,3]

my_permutations = list(permutations(my_list))
print(my_permutations)

my_combinations = list(combinations(my_list, 2))
print(my_combinations)

print("================")