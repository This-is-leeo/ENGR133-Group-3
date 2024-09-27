"""
Course Number: ENGR 13300
Semester: e.g. Fall 2024

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     8.2.3 Team Task 3
    Team ID:        LC18 03
    Author:         Leo Yu, yu1398@purdue.edu
                    Megan Puntney, mpuntney@purdue.edu
                    Megan Raupp, mraupp@purdue.edu
                    Sarah Kaufman, kaufman62@purdue.edu
    Date:           9/26/2024

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
import os
import numpy as np

def main():
    current_folder = os.path.dirname(os.path.abspath(__file__)) #gets current folder for auto grader
    input_path = os.path.join(current_folder,'py4_task3_input.txt') #set path to find input file 
    data = np.genfromtxt(input_path, delimiter=': ', dtype=str)
    data = {str(data[i][0]).strip() : [str(data[n][1]).strip() for n in range(len(data)) if data[n][0] == data[i][0]] for i in range(len(data))}
    #^this mess of a code will sort out the list we get from np.genfromtext to a organized dictionary
    #print(data) #<- trying running this if confused

    absorb_calc = lambda molar_extinction_coefficient, absorbency , path_length: path_length * absorbency / molar_extinction_coefficient 
    #^creates a function absorb_calc() that takes three parameters and return the concentration :)
    print(f'The name of the substance is {data.get("Name")[0]}')
    for absorbency in data.get('Absorbancy'):
        concentration = absorb_calc(float(data.get("Molar Extinction Coefficient")[0]), float(absorbency), float(data.get("Path length")[0]))
        #calculates the concentration
        print(f'For {absorbency} absorbency value, the concentration is {concentration:.7f}')
        #Prints everything

if __name__ == "__main__":
    main()
