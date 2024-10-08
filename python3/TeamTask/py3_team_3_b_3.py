"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Program generates as many terms needed to approximate the function
    to a specifed level of accuracy and prints the number of terms it 
    took.

Assignment Information:
    Assignment:     Py3 Team 3 b
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
import sys
#print(sys.getrecursionlimit())
sys.setrecursionlimit(3000)
from py3_team_2_b_3 import my_factorial
import math

def maclaurinSeries(x,n):
    return 1 if n == 0 else (x ** n) / my_factorial(n) + maclaurinSeries(x,n - 1)

def main():
    
    x = float(input("Enter the value of x: "))
    targetError = float(input("Enter the target error threshold: "))
    error = 100
    n = 0
    actual = math.exp(x)
    while abs(error) > 0.01 * targetError:
        n += 1
        approx = maclaurinSeries(x, n)
        error = (approx - actual)/actual
        #print(f'approx: {approx}, actual: {actual}, error: {error}, n: {n}')
    print(f'Terms needed: {n+1}')
    print(f"Actual value: {actual:.2f}")
    print(f"Approximate value: {approx:.2f}")
    print(f"Target error threshold: {targetError:.1f}%")
 #Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
#Nullam sit amet suscipit sem, non hendrerit lorem. 
#Integer ut lacus augue. Maecenas dignissim erat ligula, eu viverra libero mollis ut. 
#Ut id hendrerit dui, at auctor est. 
#Ut felis lacus, vulputate vel lorem eget, viverra suscipit leo.    


if __name__ == "__main__":
    main()
