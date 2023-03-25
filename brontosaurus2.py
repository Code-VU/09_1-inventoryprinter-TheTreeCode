word = 'brontosaurus'
myHistogram = dict()
for letter in word:
    myHistogram[letter] = myHistogram.get(letter, 0)+1

print(myHistogram)