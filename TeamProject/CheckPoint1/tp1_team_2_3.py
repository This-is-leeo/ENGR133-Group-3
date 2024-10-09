"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Program extracts binary data of each pixel's value in an image.

Assignment Information:
    Assignment:     9.2.1 Team Project Task 2
    Team ID:        018 - 03
    Author:         Leo Yu, yu1398@purdue.edu
                    Megan Puntney, mpuntney@purdue.edu
                    Megan Raupp, mraupp@purdue.edu
                    Sarah Kaufman, kaufman62@purdue.edu
    Date:           10/01/2024
    
Contributors:
    Name, login@purdue [repeat for each]
    None
    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

""" Write any import statements here (and delete this line)."""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import numpy as np
from tp1_team_1_3 import importImage,visualize_image

def to_binary(str):
    binary_value = ''
    for i in str:
        binary_value += format(ord(i) , '08b')
    return binary_value

def extract_message(img, start_value = None, end_value = None):
    start_value = input("Enter the start sequence: ")
    end_value = input("Enter the end sequence: ")

    flattend_image = img.flatten()
    lsb_values = []
    for i in flattend_image:
        i *= 255
        i = int(i)
        i = format(i, '08b')
        lsb_values.append(int(i[-1]))
    lsb_str = ''.join( str(n) for n in lsb_values)
    binary_of_start = to_binary(start_value)
    binary_of_end = to_binary(end_value)
    if binary_of_start in lsb_str and binary_of_end in lsb_str:
        encrypted_starting_value = lsb_str.index(binary_of_start) + len(binary_of_start)
        lsb_str = lsb_str[encrypted_starting_value:]
        encrypted_end_value = lsb_str.index(binary_of_end)
        encrypted_message = lsb_str[:encrypted_end_value]
        print(f'Extracted Message: {encrypted_message}')
        return encrypted_message
    else:
        return None
    
def main():
    img,image_message = importImage()
   
    if extract_message(img) == None:
        print('Start or end sequence not found in the image.')

if __name__ == "__main__":
    main()
