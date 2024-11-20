function TTYK5_C_func_yu1398(engPower, gpsSpeed) 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ENGR 133 Fall 2024
%
% Function Call
%TTYK5_C_func_yu1398()
%
% Input Arguments
% engPower, GPSspeed
%
% Output Arguments
% NA
% Function Description: Add the function description here and delete this
%                       line.
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


engPower = engPower * 1.34102;
ratio = [];
for i = 1:length(engPower)
    instantSpeed = gpsSpeed(i);
    if instantSpeed ~= 0
        instantRatio = engPower(i) / instantSpeed;
        ratio = [ratio, instantRatio];
    end
end

averagePowertoSpeed = mean(ratio);
fprintf('average Power: %.2f\n', averagePowertoSpeed)


power_to_speed_ratio = ratio;
















%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    figure
    time = 1:length(power_to_speed_ratio);  % each step is 1 second
    plot(time, power_to_speed_ratio)
    xlabel('Time (s)')
    ylabel('Power-to-Speed Ratio (hp/mph)')
    title('Engine Power-to-Speed Ratio Over Time')