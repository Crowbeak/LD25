import time

def printText(stringList):
    """
    Prints strings in list with a 0.1 second time step between each string.
    """
    for i in stringList:
        print i
        time.sleep(0.1)

def printFromFile(filename):
    """
    Prints lines read from a text file with a 0.1 second time step between each
    line.
    
    filename must be a string.
    """
    with open(filename, "r") as file:
        for line in file.readlines():
            print line,
            time.sleep(0.1)