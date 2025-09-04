    
try:
    user_input_1 = float(input("Enter 1st number : "))
    user_input_2 = float(input("Enter 2nd number : "))
    user_input_3 = float(input("Enter 3rd number : "))
    print("enetered numbers are:",user_input_1,user_input_2,user_input_3)
except ValueError:
    print("Enter the number only")
    exit()
def bigger_number(a,b,c):
    if a > (b and c):
        print ("bigger number is", a)
    elif b > (a and c):
        print ("bigger number is", b)
    else:
        print ("bigger number is", c)

bigger_number(user_input_1,user_input_2,user_input_3)


