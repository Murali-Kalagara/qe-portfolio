def sum_average(numbers):
    result = 0
    b = len(numbers)
    for num in numbers:
        result+=num
            
    return result/b



if __name__ == "__main__":
    try:
        user_input = list(map(float,input("enter the number seperated by commas:").split(',')))
    except ValueError:
        print("Enter valid number")
        exit()
    
    largest = sum_average(user_input)
    print("Biggest number is :",largest)