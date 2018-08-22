##### creates a list called "stems"


def tokenize_and_stem(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    # empty list
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems

# creates a list called "filtered_tokens"
def tokenize_only(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens
	
	
	
def open_and_tokenize(counter, folder):
	
    ### First: define name of file to open
    file = os.listdir(folder)[counter]
    type(file)
    file

    ### specify file number (starting from 1)
    file_num = counter + 1

    ### print file name and number:
    print()
    print("File number: %s" %file_num)
    print("File name: %s" %file)


    f = open(file)
    print("Open file and display 'type' = {}".format(type(f)))

    f2   = f.read()
    print("Read file and display 'type' = {}".format(type(f2)))
    type(f2)

    ### Tokenize the text:
    tokens = tokenize_only(f2)
    print("Tokenise file and display 'type' = {}".format(type(tokens))) 

    print()
    print("Just show the first & last 10 words of the main dialogue text file")
    print("...These are first 10 words:")
    #### Just show the first & last 10 words of the main dialogue text file
    temp = tokens[:10]
    for a in temp:
        print(a)
    print("...These are last 10 words:")
    temp = tokens[-10:]
    for a in temp:
        print(a)

    print("return tokens")
    return tokens

