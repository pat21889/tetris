from typing import TypeVar, List

Numeric = TypeVar('Numeric', int, float)

def clamp(value: Numeric, min_val: Numeric, max_val: Numeric) -> Numeric:
    return min(max_val, max(min_val, value))

def rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix or not matrix[0]:
        return []
    return [list(row) for row in zip(*matrix[::-1])]

def flatten(matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []
    
    return [col for row in matrix for col in row]