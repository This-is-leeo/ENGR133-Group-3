%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Course Number: ENGR 13300
% Semester: e.g. Fall 2024
%
% Problem Description: Add the problem description here and delete this
%                      line.
%
% Assignment Information
%   Assignment:     Pre 4
%   Author:         Leo Yu, yu1398@purdue.edu
%   Team ID:        LC18 - 03 (e.g. LC1 - 01; for section LC1, team 01)
%   Date:           11/11/2024
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

M = [1, 2, 3; 4, 5, 6; 7, 8, 9];
%% ____________________
%% INITIALIZATION

%% ____________________
%% CALCULATIONS


%% ____________________
%% OUTPUTS
% Outer loop iterates through rows
for i = 1:size(M, 1)
    % Inner loop iterates through columns in each row
    for j = 1:size(M, 2)
        fprintf("%d\n", M(i, j));
    end
end

%% ____________________
