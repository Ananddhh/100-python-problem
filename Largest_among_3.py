Num_1 = int(input("Enter first number: "))
Num_2 = int(input("Enter second number: "))
Num_3 = int(input("Enter third number: "))

if (Num_1 > Num_2) and (Num_1 > Num_3):
    print(f"The largest number is {Num_1}")
elif (Num_2 > Num_1) and (Num_2 > Num_3):
    print(f"The largest number is {Num_2}")
else:
    print(f"the largest number is {Num_3}")

