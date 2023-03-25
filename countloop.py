counts = {'chuck':1, 'annie':42, 'jan':100}
for key in counts: print(key, counts[key])

print('_______________________________________')
for key in counts:
    if counts[key] > 10: print(key, counts[key])

print('_______________________________________')

keylist = list(counts.keys())
keylist.sort()
for key in keylist:
    print(key, counts[key])

print('_______________________________________')

"""valuelist = list()
for key in counts:
    valuelist.append(counts[key])
    valuelist.sort()
    valuelist.reverse()

for key in counts:
    for v in valuelist:
        print(counts.get(v, key), v)"""