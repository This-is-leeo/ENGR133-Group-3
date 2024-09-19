"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Program computes the factorial of a number given by user, and prints it out.

Assignment Information:
    Assignment:     Py3 Team 3
    Team ID:        LC 18 - 03
    Author:         Megan Puntney, mpuntney@purdue.edu
                    Megan Raupp, mraupp@purdue.edu
                    Leo Yu, yu1398@purdue.edu
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

def my_factorial(n):
    if n < 0:
        print("error! n < 0")
        return 0
    return 1 if n == 0 else n * my_factorial(n-1)
    
def main():

    easy_factorial = lambda x: 1 if x == 0 else x * easy_factorial(x-1)
    #creating a factorial function without defining it outside of main, just a useless flex

    n = int(input("Enter a number: "))
    if n < 0:
        print("Error 999 [Negative input].")
    else:
        print(f"The Factorial of {n} is {my_factorial(n)}")

if __name__ == "__main__":
    main()
