"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Program uses the Maclaurin series to approximate e^x with specified values 
    of n and x. It then prints the percent error of the estimated value with 
    respect to the actual value. 

Assignment Information:
    Assignment:     Py3 Team 3 a 
    Team ID:        LC 18 - 03
    Author:         Leo Yu, yu1398@purdue.edu
                    Megan Puntney, mpuntney@purdue.edu
                    Megan Raupp, mraupp@purdue.edu
                    Sarah Kaufman, kaufman62@purdue.edu
    Date:           09/17/2024

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
import sys
#print(sys.getrecursionlimit())
sys.setrecursionlimit(3000)

from python3.TeamTask.py3_team_2_b_3 import my_factorial
import math
def maclaurinSeries(x,n):
    return 1 if n == 0 else (x ** n) / my_factorial(n) + maclaurinSeries(x,n - 1)

def main():
    n = int(input("Enter the value of n: "))
    x = float(input("Enter the value of x: "))
    actual = math.exp(x)
    approx = maclaurinSeries(x, n)
    error = (approx - actual)/actual
    print(f"Actual value: {actual:.2f}")
    print(f"Approximate value: {approx:.2f}")
    print(f"Error: {error * 100}%")


if __name__ == "__main__":
    main()
