import string

fname = input('Enter a file name: ')
try: fhand = open(fname)
except:
    print('File not found: '+fname+'.')
    exit()
word_counter = dict()
for line in fhand:
    line = line.rstrip().lower()
    line = line.translate(line.maketrans('','', string.punctuation))
    words = line.split()
    for word in words:
        if word not in word_counter:
            word_counter[word] = 1
        else:
            word_counter[word] += 1

print(word_counter)

