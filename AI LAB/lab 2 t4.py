# Task 4: Find specific characters in a string

message = "Programming language"
characters = ['r', 'a', 'm', 'n', 'u']

for char in characters:
    print(f"'{char}' found at index: {message.index(char)}")
