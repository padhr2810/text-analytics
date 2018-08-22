
opened = open('defaultDict.txt', "r")
print(opened)
opened
lines = opened.readlines()

## the clinical concept (e.g. blood) = always appears before \t
##      this can be multiple words separated by spaces
## the classification (e.g. TREATMENT) = always appears after \t
##      this can be multiple words separated by hyphens (I.E. if multiple classes apply to the same concept)
"""
EXAMPLES:
Clip	THERPROCDEV
CT	PROBLEM-THERPROCDEV-DIAGPROC-LABTEST
CHEST	BODYLOC
Reason	BODYMEAS
Radiology	DIAGPROC-LABTEST
carotid artery bypass	THERPROCDEV
"""


clin_concepts_dict = {}

for x in lines:
    concept          =  (re.split(r'\t+', x))[0]
    classification   =  (re.split(r'\t+', x))[1]
    clin_concepts_dict[concept] = classification

###  remove "/n" from the value
clin_concepts_dict = dict(map(str.strip,x) for x in clin_concepts_dict.items()) 
###  lower case - apply to key.
clin_concepts_dict =  {k.lower(): v for k, v in clin_concepts_dict.items()}

clin_concepts_dict




not_clinical_term = ["aaa", 
    "ah", 
    "all", 
    "am", 
    "an", 
    "and", 
    "as", 
    "ask", 
    "asked", 
    "asking", 
    "at", 
    "be ", 
    "before", 
    "but", 
    "call", 
    "can", 
    "chat", 
    "chips", 
    "cop", 
    "day", 
    "days", 
    "did", 
    "do", 
    "does", 
    "doing", 
    "don", 
    "door", 
    "down", 
    "due", 
    "e", 
    "eat", 
    "eating", 
    "eh", 
    "eight", 
    "eleven", 
    "em", 
    "even", 
    "ever", 
    "feel", 
    "feeling", 
    "feels", 
    "find", 
    "finding", 
    "five", 
    "food", 
    "for", 
    "four", 
    "get", 
    "getting", 
    "go", 
    "going", 
    "got", 
    "h", 
    "had", 
    "hang", 
    "hard", 
    "he", 
    "her", 
    "hi", 
    "hm", 
    "home", 
    "hundred", 
    "if", 
    "initially", 
    "into", 
    "is", 
    "isn", 
    "laughs", 
    "leaning", 
    "leave", 
    "let", 
    "like", 
    "listen", 
    "literally", 
    "little", 
    "ll", 
    "look", 
    "looking", 
    "lovely", 
    "me", 
    "meet", 
    "mic", 
    "mind", 
    "mm", 
    "morning", 
    "mrs", 
    "n1", 
    "name", 
    "ninety", 
    "no", 
    "not", 
    "oh", 
    "okay", 
    "on", 
    "one", 
    "organised", 
    "other", 
    "questions", 
    "re", 
    "run", 
    "said", 
    "see", 
    "set", 
    "seven", 
    "since", 
    "sit", 
    "sitting", 
    "six", 
    "sixty", 
    "smoke", 
    "sort", 
    "sorted", 
    "stay", 
    "still", 
    "switch", 
    "talk", 
    "ten", 
    "think", 
    "thirty", 
    "this", 
    "three", 
    "too", 
    "transferred", 
    "turn", 
    "twelve", 
    "twenty", 
    "two", 
    "understand", 
    "until", 
    "us", 
    "used", 
    "ve", 
    "want", 
    "was", 
    "well", 
    "while", 
    "x1", 
    "x2", 
    "year"]

	
#### dELETE if dict key (clinical concept) was in the list - "not_clinical_term"
original_len_clin_concepts_dict =   len(clin_concepts_dict)
num_concepts_to_remove = 0
for key, value in list(clin_concepts_dict.items()):
    if key in not_clinical_term:
        del clin_concepts_dict[key]
        num_concepts_to_remove += 1

