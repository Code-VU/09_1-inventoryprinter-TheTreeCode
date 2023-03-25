counts = {'chuck':1, 'annie':42, 'jan':100}
userinput = input('Please enter a name to search for: ')
print(counts.get(userinput, f'The namne, \"{userinput}\" was not found.'))
print(counts)
userinput = input('Please enter a name to search for: ')
print(counts.get(userinput, f'The namne, \"{userinput}\" was not found.'))
print(counts)