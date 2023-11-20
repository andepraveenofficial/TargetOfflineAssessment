
# Zero matrix
# Matrix zero sides

# read matrix
def read_matrix(rows):
    matrix = []
    for row_count in range(rows):
        add_row = list(map(int, input().split()))
        # print(add_row)
        matrix.append(add_row)
    return matrix

# zero sides    
def zero_sides(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    sides_list = []
    # values_list = []
    for row_index in range(rows):
        for column_index in range(columns):
            # element = matrix[row_index][column_index]
            # print(element)
            if matrix[row_index][column_index] == 0:
                # element = matrix[row_index][column_index]
                # print(element)
                # add_values = []
                add_sides = []
                
                # if row_index > 0:
                if row_index != 0:
                    # top_value = matrix[row_index-1][column_index]
                    # add_values.append(top_value)
                    top = (row_index-1, column_index)
                    add_sides.append(top)
                
                # if column_index > 0:
                if column_index != 0:
                    # left_value = matrix[row_index][column_index-1]
                    # add_values.append(left_value)
                    left = (row_index, column_index-1)
                    add_sides.append(left)
                
                # if column_index < (columns-1):
                if column_index != (columns-1):
                    # right_value = matrix[row_index][column_index+1]
                    # add_values.append(right_value)
                    right = (row_index, column_index+1)
                    add_sides.append(right)
                
                # if row_index < (rows-1):    
                if row_index != (rows-1):
                    # bottom_value = matrix[row_index+1][column_index]
                    # add_values.append(bottom_value)
                    bottom = (row_index+1, column_index)
                    add_sides.append(bottom)
                
                # values_list.append(add_values)
                sides_list.append(add_sides)
    return sides_list            
    
    
rows, columns = list(map(int, input().split()))

matrix = read_matrix(rows)
print(matrix)    

print("---------")

matrix_zero_sides = zero_sides(matrix)
print(matrix_zero_sides)    

print("=============")
 
#=======================#
# Input :
#-----------------#
# 3 3
# 1 2 3 
# 4 0 6
# 7 8 9
#-----------------#
# Output :
#-----------------#
# [[(0, 1), (1, 0), (1, 2), (2, 1)]]
#=======================#


