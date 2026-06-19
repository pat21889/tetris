from typing import TypeVar, List

numeric = TypeVar('numeric', int, float)

def clamp(value: numeric, min_val: numeric, max_val: numeric) -> numeric:
    if min_val <= value <= max_val:
        return value
    return min_val if value < min_val else max_val

def rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix or not matrix[0]:
        return []
    
    old_rows_size = len(matrix)
    old_cols_size = len(matrix[0])
    
    temp = [[0] * old_rows_size for _ in range(old_cols_size)]
    
    for row in range(old_rows_size):
        for col in range(old_cols_size):
            temp[col][old_rows_size-1-row] = matrix[row][col]
    
    return temp

def flatten(matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []
    
    return [col for row in matrix for col in row]