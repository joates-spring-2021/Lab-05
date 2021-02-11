# -*- coding: utf-8 -*-
"""

johnwoates
CPSC 223P-01
Wed Feb 10, 2021
joates@fullerton.edu

"""

# Maybe you can use some functions from the string module
import string

# This is the function that you must write the code for
def numWordsSpoken(candidate, word):
    """"This is a doc string that describes the function. Change it to your liking.
    Something like: This function returns the number of times a given word was 
    spoken by a given speaker"""

    # When a function is empty, this line is required to avoid a syntax error
    # When you add code here, remove "pass"
    pass


# This code will extract the data from the debate file and read it into one big
# string named debateString
debateFile = open("debate.txt", "r")
debateString = debateFile.read() 
debateFile.close()

# This code will extract the data from the stop words file and read it into one big
# string named StopWordsString
stopWordsFile = open("stopWords.txt", "r")
stopWordsString = stopWordsFile.read()
stopWordsFile.close()


# Start your code here

