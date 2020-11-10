# creating a empty dict
d = {}

#  getting value for "n" from user
n = int(input())

# appending i as key and i*i as value to d
for i in range(1, n + 1):
    d[i] = i * i

# print dictionary d
print(d)
