# Delete Duplicates in the list without set function

integers_list = list(map(int, input().split()))
print(integers_list)

print("--------------------")

result_list = []
for item in integers_list:
    if item in result_list:
        pass
    else:
        result_list.append(item)

print(result_list)        

print("=========================")
        
#======================#
# Input:
#--------------#
# 1 1 2 2 3 3 3 4 4
#--------------------#
# Output:
#------------------#
# 1 2 3 4
#=======================#