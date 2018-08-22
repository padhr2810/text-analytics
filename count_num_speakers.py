
"""
if participant ID appears in 'tokens' at least once
    +1 to final number in pre-existing list "Num_speakers"
"""


############################################################################ No. of participants:
# Master list of participants: = P1 / N1 / D1 / D1 / R1 / R2 (i.e. patient, nurse, 2 x interns, 2 x registrars)
temp_var = 0

for x in speaker_ids:
    if x in tokens:
        temp_var += 1

### Produced the empty list "Num_speakers" already.
Num_speakers.append(str(temp_var))
    ### note: append works fine for numbers.

