"""
Course Number: ENGR 13300
Semester: e.g. Fall 2024

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     6.1.2 py2 pre task 0
    Team ID:        LC18, team 3
    Author:         Leo Yu, yu1398@purdue.edu
    Date:           9/5/2024

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

def calc_perform(a,b,c):
    if a >= 4:
        ans = (a-b+math.sin(c))/(a*c)
    else:
        ans = (math.tan(c))/(a-(a*c)/b)
    return ans

def main():
    print(round(calc_perform(int(input("a: ")),20,47),2))


if __name__ == "__main__":
    main()
