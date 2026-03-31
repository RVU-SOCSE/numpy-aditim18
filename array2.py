import numpy as np


arr = np.array([1, 2, 3, 4, 5, 6])
print("Original Array:")
print(arr)


reshaped = arr.reshape(2, 3)
print("\nReshaped Array (2x3):")
print(reshaped)


print("\nFirst element:", arr[0])
print("Element at row 1, column 2:", reshaped[0][1])


total = np.sum(arr)
print("\nSum of elements:", total)
