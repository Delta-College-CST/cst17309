# This program encrypts a word or phrase by shifting the characters
# a defined number of positions of the alphabet.  Spaces, numbers, or
# other special characters are removed from the final message.

SHIFT_POSITION_COUNT = 3

# Capture input from user
plaintext = input("Enter phrase to encrypt: ")

# Begin encryption
length = len(plaintext)
encrypted = ""
for i in range(length):
    if plaintext[i].isalpha() == True:
        newChar = plaintext[i].upper()
        newCharInt = ord(newChar) + SHIFT_POSITION_COUNT
        if newCharInt > ord("Z"):
            newCharInt = newCharInt - 26
        encrypted += chr(newCharInt)

# Output encrypted message
print(encrypted)
    
