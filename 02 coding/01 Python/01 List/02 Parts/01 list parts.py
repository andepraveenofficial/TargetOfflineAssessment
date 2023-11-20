# list parts

string = input() # 1 2 3 4 5

integers_list = list(map(int, string.split()))
print(integers_list)

print("-----------------")

list_parts = []
for main_counter in range(len(integers_list)):
    main_part = integers_list[main_counter:]
    # print(main_part)
    for sub_counter in range(len(main_part)):
        sub_part = main_part[:sub_counter+1]
        # print(sub_part)
        list_parts.append(sub_part)
    # print("-----------------")    
    
print(list_parts)    

print("=============")
