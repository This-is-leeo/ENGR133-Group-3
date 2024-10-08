"""
Course Number: ENGR 13300
Semester: e.g. Fall 2024

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     8.2.2
    Team ID:        LC18 03
    Author:         Leo Yu, yu1398@purdue.edu
                    Megan Puntney, mpuntney@purdue.edu
                    Megan Raupp, mraupp@purdue.edu
                    Sarah Kaufman, kaufman62@purdue.edu
    Date:           9/26/2024

Contributors:


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
import os

def calculateAge(age,days):
    daysPerYear = 365.242199
    return age + days/daysPerYear

def yearToSeconds(years):
    return round(years * 365.242199 * 24 * 3600)

def main():
    #define Path (doesn't need to be in the flow chart)
    currentFolder = os.path.dirname(os.path.abspath(__file__)) 
    outputPath = os.path.join(currentFolder,'py4_team_2_3.txt')
    #input from users
    lastName = input('Enter your last name:\n')
    firstName = input('Enter your first name:\n')
    ageInYears = float(input('Enter your age in whole years:\n'))
    daysSinceBirthday = float(input('Enter the days elapsed since your last birthday:\n'))
    exactAge = calculateAge(ageInYears,daysSinceBirthday)
    ageInSeconds = yearToSeconds(exactAge)

    with open(outputPath, 'w') as output:
        output.write(f'{firstName} {lastName}\n')
        output.write(f'You are {exactAge} years old\n')
        output.write(f'You are {ageInSeconds} seconds old.')
    

if __name__ == "__main__":
    main()
