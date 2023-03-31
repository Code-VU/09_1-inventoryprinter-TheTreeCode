txtfile = input('Please enter the filename you would like to add to the dictionary: ')
try: filehandle = open(txtfile)
except: print('Could not locate file.')
outputdictionary = dict()

def isthisstringinfile():
    print(input('Which word would you like to check?: ') in outputdictionary)

def file2dictionary(thefile):
    for line in thefile:
        tempwordslist = line.split()
        for word in tempwordslist:
            if word not in outputdictionary:
                outputdictionary[word] = 'Noice!'
    print(outputdictionary)
    isthisstringinfile()

file2dictionary(filehandle)
