# list 
# matrix

"""
01 read matrix
02 copy matrix
03 rotate matrix
04 rotate matrix with degrees
05 anti clockwise rotation
06 Spiral Matrix
07 matrix diagonals:
    01 principal diagonal
    02 secondary diagonal
    03 diagonal items
    04 non diagonal items
    04 anti diagonal rows
08 zero sides
09 zero corners
10 matrix parts
"""

"""
Input :
3 3 
1 2 3
4 5 6 
7 8 9
"""

### Functions

# read matrix
def read_matrix():
    original_matrix = []
    for row_count in range(rows):
        add_row = list(map(int, input().split()))
        # print(add_row)
        original_matrix.append(add_row)
    return original_matrix

# copy matrix 
def copy_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    copied_matrix = []
    for row_index in range(rows):
        add_row = []
        for column_index in range(columns):
            add_column = original_matrix[row_index][column_index]
            add_row.append(add_column)
        copied_matrix.append(add_row)
    return copied_matrix

# 03 rotate matrix 
def rotate_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    rotated_matrix = []
    for column_index in range(columns):
        add_row = []
        for row_index in range(rows):
            add_column = matrix[row_index][column_index]
            add_row.append(add_column)
        add_row = add_row[::-1]    
        rotated_matrix.append(add_row)
    return rotated_matrix
    
# 04 rotate matrix with degrees
def rotate_matrix_with_degrees(matrix, degrees):
    number_of_rotations = degrees // 90
    # matrix = original_matrix
    for rotate_count in range(number_of_rotations):
        rotated_matrix = rotate_matrix(matrix)
        matrix = rotated_matrix
    return rotated_matrix
 
# 05 anti clockwise rotation
def anti_clockwise_rotation(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    rotated_matrix = []
    for column_index in range(columns):
        add_row = []
        for row_index in range(rows):
            add_column = matrix[row_index][column_index]
            add_row.append(add_column)
        rotated_matrix.append(add_row)
    anti_clockwise_rotated_matrix = rotated_matrix[::-1]    
    return anti_clockwise_rotated_matrix   



### Callings

# 01 read matrix
rows, columns = list(map(int, input().split()))
original_matrix = read_matrix()
print(original_matrix)

# 02 copy matrix
copied_matrix = copy_matrix(original_matrix)
print(copied_matrix)

# 03 rotate matrix
rotated_matrix = rotate_matrix(original_matrix)
print(rotated_matrix)

# 04 rotate matrix with degrees
degrees = 180
rotated_matrix_with_degrees = rotate_matrix_with_degrees(original_matrix, degrees)
print(rotated_matrix_with_degrees)
 
# 05 anti clockwise rotation
anti_clockwise_rotated_matrix = anti_clockwise_rotation(original_matrix) 
print(anti_clockwise_rotated_matrix)
    
print("--------------") 

# 06 Spiral Matrix 
total_elements = []
for row in original_matrix:
    total_elements.extend(row)
number_of_elements = len(total_elements)
    
spiral_matrix = []
while True:
    if number_of_elements == 0:
        break 
    else:
        # print(original_matrix)
        add_row = original_matrix[0]
        # print(add_row)
        spiral_matrix.append(add_row)
        original_matrix = original_matrix[1:]
        total_elements = []
        for row in original_matrix:
            total_elements.extend(row)
        number_of_elements = len(total_elements)
        if number_of_elements == 0:
            break
        original_matrix = anti_clockwise_rotation(original_matrix)    
        
print(spiral_matrix)

### matrix diagonals
print("-----matrix diagonals-----")

matrix = copied_matrix

'''
1 2 3    00 01 02    0 1 2 
4 5 6    10 11 12    1 2 3 
7 8 9    20 21 22    2 3 4
'''

'''
1         00            0 
2 4       01 10         1 1 
3 5 6     02 11 20      2 2 2 
6 8       12 21         3 3
9         22            4
'''

# Functions

# principal diagonal
def principal_diagonal(matrix):
    rows = len(matrix)
    coumns = len(matrix[0])
    principal_diagonal_list = []
    for row_index in range(rows):
        for column_index in range(columns):
            item = matrix[row_index][column_index]
            # print(item)
            if row_index == column_index:
                # print(item)
                principal_diagonal_list.append(item)
    return principal_diagonal_list

# secondary diagonal 
def secondary_diagonal(matrix):
    rows = len(matrix)
    coumns = len(matrix[0])
    secondary_diagonal_list = []
    for row_index in range(rows):
        for column_index in range(columns):
            item = matrix[row_index][column_index]
            # print(item)
            if (row_index+column_index) == (columns-1):
                # print(item)
                secondary_diagonal_list.append(item)
    return secondary_diagonal_list 

# diagonal items 
def diagonal_items(matrix):
    rows = len(matrix)
    coumns = len(matrix[0])
    diagonal_items_list = []
    for row_index in range(rows):
        for column_index in range(columns):
            item = matrix[row_index][column_index]
            # print(item)
            if (row_index == column_index) or ((row_index+column_index) == (columns-1)):
                # print(item)
                diagonal_items_list.append(item)
    return diagonal_items_list 

# non diagonal items 
def non_diagonal_items(matrix):
    rows = len(matrix)
    coumns = len(matrix[0])
    non_diagonal_items = []
    for row_index in range(rows):
        for column_index in range(columns):
            item = matrix[row_index][column_index]
            # print(item)
            if not ((row_index == column_index) or ((row_index+column_index) == (columns-1))):
                # print(item)
                non_diagonal_items.append(item)
    return non_diagonal_items

# anti diagonal rows
def anti_diagonal_rows(matrix):
    rows = len(matrix)
    coumns = len(matrix[0])
    number_of_anti_diagonal_rows = rows+(columns-1)
    anti_diagonal_rows_list = []
    for anti_diagonal_count in range(number_of_anti_diagonal_rows):
        anti_diagonal_row = []
        for row_index in range(rows):
            for column_index in range(columns):
                item = matrix[row_index][column_index]
                if (row_index+column_index) == anti_diagonal_count:
                    # print(item)
                    anti_diagonal_row.append(item)
        # print(anti_diagonal_row)            
        anti_diagonal_rows_list.append(anti_diagonal_row)       
    return anti_diagonal_rows_list  

# Callings 

# principal diagonal 
principal_diagonal_list = principal_diagonal(matrix)
print(principal_diagonal_list)

# secondary diagonal
secondary_diagonal_list = secondary_diagonal(matrix)
print(secondary_diagonal_list)

# diagonal items
diagonal_items_list = diagonal_items(matrix)          
print(diagonal_items_list)

# non diagonal items
non_diagonal_items_list = non_diagonal_items(matrix)
print(non_diagonal_items_list)

# anti diagonal rows
anti_diagonal_rows_list = anti_diagonal_rows(matrix)
print(anti_diagonal_rows_list)

# Sides & Corners & Parts
print("------sides & corners & parts------") 

# Functions

# zero sides
def zero_sides(matrix):
    rows = len(matrix)
    coumns = len(matrix[0])
    zero_sides_list = []
    for row_index in range(rows):
        for column_index in range(columns):
            item = matrix[row_index][column_index]
            # print(item)
            add_sides = []
            if item == 0:
                # print(row_index, column_index)
                if row_index != 0:
                    top = matrix[row_index-1][column_index]
                    # print(top)
                    add_sides.append(top)
                if column_index != (columns-1):
                    right = matrix[row_index][column_index+1]
                    # print(right)
                    add_sides.append(right)
                if row_index != (rows-1):
                    bottom = matrix[row_index+1][column_index]
                    # print(bottom)
                    add_sides.append(bottom)
                if column_index != 0:
                    left = matrix[row_index][column_index-1]
                    # print(left)
                    add_sides.append(left)
                zero_sides_list.append(add_sides)
            # print(add_sides)    
    return zero_sides_list

# zero corners
def zero_corners(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    zero_corners_list = []
    for row_index in range(rows):
        for column_index in range(columns):
            item = matrix[row_index][column_index]
            # print(item)
            add_corners = []
            if item == 0:
                # print(row_index, column_index)
                if (row_index != 0) and (column_index != (columns-1)):
                    top_right = matrix[row_index-1][column_index+1]
                    # print(top_right)
                    add_corners.append(top_right)
                if (row_index != (rows-1)) and (column_index != (columns-1)):
                    bottom_right = matrix[row_index+1][column_index+1]
                    # print(bottom_right)
                    add_corners.append(bottom_right)
                if (row_index != (rows-1)) and (column_index != 0):
                    bottom_left = matrix[row_index+1][column_index-1]
                    # print(bottom_left)
                    add_corners.append(bottom_left)
                if (row_index != 0) and (column_index != 0):
                    top_left = matrix[row_index-1][column_index-1]
                    # print(top_left)
                    add_corners.append(top_left)
                zero_corners_list.append(add_corners)    
                
            # print(add_corners)        
    return zero_corners_list             
      
# 08 zero sides
zero_sides_list = zero_sides(matrix)
print(zero_sides_list)

# 09 zero corners
zero_sides_list = zero_corners(matrix)
print(zero_sides_list)

print("-------------")

# 10 matrix parts

'''
step 1 : fix the index 
step 2 : divide into parts
'''

matrix_sub_parts = []
for main_row in range(rows):
    for main_column in range(columns):
        # print(main_row, main_column)
        add_part = []
        for sub_row in range(rows-main_row):
            add_row = []
            for sub_column in range(columns-main_column):
                add_item = matrix[main_row+sub_row][main_column+sub_column]
                add_row.append(add_item)
            add_part.append(add_row)
        # print(add_part) 
        matrix_sub_parts.append(add_part)
print(matrix_sub_parts)
        
matrix_parts = []        
for part in matrix_sub_parts:
    rows = len(part)
    columns = len(part[0])
    for row_index in range(rows):
        for column_index in range(columns):
            # element = matrix[row_index][column_index]
            # print(element)
            # if row_index == column_index:  # Square Parts
                add_part = []
                for row_check in range(row_index+1):
                    add_row = []
                    for column_check in range(column_index+1):
                        item = part[row_check][column_check]
                        add_row.append(item)
                    # print(add_row)
                    add_part.extend(add_row)
                # print(add_part)    
                matrix_parts.append(add_part)  
print(matrix_parts)            

print("====================")