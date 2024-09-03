"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Design a program with user-defined functions
Assignment Information:
    Assignment:     5.2.3 Py1 Team 3 
    Team ID:        018 - 03 
    Author:         Leo Yu yu1398@purdue.edu, Megan Puntney  mpuntney@purdue.edu, Sarah Kaufman kaufman62@purdue.edu, Megan Raupp mraupp@purdue.edu
    Date:           09/03/2024

Contributors:
    Leo Yu yu1398@purdue.edu
    Megan Puntney  mpuntney@purdue.edu
    Sarah Kaufman kaufman62@purdue.edu
    Megan Raupp mraupp@purdue.edu
    
    My contributor(s) helped me:
    [ x] understand the assignment expectations without
        telling me how they will approach it.
    [ x] understand different ways to think about a solution
        without helping me plan my solution.
    [ x] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

""" Write any import statements here (and delete this line)."""

def turbine_power(rho, A, Cp, v):
    power = 0.5 * rho * A * Cp * v**3   
    return power

def accumulated_energy(power, t):
    energy = power * t
    return energy

def vehicle_distance(energy, epsilon):
    distance = energy * epsilon
    return distance

def main():
    testCase1 = [1.2,400,0.3,6,1,0.007]
    testCase2 = [1.2,2500,0.3,4,5,0.007]
    rho, A, Cp, v, t, epsilon =  testCase1 #change the case for different output
    power = turbine_power(rho, A, Cp, v)
    energy = accumulated_energy(power, t)
    distance = vehicle_distance(energy, epsilon)
    print(f"The turbine generates {power} W, which accumulated {energy} Wh of energy. The vehicle has a range of {distance} km")

if __name__ == "__main__":
    main()
