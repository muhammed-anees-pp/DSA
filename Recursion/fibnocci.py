"""
Print the first 10 fibocci number using recursion
"""
def fibnocci(num):
    if num <= 1:
        return num
    
    return fibnocci(num - 1) + fibnocci(num - 2)


new = []
for i in range(10):
    new.append(fibnocci(i))
print(new)
