# importing numpy library.
import numpy as np

# creating to empty list x and y.
x = []
y = []

# taking input from user for list x and appending elements to it.
for i in range(5):
    a = float(input("Enter elements of list 1 : "))
    x.append(a)

# taking input from user for list y and appending elements to it.
for j in range(5):
    b = float(input("Enter elements of list 2 : "))
    y.append(b)

# converting both lists into array and concatenating it.
c = np.concatenate((x, y))
# printing concatenated array.
print(c)

# sorting the concatenated array.
d = np.sort(c)
# printing the sorted array.
print(d)