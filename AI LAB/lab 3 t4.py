# Prompt the user to enter their salary and years of service
salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))

# Calculate the bonus amount if years of service are more than 5 years
if years_of_service > 5:
    bonus = salary * 0.05
    result = f"You have earned a bonus of {bonus}."
else:
    result = "You are not eligible for a bonus."

# Print the result
print(result)
