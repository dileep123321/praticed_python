num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
