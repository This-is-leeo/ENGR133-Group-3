
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ENGR 133
%
% Function Call
%
% Input Arguments
%
% Output Arguments
%
% Problem Description: Add the problem description here and delete this
%                      line.
%
% Assignment Information
%   Assignment:     e.g. Ind HW9 - MA1
%   Author:         Name, login@purdue.edu
%   Team ID:        LC#-## (e.g. LC1 - 01; for section LC1, team 01)
%   Date:           e.g. 08/29/2024
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
%
%
%% ____________________
%% INITIALIZATION

function slope = ma3_ind_2_secantline_yu1398(time_vec, conc_vec, idx1, idx2)
    delta_conc = conc_vec(idx2) - conc_vec(idx1);
    delta_time = time_vec(idx2) - time_vec(idx1);
    slope = delta_conc / delta_time;

end

%% ____________________
