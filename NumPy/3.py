import numpy as np

# Create a simple array
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

# 1. Basic Slicing (Index 2 to 5)
print(arr[2:5])      # Output: [30, 40, 50]

# 2. Slice from the start to index 4
print(arr[:4])       # Output: [10, 20, 30, 40]

# 3. Slice from index 5 to the end
print(arr[5:])       # Output: [60, 70, 80, 90]

# 4. Using a Step (Every 2nd element)
print(arr[1:len(arr)-1:2])    # Output: [20, 40, 60, 80]

# 5. Reverse the array using negative steps
print(arr[::-1])     # Output: [90, 80, 70, 60, 50, 40, 30, 20, 10]