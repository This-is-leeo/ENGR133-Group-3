"""
Course Number: ENGR 13300
Semester: e.g. Fall 2024

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     8.3.2 Ind Task 2
    Team ID:        LC18 3
    Author:         Leo Yu yu1398@purdue.edu
    Date:           9/28/2024

Contributors:
    Megan Puntney mpuntney@purdue.edu

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

def atbash_cipyer(str):
    encrypted_message = ''
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
           encrypted_message += chr(ord('z') - (ord(char)-ord('a')))
        elif ord(char) >= ord('A') and ord(char) <= ord('Z'):
           encrypted_message += chr(ord('Z') - (ord(char)-ord('A')))
        elif ord(char) >= ord('1') and ord(char) <= ord('9'):
           encrypted_message += chr(ord('9') - (ord(char)-ord('1')))
        else:
            encrypted_message += char
    return encrypted_message
    #Explaination for the flowchart :)
    #for each character, converts the char to ascii table value
    #then check if it is within the range we want to change for example: 'a - z'
    #lastly converts it from 'a' to 'z' or 'B' to 'Y' etc
    # :)

def main():
    current_folder = os.path.dirname(os.path.abspath(__file__)) 
    atbash_cipher_but_in_one_line = lambda s: ''.join(map(lambda char: chr(ord('z') - (ord(char) - ord('a'))) if 'a' <= char <= 'z' else chr(ord('Z') - (ord(char) - ord('A'))) if 'A' <= char <= 'Z' else chr(ord('9') - (ord(char) - ord('0'))) if '0' <= char <= '9' else char, s))
    #gotta flex on the TA, 
    #Is this 'crazy' enough
    try:
        with open(os.path.join(current_folder, str(input('Enter the name of the file: '))), 'r') as input_file:
            text = input_file.read()
            encrypted_message = atbash_cipher_but_in_one_line(text)
            print(f'The encrypted message is: {encrypted_message}')
            with open(os.path.join(current_folder, 'output_file2.txt') , 'w') as output_file:
                output_file.write(encrypted_message)
                print('Encryption completed. Check the output files for results.')

    except FileNotFoundError:
        print("The file was not found. Put the RIGHT file name, maybe...")
    except Exception as e:
        print(e)




if __name__ == "__main__":
    main()
