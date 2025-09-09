import logging

logging.basicConfig(filename ='logging_file.log',level = logging.ERROR, format ='%(asctime)s - %(levelname)s - %(funcName)s - Line %(lineno)d - %(message)s')



def factorial(n):
    result = 1
    for i in range(2,n+1):
        result*= i
    return result
    

    
try:
    user_input =  int(input("enter the number:"))
    if user_input < 0:
        logging.error("user input not defined for negative numbers")
    else:
        result = factorial(user_input)
        print(result)
except ValueError:
    logging.error("Inavlid input")