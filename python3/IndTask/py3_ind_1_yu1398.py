"""
Course Number: ENGR 13300
Semester: e.g. Fall 2024

Description:
    maps the chromosome combinations to their respective phenotypes using the provided flowchart.

Assignment Information:
    Assignment:     7.3.1 py3 Ind 1 py3task6 for auto grader becasue the number is wrong
    Team ID:        LC18 03
    Author:         Leo Yu, yu1398@purdue.edu
    Date:           9/24/2024

Contributors:
    Meagan Puntney mpuntney@purdue.edu

    My contributor(s) helped me:
    [x] understand the assignment expectations without
        telling me how they will approach it.
    [x] understand different ways to think about a solution
        without helping me plan my solution.
    [x] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:   I have not used source code obtained from any other unauthorized
  source, either modified or unmodified. Neither have I provided
  access to my code to another. The project I am submitting
  is my own original work.
"""

import matplotlib.pyplot as plt
import numpy as np
import os


def invalidResult():
    print('Invalid input.')

def runAgain():
    option = input('Would you like to run again? (y or n): ')
    if option != 'y' and option != 'n':
        invalidResult()
        return runAgain()
    return True if option == 'y' else False

def main():
    current_folder = os.path.dirname(os.path.abspath(__file__))
    inputPath = os.path.join(current_folder, 'list_of_features.csv')
    run_again = True
    data = np.genfromtxt(inputPath, delimiter=',', dtype=str, skip_header=1)
    avilGenotypes = {data[i][0].strip(): [[data[n][3].strip(), data[n][5].strip()] for n in range(i, i+int(data[i][4]))] for i in range(len(data)) if data[i][0].strip() != ''}
    while(run_again):
        print('AVAILABLE FEATURES:')
        print('\n'.join(avilGenotypes.keys()))     
        if (inputFeature := input("Please select a feature: ")) in avilGenotypes.keys():
            print("POSSIBLE GENOTYPES:")
            print('\n'.join(genotypes[0] for genotypes in avilGenotypes.get(inputFeature)))
            if (genotype := input('Please input the genotype: ')) in [genotypes[0] for genotypes in avilGenotypes.get(inputFeature)]:
                print(f'This corresponds to the physical attribute: {[genotypes[1] for genotypes in avilGenotypes.get(inputFeature) if genotypes[0] == genotype][0]}')
            else:
                invalidResult()
        run_again = runAgain()

if __name__ == "__main__":
    main()
