# Basic Matrix

"""
01 read matrix
02 copy matrix
03 rotate matrix
04 rotate matrix with degrees
"""

# read matrix
def read_matrix(rows):
    matrix = []
    for row_count in range(rows):
        add_row = list(map(int, input().split()))
        # print(add_row)
        matrix.append(add_row)
    return matrix    

# copy matrix
def copy_matrix(original_matrix):
    rows = len(original_matrix)
    columns = len(original_matrix[0])
    matrix = []
    for row in original_matrix:
        add_row = row.copy()
        # print(add_row)
        matrix.append(add_row)
    return matrix    

# rotate matrix
def rotate_matrix(original_matrix):
    matrix = []
    for column_index in range(columns):    
        add_row = []
        for row_index in range(rows):
            # print(row_index, column_index)
            # element = original_matrix[row_index][column_index]
            # print(element)
            add_column = original_matrix[row_index][column_index]
            add_row.append(add_column)
        add_row = add_row[::-1]
        # print(add_row)
        matrix.append(add_row)
    return matrix   

# rotate_matrix_with_degrees
def rotate_matrix_with_degrees(original_matrix, degrees):
    number_of_rotations = degrees // 90
    for rotation_count in range(number_of_rotations):
        rotated_matrix = rotate_matrix(original_matrix)
        original_matrix = rotated_matrix
    return rotated_matrix    
    

rows, columns = list(map(int, input().split()))
# print(rows, columns)

original_matrix = read_matrix(rows)
print(original_matrix)    

copied_matrix = copy_matrix(original_matrix)
print(copied_matrix)    

print("-----------------")

rotated_matrix = rotate_matrix(original_matrix)
print(rotated_matrix)  

degrees = 180
rotated_matrix_with_degrees = rotate_matrix_with_degrees(original_matrix, degrees)
print(rotated_matrix_with_degrees)    

print("===================")


#=================#
# input :
#-----------------#
# 3 3
# 1 2 3
# 4 5 6
# 7 8 9
#==================#






