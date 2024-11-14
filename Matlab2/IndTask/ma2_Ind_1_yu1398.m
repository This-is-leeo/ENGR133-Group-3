%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Course Number: ENGR 13300
% Semester: e.g. Fall 2024
%
% Problem Description: Add the problem description here and delete this
%                      line.
%
% Assignment Information
%   Assignment:     MA2 
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


%%_______________
%% INITIALIZATION
% Define tank dimensions
r = 1.25; % Inner radius in meters
length = 5.5; % Inner length in meters
height_increment = 0.1; % Height decrease in meters (sensor interval)

% Calculate maximum volume and threshold volume
max_volume = pi * r^2 * length;
threshold_volume = 0.2 * max_volume;
fprintf('max volume: %.2f m^3\n', threshold_volume);
% Initialize variables
h = 2 * r; % Starting fluid height (full tank)
index = 1;
volume = [];

%% CALCULATIONS
% While loop to simulate tank emptying
while h > 0
    % Calculate volume at current height
    current_volume = length * (acos((r - h) / r) * r^2 - (r - h) * sqrt(2 * r * h - h^2));
    volume(index) = current_volume; % Store in volume vector
    % Check if the current volume is below the threshold
    if current_volume < threshold_volume
        break; % Exit loop once below 20% capacity
    end
    
    % Update variables
    h = h - height_increment; % Decrement height
    index = index + 1; % Move to the next index
end

%% OUTPUTS
% Display results
fprintf('Number of iterations = %d\n', index);
fprintf('Remaining volume = %.2f m\n', current_volume);
fprintf('Fluid Height= %.2f m^3\n', h);
fprintf('Warning: The tank volume is below 20%% capacity!\n');