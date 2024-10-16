"""
Course Number: ENGR 13300
Semester: e.g. Fall 2024

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     11.1.1 Team Project Demo
    Team ID:        018 - 03
    Author:         Leo Yu
    Date:           10/12/2024

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

from tp3_image_functions import *
from tp3_ciphers import *

def task1(self, method=None, text=None, key=None, start_sequence=None, end_sequence=None, offset=None, input_path=None, output_path=None):
    method = method if method is not None else input("Enter the cipher you want to use for encryption: ")
    text = text if text is not None else input("Enter the plaintext you want to encrypt: ")
    key = key if key is not None else input("Enter key: ")
    start_sequence = start_sequence if start_sequence is not None else input("Enter start sequence: ")
    end_sequence = end_sequence if end_sequence is not None else input("Enter end sequence: ")
    offset = offset if offset is not None else input("Enter offset: ")
    input_path = input_path if input_path is not None else input("Enter input path: ")
    output_path = output_path if output_path is not None else input("Enter output path: ")

    if (method.lower()).strip() == 'caesar':
        encrypted_message = caesarCiphertoString(text,key)
    elif (method.lower()).strip() == 'xor':
        encrypted_message = xorCiphertoString(text,key)
    elif (method.lower()).strip() == ''





def main():
    task1('xor')





if __name__ == "__main__":
    main()
