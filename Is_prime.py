Num = int(input("Enter a number: "))
if Num <= 2:
    print("not a prime number")
else:
    for i in range(2,Num):
        if Num % i == 0:
            print("not a prime number")
            break
    else:
        print("a prime number")