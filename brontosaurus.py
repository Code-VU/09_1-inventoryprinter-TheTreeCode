word = 'brontosaurus'
myHistogram = dict()
for letter in word:
    if letter not in myHistogram:
        myHistogram[letter] = 1
    else: myHistogram[letter]+=1

print(myHistogram)