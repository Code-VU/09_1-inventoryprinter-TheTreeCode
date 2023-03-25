eng2span = dict()
print(eng2span)
eng2span['one'] = 'uno'
print(eng2span)
eng2span = {'one':'uno', 'two':'dos', 'three':'tres'}
print(eng2span['three'])
print(eng2span)
testvariable = 'four'
try: print(eng2span[testvariable])
except KeyError: print(f'Error! The key {testvariable} was not located in the dictionary.')
print(len(eng2span))
print('one' in eng2span)
print('uno' in eng2span)
vals = list(eng2span.values())
print(vals)
print('tres' in vals)
print(vals[1])
