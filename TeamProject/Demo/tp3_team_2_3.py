"""
Course Number: ENGR 13300
Semester: e.g. Fall 2024

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     11.1.1 Team Project Demo
    Team ID:        018 - 03
    Author:         Leo Yu
    Date:           10/17/2024

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

from PIL import Image
from tp3_image_functions import *
from tp3_ciphers import *

def extractMessageFromImage(image_path, start_sequence, end_sequence):

    flattend_image = importImage(image_path).flatten()
    lsb_values = [int(format(int(i), '08b')[-1]) for i in flattend_image]
    lsb_str = ''.join( str(n) for n in lsb_values)
    binary_of_start = ''.join(toBinary(start_sequence))
    
    binary_of_end = ''.join(toBinary(end_sequence))
    if binary_of_start in lsb_str and binary_of_end in lsb_str:
        encrypted_starting_value = lsb_str.index(binary_of_start) + len(binary_of_start)
        lsb_str = lsb_str[encrypted_starting_value:]
        encrypted_end_value = lsb_str.index(binary_of_end)
        encrypted_message = lsb_str[:encrypted_end_value]
        print(f'Extracted Binary Message: {encrypted_message}')
        return encrypted_message
    else:
        return None
def main():
    cipher = 'vigenere'
    key = 'is fun'
    #cipher = input("Enter the cipher you want to use for encryption: ").strip().lower()
    # key = input("Enter the key for the cipher: ")
    # start_seq = input("Enter the start sequence: ")
    # end_seq = input("Enter the end sequence: ")
    # input_image_path = input("Enter the path of the input image: ").strip()
    print(vigenereCipherDecryption('Usmm 489', 'is fun'))
    extracted_binary = extractMessageFromImage('ref_col_v.png', '31', '&&')
    extracted_binary_message = convertToText(extracted_binary)
    print(f'Converted Binary Text: {extracted_binary_message}')
    if(cipher == 'xor'):
        extracted_message = xorCipherDecryption(extracted_binary_message, key)
    elif(cipher == 'vigenere'):
        extracted_message = vigenereCipherDecryption(extracted_binary_message, key)
    elif(cipher) == 'caesar':
        extracted_message = caesarCipherDecryption(extracted_binary_message, key)
    print(f'Converted text: {extracted_message}')
    print(ord(' '))




if __name__ == "__main__":
    main()
