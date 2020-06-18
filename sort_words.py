def sort_words(input):
    words = input.split() # To break apart input string at spaces and get a list of individual words
    words = [w.lower() + w for w in words ] # append lower case copy of each word to front of each word
    words.sort() # to focus on alphabetical order
    words = [w[len(w)//2:] for w in words] # array indexing to keep original copy of the words

    return ' '.join(words)
