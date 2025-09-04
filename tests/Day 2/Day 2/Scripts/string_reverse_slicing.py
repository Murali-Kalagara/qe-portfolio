'''print("Hello world")
user_input = input("Enter the string: ")
reversed_string = user_input[::-1]
print("Original string: ",user_input)
print("Reversed String: ",reversed_string)'''

def reverse_str(str1):
    return str1[::-1]
user_input = input("Enter the string: ")
print("Original string: ",user_input)
print("Reversed String: ",reverse_str(user_input))