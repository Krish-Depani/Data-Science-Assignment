# creating an empty list
x = []

# number of elements
n = int(input("Enter number of elements : "))

# Below line read inputs from user using map() function
a = list(map(int, input("\nEnter the numbers with space between each number (e.g- 11 22 33): ").strip().split()))[:n]

# iterating variable a to append even elements to x
for i in a:
    if i % 2 == 0:
        x.append(i)

print(x)