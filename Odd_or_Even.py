Num = int(input("Enter a number: "))

if Num % 2 == 0:
    print(f"{Num} is even")
elif Num % 2 == 1:
    print(f"{Num} is odd")
else:
    print("Not an integer")
    
# another way
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


even_numbers = [num for num in num_list if num % 2 == 0]
odd_numbers = [num for num in num_list if num % 2 != 0]

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
