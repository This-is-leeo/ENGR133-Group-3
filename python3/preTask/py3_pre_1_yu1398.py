"""
Course Number: ENGR 13300
Semester: e.g. Fall 2024

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     7.1.2 Py3 Pre 1 
    Team ID:        LC18 03
    Author:         Leo Yu, yu1398@purdue.edu
    Date:           09/12/2024

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
import numpy as np

def main():
    X = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    r = 0
    c = 0
    for row in X:
        for y in row:
            print(f'X[{r},{c}] = {y}')
            c += 1
        r += 1
        c = 0

    r = 0
    c = 0

    print("WHILE loop:")
    while r < 3:
        while c < 3:
            print(f'X[{r},{c}] = {X[r,c]}')
            c += 1
        r += 1
        c = 0

        


            
    


if __name__ == "__main__":
    main()
