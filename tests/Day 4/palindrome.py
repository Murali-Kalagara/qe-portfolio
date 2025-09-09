user_input = input("Enter the word or sentence: ").lower().replace(" ", "")

def palindrome(s):
    emptystr = ''
    for ch in s:
        emptystr = ch + emptystr
    if emptystr == s:
        print("palindrome")
    else:
        print("not palindrome")
    return emptystr

print(palindrome(user_input))


