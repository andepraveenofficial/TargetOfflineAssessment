
# zero matrix
# Matrix zero corners

# read matrix
def read_matrix(rows):
    matrix = []
    for row_count in range(rows):
        add_row = list(map(int, input().split()))
        # print(add_row)
        matrix.append(add_row)
    return matrix    
 
# zero corners
def zero_corners(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    corners_list = []
    # values_list = []
    for row_index in range(rows):
        for column_index in range(columns):
            # element = matrix[row_index][column_index]
            # print(element)
            if matrix[row_index][column_index] == 0:
                # element = matrix[row_index][column_index]
                # print(element)
                
                # add_values = []
                add_corners = []
                
                # if (row_index > 0) and (column_index > 0):
                if (row_index != 0) and (column_index != 0):
                    # top_left_value = matrix[row_index-1][column_index-1]
                    # add_values.append(top_left_value)
                    top_left = (row_index-1, column_index-1)
                    add_corners.append(top_left)
                
                # if (row_index > 0) and (column_index < (columns-1)):
                if (row_index != 0) and (column_index != (columns-1)):
                    # top_right_value = matrix[row_index-1][column_index+1]
                    # add_values.append(top_right_value)
                    top_right = (row_index-1, column_index+1)
                    add_corners.append(top_right)
                
                # if (row_index < (rows-1)) and (column_index > 0):
                if (row_index != (rows-1)) and (column_index != 0):
                    # bottom_left_value = matrix[row_index+1][column_index-1]
                    # add_values.append(bottom_left_value)
                    bottom_left = (row_index+1, column_index-1)
                    add_corners.append(bottom_left)
                
                # if (row_index < (rows-1)) and (column_index < (columns-1)):
                if (row_index != (rows-1)) and (column_index != (columns-1)):
                    # bottom_right_value = matrix[row_index+1][column_index+1]
                    # add_values.append(bottom_right_value)
                    bottom_right = (row_index+1, column_index+1)
                    add_corners.append(bottom_right)
                
                # values_list.append(add_values)
                corners_list.append(add_corners)
    return corners_list            

    

rows, columns = list(map(int, input().split()))

matrix = read_matrix(rows)
print(matrix)

print("----------")

matrix_zero_corners = zero_corners(matrix)
print(matrix_zero_corners)

print("==============")


#======================#
# Input :
#-------------#
# 3 3
# 1 2 3
# 4 0 6
# 7 8 9
#-------------#
# Output :
#-------------#
# [[(0, 0), (0, 2), (2, 0), (2, 2)]]
#===================#
            
        







