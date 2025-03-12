"""
Q:2469 - Convert the Temperature
"""

def convert_temp(temp):
    Kelvin = temp + 273.15
    Fahrenheit = temp * 1.80 + 32
    return [Kelvin, Fahrenheit]

# Example Test Case    
print(convert_temp(36.50))
print(convert_temp(122.11))