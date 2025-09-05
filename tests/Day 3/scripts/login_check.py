user_id = 'Test'
password = 'Test123'




def userid_password_check(a,b):
    if (user_id == a) and (password == b):
        print("Entered details are correct to login")
    else:
        print("Entered login details are wrong")



if __name__ == "__main__":
    User_input = input("Enter username: ")
    User_password = input("Enter password: ")
    userid_password_check(User_input,User_password)