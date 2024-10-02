"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Program extracts binary data  of eahc pixel's value in an image.

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
from tp1_team_1_3 import importImage

def main():
    img = importImage()
    start_value = 7#int(input("Enter the start sequence: "))
    end_value = 700#int(input("Enter the end sequence: "))

    i = 0
    r = 0
    print(img)
    # for row in img:
    #    c = 0
    #    for column in row:
    #        print(column)
    #        if i > start_value:
    #            pass
               
           


if __name__ == "__main__":
    main()
