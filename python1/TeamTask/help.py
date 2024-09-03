"""
Course Number: ENGR 13300
Semester: e.g. Fall 2024

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     e.g. 5.2.2 Py1 Team 
    Team ID:         018 - 03 
    Author:         Leo Yu yu1398@purdue.edu, Megan Puntney  mpuntney@purdue.edu, Sarah Kaufman kaufman62@purdue.edu, Megan Raupp mraupp@purdue.edu
    Date:           9/3/2024

Contributors:
    Leo Yu yu1398@purdue.edu
    Megan Puntney puntney@purdue.edu
    Sarah Kaufman kaufman62@purdue.edu
    Megan Raupp mraupp@purdue.edu
    My contributor(s) helped me:
    [x ] understand the assignment expectations without
        telling me how they will approach it.
    [x ] understand different ways to think about a solution
        without helping me plan my solution.
    [x ] think through the meaning of a specific error or
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

import random
import fractions

def main():
    random.seed(int(input("Enter the seed: ")))
    
    random1 = round(random.uniform(0, 100),3)
    random2 = round(random.uniform(10, 50),3)
    random3 = round(random.uniform(20, 40),3)
    random4 = round(random.uniform(100, 200),3)
    print("First Random Number : ", random1)
    print("Second Random Number : ", random2)
    print("Third Random Number : ", random3)
    print("Fourth Random Number : ", random4)
    sum = random1 + random2 + random3 + random4
    print("Sum from decimal: ", random1, " + ", random2, " + ", random3, "+", random4, "=", sum)
    f1 = fractions.Fraction.from_float(random1)
    f2 = fractions.Fraction.from_float(random2)
    f3 = fractions.Fraction.from_float(random3)
    f4 = fractions.Fraction.from_float(random4)

    f1 = f1.limit_denominator(100)
    f2 = f2.limit_denominator(100)
    f3 = f3.limit_denominator(100)
    f4 = f4.limit_denominator(100)
    fSum = f1 + f2 + f3 + f4
    fSum = fSum.limit_denominator(100)
    print(f"Sum from fractions: {f1} + {f2} + {f3} + {f4} = {fSum}")
    
    
    

if __name__ == "__main__":
    main()
