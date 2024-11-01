# Take input from the user
num = int(input("Enter a number: "))

sum_of_digits = 0

# Calculate the sum of digits
while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num = num // 10

# Display the sum of digits
print("Sum of digits:", sum_of_digits)
