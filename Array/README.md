**ARRAY**
- An **array** is a data structure that stores elements in a **contiguous block of memory**.
- In Python, arrays can be implemented using lists or using the `array` module (though the `array` module is less commonly used in practice due to its limited functionality compared to lists).
- **List as Array**: Python lists are dynamic arrays that can store items of any data type, including integers, strings, and even other lists (i.e., lists can be heterogeneous).
    - Example:
        
        ```python
        arr = [1, 2, 3, 4, 5]
        print(arr)  # Output: [1, 2, 3, 4, 5]
        ```
        
- **Array Module**: For homogeneous data types, you can use the `array` module to create arrays.
    - Example:
        
        ```python
        import array
        
        # Creating an array with integers
        arr = array.array('i', [1, 2, 3, 4, 5])
        print(arr)  # Output: array('i', [1, 2, 3, 4, 5])
        ```
        
    

**Basic Operations:**

1.  **Init (Initialize an Array)**
    1. **Initializing an Empty Array → `O(1)`**
        
        ✅ When creating an **empty** array, it takes **constant time**, regardless of size.
        
        ```python
        arr = []  # Empty list
        ```
        
        ✔ **Time Complexity:** **O(1)** (No elements are added, just a reference is created.)
        
        ✔ **Space Complexity:** **O(1)** (Only a small memory for reference is used.)
        

**b.  Initializing a Predefined Array → `O(n)`**

✅ If we create an array with `n` elements, Python **allocates memory and assigns values**.

```python
arr = [10, 20, 30, 40, 50]  # Array of size 5
```

✔ **Time Complexity:** **O(n)** (Each element is assigned memory **one by one**.)

✔ **Space Complexity:** **O(n)** (Each element **requires space** in memory.)

**c. Initializing an Array with Default Values → `O(n)`**

✅ Using list comprehension or `*` operator fills `n` elements.

```python
arr = [0] * 100  # Creates an array of 100 zeros
```

✔ **Time Complexity:** **O(n)** (Python **allocates memory and assigns values**.)

✔ **Space Complexity:** **O(n)** (Uses **memory for 100 elements**.)

| Initialization Type | Example | Time Complexity |
| --- | --- | --- |
| Empty Array | `arr = []` | **O(1)** |
| Predefined Array | `arr = [10, 20, 30]` | **O(n)** |
| Default Values | `arr = [0] * n` | **O(n)** |

1. **Set (Update an Element)**
    
    💡 **Modify an element at a specific index.**
    
    ```python
    arr[2] = 100  # Change value at index 2
    print(arr)  # Output: [10, 20, 100, 40, 50]
    ```
    
    ✔ **Time Complexity:** **O(1)**
    
    ✔ **Space Complexity:** **O(1)**
    

1. **Get (Access an Element)**
    
    💡 **Retrieve an element using its index.**
    
    ```python
    value = arr[3]  # Get element at index 3
    print(value)  # Output: 40
    ```
    
    ✔ **Time Complexity:** **O(1)**
    
    ✔ **Space Complexity:** **O(1)**
    

1. **Insert (Add an Element)**
    
    💡 **Insert at a specific position (shifts elements to the right).**
    
    ```python
    arr.insert(2, 99)  # Insert 99 at index 2
    print(arr)  # Output: [10, 20, 99, 100, 40, 50]
    ```
    
    ✔ **Time Complexity:** **O(n)** (Shifting elements takes time)
    
    ✔ **Space Complexity:** **O(1)** (Uses same list, no extra memory)
    

1. **Traverse (Loop Through the Array)**
    
    💡 **Visit each element one by one.**
    
    ```python
    for item in arr:
        print(item, end=" ")  # Output: 10 20 99 100 40 50
    ```
    
    ✔ **Time Complexity:** **O(n)**
    
    ✔ **Space Complexity:** **O(1)**
    

1. **Delete (Remove an Element)**
    
    💡 **Remove an element at a specific index (shifts elements left).**
    
    ```python
    arr.pop(2)  # Remove element at index 2
    print(arr)  # Output: [10, 20, 100, 40, 50]
    ```
    
    ✔ **Time Complexity:** 
    
    | Deletion Case | Example | Time Complexity |
    | --- | --- | --- |
    | **At the End (Pop Last)** | `arr.pop()` | **O(1)** |
    | **At the Beginning** | `arr.pop(0)` | **O(n)** |
    | **In the Middle** | `arr.pop(n//2)` | **O(n)** |
    
    ✔ **Space Complexity:**  O(1)
    

### **Multidimensional Arrays**

- In Python, multidimensional arrays (like matrices) can be represented using lists of lists.
- **2D Array**: A 2D array (matrix) can be thought of as an array of arrays, where each inner array represents a row.
    - Example:
        
        ```python
        # 2D Array (Matrix)
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        print(matrix)
        # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        ```
        
- **Jagged Arrays**: A jagged array is an array of arrays where inner arrays can have different lengths. In Python, this can be achieved using lists.
    - Example:
        
        ```python
        # Jagged Array (different column sizes)
        jagged_array = [[1, 2, 3], [4, 5], [6]]
        print(jagged_array)
        # Output: [[1, 2, 3], [4, 5], [6]]
        ```
        
        In this example, the first row has 3 elements, the second has 2 elements, and the third has just 1 element, making it "jagged."