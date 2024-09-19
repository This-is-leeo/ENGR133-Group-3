"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Prompt the user to enter the x and y coordinates of a point and then
    display a figure window with a shape and the entered point and print the
    location of the point.

Assignment Information:
    Assignment:     TTYK #2
    Team ID:        LC18 - 03
    Author:         Leo Yu, yu1398
    Date:           09/19/2024

Contributors:
    Name, login@purdue [repeat for each]

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

import matplotlib.pyplot as plt
import math


def main():
    # Define the shape of the triangle

    a = 2 # x-axis and y-axis dimensions


    # plot figure
    # make list of x and y values
    xlist=[-a, 0, a, -a]
    ylist=[ 0, a, 0,  0]

    vert_x=[0, 0]
    vert_y=[math.floor(-a - 1), math.ceil(a + 1)]

    hor_y =[0, 0]
    hor_x =[math.floor(-a - 1), math.ceil(a + 1)]

    fig, ax = plt.subplots()    
    ax.plot(xlist, ylist)
    ax.plot(vert_x, vert_y, dashes=[4, 4])
    ax.plot( hor_x,  hor_y, dashes=[4, 4])
    ax.set_title("Triangle Bisector on y-axis")
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    # plotting the shape of the figure

    # input coordinates
    x = float(input("Enter the x value: "))
    y = float(input("Enter the y value: "))

    # plot the point on the graph to show
    ax.plot(x, y, "o")
    ax.annotate(f"({x}, {y})", (x, y), xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')

    """Write your code here (and delete this line)."""

    if x < -a or x > a:
        print("Outside")
    elif y < 0 or y > a - abs(x):
        print("Outside")
    elif y == 0 or y == a - abs(x):
        print("On the line")
    else:
        print("Inside")    

    plt.show()

    # remember to close the figure window to rerun the code

if __name__ == "__main__":
    main()