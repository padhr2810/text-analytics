
"""
For tokens - add 1 x number to variable for each speaker e.g. "Num_turns_P1"
"""


############################################################################ Number of turns per speaker:

Num_turns[counter+1] = {}

for x in speaker_ids:
    temp_var = 0
    temp_var += tokens.count(x)
    
    Num_turns[counter+1][x] =  str(temp_var)
