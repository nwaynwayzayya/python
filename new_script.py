#!/bin/python3

import sys  #sys = system functions and parameters
from datetime import datetime as dt #only import a specific part of datetime module, not the whole module
#imported with alias, dt


print(sys.version)
print(dt.now())  #print(datetime.now()) -- can be used if we didn't specify any datetime


# Advanced strings
my_name = "Norelle"
print(my_name[0])
print(my_name[-1])

sentence = "This is a sentence."
print(sentence[:4])

print(sentence.split())  #splits the sentence and returns the words as an array

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

#character escaping
quote = "He said, \"give me all your money\"."
print(quote)

#stripping the space out
too_much_space = "               hello         "
print(too_much_space.strip())

print("A" in "Apple")  #returns TRUE OR FALSE

letter = "A"
word = "Apple"
print(letter.lower() in word.lower())  #for case sensitivity

movie = "The Hangover"
print("My favourite movie is {}.".format(movie))