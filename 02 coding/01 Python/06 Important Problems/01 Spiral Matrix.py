# Spiral Matrix

def rotate_matrix(matrix):
    rotated_matrix = []
    rows = len(matrix)
    columns = len(matrix[0])
    for column_index in range(columns):
        add_row = []
        for row_index in range(rows):
            add_element = matrix[row_index][column_index]
            add_row.append(add_element)
        rotated_matrix.append(add_row)
    rotated_matrix = rotated_matrix[::-1]    
    return rotated_matrix    


rows, columns = list(map(int, input().split()))

matrix = []
for row_count in range(rows):
    add_row = list(map(int, input().split()))
    matrix.append(add_row)

print(matrix)

print("--------------")

all_elements = []
for row in matrix:
    all_elements.extend(row)
elements_count = len(all_elements)

# print(elements_count)

result_matrix = []
while True:
    if elements_count == 0:
        break
    add_top = matrix[0]
    result_matrix.append(add_top)
    del matrix[0]
    all_elements = []
    for row in matrix:
        all_elements.extend(row)
    elements_count = len(all_elements)
    if elements_count == 0:
        break
    matrix = rotate_matrix(matrix)

print(result_matrix)    
    
print("===============")    
        


        
# Input
           
# 4 5
# 12 31 20 50 54
# 53 24 32 52 65
# 38 10 99 1 44 
# 1 62 89 22 39

# output:

# 12 31 20 50 54 65 44 39 22 89 62 1 38 53 24 32 52 1 99 10