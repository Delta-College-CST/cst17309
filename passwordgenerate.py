# This program generates a random password 8 chars long

import random

PASSLENGTH = 8

# Character to randomly select from
characters = "abcdefghijklmnopqrstuvwxyz" + \
             "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + \
             "0123456789" + "!@#$%^&*+"

lengthChars = len(characters)
password    = ""

# Loop to generate one random character at a time.
# Concatentate to end of evolving password
for n in range(PASSLENGTH):
    charIndex = random.randrange(lengthChars)
    newPassChar = characters[charIndex]
    password = password + newPassChar
    
# Output random password
print(password)
