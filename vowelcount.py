# This program reads a word or phrase, stores it, and counts
# the number of vowels

# Input phrase and convert all to lower case.
phrase = input("Enter word or phrase to analysis: ")
phrase = phrase.lower()

# Loop through character by character and test for a vowel.  If vowel
# detected, increment counter
vowels = 0
for aChar in phrase:
    if aChar == "a" or aChar == "e" or aChar == "i" or aChar == "o" or aChar == "u":
        vowels += 1

# Output summary
print("In: \"",phrase,"\"")
print("there are: ",vowels," vowels")
