# This extracts email addresses from a web page script

htmlfile = open("home.html.txt", "r")   # Open file for reading

# Perform file processing loop until end
for aLine in htmlfile:

    # Determine if 'mailto' tag in current HTML code lien
    if "mailto" in aLine:
        
        # Mark beginning and end of email message
        start = aLine.find("mailto") + 7
        end   = aLine.find("\">",start)

        # Extract email as substring
        email = aLine[start : end]   

        # Write email(s) in web page
        print(email)
    
    









