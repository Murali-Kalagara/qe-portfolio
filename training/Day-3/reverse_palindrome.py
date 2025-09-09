#user_input = input("Enter any string to reverse it and find palindrome or not : ")


def palindrome(n):
    if n == n[::-1]:
      print(n[::-1])
      print("palindrome")
    else:
       print("not palindrome")
    return n[::-1]
    
  

#print(palindrome(user_input))



