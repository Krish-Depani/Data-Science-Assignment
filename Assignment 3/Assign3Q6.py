# importing numpy library.
import numpy as np

# creating an 1D array.
x = np.array([2, 5, 3, 2, 6, 8, 9, 3, 5])
# printing 1D array.
print("Original array :", x)

# getting unique values and occurrence of it.
y, z = np.unique(x, return_counts=True)

# printing unique elements.
print("Unique elements are :", y)
# printing count of unique elements.
print("count of unique value :", z)

