"""
Course Number: ENGR 13300
Semester: e.g. Fall 2024

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     10.2.3
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
from tp2_team_2_3 import encryptMessageToBinary
from PIL import Image

def encryptMessageInImage(binary_message, input_image_path, output_image_path):
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
    if len(binary_message) > total_bits:
        print('Given message is too long to be encoded in the image.')
        return None
    if checkGrayscale(input_image):
        output_image = input_image[:,:]
        index_of_string = 0
        for row in range(image_shape[0]):
            for pixel in range(image_shape[1]):
                if index_of_string < len(binary_message):
                    binary_value_of_bit = str(format(int(input_image[row,pixel]) , '08b'))
                    binary_value_of_bit = binary_value_of_bit[:-1] + binary_message[index_of_string]
                    #print(binary_value_of_bit)
                    index_of_string += 1
                    output_image[row,pixel] = int(binary_value_of_bit, 2)
                                    
        pil_image = Image.fromarray(output_image, mode = 'L')
        pil_image.save(os.path.join(current_folder, 'output' output_image_path))
        return output_image_path
    else:
        output_image = input_image[:,:,:3]
        index_of_string = 0
        for row in range(image_shape[0]):
            for pixel in range(image_shape[1]):
                for bit in range(image_shape[2]):
                    if index_of_string < len(binary_message):
                        binary_value_of_bit = str(format(int(input_image[row,pixel,bit]) , '08b'))
                        binary_value_of_bit = binary_value_of_bit[:-1] + binary_message[index_of_string]
                        #print(binary_value_of_bit)
                        index_of_string += 1
                        output_image[row,pixel,bit] = int(binary_value_of_bit, 2)
                                    
        pil_image = Image.fromarray(output_image, mode = 'RGB')
        pil_image.save(os.path.join(current_folder, 'images', output_image_path))
        return output_image
    
        

def main():
    
    plain_text = input('Enter the plaintext you want to encrypt: ')
    key = input('Enter the key for Vigenere cipher: ')
    starting_sequence = input('Enter the start sequence: ')
    ending_sequence = input('Enter the end sequence: ')
    input_image_path = input('Enter the path of the image: ')
    output_image_path = input('Enter the path for the encoded image: ')

    # plain_text = 'hello'
    # key = 'Beau'
    # starting_sequence = '007'
    # ending_sequence = '700'
    # input_image_path = 'ref_col.png'
    # output_image_path = 'ref_col_v.png'
    
    binary_message = encryptMessageToBinary(plain_text, key, starting_sequence, ending_sequence, printout = False)
    encrypted_image = encryptMessageInImage(binary_message, input_image_path, output_image_path)
    encryptMessageToBinary(plain_text, key, starting_sequence, ending_sequence)
    visualize_image(encrypted_image)
    print(f'Message successfully encoded and saved to: {output_image_path}')


if __name__ == "__main__":
    main()
