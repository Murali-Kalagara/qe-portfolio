import sys
try:
    user_input = int(input("Enter the positive number greater than 0to check prime number or not: "))
    if user_input <= 1:
        print("Please enter the valid number greater than 0")
except ValueError:
     print("Please enter the valid number greater than 0")
     sys.exit(1)

def prime_number(n):
    if n <= 1:
        print("Not a prime number")
    elif n == 2:
        print("Prime number")
    else:
        for i in range(2, n):
            if n % i == 0:
                print("Not a prime number")
                break
        else:
            print("Prime number")
prime_number(user_input)