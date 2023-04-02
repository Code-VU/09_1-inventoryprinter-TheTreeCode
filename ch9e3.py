fname = 'mbox-short.txt'
fhand = open(fname)
sendercount = dict()
for line in fhand:
    if line.startswith('From '):
        emailstart = line.find(' ')+1
        endofemail = line.find(' ', emailstart)
        emailaddress = line[emailstart:endofemail]
        sendercount[emailaddress] = sendercount.get(emailaddress, 0) + 1

print(sendercount)

