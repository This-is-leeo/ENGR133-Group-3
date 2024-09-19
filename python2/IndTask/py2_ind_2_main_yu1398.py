"""
Course Number: ENGR 13300
Semester: e.g. Fall 2024

Description:
    A swimming pool manufacturer has asked me to develop a pool volume calculator for their customers, so i did!
    

Assignment Information:
    Assignment:     6.3.1 py2 ind 2 main
    Team ID:        LC18 group 3
    Author:         Leo Yu, yu1398@purdue.edu
    Date:           9/15/2024

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
from py2_ind_2_functions_yu1398 import *
def inputData():
    L1 = float(input('Enter the surface length or radius. ' ))
    L2 = float(input('Enter the surface width or bottom radius. '))
    Ds = float(input('Enter the shallow end depth. '))
    Dd = float(input('Enter the deep end depth. '))
    return L1, L2, Ds, Dd
def checkData(L1, L2, Ds, Dd):
    if L1 < 0 or L2 < 0 or Ds < 0 or Dd < 0:
        print("Please enter valid dimensions.")
        return False
    return True
def main():
    name = input("Enter the name of the pool to calculate (Standard, Ramp, or Round): ")
    #thanks for not telling us about the value use for conversion
    #OMG first actual comment?^
    match name:
        case 'Standard':
            L1, L2, Ds, Dd = inputData()
            if checkData(L1,L2,Ds,Dd):
                print("The volume of the Standard pool with your dimensions is {:,.2f} gallons.".format(standard(L1, L2, Ds, Dd)))
        case 'Ramp':
            L1, L2, Ds, Dd = inputData()
            if checkData(L1,L2,Ds,Dd):
                print("The volume of the Ramp pool with your dimensions is {:,.2f} gallons.".format(ramp(L1, L2, Ds, Dd)))
        case 'Round':
            L1, L2, Ds, Dd = inputData()
            if checkData(L1,L2,Ds,Dd):
                print("The volume of the Round pool with your dimensions is {:,.2f} gallons.".format(round(L1, L2, Ds, Dd)))
        case _:
            print("Please run the program again and enter a valid pool name.")
#Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
#Nullam sit amet suscipit sem, non hendrerit lorem. 
#Integer ut lacus augue. Maecenas dignissim erat ligula, eu viverra libero mollis ut. 
#Ut id hendrerit dui, at auctor est. 
#Ut felis lacus, vulputate vel lorem eget, viverra suscipit leo. 
if __name__ == "__main__":
    main()
