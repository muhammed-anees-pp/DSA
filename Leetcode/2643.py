"""
Row With Maximum Ones
"""
def row_and_maximum_ones(mat):
    max_count = 0
    row_index = 0

    for i, row in enumerate(mat):
        ones_count = sum(row)
        if ones_count > max_count:
            max_count = ones_count
            row_index = i

    return [row_index, max_count]


# Example test cases
mat1 = [
    [0, 1, 1],
    [1, 1, 0],
    [1, 1, 1]
]

mat2 = [
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 1]
]

result1 = row_and_maximum_ones(mat1)
result2 = row_and_maximum_ones(mat2)

print(f"Matrix 1 result: Row index = {result1[0]}, Ones count = {result1[1]}")
print(f"Matrix 2 result: Row index = {result2[0]}, Ones count = {result2[1]}")
