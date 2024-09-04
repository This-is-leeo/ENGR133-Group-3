"""
Course Number: ENGR 13300
Semester: e.g. Fall 2024

Description:
    Replace this line with a description of your program.

Assignment Information: Assignment: (5.3.2)(auto grader doesnt work!!!!!)
    Assignment:     7 
    Team ID:        LC18, team 3
    Author:         yu1398@purdue.edu
    Date:           9/3/2024

Contributors:
    NA
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
from math import *

def main():
    r1 = float(input("Input the resistance of the first resistor [Ω]: "))
    r2 = e ** 2 * sqrt(7)
    parallel_resistance = 1/(1/r1 + 1/r2)
    series_resistance = r1 + r2

    print("Type              First         Second         Total Resistance")
    print(f"Parallel{r1:14.1f} Ω{r2:12.1f} Ω{parallel_resistance:13.1f} Ω") #width modifers to make the formatting a bit better, just manually adding the spaces also works
    print(f"Series  {r1:14.1f} Ω{r2:12.1f} Ω{series_resistance:13.1f} Ω")



if __name__ == "__main__":
    main()
