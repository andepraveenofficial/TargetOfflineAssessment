# Practice

"""
General Problems:
-----------------
01 Prime Number
02 Palindrome
03 Duplicate Items
04 X pattern
05 Reverse List
06 Factorial
07 Armstrong Number
08 Fibonacci Series
09 Swap
10 Sorted List
"""

# 01 prime Number 
number = 15
prime_numbers_list = []
for main_counter in range(1, number+1):
    # print(main_counter)
    factors_count = 0 
    for sub_counter in range(1, main_counter+1):
        if main_counter % sub_counter == 0:
            factors_count += 1 
    if factors_count == 2:
        #  print(main_counter)
         prime_numbers_list.append(main_counter)
print(prime_numbers_list)         

print("--------------")            

# 02 Palindrome
word = "aba"
reversed_word = word[::-1]
is_palindrome = word == reversed_word
print(is_palindrome)

print("-----------")

# 03 Duplicate Items
my_list = [1,2,2,3,3,3,4,4,4,4]
unique_items_list = []
for each_num in my_list:
    # print(each_num)
    if each_num in unique_items_list:
        pass
    else:
        unique_items_list.append(each_num)
print(unique_items_list)        

print("----------------------")    

# 04 X pattern

number = 5
"""
*   *
 * *
  *
 * *
*   *
"""
for counter in range(1, number+1):
    # print(counter)
    star = "*"
    line = [" "] * number
    line[counter-1] = star
    line[-counter] = star
    print(*line)
    
print("---------")    
    
my_list = [1,2,3,4,5]
# my_list = my_list[::-1]
my_list.reverse()
print(my_list)

print("---------------")

# 06 Factorial
number = 5 
factorial_result = 1
for counter in range(1, number):
    # print(counter)
    factorial_result *= counter
print(factorial_result)    

print("--------------")

# 07 Armstrong Number

number = "543"

power = len(number)
result = 0
for each in number:
    each_num = int(each)
    add_num = each_num ** power 
    result += add_num

is_armstrong = int(number) == result
print(is_armstrong)    

print("---------------")

# 08 Fibonacci Series
number = 10

fibonacci_series = [0, 1]
for counter in range(number-2):
    add_number = fibonacci_series[counter] + fibonacci_series[counter+1]
    fibonacci_series.append(add_number)
print(fibonacci_series)    

print("-------------")

# 09 Swap

a = 10
b = 20
a,b = b,a
print(a)
print(b)

print("--------------")

# 10 Sorted List
my_list = [5,1,3,2,4]
print(my_list)

for main_counter in range(len(my_list)):
    for sub_counter in range(main_counter+1, len(my_list)):
        # print(my_list[main_counter], my_list[sub_counter])
        if my_list[main_counter] > my_list[sub_counter]:
            my_list[main_counter], my_list[sub_counter] =  my_list[sub_counter], my_list[main_counter]
            # print(my_list)
print(my_list)            

print("===============")