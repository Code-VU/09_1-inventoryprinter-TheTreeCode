fhand = open('words.txt')
mydictionary = {}
counter = 0
for line in fhand:
    templist = line.split()
    bigtemplist = []
    for item in templist:
        counter+=1
        mydictionary[item] = f'The word, \"{item}\", has {counter-1} words before it.'

print(mydictionary)
print('and' in mydictionary)
print(mydictionary['and'])
