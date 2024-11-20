
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ENGR 133
%
% Function Call
% ma3_Ind_1_springs_yu1398()
%
% Input Arguments
% ([diameter1, diameter2] , #ofCoils)
%
% Output Arguments
%
% Problem Description: Add the problem description here and delete this
%                      line.
%
% Assignment Information
%   Assignment:     MA3 Ind 1
%   Author:         Leo Yu, yu1398@purdue.edu
%   Team ID:        LC018-03
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

function [wireLength, springMass] = ma3_ind_1_springs_yu1398(diameters, numCoils)
    % INITIALIZATION
    springDensity = 7.861; 

    if length(diameters) ~= 2 || ~isscalar(numCoils)
        fprintf('Inputs have incorrect dimensions\n');
        wireLength = -110.00;
        springMass = -110.00;
        fprintf('Wire length: %.2f cm\n', wireLength);
        fprintf('Spring Mass: %.2f g\n', springMass);
        return;
    end

    innerDiameter = diameters(1);
    outerDiameter = diameters(2);

    if innerDiameter > 0.95 * outerDiameter
        fprintf('The inner diameter value is larger than allowed\n');
        wireLength = -27.00;
        springMass = -27.00;
        fprintf('Wire length: %.2f cm\n', wireLength);
        fprintf('Spring Mass: %.2f g\n', springMass);
        return;
    end

    if any(diameters < 2.5) || any(diameters > 30)
        fprintf('Diameter values must be between 2.5 and 30 cm, inclusive\n');
        wireLength = -99.00;
        springMass = -99.00;
        fprintf('Wire length: %.2f cm\n', wireLength);
        fprintf('Spring Mass: %.2f g\n', springMass);
        return;
    end

    if numCoils < 4
        fprintf('The spring must have at least 4 coils\n');
        wireLength = -78.00;
        springMass = -78.00;
        fprintf('Wire length: %.2f cm\n', wireLength);
        fprintf('Spring Mass: %.2f g\n', springMass);
        return;
    end

    % CALCULATIONS
    
    wireLength = pi * mean(diameters) * numCoils;
    springMass = wireLength * springDensity * (innerDiameter - outerDiameter) ^ 2;    

    fprintf('Wire length: %.2f cm\n', wireLength);
    fprintf('Spring Mass: %.2f g\n', springMass);
end




%% ____________________
%% COMMAND WINDOW OUTPUT



%% ____________________
