# Take input from the user
user_string = input("Enter a string: ")

# Reverse the string
reversed_string = ""
for char in user_string:
    reversed_string = char + reversed_string

# Display the reversed string
print("Reversed string:", reversed_string)
