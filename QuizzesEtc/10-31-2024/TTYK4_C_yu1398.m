%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Course Number: ENGR 13300
% Semester: e.g. Fall 2024
%
% % Problem Description: 
% This script will read in the weather data and analyze the humidity for
% a specified range of days, calculates the median, classifies the days
% based on the limits, counts and displays the number of specific days for
% each classification.
%
% Assignment Information
%   Assignment:     TTYK #4 Quiz
%   Version:        C4
%   Author:         Leo Yu, yu1398@purdue.edu
%   Team ID:        LC018 03
%   Date:           10/31/2024
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

% 1. Load the data 
num = readmatrix('Weather_Data_C.xlsx');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Complete this code according to the logic represented in the flowchart

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
humidity = num(end - 64: end,3);
dry_limit = 53;
humid_limit = 63;
dry_days = 0;
humid_days = 0;
confortable_days = 0;
[m,n] = size(humidity);

for i = 1:m
    if humidity(i) < dry_limit
        dry_days =  dry_days + 1;
    elseif humidity(i) > humid_limit
        humid_days = humid_days + 1;
    else
        confortable_days = confortable_days + 1;
    end
end

median_of_humidity = median(humidity);

%%displaying everything

fprintf("Dry Days: %d\nHumid Days: %d\nConfortable Days: %d\n\n", dry_days, humid_days, confortable_days);

fprintf("Median Humidity: %.2f\n", median_of_humidity);