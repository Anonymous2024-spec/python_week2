# Python List Operations

This repository demonstrates basic operations on lists in Python, showing how to create, manipulate, and access elements in a list.

## Overview

This simple script showcases fundamental list operations in Python including:
- Creating an empty list
- Adding elements (append, insert, extend)
- Removing elements
- Sorting
- Finding element positions

## Code Explanation

```python
# Create an empty list called my_list.
my_list = []

# Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15 at the second position in the list.
my_list.insert(1, 15)

# Extend my_list with another list: [50, 60, 70].
my_list.extend([50, 60, 70])

# Remove the last element from my_list.
my_list.pop()

# Sort my_list in ascending order.
my_list.sort()

# Find and print the index of the value 30 in my_list.
index_of_30 = my_list.index(30)
print("Sorted list:", my_list)
print("Index of 30:", index_of_30)
```

## Output

When executed, the script produces the following output:
```
Sorted list: [10, 15, 20, 30, 40, 50, 60]
Index of 30: 3
```

## Key List Methods Demonstrated

- `append()`: Adds an element to the end of the list
- `insert()`: Adds an element at a specified position
- `extend()`: Adds all elements of another list to the end
- `pop()`: Removes and returns the last element
- `sort()`: Sorts the list in ascending order
- `index()`: Returns the index of the first occurrence of a value

## Usage

To run this script:
```bash
python list_operations.py
```

## Requirements

- Python 3.x

## License

This project is open-source and available under the [MIT License](LICENSE).
