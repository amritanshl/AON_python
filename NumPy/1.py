import numpy as np

arr0 = np.array(42)
print(f"Array: {arr0} | Dimensions: {arr0.ndim}")

# A simple list converted to a 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr1} | Dimensions: {arr1.ndim}")

# A list of lists converted to a 2D array (Rows and Columns)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)
print(f"Dimensions: {arr2.ndim} | Shape: {arr2.shape}") # Shape shows (rows, columns)

# Two 2x3 matrices stacked together
arr3 = np.array([
    [[1, 2, 3], [4, 5, 6]], 
    [[7, 8, 9], [10, 11, 12]]
])
print("3D Array:\n", arr3)
print(f"Dimensions: {arr3.ndim} | Shape: {arr3.shape}")