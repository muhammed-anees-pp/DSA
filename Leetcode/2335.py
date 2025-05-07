"""
Minimum Amount of Time to Fill Cups
"""
def fill_cups(amount):
    total = sum(amount)
    max_cup = max(amount)
    return max(max_cup, (total + 1) // 2)

# Example test cases
test_cases = [
    [1, 4, 2],
    [5, 4, 4],
    [5, 0, 0],
    [2, 2, 2]
]

for amounts in test_cases:
    result = fill_cups(amounts)
    print(f"Amount: {amounts}, Minimum seconds to fill: {result}")
