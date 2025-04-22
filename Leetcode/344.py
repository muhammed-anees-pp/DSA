"""
Reverse String
"""
def revserString(str):
    for i in range(len(str)//2):
        str[i],str[~i] = str[~i],str[i]
        return str

# Example:
print(revserString(["h","e","l","l","o"]))
print(revserString(["H","a","n","n","a","h"]))