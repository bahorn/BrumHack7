t = " => '"
f = open('./quick').read().split('\n')[:-1]
all = []
for i in f:
    a = i.split(t)[1].strip('\',').split(">")[1].split("<")[0]
    if a != '':
        for j in a.lower().split(' '):
            if j != '' and j not in all:
                all += [j]
print all
