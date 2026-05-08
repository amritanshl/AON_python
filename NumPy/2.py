import numpy as np

arr = np.array([10, 20, 30, 40])

# print(arr[0])  # Access first element: 10
# print(arr[2])  # Access third element: 30
# print(arr[-1]) # Access last element using negative indexing: 40

arr2d = np.array([
    [1, 2, 3],# 0 -3
    [4, 5, 6], #1 -2
    [7, 8, 9]  #2 -1
])
print(arr2d[-2,-3])
print(arr2d[2,1])

print(arr2d[0])
# Access the element '6' (2nd row, 3rd column)
print(arr2d[1, 2]) 

# Access the first row
print(arr2d[0])    # Output: [1, 2, 3]

# Access an element from the last row, last column
print(arr2d[-1, -1]) # Output: 9


arr3d = np.array(
[
    [
        [1, 2], 
        [3, 4]
    ], 
    [
        [5, 6], 
        [7, 8]
    ]
]
)
print(arr3d[1,1,0])
# Access the number '6'
# It is in the 2nd matrix (index 1), 1st row (index 0), 2nd column (index 1)
print(arr3d[1, 0, 1])
print(arr3d[0,-1,-1])
