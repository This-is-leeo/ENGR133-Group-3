"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    This file contains the function `classify_point`, which classifies a point based on
    its location relative to the outer shape and the inner shape.

Assignment Information:
    Assignment:     CQ #2
    Team ID:        LC18 03
    Author:         yu1398@purdue.edu
    Date:           09/26/2024

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

########################################################################################
# Import the function(s) you need from CQ2_utils.py here.
########################################################################################
from CQ2_utils import outside_of_circle

# Shape Parameters
# Rectangle
OUTER_WIDTH, OUTER_DEPTH = 18, 12
INNER_WIDTH, INNER_DEPTH = 6, 4
# Circle
OUTER_RADIUS = 15
INNER_RADIUS = 2
# Triangle
OUTER_BASE, OUTER_HEIGHT = 45, 45
INNER_BASE, INNER_HEIGHT = 12, 12


def classify_point(x, y, user_x, user_y):
    """
    Classifies a point based on its location relative to the outer shape and the
    inner shape.

    Parameters:
        x : The x-coordinate of the center of the shape.
        y : The y-coordinate of the center of the shape.
        user_x : The x-coordinate of the user's point.
        user_y : The y-coordinate of the user's point.

    Returns:
        str: The location of the user's point.
    """
    
    if user_x == x and user_y == y:
        return 'Intersection'

    if user_x == x:
        return 'Vertical Line'

    if user_y == y:
        return 'Horizontal Line'
    
    if outside_of_circle(user_x, user_y, 0, 0, OUTER_RADIUS):
       return 'Outside'
    else:
        if outside_of_circle(user_x,user_y,x,y,INNER_RADIUS):
            if user_y > y:
                if user_x > x:
                    return 'Inside C5'
                return 'Inside C6'
            else:
                if user_x < x:
                    return 'Inside C7'
                return 'Inside C8'
        if user_y > y:
            if user_x > x:
                return 'Inside C1'
            return 'Inside C2'
        else:
            if user_x < x:
                return 'Inside C3'
            return 'Inside C4'






    ####################################################################################