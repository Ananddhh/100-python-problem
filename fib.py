def fibonacci(limit):
    # Initialize Fibonacci sequence with first two numbers
    fib_sequence = [0, 1]

    # Generate Fibonacci sequence up to the specified limit
    while fib_sequence[-1] + fib_sequence[-2] <= limit:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence

# Get input from the user
limit = int(input("Enter the limit for Fibonacci sequence generation: "))

# Generate Fibonacci sequence
fib_sequence = fibonacci(limit)

# Print the Fibonacci sequence
print("Fibonacci sequence up to", limit, ":", fib_sequence)


