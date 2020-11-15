# importing numpy & pandas.
import numpy as np
import pandas as pd

# creating an numpy array.
x = np.array([22, 11, 33, 66, 44, 77, 88, 99, 55, 00])
print(x)
print(type(x))

# creating series of array using "Series()" function.
y = pd.Series(x)
print(y)
print(type(y))