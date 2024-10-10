"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:    
This program reads the initialized file by calling the read_data function, and
reads the data from the file. The program then analyzes the data using the
data_analysis function. The data_analysis function performs the respective
operations using the data based on the flowchart logic provided. The program writes
the output data to a file that is initialized. The program prints the calculated
value to the console. 
 
Assignment Information:
    Assignment:     CQ #3
    Team ID:        LC018 - 03
    Author:         Leo Yu       yu1398@purdue.edu
    Date:           10/10/2024

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""
import os
current_folder = os.path.dirname(os.path.abspath(__file__))

def read_data(file_name):
    """Read in the CSV data file and return it as a list of lists.
    
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    YOU DO NOT NEED TO EDIT THIS FUNCTION FOR THE PURPOSES OF THIS QUIZ.
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    """
    file_name = os.path.join(current_folder, file_name)
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split(',')))
            data.append(row)
    return data


def write_out(data, output_file):
    """Write out data to a file based on its structure.

    List are written as a single column, matrices (lists of lists) are written with one
    row on each line.
    """
    output_file = os.path.join(current_folder, output_file)
    first_element = data[0]
    with open(output_file, 'w') as file:
    ####################################################################################
        if isinstance(first_element, int):  # data is a flat list
            for element in data:
                file.write(f"{element}\n")
        elif isinstance(first_element, list):  # data is a nested list
            for row in data:   
                line = ','.join(map(str, row)) + '\n'  
                file.write(line) 

########################################################################################
# Add your data_analysis function here.
########################################################################################

def data_analysis(data):
    output_data = []
    calculated_value = 0

    row_start = 0
    row_end = len(data)
    column_start = 0
    column_end = len(data[0])

    i = 0
    while i < row_end:
        new_row = []
        j = 0
        while j < column_end:
            value = data[i][j]
            new_row.append(value)
            calculated_value += abs(value)
            if calculated_value > 70000:
                output_data.append(new_row)
                
                return output_data, i+1, j+1
            j += 1
        output_data.append(new_row)
        i += 1
    return output_data, i+1, j+1

    



########################################################################################

def main():
    """Main function to read data, analyze it, write the output and print to console."""
    # Initialize the input file name
    input_filename = "CQ3_C_data.csv"

    # Call the read_data function
    data = read_data(input_filename)

    ####################################################################################
    # Call the data_analysis function with the input data as per the flowchart logic
    ####################################################################################
    output_data,row,column = data_analysis(data)
    ####################################################################################
    # Initialize the output file name
    output_filename = "CQ3_C_output.csv"

    # Call the write_out function
    write_out(output_data, output_filename) 
    print(f'Row Number of the last element summed: {row}')

    ####################################################################################
    # Print the respective variable to the console as per the paper handout
    ####################################################################################

    ####################################################################################

if __name__ == '__main__':
    main()