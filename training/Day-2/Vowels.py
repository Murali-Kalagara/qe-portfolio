user_input = input("Enter any word or senetence or alphanumeric or special characters :")
vowels = ['a','e','i','o','u']
modified_user_input = user_input.lower()
x = ''
for letter in modified_user_input:
    if letter not in vowels:
        x += letter
print (x)

y = x.replace(" ","")
print (y)

empty_set = set(y)
print(empty_set)
regular_string = '-'.join(empty_set)
print(regular_string)

