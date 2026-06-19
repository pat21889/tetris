from helpers import clamp, rotate_matrix, flatten
# --- test clamp ---
print("=== clamp ===")
print(clamp(5, 0, 10))    # expected: 5
print(clamp(-3, 0, 10))   # expected: 0
print(clamp(15, 0, 10))   # expected: 10

# --- test rotate_matrix ---
print("\n=== rotate_matrix ===")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
]
result = rotate_matrix(matrix)
for row in result:
    print(row)
# expected:
# [4, 1]
# [5, 2]
# [6, 3]

# --- test flatten ---
print("\n=== flatten ===")
print(flatten([[1, 2], [3, 4], [5, 6]]))  # expected: [1, 2, 3, 4, 5, 6]
print(flatten([[]]))                       # expected: []
print(flatten([]))                         # expected: []