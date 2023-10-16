# This program validates that a password is 7-13 characters
# with at least one lowercase, one uppercase, and one numerical
# character.

# Input password
password = input("Enter password: ")

# Assume no required candidate charaters found
digitFound = False
lowerFound = False
upperFound = False

# Scann password one char at a time
for aChar in password:
    if aChar.isdigit():
        digitFound = True
    if aChar.islower():
        lowerFound = True
    if aChar.isupper():
        upperFound = True

# Evaluate password and write outcome
print(password)
if len(password) >= 7 and len(password) <= 13 and \
    digitFound == True and lowerFound == True and upperFound == True:
    print("  is VALID")
else:
    print("  is INVALID")




    
