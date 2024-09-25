"""
Course Number: ENGR 13300
Semester: e.g. Fall 2024

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     7.3.2 py3 Ind2
    Team ID:        LC18 03
    Author:         Leo Yu yu1398@purdue.edu
    Date:           9/25/2024

Contributors:
    Megan Puntney   mpuntnet@purdue.edu

    My contributor(s) helped me:
    [x] understand the assignment expectations without
        telling me how they will approach it.
    [x] understand different ways to think about a solution
        without helping me plan my solution.
    [x] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""
def main():
    invalidInput = lambda: print('Error: Input a positive integer')
    factorial = lambda n: 1 if n == 0 else n * factorial(n-1)
    approx_sinx_over_x = lambda x,n : x if n == 0 else (pow(-1, n) * pow(x, 2 * n + 1)/((2 * n + 1) * factorial(2 * n + 1))) + approx_sinx_over_x(x, n - 1)
    lowerLimit = float(input('Enter the lower limit of integration: '))
    upperLimit = float(input('Enter the upper limit of integration: '))
    if (convergence := int(input('Enter the number of decimal places for convergence: '))) < 0:
        invalidInput()
        exit()
    if (maxTerm := int(input('Enter the maximum number of terms: '))) < 0:
        invalidInput()
        exit()
    print('Approximations:')
    n = 0
    count = 0
    realValue = round(approx_sinx_over_x(upperLimit, maxTerm + 10) - approx_sinx_over_x(lowerLimit, maxTerm + 10), convergence)
    while True:
        x = round(approx_sinx_over_x(upperLimit, n) - approx_sinx_over_x(lowerLimit, n), convergence)
        print(f'n = {n}: sum = {x}')
        if x - realValue == 0: count += 1
        if n+1 >= maxTerm:
            print(f'Error: The approximation did not converge to {convergence} decimal places with only {maxTerm} terms.')
            exit()
        if count == 3: break
        n += 1
    print(f'The integral from {lowerLimit} to {upperLimit} is estimated to be {realValue}.')
    print(f'Total number of terms: {n+1}')
        

if __name__ == "__main__":
    main()
