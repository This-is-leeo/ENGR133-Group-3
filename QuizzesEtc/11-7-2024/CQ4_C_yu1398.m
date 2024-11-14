%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Course Number: ENGR 13300
% Semester: e.g. Fall 2024
%
% Problem Description: 
% This script will read in the travel data, analyze speed, and fuel cost
% for a specified range of days, classify the days based on limits, count,
% and display the number of days for each classification.
% 
% Assignment Information
%   Assignment:     CQ #4 Quiz
%   Version:        C6
%   Author:         Leo Yu, yu1398@purdue.edu
%   Team ID:        LC18-03 (e.g. LC1 - 01; for section LC1, team 01)
%   Date:           11/07/2024
%
% Academic Integrity Statement:
%     I have not used source code obtained from any unauthorized
%     source, either modified or unmodified; nor have I provided
%     another student access to my code.  The project I am
%     submitting is my own original work.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% 1. Load the data 
data = readmatrix('CQ4_Data_Version_C.csv', 'Range', [2, 2]);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Complete this section of the code according to the logic represented in
% the flowchart


speed_data = data(5, 100-73:100);
fuel_cost_data = data(3, 100-73:100);
%convert to MPH
speed_data = 0.621371 .* speed_data;

speed_limit = 25.61;
fuel_cost_limit = 4.01;

high_speed_and_high_cost_days = 0;
high_speed_and_low_cost_days = 0;
low_speed_days = 0;

for i = 1:length(speed_data)
    if speed_data(i) > speed_limit
        if fuel_cost_data(i) > fuel_cost_limit
            high_speed_and_high_cost_days = high_speed_and_high_cost_days + 1;
        else
            high_speed_and_low_cost_days = high_speed_and_low_cost_days + 1;
        end
    else
        low_speed_days = low_speed_days + 1;
    end
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Display results
fprintf('Days with high speed and high fuel cost: %d days\n', high_speed_and_high_cost_days);
fprintf('Days with high speed and low fuel cost: %d days\n', high_speed_and_low_cost_days);
fprintf('Days with low speed: %d days\n', low_speed_days);