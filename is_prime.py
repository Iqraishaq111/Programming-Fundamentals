# Take input from the user
num = int(input("Enter a number: "))

# Assume the number is prime
is_prime = True

# Check if num is less than 2
if num < 2:
    is_prime = False
else:
    # Check for factors from 2 to sqrt(num)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

# Display if the number is prime or not
if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
