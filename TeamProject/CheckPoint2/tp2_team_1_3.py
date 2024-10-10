"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     10.2.1
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
    submitting is my own original work. Sure...
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from tp2_3_fun import *

def compare_image(input_file_name_1 = None, input_file_name_2 = None, output_file_name = 'diff.png'):
    image1 = importImage(input_file_name_1)
    image2 = importImage(input_file_name_2)
    image1 = image1[:,:,:3]
    image2 = image2[:,:,:3]
    
    if checkGrayscale(image1) != checkGrayscale(image2):
        print('Cannot compare images in different modes (RGBA and L).')
        return False
    if image1.shape[0] != image2.shape[0] or image1.shape[1] != image2.shape[1]:
        #print('The images are different.')
        return False
    
    identical = True
    #when it is not a grayscale image
    if not checkGrayscale(image1) and not checkGrayscale(image2):
        difference_image = np.zeros(image1.shape)
        for row in range(difference_image.shape[0]):
            for pixel in range(difference_image.shape[1]):
                for bit in range(difference_image.shape[2]):
                    if image1[row,pixel,bit] != image2[row,pixel,bit]:
                        difference_image[row,pixel,bit] = 255
                        identical = False
                    if bit == 3: difference_image[row,pixel,bit] = 255
                    #for some image there is a 4th pixel for brightness, lowkey dumb af

    elif len(image1.shape) == 3:
        difference_image = np.zeros(image1.shape)
        for row in range(difference_image.shape[0]):
            for pixel in range(difference_image.shape[1]):
                if image1[row,pixel,0] != image2[row,pixel,0]:
                    difference_image[row,pixel,0] = 255
                    identical = False
        
    else:
        difference_image = np.zeros(image1.shape)
        for row in range(difference_image.shape[0]):
            for pixel in range(difference_image.shape[1]):
                if image1[row,pixel] != image2[row,pixel]:
                    difference_image[row,pixel] = 255
                    identical = False

    visualize_image(difference_image, save_path=output_file_name)
    return identical
                    
    

def main():
    #visualize_image(importImage('ref_col.png'))
    if not compare_image():
        print('The images are different.')
    else:
        print("The images are the same.")


if __name__ == "__main__":
    main()
