# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Determine if the number is single-digit, double-digit, or triple-digit
if -9 <= number <= 9:
    result = "Single-digit"
elif -99 <= number <= 99:
    result = "Double-digit"
elif -999 <= number <= 999:
    result = "Triple-digit"
else:
    result = "Number has more than three digits"

# Print the result
print(f"The number {number} is a {result} number.")
34