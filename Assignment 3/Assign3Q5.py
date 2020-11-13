# importing numpy library.
import numpy as np

# taking two numpy square arrays.
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = np.array([[2, 7, 3], [5, 1, 0], [1, 4, 0]])

# vertically stacking array x and y.
a = np.vstack((x, y))
print("Horizontally stacked array : \n", a)

# horizontally stacking array x and y.
b = np.hstack((x, y))
print("Vertically stacked array : \n", b)