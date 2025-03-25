"""
412 - Fizz Buzz
"""
def fizzBuzz(num):
    answer = []
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(i))
        
    return answer

print(fizzBuzz(3))
print(fizzBuzz(5))
print(fizzBuzz(15))

