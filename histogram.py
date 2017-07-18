#!/usr/local/bin/python3
"""
Create a histogram from a txt doc, taken from sys.argv[1]
"""
import sys, os

try:
    file  = sys.argv[1]
except IndexError:
    fn = input("File: ")
    file = os.path.join(os.getcwd(), fn)
#characters to exclude
punc = (',','.',':',';',"'",'"','?','!','&','-','[',']','{','}',)

#key = letter_count, value =  number of words w/ letter count, 
word_counter = {}

with open(file, 'r') as infile:
    words = infile.readlines()
     
def word_len(text):
    """
    Adds the kev/value  = word-length/number of words of that length,
    not counting punctuation, to dict() word_counter
    """
    new = ''
    for index, word in enumerate(text):
        for char in words[index]:       
            if char in punc:
                pass
            else:
                new += char    
    for i in new.split():
        if len(i) not in word_counter.keys():
            word_counter[len(i)] = 1
        else:
            word_counter[len(i)] += 1
    
word_len(words)

#Create a list of lists to be formatted as a grid, and adjust its size according
#to the contents of {word_counter}
grid = [['{0:3}'.format('___')]*(max(word_counter.keys())+1) \
        for i in range(max(word_counter.values())+5)]

#print numeric representation of number of letters/number of words with letter
#count
print('{0:6}{1:>8}'.format('Length', 'Count'))
for key, value in word_counter.items():
    print('{0:>6}{1:.>8}'.format(key, value))   
    #create columns of '*' to represent numb of words
    for i in range(value):
        grid[-value -1][key] = '{0:^3}'.format('*')
        value -=1

#set X-axis markers
for i in range(max(word_counter.keys())):
    grid[-1][i +1] = '{0:^3}'.format(i+1)
#set Y-axis scale to 1:5
for i in range(0, max(word_counter.values())+5, 5):
    grid[-i-1][0] = '{0:-<3}'.format(i)

#print histogram
for row in grid:
    print('|'.join(row))
