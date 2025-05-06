# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Check if the number is odd or even
if number % 2 == 0:
    result = "Even"
else:
    result = "Odd"

# Print the result
print(f"The number {number} is {result}.")
4