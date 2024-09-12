"""
Course Number: ENGR 13300
Semester: e.g. Fall 2024

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     6.3.1 Team Task 1
    Team ID:        018 - 03
    Author:         Leo Yu yu1398@purdue.edu
    Date:           09/10/2024

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



def check_status(temperature, pressure):
    criticalValues = [304.2, 344.14, 73.8, 137]
    if temperature < criticalValues[0]:
        print(f"CO2 is below the critical temperature.\nIncrease the temperature by at least {criticalValues[0] - temperature} Kelvin.")
    elif temperature > criticalValues[1]:
        print("Warning! Reduce the temperature!\nDecrease the temperature by at least 22.37 Kelvin.")
        


def main():
    """Write your code here (and delete this line)."""


if __name__ == "__main__":
    main()
