# Create word dictionary from the comprehensive word list 
word_dict = {}
def create_word_dict ():
    dict_file = open("words.txt", "r")
    for line in dict_file:
        line = line.strip()
        word_dict[line] = 1
        
# Removes punctuation marks from a string
def parseString (st):
    new_st = ""
    for character in st:
        if (character.isalpha() or character.isspace() or character == "'"):
            new_st += character
        else:
            new_st +=' '
    return new_st
    
# Returns a dictionary of words and their frequencies
def getWordFreq (file):
    book = open(file, "r")
    freq_dict = {}
    for line in book:
        line = line.strip()
        line.replace("\'", ' ')
        line.replace("\'s",' ')
        line = parseString(line)
        word_list = line.split()
        for word in word_list:
            # add words to the dictionary, or increment freq
            if word in freq_dict:
                freq_dict[word] = freq_dict[word] + 1
            else:
                freq_dict[word] = 1
    # close input file
    book.close()
    # Remove all words that start with a capital letter.
    proper_words = []
    for word in freq_dict:
        if (word[0].isupper()):
            proper_words.append(word)
    for word in proper_words:
        if word.lower() in freq_dict:
            freq_dict[word.lower()] = freq_dict[word.lower()] + 1
        else:
            if word.lower() in word_dict:
                if word.lower() in freq_dict:
                    freq_dict[word.lower()] = freq_dict[word.lower()] + 1
                else:
                    freq_dict[word.lower()] = 1
    for word in proper_words:
        if word in freq_dict:
            del freq_dict[word]
    return freq_dict

# Compares the distinct words in two dictionaries
def wordComparison (author1, freq1, author2, freq2):
    distinct_words1 = len(freq1)
    distinct_words2 = len(freq2)

    total1 = 0
    for word in freq1:
        total1 += freq1[word]
    total2 = 0
    for word in freq2:
        total2 += freq2[word]

    ratio1 = round((distinct_words1/total1)*100,10)
    ratio2 = round((distinct_words2/total2)*100,10)

    print(author1)
    print('Total distinct words = ', distinct_words1)
    print('Total words (including duplicates) = ', total1)
    print('Ratio (% of total distinct words to total words) = ', ratio1)
    print()
    print(author2)
    print('Total distinct words = ', distinct_words2)
    print('Total words (including duplicates) = ', total2)
    print('Ratio (% of total distinct words to total words) = ', ratio2)           
    print()
    D = set(freq1)
    H = set(freq2)

    distinct1 = D - H
    distinct2 = H - D

    length1 = len(distinct1)
    length2 = len(distinct2)

    freq1_ct = 0
    for word in distinct1:
        freq1_ct += freq1[word]

    freq2_ct = 0
    for word in distinct2:
        freq2_ct += freq2[word]

    rel_freq1 = round((freq1_ct/total1)*100, 10)
    rel_freq2 = round((freq2_ct/total2)*100, 10)

    print(author1, 'used', length1, 'words that', author2, 'did not use.')
    print('Relative frequency of words used by', author1, 'not in common with', author2, '=', rel_freq1) 
    print()
    print(author2, 'used', length2, 'words that', author1, 'did not use.')
    print('Relative frequency of words used by', author2, 'not in common with', author1, '=', rel_freq2) 

def main():
  # Create word dictionary from comprehensive word list
  create_word_dict()

  # Enter names of the two books in electronic form
  book1 = input ("Enter name of first book: ")
  book2 = input ("Enter name of second book: ")
  print()

  # Enter names of the two authors
  author1 = input ("Enter last name of first author: ")
  author2 = input ("Enter last name of second author: ")
  print() 
  
  # Get the frequency of words used by the two authors
  wordFreq1 = getWordFreq (book1)
  wordFreq2 = getWordFreq (book2)

  # Compare the relative frequency of uncommon words used
  # by the two authors
  wordComparison (author1, wordFreq1, author2, wordFreq2)

main()
