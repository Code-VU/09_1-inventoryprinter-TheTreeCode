"""But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief"""

fhand = open('shakespearNoPunctuation.txt')
histogram = dict()
counts = dict()
for line in fhand:
    wordsinline = line.split()
    for word in wordsinline:
        histogram[word] = histogram.get(word, 0) + 1

fhand = open('shakespearNoPunctuation.txt')

#print(histogram)
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

if counts == histogram: print('Troof')
else: print('false')




"""
create a global variable containing an empty dictionary
read through the lines of the file
break each line into a list of words
loop through each of the words in the line
count each word using a dictionary

two for loops
"""

