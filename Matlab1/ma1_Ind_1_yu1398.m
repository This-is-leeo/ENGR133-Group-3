%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Course Number: ENGR 13300
% Semester: e.g. Fall 2024
%
% Problem Description: Add the problem description here and delete this
%                      line.
%
% Assignment Information
%   Assignment:     Ind HW9 - MA1
%   Author:         Leo Yu yu1398@purdue.edu
%   Team ID:        LC18 03 (e.g. LC1 - 01; for section LC1, team 01)
%   Date:           10/30/2024
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

clear;
%% ____________________
%% INITIALIZATION
V = [3 -6 4 2.5 0 10 -1];


%% ____________________
%% MATRIX CREATION
M = ones(5);
M(end, :) = V(1);
M(3:end, 3:end) = V(2);
M(1, 1) = V(3);
M(4, 2) = V(5);
M(:, end) = M(:, end) * V(4);
M = M * V(end);


%% ____________________
%% COPY & CONCATENATION
C = M(4, 1:2);
D = M(1, 2:3); 
E = [M(4, 1), C, M(4, 5)];
F = [D, M(1, 3), M(1, 5)];

%% ____________________
%% REPLACE MATRIX ELEMENTS
vals = zeros(4);
vals(1:3, 1) = M(1:3, 1);
vals(4,1) = M(1,5);
vals(3,2) = M(5,1);
vals(2:3, 3) = M(3:4, 3);
vals(3,4) = M(4,4);
vals(1,4) = M(2,1);
vals(4,4) = M(5,5);

%% ____________________
%% FINAL MATRIX
X = sum(vals);
G = [X; vals];
Y = sum(G, 2);
H = [G, Y];
H(end, end) = sum(diag(vals(1:4, 1:4)));


%% ____________________
%% FORMATTED TEXT DISPLAY
fprintf('After doing step 8.e, the value in the center of H is %.0f.\n', H(3, 3));  % Center value
fprintf('After doing step 8.e, the value in the upper left of H is %.1f,\n ', H(1, 1));  % Upper left
fprintf('and the value in the upper right of H is %.1f.\n', H(1, end));  % Upper right
fprintf('After doing step 8.e, the value in the lower left of H is %.1f,\n ', H(end, 1));  % Lower left
fprintf('and the value in the lower right of H is %.0f.\n', H(end, end));  % Lower right

%% ____________________
