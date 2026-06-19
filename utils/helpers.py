from typing import TypeVar, List

numeric = TypeVar('numeric', int, float)

def clamp(value: numeric, min_val: numeric, max_val: numeric) -> numeric:
    return min(max_val, max(min_val, value))

def rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix or not matrix[0]:
        return []
    return [list(row) for row in zip(*matrix[::-1])]

def flatten(matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []
    
    return [col for row in matrix for col in row]