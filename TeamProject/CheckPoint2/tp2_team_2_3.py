"""
Course Number: ENGR 13300
Semester: e.g. Fall 2024

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     10.2.2
    Team ID:        LC018 03
    Author:         Leo Yu, yu1398@purdue.edu
    Date:           10/9/2024

Contributors:
    Name, login@purdue [repeat for each]
    chatGPT.com!
    gemini.com
    siri

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
from tp2_3_fun import *

def vigenereCipher(text, key):
    #to Uppercase
    key = key.upper()

    #convert key to match length of text
    key = (key * (int(len(text)/len(key)) + 1))[:len(text)]

    #convert to numbers
    text_to_num = [ord(char) - ord('A') if ord(char) - ord('A') >= 0 and ord(char) - ord('A') < 26 else char for char in text.upper()]
    key_to_num = [ord(char) - ord('A') if ord(char) - ord('A') >= 0 and ord(char) - ord('A') < 26 else int(char) for char in key]

    decrypted_values = []
    for i in range(len(text_to_num)):
        if isinstance(text_to_num[i], int):
            if text[i].isupper():
                decrypted_values.append(chr((text_to_num[i] + key_to_num[i]) % 26 + ord('A')))
            else:
                decrypted_values.append(chr((text_to_num[i] + key_to_num[i]) % 26 + ord('a')))
        elif text_to_num[i] == ' ':
            decrypted_values.append(' ')
        else:
            decrypted_values.append((int(text_to_num[i]) + key_to_num[i]) % 10)

    return ''.join(str(i) for i in decrypted_values)

def encryptMessageToBinary(plain_text, key, starting_sequence, ending_sequence, printout = True):
    encrypted_message = vigenereCipher(plain_text, key)
    if printout: print(f'Encrypted Message using Vigenere Cipher: {encrypted_message}')
    binary_output = ' '.join(b for b in to_binary(starting_sequence) + to_binary(encrypted_message) + to_binary(ending_sequence))
    if printout: print(f'Binary output message: {binary_output}')
    return binary_output

def main():
    plain_text = input('Enter the plaintext you want to encrypt: ')
    key = input('Enter the key for Vigenere cipher: ')
    starting_sequence = input('Enter the start sequence: ')
    ending_sequence = input('Enter the end sequence: ')
    encryptMessageToBinary(plain_text, key, starting_sequence, ending_sequence)

    

if __name__ == "__main__":
    main()
