

def  reverse(s):
    reversed_string = ''
    for character in s:
        reversed_string = character + reversed_string
    return reversed_string



if __name__ == "__main__":
    user_input =  input("Enter the string : ")
    print("reveresed string",reverse(user_input) )