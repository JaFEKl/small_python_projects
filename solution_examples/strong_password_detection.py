#! python 3
# "Safe Password Detection" (Automate the Boring Stuff with Python: Chapter 7)

import re


# One or more characters [A-Z]
uppercaseRegex = re.compile(r'[A-Z]+')

# One or more characters [a-z]
lowercaseRegex = re.compile(r'[a-z]+')

# One or more digits
digitRegex = re.compile(r'\d+')

# Check if the password string matches the regular expressions

while True:
    print('Please enter a safe password suggestion')
    password_suggested = input()

    if len(password_suggested) < 8:
        print('The password needs to contain of at least 8 characters')
        continue
    elif uppercaseRegex.search(password_suggested) is None:
        print('The password needs to contain at least one uppercase letter')
        continue
    elif lowercaseRegex.search(password_suggested) is None:
        print('The password needs to contain at least one lowercase letter')
        continue
    elif digitRegex.search(password_suggested) is None:
        print('The password needs to contain at least one digit')
        continue
    else:
        print('Your suggested password can be considered as a "strong" password')
        break
