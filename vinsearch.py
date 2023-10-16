# This program seeks out VINS for specific parameters:
# - Jeeps
# - Built in 2013
# and writes them to output

JEEP_CODE       = "C4"
MODEL_YEAR_2013 = "D"

# Write heading
print("Jeeps Built 2013 \n")

datafile = open("vins.txt", "r")   # Open file for reading

# Perform file processing loop until end
for aVin in datafile:

    # Extract substrings
    manufactureCode = aVin[1:3]
    yearCode        = aVin[9:10]

    # Determine if VIN matches required parameters
    if manufactureCode == JEEP_CODE and yearCode == MODEL_YEAR_2013:
        print(aVin)


    
    









