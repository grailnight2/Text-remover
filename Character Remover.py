f = open("enter\\absolute\\path\\to\\file" , "r") # Enter the absolute path to the file you are editing, make sure to double \\
newFile = open("enter\\absolute\\path\\to\\file","a+") # Enter the absolute path to the new file you are saving to, make sure to double \\
for line in f:
    text = line
    newline = text.replace(text[:8],'')
    newFile.write(newline)
newFile.close()