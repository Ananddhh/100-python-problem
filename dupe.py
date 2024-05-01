# Define a list with duplicate elements
my_list = [1, 2, 3, 2, 4, 5, 1]

# Create an empty list to store unique elements
unique_list = []

# Iterate through the original list
for item in my_list:
    # If the item is not already in the unique_list, append it
    if item not in unique_list:
        unique_list.append(item)

# Print the unique list
print(unique_list)
