#	Write a program that checks if a given year is a leap year. A year is a leap year if:
#It is divisible by 4, but not by 100, unless it is also divisible by 400.

# Prompt the user to enter a year
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    result = f"{year} is a leap year."
else:
    result = f"{year} is not a leap year."

# Print the result
print(result)
