"""
Pascal's Triangle II
"""

def get_pascals_row(rowIndex):
    row = [1]
    for i in range(1, rowIndex + 1):
        row.append(1)
        for j in range(i - 1, 0, -1):
            row[j] = row[j] + row[j - 1]
    return row

print(get_pascals_row(0))  # Output: [1]
print(get_pascals_row(1))  # Output: [1, 1]
print(get_pascals_row(3))  # Output: [1, 3, 3, 1]
print(get_pascals_row(5))  # Output: [1, 5, 10, 10, 5, 1]
