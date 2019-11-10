# Reading data file, then parsin and storing the information in a usable format
#

import re
import os
import sys

def readInput():
    print("\nWhat would you like to do?")
    print("\n1. Read raw data (Divide into generations)")
    print("\n2. Organize data files")
    print("\n0. Exit the program")

    value = input("\n\nPlease enter a command number: ")
    
    if value == "1":
        readData()
        pass
    elif value == "2":
        organizeData()
        pass
    elif value == "0":
        print("\n\nGoodbye!")
        sys.exit()
        pass
    else:
        print("\nSorry, but you've entered an invalid input. Please try again!")
        readInput()
        pass

    pass

def readData():
    # Storing name of the data file in a string
    geneologyFilePath = "geneologyData.txt"

    # Opening the data file
    geneologyFile = open(geneologyFilePath, "r")

    # Searching data file for lines with the keyword "GENERATION"
    for x in geneologyFile:
        # Detecting header that specifies the generation of the subsection
        if "GENERATION" in x:
            # use first keyword to write all data between the current generational marker and the nest, to the assigned keyword

            # Splitting the line containing "GENERATION", and storing the specifying keyword
            generationName = re.split(" GENERATION", x)
            
            # Concatenating the specifying keyword to form file name
            generationFileName = "data/"
            generationFileName += generationName[0]
            generationFileName += ".txt"
            
            # Printing when a generation specifying line is found, printing the file name created and the line it was from
            print("Found one!")
            print(x)
            pass
        else:
            generationFile = open(generationFileName, "a+")
            generationFile.write(x)
            generationFile.close()
            pass
        
        

    # Closing the file
    geneologyFile.close()
    readInput()

    pass

def organizeData():
    # Prompting the user to select a file to organize
    print("\nHello! What files would you like to organize? Please select one from the options displayed below")
    for files in os.walk("./data/"):
        print(files)
        pass
    value = input("\nEnter the filename here: ")

    # Concatenating user input into usable generation file name
    dirtyFileName = "data/"
    dirtyFileName += value
    dirtyFile = open(dirtyFileName, "r")
    
    # Concatenating user input to store organized data
    cleanFileName = "cleanData/"
    cleanFileName += value
    cleanFile = open(cleanFileName, "a+")

    # Reading from dirty file
    line = dirtyFile.readline()
    # Looping through lines in file
    previousLineEmpty = True
    while line:
        # Splitting lines into useful lists
        periodSplit = re.split("[a-z]+\.", line)

        # Executing if a line with the keyword CHILDREN is found
        if ("Children" in line):
            newLine = "\n\n    " + line
            cleanFile.write(newLine)
            line = dirtyFile.readline()
            pass
        # Executing if an empty line is found
        if line.isspace():
            line = dirtyFile.readline()
            previousLineEmpty = True
            pass
        # Executing if the current line is not empty
        else:
            if (previousLineEmpty == True):
                if "VV" in periodSplit[0]:
                    line = line.rstrip()
                    newLine = "\n\n\nName:    " + line
                    cleanFile.write(newLine)
                    pass
                else:
                    line = line.rstrip()
                    newLine = "\n\n        " + line
                    cleanFile.write(newLine)
                    pass
                
                pass
            if (previousLineEmpty == False):
                line = line.rstrip()
                cleanFile.write(line)
                pass

            previousLineEmpty = False
            line = dirtyFile.readline()
            pass

    # Closing the file
    dirtyFile.close()
    cleanFile.close()
    readInput()
    
    pass

def identifyChildren():
    # Read file line by line, checking for keywords "Name: " and "Children "
    
    pass

# Start of program
print("\n\nWelcome User!\n")
readInput()