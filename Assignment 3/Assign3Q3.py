# importing numpy library.
import numpy as np

# creating an 2D array.
x = np.array([[1, 2, 3], [4, 5, 6]])

# printing array.
print(x)

# printing dimension of the array.
print("Dimension :", x.shape)
# (a, b) here a is number of rows and b is number of column.

# printing size of the array.
print("Size :", len(x[0]) + len(x[1]))
# here length of 1st row and 2nd row is added in order to find the size of whole array.
