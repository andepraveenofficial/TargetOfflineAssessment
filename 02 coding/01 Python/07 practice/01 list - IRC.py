# List 

'''
01 swappping with temporary variable
02 swapping concept
03 Bubble sorted
04 list ascending order with sort method 
05 list ascending order with sorted function
06 list parts
'''

# 01 swapping with temporary variable
a = 10
b = 20
temporary_variable = a
a = b 
b = temporary_variable
print(a)
print(b)

print("---------------")

# 02 swapping concept
a = 10
b = 20 
a,b = b,a
print(a)
print(b)

print("-------------")

# 03 Bubble Sort 
my_list = [5, 2, 1, 4, 3]
for main_counter in range(len(my_list)):
    # print(my_list[main_counter])
    for sub_counter in range(main_counter+1, len(my_list)):
        # print(my_list[main_counter], my_list[sub_counter])
        if my_list[main_counter] > my_list[sub_counter]:
            my_list[main_counter],  my_list[sub_counter] =  my_list[sub_counter], my_list[main_counter]
    # print(my_list)        

print(my_list)    

print("--------------")

# 04 list ascending order with sort method

my_list = [5, 2, 1, 4, 3]
my_list.sort()
print(my_list)

print("---------------------")

# 05 list ascending order with sorted function
my_list = [5, 2, 1, 4, 3]
sorted_list = sorted(my_list)
print(sorted_list)

print("----------------")

# 06 list parts

my_list = [1, 2, 3, 4, 5]

list_parts = []
for main_counter in range(len(my_list)):
    # print(my_list[main_counter:])
    main_part = my_list[main_counter:]
    for sub_counter in range(len(main_part)):
        # print(main_part[:sub_counter+1])
        sub_part = main_part[:sub_counter+1]
        list_parts.append(sub_part)
    # print('---------')   

print(list_parts)    

print("=================")