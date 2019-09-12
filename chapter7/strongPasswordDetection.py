#! python3
# detect if a string is at least eight characters long, contains both uppercase and lowercase character, and has at least one digit

import re

#TODO : test it is eight characters
lengthRegex = re.compile(r'[a-zA-Z0-9\.\-]{8,}$')

# TODO : test string contains uppercase and lowercase
uppercaseRegex = re.compile(r'[A-Z]')
lowercaseRegex = re.compile(r'[a-z]')

# TODO : test string has at least one digit
digitRegex = re.compile(r'\d')

# TODO : run all tests on password
def passwordDetection(password):
    if bool(lengthRegex.search(password))==False:
        print('Passwords must be at least eight characters long.')
        return False
    elif bool(uppercaseRegex.search(password))==False:
        print('Passwords must contain at least one uppercase character.')
        return False
    elif bool(lowercaseRegex.search(password))==False:
        print('Passwords must contain at least one lowercase character.')
        return False
    elif bool(digitRegex.search(password))==False:
        print('Passwords must contain at least one numeric digit.')
        return False
    else:
        print('Password accepted!')
        return True

accepted=False
while(accepted==False):
    print('Enter password:', end=' ')
    passwordInput = input()
    accepted = passwordDetection(passwordInput)
