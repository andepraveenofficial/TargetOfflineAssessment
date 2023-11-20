# matrix parts

# read matrix
def read_matrix(rows):
    matrix = []
    for row_count in range(rows):
        add_row = list(map(int, input().split()))
        # print(add_row)
        matrix.append(add_row)
    return matrix    
    

rows, columns = list(map(int, input().split()))

matrix = read_matrix(rows)
print(matrix)    

print("------------")

matrix_sub_parts = []
for row_index in range(rows):
    for column_index in range(columns):
        # element = matrix[row_index][column_index]
        # print(element)
        add_part = []
        for row_count in range(rows-row_index):
            add_row = []
            for column_count in range(columns-column_index):
                add_item = matrix[row_index+row_count][column_index+column_count]
                add_row.append(add_item)
            # print(add_row)
            add_part.append(add_row)
        matrix_sub_parts.append(add_part)    
            
        # print("------------")   

matrix_parts = []
for sub_part in matrix_sub_parts: 
    # print(sub_part)
    for row_index in range(len(sub_part)):
        for column_index in range(len(sub_part[0])):
            # element = matrix[row_index][column_index]
            # print(element)
            # if row_index == column_index:  // Square Parts
                add_part = []
                for row_check in range(row_index+1):
                    for column_check in range(column_index+1):
                        add_item = sub_part[row_check][column_check]
                        add_part.append(add_item)
                print(add_part)
                matrix_parts.append(add_part)
    print("------------")
            
        
print(matrix_parts)            

print("===============")        
                 

#====================#
# input :
#------------#
# 3 4
# 1 2  3  4
# 5 6  7  8
# 9 10 11 12
#-------------------#