"""
Pascal's Triangle
"""

def generate_pascals_triangle(numRows):
    triangle = []

    for row in range(numRows):
        new_row = [1] * (row + 1)

        for col in range(1, row):
            new_row[col] = triangle[row - 1][col - 1] + triangle[row - 1][col]

        triangle.append(new_row)

    return triangle


print(generate_pascals_triangle(1))
# Output: [[1]]

print(generate_pascals_triangle(3))
# Output: [[1], [1, 1], [1, 2, 1]]

print(generate_pascals_triangle(5))
# Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
