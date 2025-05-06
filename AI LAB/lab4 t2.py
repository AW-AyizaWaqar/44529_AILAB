numbers = [11, 50, 38, 73, 29]
smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("The smallest number in the list is:", smallest)
