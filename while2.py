# Define a list of numbers
num_list = [1, 2, 3, 4, 5]

# Initialize the sum and index
sum_of_numbers = 0
index = 0

# Use a while loop to sum the numbers
while index < len(num_list):
    sum_of_numbers += num_list[index]
    index += 1

# Print the sum
print("Sum of numbers in the list:", sum_of_numbers)
