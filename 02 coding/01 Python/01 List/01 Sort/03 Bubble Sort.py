# list ascending order

string = input()  # 5 2 1 4 3
integers_list = list(map(int, string.split()))
print(integers_list)

print("------------------")

for main_counter in range(len(integers_list)):
    for sub_counter in range(main_counter+1, len(integers_list)):
        if integers_list[main_counter] > integers_list[sub_counter]:
            integers_list[main_counter], integers_list[sub_counter] = integers_list[sub_counter], integers_list[main_counter]
        # print(integers_list)    

print(integers_list)  # [1, 2, 3, 4, 5]     

print("====================")