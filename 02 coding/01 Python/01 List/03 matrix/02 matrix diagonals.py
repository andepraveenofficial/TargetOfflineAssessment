# matrix diagonals

"""
01 principal diagonal
02 secondary diagonal
03 diagonal items
04 non diagonal items
04 anti diagonal rows
"""

# Functions Defining

# read matrix
def read_matrix(rows):
    matrix = []
    for row_count in range(rows):
        add_row = list(map(int, input().split()))
        matrix.append(add_row)
    return matrix   
    
# principal diagonal   
def principal_diagonal(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    principal_diagonal_list = []
    for row_index in range(rows):
        for column_index in range(columns):
            if row_index == column_index:
                element = matrix[row_index][column_index]
                # print(element)
                principal_diagonal_list.append(element)
    return principal_diagonal_list

# secondary diagonal
def secondary_diagonal(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    secondary_diagonal_list = []
    for row_index in range(rows):
        for column_index in range(columns):
            if row_index+column_index == columns-1:
                element = matrix[row_index][column_index]
                # print(element)
                secondary_diagonal_list.append(element)
    return secondary_diagonal_list
 
 # diagonal items 
def diagonal_items(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    diagonal_items_list = []
    for row_index in range(rows):
        for column_index in range(columns):
            if (row_index == column_index) or (row_index+column_index == columns-1):
                element = matrix[row_index][column_index]
                # print(element)
                diagonal_items_list.append(element)
    return diagonal_items_list
     
# non diagonal items 
def non_diagonal_items(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    non_diagonal_items_list = []
    for row_index in range(rows):
        for column_index in range(columns):
            if  (row_index != column_index) and  (row_index+column_index != columns-1):
                element = matrix[row_index][column_index]
                # print(element)
                non_diagonal_items_list.append(element)
    return non_diagonal_items_list
 
# anti diagonal rows 
def anti_diagonal_rows(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    number_of_anti_diagonal_rows = columns + (rows-1)
    anti_diagonal_rows_list = []
    for counter in range(number_of_anti_diagonal_rows):
        add_row = []
        for row_index in range(rows):
            for column_index in range(columns):
                if row_index+column_index == counter:
                    element = matrix[row_index][column_index]
                    # print(element)
                    add_row.append(element)
        anti_diagonal_rows_list.append(add_row)             
    return anti_diagonal_rows_list
    

# Functions Calling    
    
rows, columns = list(map(int, input().split()))

# read matrix
matrix = read_matrix(rows)
print(matrix)

print("--------------")

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
      
print("-----------------")

# anti diagonal rows 
anti_diagonal_rows_list = anti_diagonal_rows(matrix)    
print(anti_diagonal_rows_list)

print("------------")

for row in anti_diagonal_rows_list:
    print(*row)

print("====================")


"""
1 2 3   00 01 02    0 1 2 
4 5 6   10 11 12    1 2 3 
7 8 9   20 21 22    2 3 4
"""

"""
output :
===============
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
--------------
[1, 5, 9]
[3, 5, 7]
[1, 3, 5, 7, 9]
[2, 4, 6, 8]
-----------------
[[1], [2, 4], [3, 5, 7], [6, 8], [9]]
------------
1
2 4
3 5 7
6 8
9
====================
"""


