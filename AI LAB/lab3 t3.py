#Take values of length and breadth of a rectangle from user and check if it is square or not.
# Prompt the user to enter the length and breadth of the rectangle
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

# Check if the rectangle is a square
if length == breadth:
    result = "It is a square."
else:
    result = "It is not a square."

# Print the result
print(result)
