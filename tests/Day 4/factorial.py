import sys
try:
    user_input = int(input("Enter the number greater than or equal to 0 to find factorial : "))
    if user_input < 0:
        print("Please enter the number greater than or equal to 0 ")
except ValueError:
    print("Please enter numbers only")
    sys.exit(1)

def factorial_finder(n):
    if n == 0 or n ==1:
         return 1
    result = 1  
    for num in range(2,n+1):
        result *= num
    return result

print(factorial_finder(user_input))