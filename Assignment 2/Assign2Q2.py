# List comprehensions are used to create lists from other iterable objects.

# syntax for list comprehensions is as follows:-
# SYNTAX = [expression for ITEM in COLLECTION]

# After the for loop we can also add conditional statements, but they are optional.

# lets take one example of list comprehensions.


# Example 1:-

# making list of iterable object('LETS_UPGRADE') with 'i' as expression using for loop.
x = [i for i in 'LETS_UPGRADE']
print(x)


# Example 2:-

# making list of even numbers from 1 to 50 using for loop and conditional statement.
even_num = [y for y in range(51) if y % 2 == 0]
print(even_num)