#TODO: There are functions for wrapping text. See tutorial pg 77 (PDF).

import time

def print_text(string_list):
    """
    Prints strings in list with a 0.1 second time step between each string.
    """
    for i in string_list:
        print i
        time.sleep(0.1)

def print_from_file(filename):
    """
    Prints lines read from a text file with a 0.1 second time step between each
    line.
    
    filename must be a string.
    """
    with open(filename, "r") as file:
        for line in file.readlines():
            print line,
            time.sleep(0.1)