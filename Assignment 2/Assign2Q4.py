# importing math module for calculation
import math

# creating an origin position
x, y = 0, 0

# taking input for number of directions
n = int(input("Enter the number of directions to be applied : "))

# taking input for directions and steps
for i in range(n):
    step = input("Type direction UP/DOWN/LEFT/RIGHT, No. of steps: ")

# applying steps and direction
    if step == "":
        break

    else:
        step = step.split(" ")

        if step[0] == "UP":
            y = y + int(step[1])
        elif step[0] == "DOWN":
            y = y - int(step[1])
        elif step[0] == "LEFT":
            x = x - int(step[1])
        elif step[0] == "RIGHT":
            x = x + int(step[1])

# calculating distance from original position to current position
c = math.sqrt(x**2 + y**2)

# applying round() function to round off the value
cround = round(c)

# printing distance from original position to current position
print("Distance : ", cround)