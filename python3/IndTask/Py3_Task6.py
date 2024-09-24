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

Academic Integrity Statement:   I have not used source code obtained from any other unauthorized
  source, either modified or unmodified. Neither have I provided
  access to my code to another. The project I am submitting
  is my own original work.
"""

import matplotlib.pyplot as plt
import numpy as np
import os
import csv
def invalidResult():
    print('Invalid input.')

def runAgain():
    
    option = input('Would you like to run again? (y or n): ')

    print(option)
    if option != 'y' and option != 'n':
        return invalidResult()
    return True if option == 'y' else False

def main():
    current_folder = os.path.dirname(os.path.abspath(__file__))
    inputPath = os.path.join(current_folder, 'list_of_features.csv')
    run_again = True
    with open(inputPath, 'r', encoding='utf-8-sig') as data:
        fullList = list(csv.reader(data))
        fullList.pop(0) #removing the first line of the data
        
        avilFeatures = []
        avilGenotypes = []
        n = -1 #n is the number of feature currently on
        for i in range(len(fullList)):#good luck reading this, i dont think anyone can read this(for comment count)
            if fullList[i][0] != '':
                avilFeatures.append(fullList[i][0])
                n = n + 1
                avilGenotypes.append([])
            avilGenotypes[n].append([fullList[i][3],fullList[i][5]])
        while(run_again):
            attribute = None
            featureNum = None
            print('AVAILABLE FEATURES:')
            for feature in avilFeatures:
                print(feature)
            inputFeature = input("Please select a feature: ")
            for i in range(len(avilFeatures)):
                featureNum = i if inputFeature == avilFeatures[i] else featureNum
            if featureNum != None:
                possibleGenotype = avilGenotypes[featureNum]
                print("POSSIBLE GENOTYPES:")
                for str in possibleGenotype:
                    print(str[0])
                genotype = input('Please input the genotype: ') 
                for i in range(len(possibleGenotype)):
                    attribute = possibleGenotype[i][1] if possibleGenotype[i][0] == genotype else attribute
                if attribute != None:
                    print(f'This corresponds to the physical attribute: {attribute}')
                    run_again = runAgain()
                else:
                    invalidResult()
                    run_again = runAgain()
            else:
                invalidResult()
                run_again = runAgain()
        


if __name__ == "__main__":
    main()
