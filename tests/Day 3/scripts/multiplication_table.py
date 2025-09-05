
import sys
def multiplication(s):
   multiplied_until = 15
   for i in range(1,multiplied_until+1):
       
       print(s,'*',i,'=',s*i)
      
       
        
if __name__ == "__main__":
    try:
        user_input = int(input("enter any valid number : "))
        if user_input <= 0:
            print("Please enter a positive number greater than 0.")
            sys.exit(1)
    except ValueError:
        print("enter valid number")
        sys.exit(1)
    print("DEBUG: Input received:", user_input)
    multiplication(user_input)