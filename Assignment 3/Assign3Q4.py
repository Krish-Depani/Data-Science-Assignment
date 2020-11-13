# importing numpy library.
import numpy as np

# creating an 1D array.
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# converting 1D array to 2D using reshape function.
y = x.reshape(3, 3)
print(y)
print(y.shape)
# converted to 2D array with 3 rows and 3 columns.

# converting 1D array to 2D using newaxis attribute.
z = x[:, np.newaxis]
print(z)
print(z.shape)
# converted to 2D array with 9 rows and 1 columns.

# converting 1D array to 2D using expand_dims function.
w = np.expand_dims(x, axis=0)
print(w)
print(w.shape)
# converted to 2D array with 1 rows and 9 columns.