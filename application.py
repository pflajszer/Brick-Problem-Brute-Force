#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 20:24:49 2019

The program calculates maximum load that can be placed on top of the given wall.

@author: Pawel Flajszer
"""

# Import modules:
# ======================================================================================================================

import re
import sys

# Functions:
# ======================================================================================================================

def check_args():
    """ Check the number of command line arguments. Return error if not equals 3. """
    if len(sys.argv) != 3:
        raise TypeError(f"This app takes exactly 3 arguments ({len(sys.argv)} given). \
Usage: python app.py text_file.txt input_position")

def check_extension():
    """ Check if first argument ends with the right extension (*.txt) """
    if sys.argv[1][-4:] != '.txt':
        raise TypeError("The text file has to have the right extension (*.txt)")

def check_input_position(wall):
    """ Validate the input position. """
    if int(sys.argv[2]) > len(wall[0]):
        raise ValueError("The input position is larger than the lenght of the wall (index 0 is position 1).")
    if int(sys.argv[2]) < 1:
        raise ValueError("The input position must be a positive integer.")
    if int(sys.argv[2]) < len(wall)-1 or int(sys.argv[2]) > len(wall[0]) - (len(wall)-1):
        raise ValueError("The calculation cannot touch the side wall for the accuracy purposes. \
Place the input position closer to the middle of the wall.")

def read_file(file):
    """ Open given file and returns the content as a string """
    with open(file) as f:
        wall = f.read()
    return wall

def check_file_format(wall):
    """ Using regex check if the string in the text file has the right formatting. """
    if re.match('^-*\n\| \d{3} \|', wall) is not None:
        return True

def create_wall(file):
    """ Create an iterable list of lists out of the single string read from the file. """
    wall = read_file(file)  
    if check_file_format(wall):                                 
        wall = wall.split('\n')                                 # Split a wall into rows on newline char
        for row in range(0, len(wall)):                         
            wall[row] = re.split('[^\d{3}]', wall[row])         # Split wall into rows of 3 digits using regex
            wall[row] = list(filter(None, wall[row]))           # Remove empty strings from each row
        wall = [row for row in wall if row != []]               # Remove empty lists from rows
        return wall

def divide_bricks(pyramid):
    """ Divide every bricks' strenght rating by 990 to prepare them for multiplication. """
    for row in pyramid:
        for i in range(0, len(row)):
            row[i] /= 990


def create_pyramid(wall, ip):
    """ Shorten the rows to relevant values - integers in range 800-999 under the initial position brick."""
    ni = ip        # Negative index
    pi = ip+1      # Positive index
    for row in range(0, len(wall)):
        if row % 2 == 0 and row != 0:
            pi += 1
        elif row != 0:
            ni -= 1
        wall[row] = wall[row][ni:pi]
        wall[row] = list(map(int, wall[row]))
    return wall

def pathway_last_two_rows(pyramid, counter, i):
    """ Iterate over the paths for two bottom rows (since they're consistent for every step). """
    if counter % 2 != 0 and i[-1] < len(pyramid[-1])-1:
        i[-1] += 1
    if (counter-2) % 2**2 == 0 and i[-2] < len(pyramid[-2])-1:
        i[-2] += 1

def pathways(pyramid, row_index, counter, i):
    """ Find all the possible pathways from top brick to the bottom of the wall. """
    if (counter-2**(row_index-1)) % 2**row_index == 0 and i[-row_index]< len(pyramid[-row_index])-1:
        i[-row_index] += 1
        for y, x in enumerate(range((-row_index+2), 0), 1):
            i[x] -= y

def calculations(pyramid, i):
    """ Calculate the value of the given path. """
    res = 1
    for x, row in enumerate(pyramid):
        res *= row[i[x]]
    return res



# Main:
# ======================================================================================================================
def main():

    check_args()
    check_extension()
    file = sys.argv[1]
    input_pos = (int(sys.argv[2])) - 1
    results = []
    counter = 0
    wall = create_wall(file)
    check_input_position(wall)
    pyramid = create_pyramid(wall, input_pos)
    divide_bricks(pyramid)
    i = [0 for x in range(0,len(pyramid))]

    # Main loop. Iterate over every possible pathway, perform calculations on them and append to results list.
    while True:
        pathway_last_two_rows(pyramid, counter, i)
        for row in range(3, len(pyramid)):
            pathways(pyramid, row, counter, i)
        results.append(calculations(pyramid, i))
        counter += 1
        if counter == 2**(len(pyramid)-1):
            break
        
    results.sort()
    print("%.4f" % results[0])

# ======================================================================================================================

if __name__ == '__main__':
    main()