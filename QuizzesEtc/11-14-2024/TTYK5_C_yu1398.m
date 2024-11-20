%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Course Number: ENGR 13300
% Semester: e.g. Fall 2024
%
% % Problem Description: This main script loads the bus data and extracts the
% specific data columns from the bus data csv. It then calls the function to
% calculate the specific parameter as mentioned in the paper handout.
%
% Assignment Information
%   Assignment:     TTYK #5 Quiz
%   Version:        C#3
%   Author:         Leo Yu, yu1398@purdue.edu
%   Team ID:        LC018 - 03 (e.g. LC1 - 01; for section LC1, team 01)
%   Date:           11/14/2024
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

% 1. Load the bus data csv
data = readmatrix('Bus3.csv');

% 2. Extract the specific data column(s) from the bus data csv

engPower = data(:, 14);
gpsSpeed = data(:, 7);


% 3. Call the function to calculate the specific parameter as per the handout

TTYK5_C_func_yu1398(engPower, gpsSpeed)
