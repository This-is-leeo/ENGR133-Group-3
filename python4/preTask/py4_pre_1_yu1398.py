"""
Course Number: ENGR 13300
Semester: e.g. Fall 2024

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     8.1.2 py4 pre 1
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

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

import csv
from matplotlib import pyplot as plt
import numpy as np
import os #auto grader sucks

def main():
    current_folder = os.path.dirname(os.path.abspath(__file__)) #find current folder, to solve the stupid auto grader stuffs
    outputPath = os.path.join(current_folder, 'py4_pre_1_yu1398.csv')
    inputPath = os.path.join(current_folder, 'py4_pre_task0_data.csv')
    #establish x and y value arrays
    x_value = []
    y_value = []
    with open(inputPath , 'r', encoding='utf-8-sig') as inputData, open(outputPath, 'w') as output: #the utf 8 sig allows proper reading of the csv files
        data = csv.reader(inputData) #read the files
        for line in data:
            x_value.append(int(line[0]))
            y_value.append(int(line[1]) * 4)
            #another (harder) way is y_value = list(map(lambda y: y * 4, y_values))
            #add all values
            #print(line)
        """ The following code generates the random color showned in the website, but apperently if you include this it becomes too long :/ """
        #colors = np.random.rand((len(x_value))) #create a random color array
        plt.scatter(x_value, y_value) #, c=colors, cmap = 'plasma')
        #set proper titles etc
        plt.xlabel('Time (s)')
        plt.ylabel('Original Data * 4')
        plt.title('Py4_Pre_1_data')

        for i in range(len(x_value)):
            output.write(f'{x_value[i]},{y_value[i]}\n')

    plt.show()

if __name__ == "__main__":
    main()
