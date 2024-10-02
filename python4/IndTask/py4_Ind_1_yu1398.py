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
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

current_folder = os.path.dirname(os.path.abspath(__file__)) 

def load_image(directory):
    directory = Path(directory)
    images = list(directory.glob("*.jpeg"))
    return [(mpimg.imread(str(image_path)), image_path.name) for image_path in images]   

def analyze_red_content(image):
    if image.ndim == 2: return 0.0
    average = lambda lst: sum(lst)/len(lst)
    total_list = np.array([i for i in image[:,:,0].flatten()], dtype=np.float64) 
    #There is so much points that the number overflows so 64 bit int is required
    return average(total_list)

def calculate_brightness(image):
    if image.ndim == 2: return 0.0
    average = lambda lst: sum(lst)/len(lst)
    red_list = np.array([i * 0.299 for i in image[:,:,0].flatten()], dtype=np.float64) 
    green_list = np.array([i * 0.587 for i in image[:,:,1].flatten()], dtype=np.float64)
    blue_list = np.array([i  * 0.114 for i in image[:,:,2].flatten()], dtype=np.float64)
    return (average(red_list) + average(blue_list) + average(green_list))
    

def write_result(filename, images):
    for image_with_name in images:
        brightness = calculate_brightness(image_with_name[0])
        red_content = analyze_red_content(image_with_name[0])
        with open(os.path.join(current_folder, filename), 'w') as output_file:
            output = f'{image_with_name[1]}: Brightness: {brightness:.2f}, Red Content: {red_content:.2f}'
            output_file.write(output)
            print(output)
            #print(f'output saved to file{filename}')

def generate_visualizations(images):
    image = images[0]
    name = images[1]
    #idk why my formatting is weird but this does the trick
    plt.figure()  # Create a new figure
    if image.ndim == 2:  # Check if the image is grayscale
        # Plot histogram for grayscale image
        plt.hist(image.flatten(), bins=256, color='gray', alpha=0.7, label='Intensity')
        plt.title(f'Intensity Histogram - {name}')  # Set the title of the histogram

    elif image.ndim == 3:  # Check if the image is color
        # Plot histograms for each color channel and the total intensity
        plt.hist(image.flatten(), bins=256, color='orange', alpha=0.5, label='Total')
        #here is the code you need
        plt.hist(image[:,:,0].flatten(), bins = 256, color = 'r',alpha = 0.5, label = 'Red')
        plt.hist(image[:,:,1].flatten(), bins = 256, color = 'g',alpha = 0.5, label = 'Green')
        plt.hist(image[:,:,2].flatten(), bins = 256, color = 'b',alpha = 0.5, label = 'Blue')

        plt.title(f'Color Histogram - {name}')  # Set the title of the histogram
    plt.xlabel('Intensity')  # Label the x-axis
    plt.ylabel('Frequency')  # Label the y-axis
    plt.legend()  # Display the legend
    plt.savefig('Histogram.png')  # Show the plot
    plt.show()
    
def main():
    images = load_image(os.path.join(current_folder, str(input('Enter the path of the image folder: '))))
    write_result('output_file.txt', images)
    for image_with_name in images:
        generate_visualizations(image_with_name)
        
if __name__ == "__main__":
    main()
