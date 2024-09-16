"""
Course Number: ENGR 13300
Semester: e.g. Fall 2024

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     6.3.1 Team Task 1
    Team ID:        018 - 03
    Author:         Leo Yu yu1398@purdue.edu
    Date:           09/10/2024

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

#guys, I love commenting on my programs becasue I can leave a message to whoever reads my code <3

def check_status(temperature, pressure):
    criticalValues = [304.2, 344.14, 73.8, 137] #constant 
    criticalValues[3] *= 0.95
    criticalValues[1] *= 0.95
    if temperature == criticalValues[0] or pressure == criticalValues[2]:
        print("CO2 is at the critical point.")
        return

    if temperature < criticalValues[0]:
        print(f"CO2 is below the critical temperature.\nIncrease the temperature by at least {criticalValues[0] - temperature} Kelvin.")
    elif temperature > criticalValues[1]:
        print(f"Warning! Reduce the temperature!\nDecrease the temperature by at least {0 - criticalValues[1] + temperature:.2f} Kelvin.")
    else:
        print('Temperature is within safe operating coditions.')

    if pressure < criticalValues[2]:
        print(f"CO2 is below the critical pressure.\nIncrease the pressure by at least {criticalValues[2] - pressure} Kelvin.")
    elif pressure > criticalValues[3]:
        print(f"Warning! Reduce the pressure!\nDecrease the pressure by at least {0 - criticalValues[3] + pressure:.2f} Kelvin.")
    else:
        print('Pressure is within safe operating coditions.')
    return




def main():
    temp = float(input("Enter the temperature of carbon dioxide in Kelvin: "))
    #the temp check thingy, (hopefully there is enough comments, i will come back)
    if temp < 0:
        print("Error: Please enter a valid temperature.")
    else:
        pres = float(input("Enter the pressure of carbon dioxide in bar: "))
        if pres < 0:
            print("Error: Please enter a valid pressure.")
        else:
            check_status(temp, pres)

if __name__ == "__main__":
    main()
