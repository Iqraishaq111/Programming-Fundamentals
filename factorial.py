# Take input from the user
num = int(input("Enter a number: "))

factorial = 1

# Calculate the factorial
for i in range(1, num + 1):
    factorial *= i

# Display the result
print(f"The factorial of {num} is {factorial}")
