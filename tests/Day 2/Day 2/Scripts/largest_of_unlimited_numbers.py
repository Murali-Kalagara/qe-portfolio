

def biggest_number(numbers):
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest



if __name__ == "__main__":
    try:
        user_input = list(map(float,input("enter the number seperated by commas:").split(',')))
    except ValueError:
        print("Enter valid number")
        exit()
    
    largest = biggest_number(user_input)
    print("Biggest number is :",largest)