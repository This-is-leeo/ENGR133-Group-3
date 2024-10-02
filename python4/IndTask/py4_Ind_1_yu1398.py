"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     8.3.1 Ind Task 1
    Team ID:        LC18 3
    Author:         Leo Yu yu1398@purdue.edu
    Date:           9/28/2024

Contributors:
    Megan Puntney, mpuntney@purdue.edu
    Megan Raupp, mraupp@purdue.edu
    Sarah Kaufman, kaufman62@purdue.edu

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

from pathlib import Path
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt


def load_image(directory):
    """
    Loads All the image from a directory, only jpeg becasue that is what this class uses

    Parameters:
    directory (str): The string of the directory

    returns:
    A list of tuples, each containing an image loaded into a numpy array and its filename.
    """
    directory = Path(directory)
    images = list(directory.glob("*.jpeg"))
    return [cv2.imread(str(image_path)) for image_path in images]   

def anayze_red_content(image):
    average = lambda lst: sum(lst)/len(lst)
    total_list = []
    for row in image[:,:,0] * 0.299:
        for column in row:
            total_list.append(int(column))
    print(f'{average(total_list)*2:.2f}')

def generate_visualizations(images):
    for image in images:
        plt.figure()  # Create a new figure
        test = 'test'
        if image.ndim == 2:  # Check if the image is grayscale
            # Plot histogram for grayscale image
            plt.hist(image.flatten(), bins=256, color='gray', alpha=0.7, label='Intensity')
            plt.title(f'Intensity Histogram - {test}')  # Set the title of the histogram

        elif image.ndim == 3:  # Check if the image is color
            # Plot histograms for each color channel and the total intensity
            plt.hist(image.flatten(), bins=256, color='orange', alpha=0.5, label='Total')
            ### Start of your code

            ### End of your code
            plt.title(f'Color Histogram - {test}')  # Set the title of the histogram
        plt.xlabel('Intensity')  # Label the x-axis
        plt.ylabel('Frequency')  # Label the y-axis
        plt.legend()  # Display the legend
        plt.savefig('Histogram.png')  # Show the plot
        plt.show()
    
def main():
    current_folder = os.path.dirname(os.path.abspath(__file__)) 
    images = load_image(current_folder)
    anayze_red_content(images[0])
    generate_visualizations(images)
    
    
        
if __name__ == "__main__":
    main()
