%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Course Number: ENGR 13300
% Semester: e.g. Fall 2024
%
% Problem Description: Add the problem description here and delete this
%                      line.
%
% Assignment Information
%   Assignment:     13.1.2 Mat Pre 2
%   Author:         Leo Yu, yu1398@purdue.edu
%   Team ID:        LC18_03
%   Date:           10/28/2024
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



%% While Loop
%% INITIALIZATION
x = 0;
%% While Loop
%% CALCULATIONS
while x < 11
    x = x + 1;
    y = 4 * x + 5;
    fprintf('The value of x = %d. The value of y = %d.\n', x, y)
end

%% For Loop
%% INITIALIZATION
k = linspace(1, 10 ,5);
%% For Loop
%% CALCULATIONS
for element = k
    s = element * 2;
    fprintf('The value of s = %.1f\n', s)
end

%% ____________________
%% OUTPUTS


%% ____________________
