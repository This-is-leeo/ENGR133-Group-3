"""
Course Number: ENGR 13300
Semester: e.g. Fall 2024

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:  pretask 1
    Team ID:     team 03
    Author:      yu1398@purdue.edu
    Date:        09/03/2024

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

""" Write any import statements here (and delete this line)."""

import math
def main():
    a = 5
    b = 9 
    c = 2
    equation1 = a * pow(b,2) + math.sin(c)
    equation2 = (math.pi/c) - math.factorial(b)
    equation3 = pow(b,3) + (c/4) + math.asin(1)
    print("equation 1: " + str(round(equation1,4)))
    print("equation 2: " + str(round(equation2,4)))
    print("equation 3: " + str(round(equation3,4)))
    
    


if __name__ == "__main__":
    main()
