# Create word dictionary from the comprehensive word list 
comprehensive_words = {}
def create_word_dict():
    lines = [line.rstrip('\n') for line in open('words.txt')]
    for line in lines:
        comprehensive_words.setdefault(line,1)
        
# Removes punctuation marks from a string
def parseString (string):
    new = ''
    for current in string:
        # If there is an apostrophe followed by a character that is not an 's' keep the apostrophe.
        # Accept only letters (using isalpha()) and spaces (using isspace()) and apostrophes only for the special cases mentioned above
        if (current.isalpha() or current.isspace() or current == '\''):
            new += current
        else:
            new += " "        
    return new

# Returns a dictionary of words and their frequencies
def getWordFreq(file):
    # open the book
    book = open (file, "r")

    # create an empty set for unique words
    word_set = set()

    # create a dictionary for word frequency
    word_dict = {}

    # track the total number of words
    total_words = 0

    for line in book:
        # strip the end-of-line character
        line = line.strip()
        # remove apostrophes (') at the end of a word or ('s) at the end of a word.
        line.replace('\' ', '')
        line.replace('\'s' ,'')
        line = parseString(line)

        # split the line into words
        word_list = line.split()

        # add each word to the set and to the dictionary
        for word in word_list:
            word_set.add (word)

            # add words to the dictionary
            if word in word_dict:
                word_dict[word] = word_dict[word] + 1
            else:
                word_dict[word] = 1

    # close the file
    book.close()

    # Remove all words that start with a capital letter.
    capital_words = []
    for word in word_set:
        if (word[0].isupper()):
            capital_words.append(word)
    # go through the list of capitalized words and
    # check if the lower case version of that word exists in the frequency dictionary.
    for capital in capital_words:
        # If it exists, then add the upper case word's frequency to the lower case word's frequency.
        if capital.lower() in word_dict:
            word_dict[capital.lower()] = word_dict[capital.lower()] + 1
        else:
        # If the lower case version does not exist in the dictionary,
        # check if it exists in a comprehensive word list that is used for crossword and Scrabble players.
        # If it does, create an entry in the frequency dictionary with the lower case version of the word and the word frequency computed.
            if capital.lower() in comprehensive_words:
                if capital.lower() in word_dict:
                    word_dict[capital.lower()] = word_dict[capital.lower()] + 1
                else:
                    word_dict[capital.lower()] = 1
                    
    # After you have checked for all capitalized words, remove all those words in the list of capitalized words and
    # their frequencies from the word frequency dictionary.
    for capital in capital_words:
        if capital.lower() in word_dict:
            del word_dict[capital.lower()]

    with open('word_list.out', 'w') as file:
        for word in word_set:
            file.write("{}\n".format(word))

##    with open('word_dict.out', 'w') as file:
##        for word in word_dict:
##            file.writelines('{}:{}\n'.format(k,v) for k, v in word_dict.items())
            
# Compares the distinct words in two dictionaries
#def wordComparison (author1, freq1, author2, freq2):

    
def main():
    # Create word dictionary from comprehensive word list
    create_word_dict()

    # Enter names of the two books in electronic form
    ##book1 = input ("Enter name of first book: ")
    getWordFreq('Tale.txt')
    ##book2 = input ("Enter name of second book: ")
    print()

    # Enter names of the two authors
    ##author1 = input ("Enter last name of first author: ")
    ##author2 = input ("Enter last name of second author: ")
    ##print() 
  
    # Get the frequency of words used by the two authors
    ##wordFreq1 = getWordFreq (book1)
    ##wordFreq2 = getWordFreq (book2)

    # Compare the relative frequency of uncommon words used
    # by the two authors
    ##wordComparison (author1, wordFreq1, author2, wordFreq2)

main()
