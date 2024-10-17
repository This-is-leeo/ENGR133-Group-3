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
    mixuan pan 
    panFORGOTNUMBER@purdue.edu

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



def encipher(method=None, text=None, key=None, printout = False):
    method = method if method is not None else input("Enter the cipher you want to use for encryption: ")
    text = text if text is not None else input("Enter the plaintext you want to encrypt: ")
    key = key if key is not None else input("Enter key: ")
    
    
    if (method.lower()).strip() == 'caesar':
        encrypted_message = caesarCiphertoString(text,key)
        if printout: print(f'Encrypted Message using Caesar Cipher: {encrypted_message}')
    elif (method.lower()).strip() == 'xor':
        encrypted_message = xorCiphertoString(text,key)
        if printout: print(f'Encrypted Message using XOR Cipher: {encrypted_message}')
    elif (method.lower()).strip() == 'vigenere':
        encrypted_message = vigenereCipherToString(text,key)
        if printout: print(f'Encrypted Message using Vigenere Cipher: {encrypted_message}')
    return encrypted_message

def binaryOfFullMessage(encrypted_message = None, start_sequence = None, end_sequence = None ):
    start_sequence = start_sequence if start_sequence is not None else input("Enter start sequence: ")
    end_sequence = end_sequence if end_sequence is not None else input("Enter end sequence: ")
    binary_of_start = ' '.join(i for i in toBinary(start_sequence))
    binary_of_end = ' '.join(i for i in toBinary(end_sequence))
    binary_of_message = ' '.join(i for i in toBinary(encrypted_message))

    
    return binary_of_start + ' '  + binary_of_message + ' ' + binary_of_end

def encryptMessageInImage(binary_message = None, offset = None,  input_image_path = None, output_image_path = None):
    offset = offset if offset is not None else input("Enter offset: ")
    offset = int(offset)
    input_image_path = input_image_path if input_image_path is not None else input("Enter input path: ")
    output_image_path = output_image_path if output_image_path is not None else input("Enter output path: ")

    input_image = importImage(input_image_path)
    image_shape = list(input_image.shape)
    if not checkGrayscale(input_image):
        if image_shape[2] == 4:
            image_shape[2] = 3
                #why do this class hate us!
    total_bits = 1
    for i in image_shape:
        total_bits *= i
    binary_message = binary_message.replace(' ','')
    if len(binary_message) + offset > total_bits:
        print('Given message is too long to be encoded in the image.')
        return None
    if checkGrayscale(input_image):
        output_image = input_image[:,:]
        index_of_string = -offset
        for row in range(image_shape[0]):
            for pixel in range(image_shape[1]):
                if index_of_string < len(binary_message) and index_of_string >= 0:
                    binary_value_of_bit = str(format(int(input_image[row,pixel]) , '08b'))
                    binary_value_of_bit = binary_value_of_bit[:-1] + binary_message[index_of_string]
                    #print(binary_value_of_bit)
                    output_image[row,pixel] = int(binary_value_of_bit, 2)
                    
                index_of_string += 1

        output_image = output_image.astype(np.uint8)
        pil_image = Image.fromarray(output_image, mode= 'L')
        pil_image.save(os.path.join(current_folder, 'images', output_image_path))
        print(f'Message successfully encoded and saved to: {output_image_path}')
        return output_image
    else:
        output_image = input_image[:,:,:3]
        index_of_string = -offset
        for row in range(image_shape[0]):
            for pixel in range(image_shape[1]):
                for bit in range(image_shape[2]):
                    if index_of_string < len(binary_message) and index_of_string >= 0:
                        binary_value_of_bit = str(format(int(input_image[row,pixel,bit]) , '08b'))
                        binary_value_of_bit = binary_value_of_bit[:-1] + binary_message[index_of_string]
                        #print(binary_value_of_bit)
                        output_image[row,pixel,bit] = int(binary_value_of_bit, 2)
                    index_of_string += 1

        output_image = output_image.astype(np.uint8)
        pil_image = Image.fromarray(output_image, mode = 'RGB')
        pil_image.save(os.path.join(current_folder, 'images', output_image_path))
        print(f'Message successfully encoded and saved to: {output_image_path}')
        return output_image
    



def main():
    try:
        cipher = input("Enter the cipher you want to use for encryption: ")
        plaintext = input("Enter the plaintext you want to encrypt: ")
        key = input("Enter the key for the cipher: ")
        start_sequence = input("Enter the start sequence: ")
        end_sequence = input("Enter the end sequence: ")
        bit_offset = input("Enter the bit offset before you want to start encoding: ")
        input_image_path = input("Enter the path of the input image: ")
        encoded_image_path = input("Enter the path for your encoded image: ")
        comparison_image_path = input("Enter the path of the image you want to compare: ")

        encrypted_message = encipher(cipher, plaintext,  key, printout=True)

        full_binary = binaryOfFullMessage(encrypted_message, start_sequence, end_sequence)

        output_image = encryptMessageInImage(full_binary, bit_offset, input_image_path, encoded_image_path)
        print(f'Binary output message: {full_binary}')
        
        visualizeImage(output_image)

        compare_image(encoded_image_path, comparison_image_path, printout = True)
    except Exception as e:
        print(f"An error occurred: {e}")
        #but idgaf!

if __name__ == "__main__":
    main()
