

###################################### LIST OF POS & NEG WORDS IN THIS FILE:


pos_in_this = [x for x in tokens if x in positive]
print("These are POSITIVE words")
pos_freq_in_this = pos_in_this
pos_in_this = sorted(set(pos_in_this))
print(pos_in_this)

print("")

neg_in_this = [x for x in tokens if x in negative]
print("These are NEGATIVE words")
neg_freq_in_this = neg_in_this
neg_in_this = sorted(set(neg_in_this))
print(neg_in_this)


###################################### Sets of pos & neg words across all files:
    
pos_set_all_dialogue.extend(pos_in_this)
### i.e. append would imply nested lists... but we want one large list.
### created the empty list earlier
pos_set_all_dialogue = sorted(set(pos_set_all_dialogue))

neg_set_all_dialogue.extend(neg_in_this)
### i.e. append would imply nested lists... but we want one large list.
neg_set_all_dialogue = sorted(set(neg_set_all_dialogue))


###################################### Freqs of pos & neg words across all files:
pos_freq_all_dialogue.extend(pos_freq_in_this)
### i.e. append would imply nested lists... but we want one large list.
### created the empty list earlier

neg_freq_all_dialogue.extend(neg_freq_in_this)
### i.e. append would imply nested lists... but we want one large list.

pos_FreqDist_all_dialogue = dict(nltk.FreqDist(pos_freq_all_dialogue))
neg_FreqDist_all_dialogue = dict(nltk.FreqDist(neg_freq_all_dialogue))

