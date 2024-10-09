"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Program converts a binary string into ASCII text.

Assignment Information:
    Assignment:     9.2.1 Team Project Task 3
    Team ID:        018 - 03
    Author:         Leo Yu, yu1398@purdue.edu
                    Megan Puntney, mpuntney@purdue.edu
                    Megan Raupp, mraupp@purdue.edu
                    Sarah Kaufman, kaufman62@purdue.edu
    Date:           10/03/2024

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

from tp1_team_2_3 import *

def convert_to_list(extracted_message):
    return [extracted_message[i:i+8] for i in range(0, len(extracted_message), 8)]
def convert_text(extracted_message = None):  
    extracted_message = convert_to_list(extracted_message)   
    ans = ''
    for i in extracted_message:
        i = int(i,2)
        ans += chr(i)  
    print(f'Converted Text: {ans}')
    return ans
def main():
    """
    binary_number = input("Enter the binary message: ")
    convert_text(binary_number)
    for the sample userinput
    """
    img,image_message = importImage()
    
    if (extracted_message := extract_message(img)) != None:
        visualize_image(img, image_message)
        convert_text(extracted_message)
    else:
        visualize_image(img, image_message)
        print('Start or end sequence not found in the image.')


if __name__ == "__main__":
    main()
