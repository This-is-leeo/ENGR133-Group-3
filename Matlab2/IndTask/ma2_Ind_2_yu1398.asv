%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Course Number: ENGR 13300
% Semester: e.g. Fall 2024
%
% Problem Description: Add the problem description here and delete this
%                      line.
%
% Assignment Information
%   Assignment:     MA2 Task 2
%   Author:         Leo Yu, yu1398@purdue.edu
%   Team ID:        LC018-03
%   Date:           11/6/2024
%
%   Contributor:    Name, login@purdue [repeat for each]
%   My contributor(s) helped me:
%     [ ] understand the assignment expectations without
%         telling me how they will approach it.
%     [ ] understand different ways to think about a solution
%         without helping me plan my solution.
%     [ ] think through the meaning of a specific error or
%         bug present in my code without looking at my code.
%   Note that if you helped somebody else with their code, you
%   have to list that person as a contributor here as well.
%
% Academic Integrity Statement:
%     I have not used source code obtained from any unauthorized
%     source, either modified or unmodified; nor have I provided
%     another student access to my code.  The project I am
%     submitting is my own original work.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%% ____________________
%% INITIALIZATION
loan_amount = 500000;
r = 0.07; %Interest Rate
n = input("Input the number of years for repayment. ");
%% ____________________
%% CALCULATIONS
mi = r / 12; %monthly interest
fixed_payment_amount = loan_amount * (mi * (mi + 1) ^ (n * 12)) / ( (mi + 1) ^ (n * 12) - 1);
total_amount = fixed_payment_amount * n * 12;
extra_payed = total_amount - loan_amount;

for i = 1:n*12
    principle_payment = (fixed_payment_amount * (1 + mi) ^ -(n*12 - i + 1));
    interest_payment = fixed_payment_amount - principle_payment;
    if principle_payment > interest_payment
        break
    end
end


%% ____________________
%% OUTPUTS

fprintf("The principal amount is $%d.\n", loan_amount)
fprintf("The annual interest rate is %.2f%.\n", 100 * r)
fprintf("The repayment period is %d years.\n", n)
fprintf("The total amount repaid is $%2f.\n", total_amount)
fprintf("The total amount of interest paid is $%.2f.\n", extra_payed)
fprintf("The payments on the principal exceed the payments on the interest after %d months.\n", i)
%% ____________________
