"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    This code is used to monitor the temperature of the manufacturing process
    and display the temperature range.

Quiz Information:
    Quiz:       Mock Quiz C
    Team ID:    ### - ## (e.g. LC1 - 01; for section LC1, team 01)
    Author:     Name, login@purdue.edu

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

def main():
    
    temperature = 16    # Input temperature from the paper handout
    
    # Check the temperature range and display the result
    if temperature <= 5:
        print("Too Cold")
    elif temperature <= 15:
        print("Cold")
    elif temperature <= 25:
        print("Optimal")
    elif temperature <= 35:
        print("Warm")
    elif temperature <= 45:
        print("Hot")
    else:
        print("Too Hot")

if __name__ == "__main__":
    main()