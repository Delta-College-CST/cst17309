# This program encrypts a word or phrase by character replacement
# using a key.  

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key   = "KQBZCGOAWPMHVLFXEDURIYSJNT"

# Capture input from user
message = input("Enter message to encrypt: ")

# Begin encryption
length = len(message)                 # Get length of message
encrypted = ""                        # Initialize encrypted message
for i in range(length):
    currChar = message[i].upper()     # Convert to uppercase
    charPos  = alpha.find(currChar)   # Locate position of character in alphabet
    codeChar = key[charPos]           # Find corresponding char in key
    encrypted = encrypted + codeChar  # Append to end of encrypted messge

# Output encrypted message
print(encrypted)
    



