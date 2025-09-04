try:
    user_input_1 = int(input("enter the first number : " ))
    user_input_2 = int(input("enter the second number : " ))
    user_input_3 = int(input("enter the third number : " ))
except ValueError:
    print("Please enter numbers only")
    exit()
def largest_of_three_numbers():
    if user_input_1 > (user_input_2 and user_input_3):
         print ("Bigger number is:",user_input_1 )
    elif user_input_2 > (user_input_1 and user_input_3):
         print ("Bigger number is:",user_input_2 )
    else: 
         print ("Bigger number is:",user_input_3 )

largest_of_three_numbers()     

