# This program lists a variety products along with the
# customer reviews.

def reformatDate(inDate):
    outDate = inDate

    # Convert coded month to month name
    monthCode = inDate[0:2]
    if monthCode == "01":
        outDate = "January "
    elif monthCode == "02":
        outDate = "February "
    elif monthCode == "03":
        outDate = "March "
    elif monthCode == "04":
        outDate = "April "
    elif monthCode == "05":
        outDate = "May "
    elif monthCode == "06":
        outDate = "June "
    elif monthCode == "07":
        outDate = "July "
    elif monthCode == "08":
        outDate = "August "
    elif monthCode == "09":
        outDate = "September "        
    elif monthCode == "10":
        outDate = "October"
    elif monthCode == "11":
        outDate = "November "
    else:
        outDate = "December "

    # Manage day of month
    if inDate[3:4] == "0":
        outDate = outDate + inDate[4:5]
    else:
        outDate = outDate + inDate[3:5]       

    # Add year
    outDate = outDate + ", " + inDate[6:]
        
    return outDate

# -------- MAIN ROUTINE --------- #

datafile = open("statefacts.txt", "r")   # Open file for input

# Process product file one at a time
for line in datafile:

    # Read/split one line of data containing state info
    code, name, nickname, capital, startdate, \
    enterNum, animal, bird, flower = line.split(",")

    # Call function to reformat coded date int long format
    detailedDate = reformatDate(startdate)
   
    # Write one line of output
    print ("%-15s became a state on %-16s" % (name, detailedDate))




