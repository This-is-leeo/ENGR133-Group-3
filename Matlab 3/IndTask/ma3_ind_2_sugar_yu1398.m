%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Course Number: ENGR 13300
% Semester: e.g. Fall 2024
%
% Problem Description: Add the problem description here and delete this
%                      line.
%
% Assignment Information
%   Assignment:     MA2, Ind 2
%   Author:         Leo Yu, yu1398@purdue.edu
%   Team ID:        LC018 - 03
%   Date:           11/13/2024
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
data = readmatrix('Sucrose_Data.csv');
time = data(:, 1);
conc_test1 = data(:, 2);
conc_test2 = data(:, 3);
conc_test3 = data(:, 4);
%% ____________________
%% CALCULATIONS
mean_concentration = mean([conc_test1, conc_test2, conc_test3], 2);
std_concentration = std([conc_test1; conc_test2; conc_test3], 0, 1);
idx1 = find(time == 1);  % Index for 1 minute
idx2 = find(time == 10); % Index for 10 minutes

slope_test1 = ma3_ind_2_secantline_yu1398(time, conc_test1, idx1, idx2);

slope_test2 = ma3_ind_2_secantline_yu1398(time, conc_test2, idx1, idx2);

slope_test3 = ma3_ind_2_secantline_yu1398(time, conc_test3, idx1, idx2);

%% ____________________
%% FIGURE DISPLAY - First Figure (Original Data and Model)
concentration = 0.5867 * exp(-0.06 * time);
% Create a new figure
figure;

% Plot the original data for each test
plot(time, conc_test1, 'o', 'MarkerSize', 6, 'DisplayName', 'Data - Test 1'); hold on;
plot(time, conc_test2, 's', 'MarkerSize', 6, 'DisplayName', 'Data - Test 2');
plot(time, conc_test3, '^', 'MarkerSize', 6, 'DisplayName', 'Data - Test 3');

model = polyfit(time, mean_concentration, 3); 
y_model = polyval(model, time);
plot(time, concentration,'r-', 'LineWidth', 1, 'Color', 'k', 'DisplayName', 'Model');

% Formatting the plot
title('Sucrose Decomposition - Original Data and Model');
xlabel('Time (minutes)');
ylabel('Sucrose Concentration (M)');
grid on;
legend('show', 'Location', 'best');
hold off;

%% ____________________
%% TEXT DISPLAY - Average Rates of Change


rate_test1 = (conc_test1(idx2) - conc_test1(idx1)) / (time(idx2) - time(idx1));  % Example rate calculation
rate_test2 = (conc_test2(idx2) - conc_test2(idx1)) / (time(idx2) - time(idx1));  % Example rate calculation
rate_test3 = (conc_test3(idx2) - conc_test3(idx1)) / (time(idx2) - time(idx1));  % Example rate calculation

% If you have a model rate of change (if required):

% Display the results using fprintf
fprintf('\nAverage Rates of Change (Calculated from Time = 1 to Time = 10 minutes):\n');
fprintf('--------------------------------------------------------------\n');
fprintf('Test 1 Rate of Change: %.3f M/min\n', rate_test1);
fprintf('Test 2 Rate of Change: %.3f M/min\n', rate_test2);
fprintf('Test 3 Rate of Change: %.3f M/min\n', rate_test3);
fprintf('--------------------------------------------------------------\n');
fprintf('Note: These values represent the average rate of change in sucrose concentration from 1 minute to 10 minutes.\n');
fprintf('--------------------------------------------------------------\n');
