# This program converts alphabetic phone numbers to digits.
# Error checking is excluded from this version.

# Input phone number
phoneNum = input("Enter 10-character phonetic phone number: ")

newPhoneNum = ""    # Ready variable for digital phone number

# Convert alphabetic phone number to digital. If already a digit
# or a dash, simply write the character.  Otherwise, convert
# alpha character to a numerical character.
for digit in phoneNum:
    if digit.isdigit():
        newPhoneNum += digit
    if digit == "-":
        newPhoneNum += "-"
    if digit == "A" or digit == "B" or digit == "C":
        newPhoneNum += "2"
    if digit == "D" or digit == "E" or digit == "F":
        newPhoneNum += "3"
    if digit == "G" or digit == "H" or digit == "I":
        newPhoneNum += "4"
    if digit == "J" or digit == "K" or digit == "L":
        newPhoneNum += "5"
    if digit == "M" or digit == "N" or digit == "O":
        newPhoneNum += "6"
    if digit == "P" or digit == "Q" or digit == "R" or digit == "S":
        newPhoneNum += "7"
    if digit == "T" or digit == "U" or digit == "V":
        newPhoneNum += "8"
    if digit == "W" or digit == "X" or digit == "Y" or digit == "Z":
        newPhoneNum += "9"

# Output phone number
print(newPhoneNum)


    
