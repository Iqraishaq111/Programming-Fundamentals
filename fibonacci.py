# Take the number of terms as input from the user
n_terms = int(input("Enter the number of terms: "))

# First two terms
a, b = 0, 1

# Print Fibonacci sequence up to n terms
print("Fibonacci Sequence:")
for _ in range(n_terms):
    print(a, end=" ")
    a, b = b, a + b
