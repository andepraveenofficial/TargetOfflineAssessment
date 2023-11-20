# Phone Number Conversion

phone_number = input()  # 9887776666
print(phone_number)

print("--------------")

numbers = {0:"zero",1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}

seperated_numbers_list = []
add_num = ""
for counter in range(len(phone_number)):
    # print(counter)
    each = phone_number[counter]
    next_each = ""
    if counter+1 < len(phone_number):
        next_each = phone_number[counter+1]
    # print(each)
    add_num += each
    if each == next_each:
        pass
    else:
        seperated_numbers_list.append(add_num)
        add_num = ""
        
print(seperated_numbers_list)

print("-------------")


output = []
for each in seperated_numbers_list:
    # print(each)
    num = int(each[0])
    string = numbers[num]
    add_string = ""
    if len(each) == 1:
        add_string = string
        # print(add_string)
    elif len(each) == 2:
        add_string = "double" + " " + string
        # print(add_string)
    elif len(each) == 3:
        add_string = "triple" + " " + string
        # print(add_string)
    elif len(each) == 4:
        add_string = ("double" + " " + string + " ") * 2
    output.append(add_string)

print(*output)    
    
print("=============")

'''
Output :
=============
9887776666
--------------
['9', '88', '777', '6666']
-------------
nine double eight triple seven double six double six 
=============


'''