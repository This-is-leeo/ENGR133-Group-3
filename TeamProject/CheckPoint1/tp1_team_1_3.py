"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Program gets image fle from user and prepares it for message extraction.

Assignment Information:
    Assignment:     9.2.1 Team Project Task 1
    Team ID:        018 - 03
    Author:         Leo Yu, yu1398@purdue.edu
                    Megan Puntney, mpuntney@purdue.edu
                    Megan Raupp, mraupp@purdue.edu
                    Sarah Kaufman, kaufman62@purdue.edu
    Date:           10/01/2024

Contributors:
    Name, login@purdue [repeat for each]
    None
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

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

def importImage(image_name = None):
    current_folder = os.path.dirname(os.path.abspath(__file__))
    if image_name == None: image_name = input("Enter the path of the image you want to load: ")
    image_path = os.path.join(current_folder, image_name)
    return mpimg.imread(image_path),image_name

def visualize_image(img,image_name):
    print(f'Below is the img_array output of {image_name}:')
    plt.imshow(img)
    plt.show()

def main():
    visualize_image(importImage())
    

if __name__ == "__main__":
    main()
