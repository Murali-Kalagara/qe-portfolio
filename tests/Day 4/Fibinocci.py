import math

import sys
try:
    user_input = int(input("Enter the number greater than or equal to 0 to find fibanocci : "))
    if user_input < 0:
        print("Please enter the number greater than or equal to 0 ")
except ValueError:
    print("Please enter numbers only")
    sys.exit(1)

def fibanocci(n):
    result = 0
    for num in range(0,n+1):
        result += num
        print(result)
    return result

print (fibanocci(user_input))