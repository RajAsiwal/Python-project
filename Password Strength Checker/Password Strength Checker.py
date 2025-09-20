#Password Strength Checker
#Conditions
#Minimum 8 chars,digit,upper case,lower case& special char.

import re
#re=regular expression it's helps find special characters in programme

def check_password_strength(password):
    if len(password)<8: #length of password 
        return "Weak:password must be at least 8 character"

    if not any(char.isdigit() for char in password):
        return "Weak:password must contain a digit"
        #{isdigit() cheak digit in password}

    if not any(char.isupper() for char in password):
        return "Weak:password must contain a upper char"

    
    if not any(char.islower() for char in password):
        return "Weak:password must contain a lower char"

    if not re.search(r'[!@#$%^&*()-_=+\|{};/?.><]',password):
        return "Medium:Password must contian a special char"

    return "Strong:Your Password is secured!"

def password_checker():
    print("Welcome to the password strength checker")

    while True:
        password=input("Enter your password(or type 'exit' to quite):")

        if password.lower()=='exit':
            print("Thank you for using")
            break
        result=check_password_strength(password)
        print(result)

#Run the password checker tool
        if_name_=="_main_":
            password_checker()
        

    
    
